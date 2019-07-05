#!/usr/bin/python3
""" class prevents creating new instance"""


class LockedClass:
    """ prevents snu instance unless called first_name"""
    __slot__ ='first_name'
