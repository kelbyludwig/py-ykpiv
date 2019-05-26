# py-ykpiv

Python bindings for the `ykpiv` library.

Tested with a Yubikey Neo and `ykpiv` bundled with version 1.6.1 of `yubico-piv-tool` on macOS.

# support

| ykpiv function                     | implemented? | py-ykpiv function |
|------------------------------------|--------------|-------------------|
| `ykpiv_init`                       | ✅           | `init`            |
| `ykpiv_done`                       | ⛔           |                   |
| `ykpiv_connect`                    | ✅           | `connect`         |
| `ykpiv_list_readers`               | ✅           | `list_readers`    |
| `ykpiv_disconnect`                 | ✅           | `disconnect`      |
| `ykpiv_transfer_data`              | ⛔           |                   |
| `ykpiv_authenticate`               | ⛔           |                   |
| `ykpiv_set_mgmkey`                 | ⛔           |                   |
| `ykpiv_hex_decode`                 | ✅           | `hex_decode`      |
| `ykpiv_sign_data`                  | ✅           | `sign_data`       |
| `ykpiv_decipher_data`              | ⛔           |                   |
| `ykpiv_get_version`                | ⛔           |                   |
| `ykpiv_verify`                     | ✅           | `verify`          |
| `ykpiv_change_pin`                 | ⛔           |                   |
| `ykpiv_change_puk`                 | ⛔           |                   |
| `ykpiv_unblock_pin`                | ⛔           |                   |
| `ykpiv_fetch_object`               | ⛔           |                   |
| `ykpiv_set_mgmkey2`                | ⛔           |                   |
| `ykpiv_save_object`                | ⛔           |                   |
| `ykpiv_import_private_key`         | ⛔           |                   |
| `ykpiv_attest`                     | ⛔           |                   |
| `ykpiv_get_pin_retries`            | ⛔           |                   |
| `ykpiv_set_pin_retries`            | ⛔           |                   |
| `ykpiv_connect_with_external_card` | ⛔           |                   |
| `ykpiv_done_with_external_card`    | ⛔           |                   |
| `ykpiv_verify_select`              | ⛔           |                   |
| `ykpiv_get_serial`                 | ⛔           |                   |
| `ykpiv_util_*`                     | ⛔           |                   | 
