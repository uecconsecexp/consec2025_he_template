import secrets
from dataclasses import dataclass

P = 2027
G = 2


@dataclass
class PublicKey:
    p: int
    g: int
    h: int


@dataclass
class SecretKey:
    x: int


@dataclass
class Ciphertext:
    c1: int
    c2: int


def keygen(p: int = P, g: int = G) -> tuple[PublicKey, SecretKey]:
    """【課題1-1】ElGamal暗号の実装: 鍵生成アルゴリズムを実装せよ．

    Args:
        p: 素数位数
        g: 生成元

    Returns:
        (PublicKey, SecretKey): 公開鍵と秘密鍵のペア
    """
    pass


def encrypt(public_key: PublicKey, message: int) -> Ciphertext:
    """【課題1-1】ElGamal暗号の実装: 暗号化アルゴリズムを実装せよ．

    Args:
        public_key: 公開鍵
        message: 平文

    Returns:
        Ciphertext: 暗号文
    """
    pass


def decrypt(public_key: PublicKey, secret_key: SecretKey, ciphertext: Ciphertext) -> int:
    """【課題1-1】ElGamal暗号の実装: 復号アルゴリズムを実装せよ．

    Args:
        public_key: 公開鍵
        secret_key: 秘密鍵
        ciphertext: 暗号文

    Returns:
        int: 平文
    """
    pass


def hmul(public_key: PublicKey, ct1: Ciphertext, ct2: Ciphertext) -> Ciphertext:
    """【課題2-1】暗号化したままの乗算を実装せよ．

    Args:
        public_key: 公開鍵
        ct1: 1つめの暗号文
        ct2: 2つめの暗号文

    Returns:
        Ciphertext: 暗号文
    """
    pass


def hpow(public_key: PublicKey, ciphertext: Ciphertext, exponent: int) -> Ciphertext:
    """【課題2-1】暗号化したままの累乗を実装せよ．

    Args:
        public_key: 公開鍵
        ciphertext: 暗号文
        exponent: 指数

    Returns:
        Ciphertext: 暗号文
    """
    pass
