#!/usr/bin/env python3

from ctypes import *
lib = cdll.LoadLibrary("./sieve.so")
lib.Sieve.argtypes = [c_longlong]
lib.Sieve(10000)
print("all done, go")
