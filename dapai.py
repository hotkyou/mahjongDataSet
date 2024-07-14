import csv
import copy
from collections import Counter
import mahjong
from mahjong.hand_calculating.hand import HandCalculator
from mahjong.tile import TilesConverter
from mahjong.hand_calculating.hand_config import HandConfig
from mahjong.constants import EAST, SOUTH
import sys

calculator = HandCalculator()


# def is_tenpai(tiles, melds, dora_indicators, config):
#     for i in range(1, 10):  # 数牌（萬子、筒子、索子）の1〜9
#         for suit in ['man', 'pin', 'sou']:
#             win_tile = TilesConverter.string_to_136_array(**{suit: str(i)})[0]
#             temp_tiles = tiles + [win_tile]
#             result = calculator.estimate_hand_value(temp_tiles, win_tile, melds, dora_indicators, config)
#             if result.error is None:
#                 return True

#     for honor in ['1', '2', '3', '4', '5', '6', '7']:  # 風牌と三元牌
#         win_tile = TilesConverter.string_to_136_array(honors=honor)[0]
#         temp_tiles = tiles + [win_tile]
#         result = calculator.estimate_hand_value(temp_tiles, win_tile, melds, dora_indicators, config)
#         if result.error is None:
#             return True

#     return False

def dapai(self, i):
    d = "dapai"
    player = i["dapai"]["l"]
    tile = i["dapai"]["p"]
    tmp = ""
    tehaitmp = []
    man = []
    pin= []
    sou=[]
    ho=[]

    

     
   
    # for q in range(len(self.reach)):
    #     if(self.reach[q]==1):
    #         exit('end')
    
   
    if self.reach[player] != 1:  # リーチしていない時
        if len(tile) >= 3:
            if tile[-2:] == "_*":
                tmp = tile[:-2]
                self.dora[player] = 1
                self.score[player] -= 1000
            elif tile[2] == "_":  # 同じ牌を捨てる
                tmp = tile[:-1]
            elif tile[2] == "*": 
                print(tile) # リーチした時
                tmp = tile[:-1]
                self.dora[player] = 1
                self.score[player] -= 1000
            else:  # 例外
                raise ValueError("_か*か_*以外が存在した")
        else:
            tmp = tile

        # -- addCSV処理 --
        if self.todo == 0:
            data = []
            data += self.tehaiok[player]  # 手牌
            for j in range(len(self.reach)):  # リーチ自分から見て
                index = (player + j) % len(self.reach)
                data.append(self.reach[index])
            data += self.dora  # ドラ34
            data.append(self.parentdora)  # 場風
            data.append(self.childdora)  # 自風
            data.append(self.changbang)  # 何本場
            data.append(self.lizhibang)  # リーチ棒繰越
            for k in range(len(self.naki)):  # 鳴き自分から見て
                index = (player + k) % len(self.naki)
                data.extend(self.naki[index])
            for l in range(len(self.discard)):  # 捨て牌自分から見て
                index = (player + l) % len(self.discard)
                data.extend(self.discard[index])
            for m in range(len(self.score)):  # 点数自分から見て
                index = (player + m) % len(self.score)
                data.append(self.score[index])
            data.append(self.tiles)  # 残り牌数
            data.append(self.dorall.index(tmp))  # 何を捨てたか
            self.writer.writerow(data)
        # -- CSV処理終了 --

    else:  # リーチしている時
        tmp = tile[:2]  # 手牌に入れる必要はないが捨て牌に追加する必要はある

    # -- 捨て牌処理 --
    if self.tehaiok[player][self.dorall.index(tmp)] != 0:
        if self.tehaiok[player][self.dorall.index(tmp)] - 1 >= 0:
            self.tehaiok[player][self.dorall.index(tmp)] -= 1  # 手牌から削除
            self.discard[player][self.dorall.index(tmp)] += 1  # 捨て牌追加
        else:
            raise ValueError("手配がマイナスに！！")
    else:
        raise ValueError("手牌に存在しない")
    


    print("aa")

    
    for g in range(len(self.tehaiok[player])):
       
        if(g>=0 and 9 >= g):
            if(self.tehaiok[player][g]!=0):
        
                ten=g+1
                count=0
                while count <self.tehaiok[player][g]:
                    man.append(ten)
                    if(ten==10):
                        man.remove(10)
                        man.append(5)
                    count += 1
        elif(10<=g and g <=19):
            if(self.tehaiok[player][g]!=0):
                niju=g+1
                count=0
                while count<self.tehaiok[player][g]:
                    pin.append(niju-10)
                    if(niju==20):
                        pin.remove(10)
                        pin.append(5)
                    count +=1
        elif(20<=g and g<=29):
            if(self.tehaiok[player][g]!=0):
                sanju=g+1
                count=0
                
                while count<self.tehaiok[player][g]:

                    sou.append(sanju-20)
                    if(sanju==30):

                        sou.remove(10)
                        sou.append(5)
                    count+=1
            
        else:
            if(self.tehaiok[player][g]!=0):
                yon=g+1
                count=0
                while count<self.tehaiok[player][g]:
                    ho.append(yon-30)
                    count+=1


    man2 = ''.join(map(str, man))
    pin2=''.join(map(str, pin))
    sou2=''.join(map(str, sou))
    ho2=''.join(map(str,ho))
    print(ho2)
    print(man2, pin2, sou2, ho2)

    tiles = TilesConverter.string_to_136_array(man=man2, pin=pin2,honors=ho2,sou=sou2)

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
        print(tile)
        
        if(tile[-1]=="*" or tile[-1]=="*"):
            print(player)
            print(self.reach[player])
            data = []
            data += self.tehaiok[player]  # 手牌
            for j in range(len(self.reach)):  # リーチ自分から見て  # リーチ自分から見て
                index = (player + j) % len(self.reach)
                if j == player:
                    self.reach[j]=1
                data.append(self.reach[index])
            data += self.dora  # ドラ34
            data.append(self.parentdora)  # 場風
            data.append(self.childdora)  # 自風
            data.append(self.changbang)  # 何本場
            data.append(self.lizhibang)  # リーチ棒繰越
            for k in range(len(self.naki)):  # 鳴き自分から見て
                index = (player + k) % len(self.naki)
                data.extend(self.naki[index])
            for l in range(len(self.discard)):  # 捨て牌自分から見て
                index = (player + l) % len(self.discard)
                data.extend(self.discard[index])
            for m in range(len(self.score)):  # 点数自分から見て
                index = (player + m) % len(self.score)
                data.append(self.score[index])
            data.append(self.tiles)  # 残り牌数
            data.append(self.dorall.index(tmp))  # 何を捨てたか
            self.writer.writerow(data)
            print(self.reach)   
            exit()
        else:
            data = []
            data += self.tehaiok[player]  # 手牌
            data.append(self.reach[index])
            data += self.dora  # ドラ34
            data.append(self.parentdora)  # 場風
            data.append(self.childdora)  # 自風
            data.append(self.changbang)  # 何本場
            data.append(self.lizhibang)  # リーチ棒繰越
            for k in range(len(self.naki)):  # 鳴き自分から見て
                index = (player + k) % len(self.naki)
                data.extend(self.naki[index])
            for l in range(len(self.discard)):  # 捨て牌自分から見て
                index = (player + l) % len(self.discard)
                data.extend(self.discard[index])
            for m in range(len(self.score)):  # 点数自分から見て
                index = (player + m) % len(self.score)
                data.append(self.score[index])
            data.append(self.tiles)  # 残り牌数
            tmp2=37
            data.append(self.dorall.index(''))  # 何を捨てたか
            self.writer.writerow(data)  
               
        
    else:
        print("聴牌していません")
                    

    

    # 手牌一時保存・手牌に捨て牌追加して鳴きチェック
    if self.todo != 0:
        tehaitmp = copy.deepcopy(self.tehaiok)  # 現在の手牌に捨て牌を追加して鳴きをチェックするための変数
        for tehaiplayer, tehainakami in enumerate(tehaitmp):
            if tehaiplayer != player:  # 捨て牌を捨てた本人は鳴けないのでスキップ
                if self.reach[tehaiplayer] != 1:  # 立直してない人のみ
                    tehaitmp[tehaiplayer][self.dorall.index(tmp)] += 1

                    if self.todo == 1:  # ぽん
                        for n, o in enumerate(self.tehaiok):
                            if n != player:
                                indexes = []
                                for count, element in enumerate(tehaitmp[tehaiplayer]):  # 捨て牌と手牌を合わせてミンカンできるか確認
                                    if element == 3:  # 手牌と捨て牌を合わせて4枚ある時
                                        indexes.append(count)
                                if indexes != []:  # 4枚ある時
                                    if self.dorall.index(tmp) in indexes:
                                        data = []
                                        data += self.tehaiok[tehaiplayer]
                                        for j in range(len(self.reach)):  # リーチ自分から見て
                                            index = (tehaiplayer + j) % len(self.reach)
                                            data.append(self.reach[index])
                                        data += self.dora  # ドラ34
                                        data.append(self.parentdora)  # 場風
                                        data.append(self.childdora)  # 自風
                                        data.append(self.changbang)  # 何本場
                                        data.append(self.lizhibang)  # リーチ棒繰越
                                        for k in range(len(self.naki)):  # 鳴き自分から見て
                                            index = (tehaiplayer + k) % len(self.naki)
                                            data.extend(self.naki[index])
                                        for l in range(len(self.discard)):  # 捨て牌自分から見て
                                            index = (tehaiplayer + l) % len(self.discard)
                                            data.extend(self.discard[index])
                                        for m in range(len(self.score)):  # 点数自分から見て
                                            index = (tehaiplayer + m) % len(self.score)
                                            data.append(self.score[index] // 100)
                                        data.append(self.tiles)  # 残り牌数
                                        data.append(0)  # 0が鳴きなし 1がカン
                                        self.csvdata = data





                    elif self.todo == 2:  # チー
                        for n, o in enumerate(self.tehaiok):
                            if n != player:
                                pass
                    elif self.todo == 3:
                        pass  # カンをしたらgangで削除処理　全プレイヤーの手牌を処理
                    else:
                        raise ValueError("todoがおかしい")


    
    # # 聴牌判定処理を追加
    # tenpai=copy.deepcopy(self.tehaiok)
    # tiles = copy.deepcopy(self.tehaiok[player])
    # melds = []  # 鳴きは今のところなし
    
    # dora_indicators = [
    #     TilesConverter.string_to_136_array(pin='7')[0],
    #     TilesConverter.string_to_136_array(sou='9')[0],
    # ]
    # config = HandConfig(is_riichi=True, player_wind=SOUTH, round_wind=EAST)

    # if is_tenpai(tiles, melds, dora_indicators, config):
    #     print("聴牌しています")
    #     self.tenpai_status[player] = True
    # else:
    #     print("聴牌していません")
    #     self.tenpai_status[player] = False
def is_tenpai(tiles, melds, dora_indicators, config):
    for i in range(1, 10):  # 数牌（萬子、筒子、索子）の1〜9
        for suit in ['man', 'pin', 'sou']:
            win_tile = TilesConverter.string_to_136_array(**{suit: str(i)})[0]
            temp_tiles = tiles + [win_tile]
            result = calculator.estimate_hand_value(temp_tiles, win_tile, melds, dora_indicators, config)
            if result.error is None:
                return True

    for honor in ['1', '2', '3', '4', '5', '6', '7']:  # 風牌と三元牌
        win_tile = TilesConverter.string_to_136_array(honors=honor)[0]
        temp_tiles = tiles + [win_tile]
        result = calculator.estimate_hand_value(temp_tiles, win_tile, melds, dora_indicators, config)
        if result.error is None:
            return True

    return False
