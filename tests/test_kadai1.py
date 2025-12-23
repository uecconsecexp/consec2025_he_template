from he import Ciphertext, G, P, PublicKey, SecretKey, decrypt, encrypt, keygen


class TestKadai1:
    """
    【課題1-2】ElGamal暗号の実装テスト
    """

    def test_example(self):
        """【例】鍵生成についてのテスト"""
        # 1. 鍵生成
        public_key, secret_key = keygen()

        # 2. 指定した定数を使っているかをテスト
        assert public_key.p == P and public_key.g == G

    def test_correctness(self):
        """【課題1-2】ElGamal暗号の実装テスト
        - 正しく生成した鍵で，正しく生成した平文mの暗号文を復号すると，必ずmを得られることをテストせよ．
        """
        pass
