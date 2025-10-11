# Day5: メモをファイルに保存するプログラム
# memo = input("今日のメモを入力して下さい: ")

# # ファイルに書き込む
# # with open("memo.txt", "w", encoding="utf-8") as f:
# #     f.write(memo)

# # print("メモを保存しました！")

# # 追記モード（"a"）にしてみよう
# with open("memo.txt", "a", encoding="utf-8") as f:
#     f.write(memo + "\n") # 改行も追加

# print("メモを追記しました！")

# 日付付きメモを追記するプログラム
from datetime import datetime
import os

MEMO_FILE = "memo.txt"

def add_memo():
    memo = input("今日のメモを入力して下さい: ").strip()
    if not memo:
        print("空のメモは保存しません。")
        return
    # 日本式の日付と時刻(例: 2025-10-09 21:15)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    line = f"[{timestamp}] {memo}\n"
    with open(MEMO_FILE, "a", encoding="utf-8") as f:
        f.write(line)
    print("メモを追記しました！")

def show_tail(n=5):
    """最後の n 行だけ表示(なければスキップ)"""
    if not os.path.exists(MEMO_FILE):
        return
    print("\n--- 直近のメモ ---")
    with open(MEMO_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for s in lines[-n:]:
        print(s.rstrip())
    print("--------------\n")

# if __name__ == "__main__":
#     add_memo()
#     show_tail(5) # 直近5件を実行後にチラ見できる
#     search_memo()

def search_memo():
    keyword = input("検索したキーワードを入力してください： ").strip()
    found = False
    
    with open(MEMO_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if keyword.lower() in line.lower():
                print(line.strip())
                found = True
    
    if not found:
        print("該当するメモが見つかりませんでした。")


if __name__ == "__main__":
    add_memo()
    show_tail(5) # 直近5件を実行後にチラ見できる
    search_memo()

def main_menu():
    while True:
        print("\n=== メモアプリ ===")
        print("1) メモを追加")
        print("2) 直近のメモを表示")
        print("3) キーワードの検索")
        print("4) 終了")
        choice = input("番号を選んでください: ").strip()

        if choice == "1":
            add_memo()
        elif choice == "2":
            try:
                n = int(input("何件表示しますか？(規定=5): ") or "5")
            except ValueError:
                n = 5
            show_tail(n)
        elif choice == "3":
            search_memo()
        elif choice == "4":
            print("終了します。")
            break
        else:
            print("1～4の番号で選んでください。")

if __name__ == "__main__":
    main_menu()