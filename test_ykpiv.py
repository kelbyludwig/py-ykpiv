import ykpiv
import pytest

DEFAULT_PIN = b"123456"
DEFAULT_MGM_KEY = b"010203040506070801020304050607080102030405060708"


class TestYKPIV(object):

    state = None

    def setup_class(cls):
        TestYKPIV.state = ykpiv.init()
        readers = ykpiv.list_readers(TestYKPIV.state)
        assert len(readers) >= 1, "no yubikey detected"
        ykpiv.connect(TestYKPIV.state, readers[0])

    def teardown_class(cls):
        ykpiv.done(TestYKPIV.state)

    def test_hex_decode(self):
        assert ykpiv.hex_decode(b"deadbeef") == b"\xde\xad\xbe\xef"
        assert (
            ykpiv.hex_decode(DEFAULT_MGM_KEY)
            == b"\x01\x02\x03\x04\x05\x06\x07\x08\x01\x02\x03\x04\x05\x06\x07\x08\x01\x02\x03\x04\x05\x06\x07\x08"
        )

    def test_verify(self):
        ykpiv.verify(TestYKPIV.state, DEFAULT_PIN)
        with pytest.raises(Exception):
            ykpiv.verify(TestYKPIV.state, b"111111")
        ykpiv.verify(TestYKPIV.state, DEFAULT_PIN)

    def test_get_version(self):
        version = ykpiv.get_version(TestYKPIV.state)
        assert len(version.split(b".")) == 3
