import pytest

from onyx.utils.encryption import encrypt_string_to_bytes, decrypt_bytes_to_string


def test_encrypt_decrypt_roundtrip() -> None:
    original = "secret-data"
    encrypted = encrypt_string_to_bytes(original)
    assert isinstance(encrypted, bytes)
    decrypted = decrypt_bytes_to_string(encrypted)
    assert decrypted == original
