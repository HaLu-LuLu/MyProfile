# Day3: 関数の練習
def greet(name, age):
  return f"こんにちは、{name} さん！年齢は{age}歳ですね。"

print(greet("太郎", 20))
print(greet("花子", 15))

# Day3: 辞書の練習
person = {
  "name": "Haru",
  "age": 36,
  "hobby": "プログラミング",
  "food": "お肉"
}

print("名前:",  person["name"])
print("年齢:",  person["age"])
print("趣味:",  person["hobby"])
print("好きな食べ物:",  person["food"])

# Day3: 辞書とfor文の組み合わせ

for key, value in person.items():
  print(key, ":", value)