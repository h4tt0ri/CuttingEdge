import sqlite3
import os
import sys
import pandas as pd
import time
from datetime import datetime
import datetime as dt
import argparse

windows_epoch = dt.datetime(year=1601, month=1, day=1)

# parse SQLite tables from history.db 
def parse_edge_history(history_db_path, output_file):

    conn = sqlite3.connect(history_db_path) # connect database
    try:
        df = pd.read_sql_query("SELECT * from urls", conn) # get url table from history file
    except:
        print("[+] No database found, are you using the correct input file?")
        exit()
    for index, row in df.iterrows(): # Convert last_visit_time column in human readable
        row["last_visit_time"] = datetime_from_window_ts(row["last_visit_time"])
        df.at[index,'last_visit_time'] = row["last_visit_time"]

    df.to_csv(output_file+'.csv')
    conn.close()
    return

def parse_download_history(history_db_path, output_file):

    conn = sqlite3.connect(history_db_path) # connect database
    try:
        df = pd.read_sql_query("SELECT tab_url, current_path, target_path, start_time, end_time from downloads", conn) # get downloads table from history file
    except:
        print("[+] No database found, are you using the correct input file?")
        exit()
    pd.set_option('display.float_format', lambda x: '%.0f' % x)
    pd.set_option('display.max_rows', None)

    for index, row in df.iterrows():
        row["start_time"] = datetime_from_window_ts(row["start_time"])
        df.at[index,'start_time'] = row["start_time"]
        row["end_time"] = datetime_from_window_ts(row["end_time"])
        df.at[index,'end_time'] = row["end_time"]

    df.to_csv(output_file+'.csv')
    conn.close()
    return

def parse_favicons(history_db_path, output_file):

    conn = sqlite3.connect(history_db_path) # connect database
    try:
        df = pd.read_sql_query("SELECT page_url, icon_id from icon_mapping", conn) # get downloads table from history file
    except:
        print("[+] No database found, are you using the correct input file?")
        exit()

    df.to_csv(output_file+'.csv')
    conn.close()
    return

def parse_shortcuts(history_db_path, output_file):

    conn = sqlite3.connect(history_db_path) # connect database
    try:
        df = pd.read_sql_query("SELECT text, fill_into_edit, url, contents, last_access_time from omni_box_shortcuts", conn) # get downloads table from history file
    except:
        print("[+] No database found, are you using the correct input file?")
        exit()

    for index, row in df.iterrows():
        row["last_access_time"] = datetime_from_window_ts(row["last_access_time"])
        df.at[index,'last_access_time'] = row["last_access_time"]

    df.to_csv(output_file+'.csv')
    conn.close()
    return

# transform windows epoch time to human timestamps
def datetime_from_window_ts(timestamp):
    return windows_epoch + dt.timedelta(seconds=timestamp/1e6)

def main():

    class colors():

        blue    = '\033[1;34m'
        green   = '\033[1;32m'
        red     = '\033[1;31m'
        orange  = '\033[1;33m'
        white   = '\033[1m'
        gray    = '\033[1;37m'
        default = '\033[0m'

    parser = argparse.ArgumentParser(prog="cutting_edge.py",description= colors.white + "Microsoft" + colors.blue + " Edge" + colors.blue + " Parser" + colors.default)
    parser.add_argument('-f',   dest="INPUT",    help='history edge file', required= True)
    parser.add_argument('-t',   dest="TYPE",    help='ex: history, downloads, favicons, shortcuts', required= True)
    parser.add_argument('-o', dest="OUTPUT", help='file output in csv format', required= True)
    args        =   parser.parse_args()
    dbfile      =   args.INPUT
    parse_type  =   args.TYPE
    output_file =   args.OUTPUT

    input_db_file = os.path.expanduser(dbfile)
    print("["+colors.blue+"+"+colors.default+"] parsing edge "+ parse_type)


    if parse_type.lower() == 'history':
        parse_edge_history(input_db_file, output_file)

    elif parse_type.lower() == 'downloads':
        parse_download_history(input_db_file, output_file)

    elif parse_type.lower() == 'favicons':
        parse_favicons(input_db_file, output_file)

    elif parse_type.lower() == 'shortcuts':
        parse_shortcuts(input_db_file, output_file)

    else:
        print("["+colors.red+"+"+colors.default+"] No recognized TYPE argument, try again")
        exit()

    print("["+colors.blue+"+"+colors.default+"] Finished, results saved at "+output_file+".csv")

if __name__ == '__main__':
    main()