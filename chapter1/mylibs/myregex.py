#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re


def sayhello():
    print('hello aqie')


def myreg(regex_str, line):
    match_obj = re.match(regex_str, line)
    if match_obj:
        print(match_obj.group(1))
    else:
        print('no match')
