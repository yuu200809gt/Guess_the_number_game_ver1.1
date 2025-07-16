import random

print("このゲームは任意の最小値と最大値を決め、5回以内に数字を当てるゲームです!")

min = int(input("最小値:")) #最小値の入力
max = int(input("最大値:")) #最大値の入力

target = random.randint(min,max) #最小値と最大値の間の数字で解答を生成する
answer_chance = 5 #試行回数5回


for i in range(1,answer_chance+1):
    try:
        guess = int(input(f"[{i}回目] 数字を入力してください : "))
        if guess < min or guess > max:
            print("範囲内の数字を入力してください！")
            continue
        if guess == target:
            print(f"正解です！{i}回目で当てました！")   
            break
        elif guess < target:
            print("小さすぎます！ \n")
        else: 
            print("大きすぎます！")
    except ValueError:
        print("数字を入力してください \n")
else:
    print(f"残念!答えは{target}でした！")        
