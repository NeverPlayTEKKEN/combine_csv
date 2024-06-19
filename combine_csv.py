import os
import shutil
import datetime

def main():
    csv_path = input("csv格納先のパスを入力してください：\n")
    
    # ディレクトリの存在チェック
    if(not os.path.isdir(csv_path)):
        print("ファイルが存在しません")
        return
    
    # カレントディレクトリにworkディレクトリを作成
    os.mkdir("./work")
    
    # カレントディレクトリに成果物ファイルを作成
    all_csv_file = open("./all_" + datetime.datetime.now().strftime('%Y%m%d%H%M') + ".csv", 'a')


    # すべてのcsvファイルに対して処理を実行
    for csv_file in os.listdir(csv_path):
        shutil.copy(csv_path + "/" + csv_file, "./work/" + csv_file)
    
    # ループのカウントを行う
    loop_cnt = 0
    # workフォルダ内のすべてのファイルに対して処理を実行
    for csv_file in os.listdir("./work"):
        with open("./work/" + csv_file) as file_obj:
            data_list = file_obj.readlines()
            # 初回のみカラム名を取得し成果物ファイルに書き込み
            if loop_cnt == 0:
                all_csv_file.write(data_list[0])
                loop_cnt += 1
            # 最初の行（カラム名）と最後の行（改行）を削除し成果物ファイルに書き込み
            data_list.pop(-1)
            data_list.pop(0)
            all_csv_file.writelines(data_list)
    
    # 成果物ファイルの最終行に改行を追加する
    all_csv_file.write("\n")

    # workディレクトリを削除する
    shutil.rmtree("./work")

    # 成果物ファイルを閉じる
    all_csv_file.close()

        

if __name__ == '__main__':
    main()