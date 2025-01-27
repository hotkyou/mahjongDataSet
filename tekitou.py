import re

shoupai = "p66677s46p5,"
match = re.search(r"(..),(?=\S)", shoupai)

if match:
    print(match.group(1))  # 出力: "s5"
else:
    print("該当する部分が見つかりません")