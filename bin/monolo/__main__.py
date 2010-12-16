#!/usr/bin/env python3
import monolo.conf, monolo.core.engine
import sys

monolo.conf.debug = True
monolo.conf.engine = monolo.core.engine.Engine(sys.argv)

