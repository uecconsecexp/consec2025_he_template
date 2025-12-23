from he import Ciphertext, P, PublicKey, SecretKey, decrypt, encrypt, hmul, hpow, keygen


class TestKadai2:
    """
    【課題2】ElGamal暗号の準同型演算の実装
    """

    def test_hmul(self):
        """【課題2-2】hmulが正しく実装できているかをテストせよ"""
        pass

    def test_hpow(self):
        """【課題2-2】hpowが正しく実装できているかをテストせよ"""
        pass

    def test_many_hmul(self):
        """【課題2-3】複数の平文（4つ以上）を暗号化したまま乗算するプログラムを書け"""
        pass

    def test_hmul_and_hpow(self):
        """【課題2-4】多項式を暗号化したまま評価するプログラムを書け．
        具体的には，変数x, y, zに対して，x^123 * y^456 * z^789を評価せよ．
        """
        pass
