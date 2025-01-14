'''
Use panda_aarch64.h to compile
'''
from cffi import FFI
ffibuilder = FFI()
total = open("panda_aarch64.h").read()

ffibuilder.set_source("panda_aarch64", None)
ffibuilder.cdef(total, override=True)
ffibuilder.compile(debug=True)

from panda_aarch64 import ffi
from os.path import realpath

# build a basic shared object (it's fine because we don't really use it)
from subprocess import check_output
check_output("make -C make_so", shell=True)
aarch64 = realpath("make_so/hello.so")
panda_aarch64 = ffi.dlopen(aarch64, ffi.RTLD_GLOBAL)

pcwc = ffi.new("panda_cb*") # fails here