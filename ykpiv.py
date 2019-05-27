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


def done(state):
    rc = _ykpiv.ykpiv_done(state)
    _assert_ok(rc)


def verify(state, pin):
    pin = ffi.new("const char[]", pin)
    _tries = ffi.new("int *")
    rc = _ykpiv.ykpiv_verify(state, pin, _tries)
    _assert_ok(rc)


def sign_data(state, data):
    # ykpiv_sign_data assumes input is already padded
    assert len(data) == 256
    sign_in = ffi.new("const char []", data)
    in_len = ffi.cast("size_t", len(data))
    sign_out = ffi.new("unsigned char[256]")
    out_len = ffi.new("size_t *", 256)
    algorithm = ffi.cast("unsigned char", _ykpiv.YKPIV_ALGO_RSA2048)
    key = ffi.cast("unsigned char", _ykpiv.YKPIV_KEY_SIGNATURE)  # slot 0x9c
    rc = _ykpiv.ykpiv_sign_data(
        state, sign_in, in_len, sign_out, out_len, algorithm, key
    )
    _assert_ok(rc)
    return ffi.unpack(sign_out, out_len[0])


def hex_decode(hex_ascii):
    hex_ascii_len = len(hex_ascii)
    hex_in = ffi.new("const char[]", hex_ascii)
    hex_in_len = ffi.cast("size_t", hex_ascii_len)
    out_len = hex_ascii_len // 2
    hex_out = ffi.new("unsigned char[]", out_len)
    out_len = ffi.new("size_t *", out_len)
    rc = _ykpiv.ykpiv_hex_decode(hex_in, hex_in_len, hex_out, out_len)
    _assert_ok(rc)
    return bytes(ffi.buffer(hex_out, out_len[0]))
