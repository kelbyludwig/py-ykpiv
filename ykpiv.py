from _ykpiv_cffi import ffi, lib as _ykpiv


def _assert_ok(rc):
    if rc != _ykpiv.YKPIV_OK:
        raise Exception("not ok dude: %d", rc)


def init(verbose=False):
    state_handle = ffi.new("ykpiv_state **")
    rc = _ykpiv.ykpiv_init(state_handle, verbose)
    _assert_ok(rc)
    return state_handle[0]


def list_readers(state):
    buffer_size = 2048
    readers = ffi.new("char[%d]" % buffer_size)
    readers_len = ffi.new("size_t *", buffer_size)
    rc = _ykpiv.ykpiv_list_readers(state, readers, readers_len)
    _assert_ok(rc)
    readers_list_bytes = ffi.unpack(readers, buffer_size)
    readers_list_bytes = readers_list_bytes.rstrip(b"\x00")
    return readers_list_bytes.split(b"\x00")


def connect(state, wanted):
    wanted = ffi.new("const char[]", wanted)
    rc = _ykpiv.ykpiv_connect(state, wanted)
    _assert_ok(rc)


def disconnect(state):
    rc = _ykpiv.ykpiv_disconnect(state)
    _assert_ok(rc)


def hex_decode(hex_ascii):
    hex_ascii_len = len(hex_ascii)
    hex_in = ffi.new("const char[]", hex_ascii)
    hex_in_len = ffi.cast("size_t", hex_ascii_len)
    hex_out = ffi.new("unsigned char *")
    out_len = ffi.new("size_t *", hex_ascii_len // 2)
    rc = _ykpiv.ykpiv_hex_decode(hex_in, hex_in_len, hex_out, out_len)
    _assert_ok(rc)
    return ffi.string(hex_out)


if __name__ == "__main__":
    # simple functional test
    import sys

    assert hex_decode(b"deadbeef") == b"\xde\xad\xbe\xef"
    state = init(verbose=True)
    readers = list_readers(state)
    if not len(readers):
        print("no readers to connect to")
        sys.exit(1)
    connect(state, readers[0])
    disconnect(state)
    print("done!")
