import mahjong
from mahjong.hand_calculating.hand import HandCalculator
from mahjong.tile import TilesConverter
from mahjong.hand_calculating.hand_config import HandConfig
from mahjong.constants import EAST, SOUTH

calculator = HandCalculator()

def is_tenpai(tiles, melds, dora_indicators, config):
    result = calculator.estimate_hand_value(tiles,melds, dora_indicators, config)
    return 

# 手牌の定義
tiles = TilesConverter.string_to_136_array(man='66', sou='4555999', honors='333567')

# 鳴き（なし）
melds = []

# ドラ（表示牌, 裏ドラ）
dora_indicators = [
    TilesConverter.string_to_136_array(pin='7')[0],
    TilesConverter.string_to_136_array(sou='9')[0],
]

# オプション（リーチ, 自風, 場風）
config = HandConfig(is_riichi=True, player_wind=SOUTH, round_wind=EAST)

# テンパイ判定
if is_tenpai(tiles, melds, dora_indicators, config):
    print("聴牌しています")
else:
    print("聴牌していません")
