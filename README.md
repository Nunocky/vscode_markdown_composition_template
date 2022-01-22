# Markdown composition template for VSCode

VSCodeで markdownを使った組版を行うワークスペースを作成するためのテンプレート


## 導入

[yuanhjty/code-template-tool](https://github.com/yuanhjty/code-template-tool)を VSCodeにインストール

<img width="607" alt="スクリーンショット 2022-01-22 午後4 15 30" src="https://user-images.githubusercontent.com/750091/150629225-2e4e348f-d4db-4700-81b8-389a63874b13.png">

このプロジェクトを `~/.vscode/templates`以下に展開

``` sh
cd ~/.vscode/templates
git clone git@github.com:Nunocky/vscode_markdown_composition_template.git
```

コマンドパレットから `template: Reload Templates` を実行

<img width="249" alt="スクリーンショット 2022-01-22 午後4 17 09" src="https://user-images.githubusercontent.com/750091/150629236-bc110a3c-7a05-4277-918c-514701bcd540.png">


## テンプレートの利用方法

コマンドパレットから `template: New File/Folder From Template`を実行

<img width="345" alt="スクリーンショット 2022-01-22 午後4 27 02" src="https://user-images.githubusercontent.com/750091/150629488-784b29cc-6947-4654-bdc8-2e7c27740c10.png">

作業ディレクトリ、タイトル、著者名を入力して `Confirm`

<img width="905" alt="スクリーンショット 2022-01-22 午後4 30 09" src="https://user-images.githubusercontent.com/750091/150629498-cd66ef76-0ba5-48f8-ac63-aee2c0c2372b.png">

メニュー `ファイル→ファイルでワークスペースを開く` で、上記ディレクトリの `*.code-workspace`を開く。

## 組版の手順

### 使用する VSCodeプラグイン

* Markdown PDF
  * markdown → pdfの変換を行う。

* Markdown TOC, Markdown All in One (optional)
  * 目次作成。どちらか好きな方を。
  * Markdown TOCはセクション番号を付与してくれるが、レイアウトがいまいち
  * Markdown All in One は markdown 編集に便利な機能も提供してくれる。

### ファイル編集

markdownファイルを書く。 章ごとにファイルに分けてもいい。

### files.jsonの編集

pdf化したい markdownファイルを files.jsonに列挙する。jsonオブジェクトは文字列の配列。

### make

ターミナルから makeコマンド実行。 ファイルが結合され INPUT.mdが作成される。

必要なら INPUT.mdを編集して目次を作成する。

### pdf化

markdown-pdfで INPUT.mdを PDF化する。output以下にファイルが作成される。


## 参考
* [VSCodeとMarkdownで技術同人誌書いたので拡張機能とかまとめ](https://qiita.com/reona396/items/40b234108f7664267db8#comment-2daa99ab4468e7961ae6)
* [Markdown PDF のスタイル(CSS)を変える方法](https://h-s-hige.hateblo.jp/entry/20190405/1554467885)
* [Markdownにおける目次(TOC)の作成に、Markdown All in Oneが便利だった件](https://qiita.com/eyuta/items/b1a53f3da8c5f8e7f41d) ... 見出し番号を付ける方法
