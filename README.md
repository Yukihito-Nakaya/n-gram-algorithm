# n-gram-algorithm
technical exam

# 開発環境
    ・macOS
    ・Python 3.9.6

### 追加 package
    ・chardet #csvエンコード

# 利用方法

### 事前準備
    （ http://jusyo.jp/downloads/new/csv/csv_zenkoku.zip ）をダウンロードし解凍後同ディレクトリに配置してください
    ・pip3 install chardet (pip install chardet)
    ・python3 encoding.py  (python encoding.py)

### 検索処理
    ・pyhton3 n-gram.py (pyhton n-gram.py)
    ・コンソールに「検索文字列入力:」が出力されるので任意の文字(問題の例題では都都道府県や、地名等)を入力しEnterを押下してください
    ・検索情報が出力されます。
    ・一致するもがなければ一致するものが見つかりませんでしたと表示されます。

# 技術説明

## 概要
    与えられたデータセットから単語を高速に検索し、一致する文章または、部分一致する単語が含まれる文章を返します。
    ・転置インデックスを利用して単語と文書IDのマッピングを高速に検索を行う
    ・接頭辞木を利用して部分一致検索を効率的に実行
    ・拡張性、データ件数が増加する可能性もあると考えています。

## データフロー

### データ登録
    ユーザーは文書IDとその内容を入力します。
    転置インデックスとTrieの両方にデータが登録されます。
    転置インデックス: 単語ごとに文書IDを登録。
    Trie: 単語の各文字を追加し、文書IDを登録。

### 検索
    完全一致検索: 転置インデックスにキーとして単語を入力し、結果を取得します。
    部分一致検索: Trieに接頭辞を入力し、該当する文書IDのセットを返します。
