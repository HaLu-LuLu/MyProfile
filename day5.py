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

if __name__ == "__main__":
    add_memo()
    show_tail(5) # 直近5件を実行後にチラ見できる