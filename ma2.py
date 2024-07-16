import mahjong
from mahjong.hand_calculating.hand import HandCalculator
from mahjong.tile import TilesConverter
from mahjong.hand_calculating.hand_config import HandConfig
from mahjong.constants import EAST, SOUTH

calculator = HandCalculator()

def print_hand_result(hand_result):
    # 翻数, 符数
    print(f"翻数: {hand_result.han}, 符数: {hand_result.fu}")
    # 点数(ツモアガリの場合[左：親失点, 右:子失点], ロンアガリの場合[左:放銃者失点, 右:0])
    print(f"点数: {hand_result.cost['main']}, 追加点数: {hand_result.cost['additional']}")
    # 役
    print(f"役: {hand_result.yaku}")
    # 符数の詳細
    for fu_item in hand_result.fu_details:
        print(f"符数詳細: {fu_item}")
    print('')

def is_tenpai(tiles, win_tile, melds, dora_indicators, config):
    result = calculator.estimate_hand_value(tiles, win_tile, melds, dora_indicators, config)
    return result.error is None  # エラーがなければ聴牌していると判断

# 手牌の定義
tiles = TilesConverter.string_to_136_array(man='677889', pin='88', sou='456', honors='222')

# アガリ牌(マンズの8)
win_tile = TilesConverter.string_to_136_array(sou='6' or man='4')[0]

# 鳴き(なし)
melds = []

# ドラ(表示牌,裏ドラ)
dora_indicators = [
    TilesConverter.string_to_136_array(pin='7')[0],
    TilesConverter.string_to_136_array(sou='9')[0],
]

# オプション(リーチ, 自風, 場風)
config = HandConfig(is_riichi=True, player_wind=SOUTH, round_wind=EAST)

# 手牌とアガリ牌を結合して和了判定
if is_tenpai(tiles, win_tile, melds, dora_indicators, config):
    print("聴牌しています")
else:
    print("聴牌していません")

# 計算結果を表示
result = calculator.estimate_hand_value(tiles, win_tile, melds, dora_indicators, config)
print_hand_result(result)
