import secrets

from .elgamal import Ciphertext, G, P, PublicKey, SecretKey


def encrypt_lifted(public_key: PublicKey, message: int) -> Ciphertext:
    """【課題3-1】Lifted ElGamal暗号実装: 暗号化アルゴリズムを実装せよ．

    Args:
        public_key: 公開鍵
        message: 平文

    Returns:
        Ciphertext: 暗号文
    """
    pass


def decrypt_lifted(public_key: PublicKey, secret_key: SecretKey, ciphertext: Ciphertext) -> int:
    """【課題3-1】Lifted ElGamal暗号実装: 復号アルゴリズムを実装せよ．

    Args:
        public_key: 公開鍵
        secret_key: 秘密鍵
        ciphertext: 暗号文

    Returns:
        int: 平文
    """
    pass


def hadd(public_key: PublicKey, ct1: Ciphertext, ct2: Ciphertext) -> Ciphertext:
    """【課題3-3】暗号化したままの加算を実装せよ．

    Args:
        public_key: 公開鍵
        ct1: 1つめの暗号文
        ct2: 2つめの暗号文

    Returns:
        Ciphertext: 暗号文
    """
    pass


def hscalar(public_key: PublicKey, ciphertext: Ciphertext, scalar: int) -> Ciphertext:
    """【課題3-3】暗号化したままの乗算を実装せよ．

    Args:
        public_key: 公開鍵
        ciphertext: 暗号文
        scalar: スカラー値

    Returns:
        Ciphertext: 暗号文
    """
    pass
