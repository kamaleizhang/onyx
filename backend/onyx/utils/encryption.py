from onyx.configs.app_configs import ENCRYPTION_KEY_SECRET
from onyx.utils.logger import setup_logger
from onyx.utils.variable_functionality import fetch_versioned_implementation

logger = setup_logger()


def _encrypt_string(input_str: str) -> bytes:
    if ENCRYPTION_KEY_SECRET:
        logger.warning("MIT version of Onyx does not support encryption of secrets.")
    return input_str.encode()


def _decrypt_bytes(input_bytes: bytes) -> str:
    # No need to double warn. If you wish to learn more about encryption features
    # refer to the Onyx EE code
    return input_bytes.decode()


def encrypt_string_to_bytes(input_str: str) -> bytes:
    """Encode a string as bytes for storage.

    Historically this function accidentally used a misspelled parameter name
    ``intput_str`` which made the API a little confusing.  The parameter name
    has been corrected to ``input_str``.  The underlying behaviour is
    unchanged; the string is passed to the versioned encryption implementation
    which may simply return the encoded bytes in the MIT edition.
    """

    versioned_encryption_fn = fetch_versioned_implementation(
        "onyx.utils.encryption", "_encrypt_string"
    )
    return versioned_encryption_fn(input_str)


def decrypt_bytes_to_string(input_bytes: bytes) -> str:
    """Decode bytes previously produced by ``encrypt_string_to_bytes``."""

    versioned_decryption_fn = fetch_versioned_implementation(
        "onyx.utils.encryption", "_decrypt_bytes"
    )
    return versioned_decryption_fn(input_bytes)
