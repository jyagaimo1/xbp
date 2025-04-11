for i in range(3):
    #文字だから””いれた
    print(i,"人目")
    name=input("名前をいれてください")
    waist=float(input("腹囲を入れてください"))
    age=int(input("年齢をいれてください"))
        #int整数のこと　float実数のこと

    print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")
        #かつ＝and           #↓数字の後は：これおく
    if waist>=85 and age>=40:
        print(name,"さん、内脂肪蓄積注意です")       
    else:
        print(name,"さん、腹囲は問題ありません")





