import ykpiv


class TestYKPIV(object):

    state = None

    def setup_class(cls):
        TestYKPIV.state = ykpiv.init()
        readers = ykpiv.list_readers(TestYKPIV.state)
        assert len(readers) >= 1, "no yubikey detected"
        ykpiv.connect(TestYKPIV.state, readers[0])

    def teardown_class(cls):
        ykpiv.disconnect(TestYKPIV.state)

    def test_hex_decode(self):
        assert ykpiv.hex_decode(b"deadbeef") == b"\xde\xad\xbe\xef"
        assert (
            ykpiv.hex_decode(b"010203040506070801020304050607080102030405060708")
            == b"\x01\x02\x03\x04\x05\x06\x07\x08\x01\x02\x03\x04\x05\x06\x07\x08\x01\x02\x03\x04\x05\x06\x07\x08"
        )
