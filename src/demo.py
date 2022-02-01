import ctypes
import pathlib
import os

base = pathlib.Path()
lib_address = (base / "mylib.so").resolve()
print(lib_address)

mylib = ctypes.CDLL(lib_address)

r = mylib.myFunction(ctypes.c_int(4))
print(r)

