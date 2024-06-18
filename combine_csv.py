import os
import csv

def main():
    csv_path = input("csv格納先のパスを入力してください：\n")
    
    # ディレクトリの存在チェック
    if(not os.path.isdir(csv_path)):
        print("ファイルが存在しません")
        return
    
    # カレントディレクトリにworkディレクトリを作成
    os.mkdir("./work")
    
    # カレントディレクトリに成果物ファイルを作成
    csv_file = open("./all.csv", 'w')


if __name__ == '__main__':
    main()