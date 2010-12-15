#!/usr/bin/env python3
import monolo.conf
import monolo.engine
import sys

monolo.conf.debug = True
monolo.conf.engine = monolo.engine.Engine(sys.argv)

