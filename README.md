# py-ykpiv

Python bindings for the `ykpiv` library.

Tested with a Yubikey Neo and `ykpiv` bundled with version 1.6.1 of `yubico-piv-tool` on macOS.

# should i use this?

no, probably not.

# support

| ykpiv function                     | implemented? | py-ykpiv function |
|------------------------------------|--------------|-------------------|
| `ykpiv_init`                       | ✅           | `init`            |
| `ykpiv_done`                       | ✅           | `done`            |
| `ykpiv_connect`                    | ✅           | `connect`         |
| `ykpiv_list_readers`               | ✅           | `list_readers`    |
| `ykpiv_disconnect`                 | ✅           | `disconnect`      |
| `ykpiv_authenticate`               | ✅           | `authenticate`    |
| `ykpiv_sign_data`                  | ✅           | `sign_data`       |
| `ykpiv_get_version`                | ✅           | `get_version`     |
| `ykpiv_verify`                     | ✅           | `verify`          |
| `ykpiv_decipher_data`              | ✅           | `decipher_data`   |
| `ykpiv_transfer_data`              | ⛔           |                   |
| `ykpiv_set_mgmkey`                 | ⛔           |                   |
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
| `ykpiv_util_free`                  | ⛔           |                   |
| `ykpiv_util_list_keys`             | ⛔           |                   |
| `ykpiv_util_read_cert`             | ⛔           |                   |
| `ykpiv_util_write_cert`            | ⛔           |                   |
| `ykpiv_util_delete_cert`           | ⛔           |                   |
| `ykpiv_util_generate_key`          | ⛔           |                   |
| `ykpiv_util_get_config`            | ⛔           |                   |
| `ykpiv_util_set_pin_last_changed`  | ⛔           |                   |
| `ykpiv_util_get_derived_mgm`       | ⛔           |                   |
| `ykpiv_util_get_protected_mgm`     | ⛔           |                   |
| `ykpiv_util_set_protected_mgm`     | ⛔           |                   |
| `ykpiv_util_reset`                 | ⛔           |                   |
| `ykpiv_util_get_cardid`            | ⛔           |                   |
| `ykpiv_util_set_cardid`            | ⛔           |                   |
| `ykpiv_util_get_cccid`             | ⛔           |                   |
| `ykpiv_util_set_cccid`             | ⛔           |                   |
| `ykpiv_util_block_puk`             | ⛔           |                   |
| `ykpiv_util_read_mscmap`           | ⛔           |                   |
| `ykpiv_util_write_mscmap`          | ⛔           |                   |
| `ykpiv_util_read_msroots`          | ⛔           |                   |
| `ykpiv_util_write_msroots`         | ⛔           |                   |
