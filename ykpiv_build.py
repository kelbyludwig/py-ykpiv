from cffi import FFI

ffibuilder = FFI()

with open("include/ykpiv.h", "r") as f:
    ffibuilder.cdef(f.read())

includes = """
#include <ykpiv.h>
"""

ffibuilder.set_source(
    "_ykpiv_cffi",
    includes,
    libraries=["ykpiv"],
    include_dirs=["/usr/local/include/ykpiv"],
    extra_objects=["/usr/local/lib/libykpiv.dylib"],
)
if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
