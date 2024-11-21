import os
import csv
def main():
    csv_file = "zenkoku.csv" #csvファイル取得
    index_file = "index.pkl"

    # インデックスファイルの作成(初回だけ)
    if not os.path.exists(index_file):
        #インデックス作成処理
        print('ok')
    
    # 検索クエリ取得
    query = input("検索文字列入力: ").strip()

    #2-gram検索処理
    results = results

    #コンソール出力

if __name__ == "__main__":
    main()