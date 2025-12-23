# コンテンツセキュリティ実験2周目: 準同型暗号実装

本実験では，Pythonを使ってElGamal暗号を実装します．
穴埋め形式でコードを完成させながら，公開鍵暗号と準同型暗号の基礎を学びます．

## 本実験の構成

本実験では前述の通り，簡単なElGamal暗号を実装します．
ElGamal暗号を実装したら，その準同型性を用いて実際にいくつかの計算を行ってもらいます．

また，余力がある人向けに発展課題を用意しています．

課題の提出フォーマットは[この資料](./docs/submission_guide.md)を参照してください．

## 事前準備

本実験では，Gitとuvを使用します．IEDへのインストール方法や基本的な使い方は，一週目で挙げられている参考資料を参照してください．

次のコマンドをターミナルで実行し，本リポジトリを取得してください．

```bash
git clone https://github.com/uecconsecexp/consec2025_he_template.git consec2025_he
```

次のコマンドを実行し，依存パッケージ及び仮想環境の構築をしてください．

```bash
cd consec2025_he
uv sync
```

## 課題について

`src/he`以下にあるファイルを編集して，ElGamal暗号を実装してもらいます．
それぞれのファイルの実装は穴開きになっているので，穴を埋める形で正しく実装してください．

各々課題毎に実行するコマンドは異なりますが，主には以下のコマンドを実行して，正しく実装されているかをテストします．


```bash
uv run pytest
```

また，課題については以下の通りです．
以下で実装したプログラムは，指示がない限りレポートに載せる必要はないです．


### 課題1

1. `src/he/elgamal.py`の指示コメントに従ってElGamal暗号を実装せよ．
1. `tests/test_kadai1.py`にある`Kadai1`クラスの指示コメントに従って，正当性を確認するテストを書け．なお，テストを実行するコマンドは以下である．

    ```bash
    uv run pytest tests/test_kadai1.py -v
    ```
1. ElGamal暗号の正当性（正しく復号できること）が成り立つことを実際に確認せよ．


### 課題2

1. 課題1で実装したElGamal暗号をベースに，`src/he/elgamal.py`の指示コメントに従って，暗号化したまま平文同士の乗算を行う関数`hmul`及び累乗を行う関数`hpow`を実装せよ．
1. `tests/test_kadai2.py`の`Kadai2`クラスの指示コメントに従って，正しく乗算及び累乗ができているかを確認するテストを書け．なお，テストを実行するコマンドはそれぞれ以下である．

    ```bash
    uv run pytest tests/test_kadai2.py::TestKadai2::test_hmul -v
    uv run pytest tests/test_kadai2.py::TestKadai2::test_hpow -v
    ```
1. `tests/test_kadai2.py`にある`Kadai2`クラスの指示コメントに従って，乗算及び累乗を行うプログラム及びテストを書け．なお，テストを実行するコマンドはそれぞれ以下である．

    ```bash
    uv run pytest tests/test_kadai2.py::TestKadai2::test_many_hmul -v
    uv run pytest tests/test_kadai2.py::TestKadai2::test_hmul_and_hpow -v
    ```
1. ElGamal暗号の加法準同型性が成り立つことを実際に確認せよ．


### 課題3

課題1及び2が完成した人のみ取り組んでください．

1. `src/he/lifted_elgamal.py`の指示コメントに従って，Lifted ElGamal暗号を実装せよ．
1. `tests/test_kadai3.py`にある`Kadai3`クラスの指示コメントに従って，正しく動作するかを確認するテストを書け．なお，テストを実行するコマンドは以下である．

    ```bash
    uv run pytest tests/test_kadai3.py::TestKadai3::test_correctness -v
    ```
1. Lifted ElGamal暗号の正当性が成り立つことを実際に確認せよ．
1. 実装したLifted ElGamal暗号をベースに，`src/he/lifted_elgamal.py`の指示コメントに従って，暗号化したまま平文同士の加算を行う関数`hadd`及びスカラー倍を行う関数`hscalar`を実装せよ．
1. Lifted ElGamal暗号の加法準同型性が成り立つことを実際に確認せよ．
1. `tests/test_kadai3.py`の`Kadai3`クラスの指示コメントに従って，正しく加算及びスカラー倍ができているかを確認するテストを書け．なお，テストを実行するコマンドはそれぞれ以下である．

    ```bash
    uv run pytest tests/test_kadai2.py::TestKadai3::test_hmul -v
    uv run pytest tests/test_kadai2.py::TestKadai3::test_hscalar -v
    ```
1. `tests/test_kadai3.py`にある`Kadai3`クラスの指示コメントに従って，加算及びスカラー倍を計算するプログラム及びテストを書け．

    ```bash
    uv run pytest tests/test_kadai2.py::TestKadai3::test_many_hadd -v
    uv run pytest tests/test_kadai2.py::TestKadai3::test_hadd_and_hscalar -v
    ```
1. 上記で実装した平均を計算するプログラムにおいて復号を許しているが，この妥当性について安全性の面から考察せよ．
1. 今回，Lifted ElGamal暗号の実装に用いているパラメータは実際に使用されているものと比較して小さい．実際の大きいパラメータを用いた際（楕円曲線を用いた場合，位数は$2^{256}$程度）に考慮すべきことについて考察せよ．
