import mahjong
from mahjong.hand_calculating.hand import HandCalculator
from mahjong.tile import TilesConverter
from mahjong.hand_calculating.hand_config import HandConfig
from mahjong.constants import EAST, SOUTH

calculator = HandCalculator()

def is_tenpai(tiles, melds, dora_indicators, config):
    for i in range(1, 10):  # 数牌（萬子、筒子、索子）の1〜9
        for suit in ['man', 'pin', 'sou']:
            win_tile = TilesConverter.string_to_136_array(**{suit: str(i)})[0]
            temp_tiles = tiles + [win_tile]
            result = calculator.estimate_hand_value(tiles, win_tile, melds, dora_indicators, config)
            if result.error is None:
                return True

    for honor in ['1', '2', '3', '4', '5', '6', '7']:  # 風牌と三元牌
        win_tile = TilesConverter.string_to_136_array(honors=honor)[0]
        temp_tiles = tiles + [win_tile]
        result = calculator.estimate_hand_value(temp_tiles, win_tile, melds, dora_indicators, config)
        if result.error is None:
            return True

    return False

# 手牌の定義
tiles = TilesConverter.string_to_136_array(man='66', sou='4555999',pin='333567')

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
