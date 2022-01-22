# Markdown composition template for VSCode

VSCodeで markdownを使った組版を行うワークスペースのテンプレート


## 導入

[yuanhjty/code-template-tool](https://github.com/yuanhjty/code-template-tool)を VSCodeにインストール


このプロジェクトを `~/.vscode/templates`以下に展開

``` sh
cd ~/.vscode/templates
git clone git@github.com:Nunocky/vscode_markdown_composition_template.git
```

VSCodeで `Template: reload templates`する


## 組版の方法

### 使用するプラグイン

* Markdown PDF
  * タイトルどおり、markdown -> pdfの変換を行う。

* Markdown TOC, Markdown All in One (optional)
  * 目次作成。どちらか好きな方を。
  * Markdown TOCはセクション番号を付与してくれるが、レイアウトがいまいち
  * Markdown All in One は markdown 編集に便利な機能も提供してくれるが、セクション番号は付けてくれない。

### files.jsonの編集

pdf化したいファイルを順に files.jsonに列挙する。jsonオブジェクトは文字列の配列。

### make

ターミナルから makeコマンド実行。 INPUT.mdが作成される。

### 目次作成

必要なら INPUT.mdを編集して目次を作成する。

### pdf化

markdown-pdfで PDF化。output以下にファイルが作成される。
