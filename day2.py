# Day2: if文・for文・while文・リストの練習

#1.if文
age = 15

if age >= 18:
  print("成人です")
else:
  print("未成年です")

#2.for文(リストを順番に処理)
fruits = ["りんご","バナナ","みかん"]

for fruit in fruits:
  print("フルーツ:",fruit)

#3.while文(繰り返し)
count = 0

while count < 3:
  print("カウント",count)
  count +=1

#4.inを使った判定
fruits = ["りんご","バナナ","みかん"]

if "バナナ" in fruits:
  print("バナナはリストに含まれています")

if "ぶどう" not in fruits:
  print("ぶどうはリストに含まれていません")