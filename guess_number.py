# -*- coding:utf-8 -*-
#guess_number.py
#問題描述
#猜數字遊戲
#利用 random module 功能產生一個 1 ~ 100 的隨機整數
#不能用使用者知道答案
#讓使用者重複的輸入數字去猜  （使用 while 迴圈)
#如果猜的數字比真的答案大就顯示 "比答案大" 讓使用者繼續猜
#如果猜的數字比真的答案小就顯示 "比答案小" 讓使用者繼續猜
#猜對就顯示"恭喜猜對了" 並結束遊戲

import random

answer = random.randint(1, 100)
while True: