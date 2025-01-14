from cffi import FFI

ffibuilder = FFI()
total = open("panda_aarch64.h").read()

ffibuilder.set_source("panda_aarch64", None)
ffibuilder.cdef(total, override=True)
ffibuilder.compile(debug=True)

from panda_aarch64 import ffi
from os.path import realpath
aarch64 = realpath("libpanda-aarch64-softmmu.so")
panda_aarch64 = ffi.dlopen(aarch64, ffi.RTLD_GLOBAL)

pcwc = ffi.new("panda_cb*")