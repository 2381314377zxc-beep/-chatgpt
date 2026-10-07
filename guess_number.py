"""一个适合 Python 初学者的猜数字小游戏。"""

import random


def main():
    answer = random.randint(1, 100)
    attempts = 0
    print("欢迎玩猜数字！我选好了一个 1 到 100 之间的整数。")
    print("输入 q 可以退出。")

    while True:
        text = input("请输入你的猜测：").strip()
        if text.lower() == "q":
            print(f"游戏结束，答案是 {answer}。")
            break

        try:
            guess = int(text)
        except ValueError:
            print("请输入整数，例如 50；或者输入 q 退出。")
            continue

        if not 1 <= guess <= 100:
            print("数字需要在 1 到 100 之间。")
            continue

        attempts += 1
        if guess < answer:
            print("太小了，再试一次！")
        elif guess > answer:
            print("太大了，再试一次！")
        else:
            print(f"猜对了！答案是 {answer}，你一共猜了 {attempts} 次。")
            break


if __name__ == "__main__":
    main()
