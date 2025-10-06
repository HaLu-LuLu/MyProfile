# Day4: サイコロを振るプログラム

import random 

#サイコロを1回振る
# dice = random.randint(1,6)
# print("サイコロの目:", dice)

#サイコロを何回も振る
# print("サイコロを3回振ります！")
# for i in range(3):
#   dice = random.randint(1,6)
#   print(f"{i+1}回目の目:", dice)
#   if dice == 6: #6が出たら特別メッセージ
#     print("おめでとう！6が出た！🎉") 

hands = ["グー", "チョキ", "パ－"]

print("じゃんけん...")
player = input("グー / チョキ / パ－ を入力して下さい: ")
computer = random.choice(hands)

print("あなた:", player)
print("コンピュータ:", computer,)

if player == computer:
  print("あいこです")
elif (player == "グー" and computer == "チョキ") \
  or (player == "チョキ" and computer == "パ－") \
  or (player == "パ－" and computer == "グー"):
  print("あなたの勝ち🎉")
else:
  print("コンピュータの勝ち💻")


