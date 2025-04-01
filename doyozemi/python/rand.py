import random

# おみくじの運勢リスト
fortunes = ["大吉", "中吉", "小吉", "吉", "凶", "大凶"]

# ユーザーにメッセージを表示し、Enterキーを待つ関数
def wait_for_enter():
    input("Enterキーを押して運勢を占う...")

# メインのおみくじゲーム関数
def omikuji_game():
    print("おみくじゲームへようこそ！")
    wait_for_enter()

    # ランダムに運勢を選ぶ
    fortune = random.choice(fortunes)

    # 選ばれた運勢を表示
    print(f"あなたの運勢は... {fortune} です！")

if __name__ == "__main__":
    omikuji_game()

