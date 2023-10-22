import random

print("計算ゲームです")
intChallenge = int(input("挑戦回数を入力:"))

intcount = 0
intPlayer = 0
for intcount in range(intChallenge):
    lstkazu = [random.randint(0,1000),random.randint(0,10)]
    strQuestion = str(lstkazu[0]) + " + " + str(lstkazu[1]) + " = "

    intKotae = int(input(strQuestion))
    if  intKotae == sum(lstkazu):
        print("正解!")
        intPlayer += 1
    else:
        print("残念、不正解")

if intPlayer == intChallenge:
     print("おめでとう、全問正解です!")
else:
    print("残念、また挑戦してね")
        