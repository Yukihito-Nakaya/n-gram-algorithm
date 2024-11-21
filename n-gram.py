import os
import csv
import pickle
from collections import defaultdict

#転置インデックス作成
def create_index(csv_file,index_file):
    index = defaultdict(list)
    columns =["郵便番号","都道府県", "市区町村", "町域", "京都通り名", "字丁目", "事業所名", "事業所住所"]

    with open(csv_file, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for id , row in enumerate(reader):
            for col in columns:
                text = row[col]
                if text:
                    text = text.replace(" ", "").replace(" ", "")
                    for i in range(len(text) - 1):
                        token = text[i:i + 2]
                        index[token].append(id)
    # インデックのファイル保存
    with open(index_file,"wb") as file:
        pickle.dump(index,file)

def main():
    csv_file = "zenkoku.csv" #csvファイル取得
    index_file = "index.pkl"

    # インデックスファイルの作成(初回だけ)
    if not os.path.exists(index_file):
        create_index(csv_file,index_file)
        print('ok')
    
    # 検索クエリ取得
    query = input("検索文字列入力: ").strip()

    #2-gram検索処理
    results = results

    #コンソール出力

if __name__ == "__main__":
    main()