"""ucryptolib – cryptographic ciphers
"""

from typing import Optional, Any, overload
class aes:
    def __init__(self, key: bytes, mode: int, IV: Optional[Any]) -> None:
        """
        Initialize cipher object, suitable for encryption/decryption.
        Note: after initialization, cipher object can be use only either for encryption or decryption.
        Running decrypt() operation after encrypt() or vice versa is not supported.

        Parameters are:

            key is an encryption/decryption key (bytes-like).
            mode is:

                1 (or ucryptolib.MODE_ECB if it exists) for Electronic Code Book (ECB).
                2 (or ucryptolib.MODE_CBC if it exists) for Cipher Block Chaining (CBC).
                6 (or ucryptolib.MODE_CTR if it exists) for Counter mode (CTR).

            IV is an initialization vector for CBC mode.
            For Counter mode, IV is the initial value for the counter.



        :param key: Key is an encryption/decryption key (bytes-like).
        :param mode: Mode.
        :param IV: Initialization vector for CBC mode.

        :type key: bytes
        :type mode: int
        :type IV: Any
        """
        ...

    @overload
    def encrypt(self, in_buf: Any, out_buf: Any) -> None:
        """
        Encrypt in_buf. If no out_buf is given result is returned as a newly allocated bytes object.
        Otherwise, result is written into mutable buffer out_buf.
        in_buf and out_buf can also refer to the same mutable buffer, in which case data is encrypted in-place.

        :param in_buf: Input.
        :param out_buf: Output.

        :type in_buf: Any
        :type out_buf: Any
        """
        ...
    @overload
    def encrypt(self, in_buf: Any) -> bytes:
        """
        :param in_buf: Input
        :type in_buf: Any

        :return: Encrypted bytes object.
        :rtype: bytes
        """
        ...

    @overload
    def decrypt(self, in_buf: Any, out_buf: Any) -> None:
        """
        Like encrypt(), but for decryption.

        :param in_buf: Input.
        :param out_buf: Output.

        :type in_buf: Any
        :type out_buf: Any
        """
        ...

    @overload
    def decrypt(self, in_buf: Any) -> bytes:
        """
        :param in_buf: Input
        :type in_buf: Any

        :return: Encrypted bytes object.
        :rtype: bytes
        """
        ...

MODE_ECB: int
MODE_CBC: int
MODE_CTR: int