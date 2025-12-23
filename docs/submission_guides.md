# 課題提出のフォーマット

課題提出の際，以下のようにファイル・フォルダを構成して下さい．

```
week2_{学籍番号}_{氏名}
|
├── src
│   ├── __init__.py
│   ├── elgamal.py
│   └── lifted_elgamal.py
├── tests
│   ├── test_kadai1.py
│   ├── test_kadai2.py
│   └── test_kadai3.py
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
├── uv.lock
└── week2_report_{学籍番号}_{氏名}.pdf
```

## 注意点

- `.venv` フォルダは必ず除外して下さい．容量オーバーとなり，提出できない可能性があります．
- 学籍番号`1234567`，氏名`電通 太郎`の場合，フォルダ名は`week2_1234567_電通太郎`となります．
- レポートの作成方法は任意ですが（Word, LaTeX, Markdownなど），必ずPDFに変換して下さい．
