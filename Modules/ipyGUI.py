# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 09:48:59 2018

@author: Truong
"""
'''
    This works on ipython
'''
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

def func(x):
    return x**2

interact(func,x = 10)
