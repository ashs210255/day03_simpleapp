# 題目：
# 給你一個水果清單：
# 請你：
# 用 enumerate 把每個水果編上從0開始的編號。
# 把它們存成一個dict，key是編號，value是水果名字。
# 讓使用者輸入一個數字，然後顯示出對應的水果名字。
# 如果輸入的數字超出範圍，要提示錯誤訊息。
fruits = ["apple", "banana", "orange", "grape", "watermelon"]
fruit_dict = {}

for index, fruit in enumerate(fruits):
    #print(f"{index}: {fruit}")
    fruit_dict[index] = fruit

user_input = int(input("請輸入你想要查詢的水果編號:"))
try:
    if user_input in fruit_dict:
        print(f"你選擇的是:{fruit_dict[user_input]}")
    else:
        print("查無此水果!")
except ValueError:
    print("請輸入有效的數字！")
 