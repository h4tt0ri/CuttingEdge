# CuttingEdge
A forensic tool for parse Microsoft Edge `History` files. Also, it supports `favicons` and `Shortcut` artifacts.

## Requirements & Installation
- Python3.x
- pandas==1.4.3

```
git clone https://github.com/h4tt0ri/CuttingEdge
cd CuttingEdge/
pip3 install -r requirements.txt
python3 CuttingEdge.py -h
```


## Usage 💻
History files are stored in SQLite3 database format. Usually you can find these artifacts in `%USERPROFILE%\appdata\local\microsoft\edge\user_data\default`. Currently, it supports the following artifact:

- History
- Favicons
- Shortcuts

Note that, downloaded files are inside `history` artifact.

```bash
usage: CuttingEdge.py [-h] -f INPUT -t TYPE [-o OUTPUT]

Microsoft Edge Parser

optional arguments:
  -h, --help  show this help message and exit
  -f INPUT    history edge file
  -t TYPE     ex: history, downloads, favicons, shortcuts
  -o OUTPUT   file output in csv format
```

Example usage:

```bash
$ python3 CuttingEdge.py -f /path/to/Shortcuts -t shortcuts -o shortcut_parsed
$ python3 CuttingEdge.py -f /path/to/History -t history -o history_parsed
$ python3 CuttingEdge.py -f /path/to/History -t downloads -o downloads_parsed
$ python3 CuttingEdge.py -f /path/to/Favicons -t favicons -o favicons_parsed
```

The output file will be in .CSV format and you don't need to add the ".csv" in the output argument.

## License
MIT

## Find Me 🦊

- Website: https://www.h4tt0r1.cz/
- Twitter: https://mobile.twitter.com/hackttori
- Discord: https://www.discord.com/users/185572012394020864
- LinkedIn: http://linkedin.com/in/nvalenzuelam

Any feedback about the tool is welcome :)