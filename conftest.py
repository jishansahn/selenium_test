# -*-coding: utf-8-*-
# @Author = jishanshan
# @Date = 2020/4/18
import os
import sys

ROOT_DIR=os.path.abspath(os.path.dirname(__file__))
DRIVER_DIR=os.path.join(ROOT_DIR,'driver')
sys.path.append(DRIVER_DIR)
print(sys.path)
