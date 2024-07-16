import csv
import copy
from collections import Counter
from mahjong.shanten import Shanten
from mahjong.tile import TilesConverter
def check_chi_possible(tehaitmp, tile_index):
    chi_possible = False
    
    # tile_indexが27未満の場合、数牌のチーを確認
    if tile_index < 27:
        mod = tile_index % 9
        # 順子をチェック (例えば、3つの連続した牌があるか)
        if mod >= 2 and tehaitmp[tile_index - 2] > 0 and tehaitmp[tile_index - 1] > 0:
            chi_possible = True
        if mod >= 1 and mod <= 7 and tehaitmp[tile_index - 1] > 0 and tehaitmp[tile_index + 1] > 0:
            chi_possible = True
        if mod <= 6 and tehaitmp[tile_index + 1] > 0 and tehaitmp[tile_index + 2] > 0:
            chi_possible = True

    return chi_possible

# テスト配列
tehaitmp = [0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 1, 0, 0, 1, 2, 0, 1, 0, 0, 0, 1, 0, 0]

# チーの対象となる牌のインデックスを指定
tile_index =15 # 例えば、8筒をチーしようとする場合

# チー可能かどうかを確認
chi_possible = check_chi_possible(tehaitmp, tile_index)
print(f"Chi possible: {chi_possible}")
