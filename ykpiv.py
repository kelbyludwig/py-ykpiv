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
    readers = ffi.new("char[2048]")
    readers_len = ffi.new("size_t *", 2048)
    rc = _ykpiv.ykpiv_list_readers(state, readers, readers_len)
    _assert_ok(rc)
    return ffi.string(readers)


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
    assert hex_decode(b"deadbeef") == b"\xde\xad\xbe\xef"
    state = init()
    print(list_readers(state))
