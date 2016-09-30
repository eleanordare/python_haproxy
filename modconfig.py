#!/usr/bin/env python
__author__ = 'Eleanor Mehlenbacher'

import ConfigParser
import sys
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('haproxy.cfg')

print parser.sections()
