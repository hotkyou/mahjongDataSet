from mahjong.tile import TilesConverter
from mahjong.shanten import Shanten

# 手牌の定義
hand = '123456m123s'
# プレイヤーの手牌を136形式に変換
tiles = TilesConverter.string_to_136_array(hand)

# Shantenのインスタンスを作成
shanten_calculator = Shanten()

# 向聴数を計算
shanten = shanten_calculator.calculate_shanten(tiles)

# 向聴数が0の場合、聴牌であると判断
if shanten == 0:
    print("聴牌です。")
else:
    print("聴牌ではありません。")
