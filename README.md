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
