import argparse
import collections
import configparser 
from datetime import datetime
import grp, pwd
from fnmatch import fnmatch
import hashlib
from math import ceil
import os
import re
import sys
import zlib

argparser = argparse.ArgumentParser(description="The stupid content tracker")
argsubparsers = argparser.add_subparsers(title="Commands", dest="command")  #whatever command the subparser read will be sent to the field "command"
argsubparsers.required = True
