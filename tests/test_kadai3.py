import pytest

from he import (
    Ciphertext,
    P,
    PublicKey,
    SecretKey,
    decrypt_lifted,
    encrypt_lifted,
    hadd,
    hscalar,
    keygen,
)


class TestKadai3:
    """
    【課題3】Lifted ElGamal暗号及び準同型性を用いた様々な演算の実装
    """

    def test_correctness(self):
        """【課題3-2】Lifted ElGamal暗号の実装テスト
        - 正しく生成した鍵で，正しく生成した平文mの暗号文を復号すると，必ずmを得られることをテストせよ．
        """
        pass

    def test_hadd(self):
        """【課題3-4】haddが正しく実装できているかをテストせよ"""
        pass

    def test_many_hadd(self):
        """【課題3-5】複数の平文（4つ以上）を暗号化したまま平均を求めるプログラムを書け．ただし，1回の復号を許す．"""
        pass

    def test_hadd_and_hscalar(self):
        """【課題3-5】haddとhscalarを用いて，以下を計算せよ．
        変数x, y, zに対して，1234 * x + 3456 * y + 5678 * z．
        """
        pass
