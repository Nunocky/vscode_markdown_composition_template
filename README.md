# Markdown to PDF template for VSCode

VSCodeで markdownを使った組版を行うワークスペースのテンプレート


## 組版の方法

### files.jsonの編集

pdf化したいファイルを files.jsonに列挙する。jsonオブジェクトは文字列の配列。

### make

makeコマンドで INPUT.mdが作成される。

### 目次作成

必要なら INPUT.mdを編集して目次を作成する (Markdown All in One, Markdown TOCなどを使用)。

### pdf化

markdown-pdfで PDF化。output以下にファイルが作成される。

