# poc-hatch

## 以下の手順で初期構築

```console
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install hatch
hatch new --cli poc_hatch
mv poc-hatch/* .
rmdir poc-hatch
```

## パッケージのビルド

```console
hatch build
```

dist ディレクトリ配下に生成される

テスト環境用意

```console
python3 -m venv test_venv
source test_venv/bin/activate
pip install --find-links=./dist/ poc_hatch
```

下記で実行確認できる

```console
poc-hatch
```

環境削除は以下を実施

```console
deactivate
rm -rf test_venv/
```
