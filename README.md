# はじめに
FastAPIを使ってAPIサーバーを構築する際のテンプレートです。  
パッケージ管理にはpoetryを使用しています。  

# 目次
- [はじめに](#はじめに)
- [目次](#目次)
- [準備](#準備)

# 準備
## VSCode拡張機能のインストールと設定<!-- omit in toc -->
### インストール編<!-- omit in toc -->
以下のコマンドを実行して、Visual Studio Codeに必要な拡張機能をインストールしてください。
```sh
# 日本語化
code --install-extension MS-CEINTL.vscode-language-pack-ja
# Python開発必須
code --install-extension ms-python.black-formatter
code --install-extension ms-python.flake8
code --install-extension ms-python.isort
code --install-extension ms-python.mypy-type-checker
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
# 便利ツール
code --install-extension eamodio.gitlens
code --install-extension Gruntfuggly.todo-tree
code --install-extension oderwat.indent-rainbow
code --install-extension shardulm94.trailing-spaces
code --install-extension yzhang.markdown-all-in-one
# Github Copilot
code --install-extension GitHub.copilot
code --install-extension GitHub.copilot-chat
```

### 設定編<!-- omit in toc -->
Visual Studio Codeの設定は、以下のように行ってください。
```sh
mkdir .vscode
touch .vscode/settings.json
```
下記を記述
```json
{
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        },
    },
    "isort.args":[
        "--settings-file", "pyproject.toml"
    ],
    "flake8.args": [
        "--max-line-length","120",
        "--max-complexity", "10",
        "--ignore", "E203, W503",
        "--exclude", ".venv,.git,__pycache__"
    ],
    "black-formatter.args": [
        "--config", "pyproject.toml"
    ],
    "mypy-type-checker.args": [
        "--config-file=pyproject.toml"
    ]
}
```