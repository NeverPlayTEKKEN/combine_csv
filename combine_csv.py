import os
import csv
import shutil

def main():
    csv_path = input("csv格納先のパスを入力してください：\n")
    
    # ディレクトリの存在チェック
    if(not os.path.isdir(csv_path)):
        print("ファイルが存在しません")
        return
    
    # カレントディレクトリにworkディレクトリを作成
    os.mkdir("./work")
    
    # カレントディレクトリに成果物ファイルを作成
    all_csv_file = open("./all.csv", 'w')

    # すべてのcsvファイルに対して処理を実行
    for csv_file in os.listdir(csv_path):
        shutil.copy(csv_path + "/" + csv_file, "./work/" + csv_file)
    
    # workフォルダ内のすべてのファイルに対して処理を実行
    for csv_file in os.listdir("./work"):
        

if __name__ == '__main__':
    main()