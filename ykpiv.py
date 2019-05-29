from _ykpiv_cffi import ffi, lib as _ykpiv


def _assert_ok(rc):
    if rc != _ykpiv.YKPIV_OK:
        raise Exception("not ok dude: %d", rc)


def init(verbose=False):
    """Initializes and returns a ykpiv_state object that is used as an input to
    most libykpiv calls.
    """
    state_handle = ffi.new("ykpiv_state **")
    rc = _ykpiv.ykpiv_init(state_handle, verbose)
    _assert_ok(rc)
    return state_handle[0]


def list_readers(state):
    """Returns a list of available smart cards.
    """
    buffer_size = 2048
    readers = ffi.new("char[]", buffer_size)
    readers_len = ffi.new("size_t *", buffer_size)
    rc = _ykpiv.ykpiv_list_readers(state, readers, readers_len)
    _assert_ok(rc)
    readers_list_bytes = ffi.unpack(readers, buffer_size)
    readers_list_bytes = readers_list_bytes.rstrip(b"\x00")
    parts = readers_list_bytes.split(b"\x00")
    if len(parts) == 1 and parts[0] == b"":
        return []
    return parts


def connect(state, wanted):
    """Connect to the smart card corresponding to the `wanted` value.

    `wanted` will likely be a value from `list_readers`.
    """
    wanted = ffi.new("const char[]", wanted)
    rc = _ykpiv.ykpiv_connect(state, wanted)
    _assert_ok(rc)


def disconnect(state):
    """Disconnect from a smart card.

    `disconnect` is called within `done` so it is preferred to call `done`.
    """
    rc = _ykpiv.ykpiv_disconnect(state)
    _assert_ok(rc)


def done(state):
    """Terminate a connection with a smart card and cleanup.

    `done` does additional cleanup work that `disconnect` does not so usage of
    `done` is preferred.
    """
    rc = _ykpiv.ykpiv_done(state)
    _assert_ok(rc)


def verify(state, pin):
    """Authenticate to the smart card using the provided user PIN.
    """
    pin = ffi.new("const char[]", pin)
    _tries = ffi.new("int *")
    rc = _ykpiv.ykpiv_verify(state, pin, _tries)
    _assert_ok(rc)


def sign_data(state, data):
    """Use a slots private key to sign `data`.

    TODO(kkl): Both the slot and the algorithm are hardcoded. Parameterize.
    """
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


def decipher_data(state, data):
    """Use a slots private key to decrypt `data`.

    TODO(kkl): Both the slot and the algorithm are hardcoded. Parameterize.
    """
    # ykpiv_decipher_data assumes input is already padded
    assert len(data) == 256
    ciphertext_in = ffi.new("const char []", data)
    ciphertext_len = ffi.cast("size_t", len(data))
    plaintext_out = ffi.new("unsigned char[256]")
    plaintext_len = ffi.new("size_t *", 256)
    algorithm = ffi.cast("unsigned char", _ykpiv.YKPIV_ALGO_RSA2048)
    key = ffi.cast("unsigned char", _ykpiv.YKPIV_KEY_SIGNATURE)  # slot 0x9c
    rc = _ykpiv.ykpiv_decipher_data(
        state,
        ciphertext_in,
        ciphertext_len,
        plaintext_out,
        plaintext_len,
        algorithm,
        key,
    )
    _assert_ok(rc)
    return ffi.unpack(plaintext_out, plaintext_len[0])


def get_version(state):
    """Get the version string for the connected smart card. 
    """
    version = ffi.new("char []", 256)
    version_len = ffi.cast("size_t", 256)
    rc = _ykpiv.ykpiv_get_version(state, version, version_len)
    _assert_ok(rc)
    return ffi.string(version)


def authenticate(state, key):
    """Authenticate to a smart card using the provided management key.
    """
    decoded_key = bytes.fromhex(str(key, "ascii"))
    key = ffi.new("const char[]", decoded_key)
    rc = _ykpiv.ykpiv_authenticate(state, key)
    _assert_ok(rc)


def hex_decode(hex_ascii):
    """Decodes `hex_ascii`, a string of hex ascii characters, into the byte representation.
    """
    hex_ascii_len = len(hex_ascii)
    hex_in = ffi.new("const char[]", hex_ascii)
    hex_in_len = ffi.cast("size_t", hex_ascii_len)
    out_len = hex_ascii_len // 2
    hex_out = ffi.new("unsigned char[]", out_len)
    out_len = ffi.new("size_t *", out_len)
    rc = _ykpiv.ykpiv_hex_decode(hex_in, hex_in_len, hex_out, out_len)
    _assert_ok(rc)
    return bytes(ffi.buffer(hex_out, out_len[0]))
