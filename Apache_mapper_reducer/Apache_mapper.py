#!/usr/bin/env python
import sys
import requests
import apachelogs
import re
from apachelogs import LogParser

url = "https://raw.githubusercontent.com/singhj/big-data-repo/refs/heads/main/datasets/access.log"
response = requests.get(url)



# Define the log format (example for the common log format)
parser = LogParser('%h %l %u %t "%r" %>s %b "%{Referer}i" "%{User-Agent}i" "%{Referer}i"')

def mapper(argv):
   for line in sys.stdin:
      print(line)            

# This would be invoked by the Hadoop job framework
if __name__ == "__main__":
    mapper(sys.argv)
