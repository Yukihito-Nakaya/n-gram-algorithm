import chardet

def detect_encoding(file_path):
    with open(file_path, "rb") as file:
        rawdata = file.read()
    return chardet.detect(rawdata)["encoding"]

csv_file = "zenkoku.csv"
encoding = detect_encoding(csv_file)
print(encoding)