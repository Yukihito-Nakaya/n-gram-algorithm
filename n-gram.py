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

#2-gram 検索
def search(csv_file, index_file, query):
    query = query.replace(" ", "").replace(" ", "")
    query_tokens= [query[i:i + 2]for i in range(len(query)-1)]

    with open(index_file,"rb") as file:
        index = pickle.load(file)
    
    mach_id = None
    for i in query_tokens:
        if i in index:
            if mach_id is None:
                mach_id = set(index[i])
            else:
                mach_id &= set(index[i])
        else:
            mach_id = set()
            break
    
    if not mach_id:
        return[]
    
    results=[]

    with open(csv_file,encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for id , row in enumerate(reader):
            if id in mach_id:
                results.append({
                    "郵便番号": row["郵便番号"],
                    "都道府県": row["都道府県"],
                    "市区町村": row["市区町村"],
                    "町域": row["町域"],
                    "京都通り名": row["京都通り名"],
                    "字丁目": row["字丁目"],
                    "事業所名": row["事業所名"],
                    "事業所住所": row["事業所住所"],
                })
    return results

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
    results = search(csv_file, index_file, query)

    #コンソール出力
    if results:
        for ans in results:
            print(ans)
    else:
        print("一致するものが見つかりませんでした。")

if __name__ == "__main__":
    main()