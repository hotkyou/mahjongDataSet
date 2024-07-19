import csv
import copy
from collections import Counter
from mahjong.shanten import Shanten
from mahjong.tile import TilesConverter

def dapai(self, i):
    #print("捨て牌")
    
    d = "dapai"
    player = i["dapai"]["l"]
    tile = i["dapai"]["p"]
    tmp = ""
    tehaitmp = []
    
    if self.reach[player] != 1: #リーチしていない時
        if len(tile) >= 3:
            if tile[-2:] == "_*":
                tmp = tile[:-2]
                # -- リーチ時csv格納処理 --
                if self.todo == 4:
                    data = []
                    data += self.tehaiok[player] #手牌
                    for j in range(len(self.reach)): #リーチ自分から見て
                        index = (player + j) % len(self.reach)
                        #print(index)
                        data.append(self.reach[index])
                    data += self.dora #ドラ34
                    data.append(self.parentdora) #場風
                    data.append(self.childdora) #自風
                    data.append(self.changbang) #何本場
                    data.append(self.lizhibang) #リーチ棒繰越
                    for k in range(len(self.naki)): #鳴き自分から見て
                        index = (player + k) % len(self.naki)
                        data.extend(self.naki[index])
                    for l in range(len(self.discard)): #捨て牌自分から見て
                        index = (player + l) % len(self.discard)
                        data.extend(self.discard[index])
                    for m in range(len(self.score)): #点数自分から見て
                        index = (player + m) % len(self.score)
                        data.append(self.score[index] // 100)
                    data.append(self.tiles) #残り牌数
                    data.append(self.dorall.index(tmp)) #37が鳴きなし それ以外が鳴き
                    self.writer.writerow(data)
                # -- リーチ時csv格納処理終 --
                self.reach[player] = 1
                self.score[player] -= 1000
            elif tile[2] == "_": # 同じ牌を捨てる
                tmp = tile[:-1]
            elif tile[2] == "*": # リーチした時
                tmp = tile[:-1]
                # -- リーチ時csv格納処理 --
                if self.todo == 4:
                    data = []
                    data += self.tehaiok[player] #手牌
                    for j in range(len(self.reach)): #リーチ自分から見て
                        index = (player + j) % len(self.reach)
                        #print(index)
                        data.append(self.reach[index])
                    data += self.dora #ドラ34
                    data.append(self.parentdora) #場風
                    data.append(self.childdora) #自風
                    data.append(self.changbang) #何本場
                    data.append(self.lizhibang) #リーチ棒繰越
                    for k in range(len(self.naki)): #鳴き自分から見て
                        index = (player + k) % len(self.naki)
                        data.extend(self.naki[index])
                    for l in range(len(self.discard)): #捨て牌自分から見て
                        index = (player + l) % len(self.discard)
                        data.extend(self.discard[index])
                    for m in range(len(self.score)): #点数自分から見て
                        index = (player + m) % len(self.score)
                        data.append(self.score[index] // 100)
                    data.append(self.tiles) #残り牌数
                    data.append(self.dorall.index(tmp)) #37が鳴きなし それ以外が鳴き
                    self.writer.writerow(data)
                # -- リーチ時csv格納処理終 --
                self.reach[player] = 1
                self.score[player] -= 1000
            else: #例外
                print(i)
                raise ValueError("_か*か_*以外が存在した")
        else:
            tmp = tile
        
        # -- addCSV処理 --
        if self.todo == 0:
            data = []
            data += self.tehaiok[player] #手牌
            for j in range(len(self.reach)): #リーチ自分から見て
                index = (player + j) % len(self.reach)
                data.append(self.reach[index])
            data += self.dora #ドラ34
            data.append(self.parentdora) #場風
            data.append(self.childdora) #自風
            data.append(self.changbang) #何本場
            data.append(self.lizhibang) #リーチ棒繰越
            for k in range(len(self.naki)): #鳴き自分から見て
                index = (player + k) % len(self.naki)
                data.extend(self.naki[index])
            for l in range(len(self.discard)): #捨て牌自分から見て
                index = (player + l) % len(self.discard)
                data.extend(self.discard[index])
            for m in range(len(self.score)): #点数自分から見て
                index = (player + m) % len(self.score)
                data.append(self.score[index] // 100)
            data.append(self.tiles) #残り牌数
            data.append(self.dorall.index(tmp)) #何を捨てたか
            self.writer.writerow(data)
        # -- CSV処理終了 --
        # -- テンパイ確認処理 --
        elif self.todo == 4:
            if self.reach[player] != 1 and sum(self.tehaiok[player]) == 14:
                shanten = Shanten()

                man = ''.join([self.dorall[i][1] * self.tehaiok[player][i] for i in range(9)]) + '5' * self.tehaiok[player][9]
                pin = ''.join([self.dorall[i][1] * self.tehaiok[player][i] for i in range(10, 19)]) + '5' * self.tehaiok[player][19]
                sou = ''.join([self.dorall[i][1] * self.tehaiok[player][i] for i in range(20, 29)]) + '5' * self.tehaiok[player][29]
                honors = ''.join([self.dorall[i][1] * self.tehaiok[player][i] for i in range(30, 37)])

                # 34配列を文字列形式に変換
                tiles_str = TilesConverter.string_to_34_array(man=man, pin=pin, sou=sou, honors=honors)

                # シャンテン数を計算
                shanten_number = shanten.calculate_shanten(tiles_str)
                
                if shanten_number == 0:
                    # print(self.tehaiok[player])
                    # print(shanten_number, tile)
                    # print(self.reach, player)
                    data = []
                    data += self.tehaiok[player] #手牌
                    for j in range(len(self.reach)): #リーチ自分から見て
                        index = (player + j) % len(self.reach)
                        #print(index)
                        data.append(self.reach[index])
                    data += self.dora #ドラ34
                    data.append(self.parentdora) #場風
                    data.append(self.childdora) #自風
                    data.append(self.changbang) #何本場
                    data.append(self.lizhibang) #リーチ棒繰越
                    for k in range(len(self.naki)): #鳴き自分から見て
                        index = (player + k) % len(self.naki)
                        data.extend(self.naki[index])
                    for l in range(len(self.discard)): #捨て牌自分から見て
                        index = (player + l) % len(self.discard)
                        data.extend(self.discard[index])
                    for m in range(len(self.score)): #点数自分から見て
                        index = (player + m) % len(self.score)
                        data.append(self.score[index] // 100)
                    data.append(self.tiles) #残り牌数
                    data.append(37) #37が鳴きなし それ以外が鳴き
                    self.writer.writerow(data)
        # -- テンパイ確認処理終 --
        
    else: #リーチしている時
        tmp = tile[:2] #手牌に入れる必要はないが捨て牌に追加する必要はある
    
    # -- 捨て牌処理 --
    if self.tehaiok[player][self.dorall.index(tmp)] != 0:
        if self.tehaiok[player][self.dorall.index(tmp)] -1 >= 0:
            self.tehaiok[player][self.dorall.index(tmp)] -= 1 #手牌から削除
            self.discard[player][self.dorall.index(tmp)] += 1 #捨て牌追加
        else:
            print(self.tehaiok[player][self.dorall.index(tmp)])
            raise ValueError("手配がマイナスに！！")
    else:
        raise ValueError("手牌に存在しない")
    
    #手牌一時保存・手牌に捨て牌追加して鳴きチェック
    if self.todo != 0:
        tehaitmp = copy.deepcopy(self.tehaiok) #現在の手牌に捨て牌を追加して鳴きをチェックするための変数
        
        if self.todo == 2: #チー
            self.callplayer = player + 1
            if self.callplayer == 4:
                self.callplayer = 0
            if self.reach[self.callplayer] != 1: #立直してない人のみ
                calltehaiok = copy.deepcopy(tehaitmp[self.callplayer])
                #print(tmp)
                sutehaitmp = self.dorall.index(tmp)
                if sutehaitmp in [9, 19, 29]: #捨て牌が赤ドラの時
                    sutehaitmp -= 5
                if calltehaiok[9] == 1:
                    calltehaiok[9] -= 1
                    calltehaiok[4] += 1
                elif calltehaiok[19] == 1:
                    calltehaiok[19] -= 1
                    calltehaiok[14] += 1
                elif calltehaiok[29] == 1:
                    calltehaiok[29] -= 1
                    calltehaiok[24] += 1
                
                
                # チーできるパターンを格納する配列
                chi_patterns = []

                # マンズの場合
                if 0 <= sutehaitmp <= 8:
                    tile_type = 0  # マンズ
                    tile_num = sutehaitmp
                # ピンズの場合
                elif 10 <= sutehaitmp <= 18:
                    tile_type = 10  # ピンズ
                    tile_num = sutehaitmp - 10
                # ソウズの場合
                elif 20 <= sutehaitmp <= 28:
                    tile_type = 20  # ソウズ
                    tile_num = sutehaitmp - 20
                else:
                    return chi_patterns  # それ以外は無視

                possible_patterns = [
                    [-2, -1], [-1, 1], [1, 2]
                ]
                
                for pattern in possible_patterns:
                    chi_candidate = [tile_num + pattern[0], tile_num + pattern[1]]
                    if all(0 <= num <= 8 for num in chi_candidate) and all(calltehaiok[tile_type + num] > 0 for num in chi_candidate):
                        chi_patterns.append([tile_type + num for num in chi_candidate])
                
                if chi_patterns != []:
                    #print(chi_patterns, sutehaitmp)
                    data = []
                    data += self.tehaiok[self.callplayer] #手牌
                    for j in range(len(self.reach)): #リーチ自分から見て
                        index = (self.callplayer + j) % len(self.reach)
                        #print(index)
                        data.append(self.reach[index])
                    data += self.dora #ドラ34
                    data.append(self.parentdora) #場風
                    #data.append(self.childdora) #自風
                    data.append(self.callplayer) #自風
                    data.append(self.changbang) #何本場
                    data.append(self.lizhibang) #リーチ棒繰越
                    for k in range(len(self.naki)): #鳴き自分から見て
                        index = (self.callplayer + k) % len(self.naki)
                        data.extend(self.naki[index])
                    for l in range(len(self.discard)): #捨て牌自分から見て
                        index = (self.callplayer + l) % len(self.discard)
                        data.extend(self.discard[index])
                    for m in range(len(self.score)): #点数自分から見て
                        index = (self.callplayer + m) % len(self.score)
                        data.append(self.score[index] // 100)
                    data.append(self.tiles) #残り牌数
                    data.append(37) #37が鳴きなし それ以外が鳴き
                    self.csvdata = data
                #チー終わり
            
        for tehaiplayer, tehainakami in enumerate(tehaitmp):
            #print(tehaiplayer, tehainakami)
            if tehaiplayer != player:   #捨て牌を捨てた本人は鳴けないのでスキップ
                if self.reach[tehaiplayer] != 1: #立直してない人のみ
                    tehaitmp[tehaiplayer][self.dorall.index(tmp)] += 1
                    #print(tehaitmp[tehaiplayer])
                    
                    def sendCSV():
                        data = []
                        data += self.tehaiok[tehaiplayer] #手牌
                        for j in range(len(self.reach)): #リーチ自分から見て
                            index = (tehaiplayer + j) % len(self.reach)
                            #print(index)
                            data.append(self.reach[index])
                        data += self.dora #ドラ34
                        data.append(self.parentdora) #場風
                        data.append(self.childdora) #自風
                        data.append(self.changbang) #何本場
                        data.append(self.lizhibang) #リーチ棒繰越
                        for k in range(len(self.naki)): #鳴き自分から見て
                            index = (tehaiplayer + k) % len(self.naki)
                            data.extend(self.naki[index])
                        for l in range(len(self.discard)): #捨て牌自分から見て
                            index = (tehaiplayer + l) % len(self.discard)
                            data.extend(self.discard[index])
                        for m in range(len(self.score)): #点数自分から見て
                            index = (tehaiplayer + m) % len(self.score)
                            data.append(self.score[index] // 100)
                        data.append(self.tiles) #残り牌数
                        data.append(0) #0が鳴きなし 1が鳴き
                        self.csvdata = data

                    if self.todo == 1: #ぽん
                        indexes = []
                        #print(tehainakami)
                        for count, element in enumerate(tehaitmp[tehaiplayer]): #赤ドラを移動
                            if count == 9 and element == 1:
                                tehaitmp[tehaiplayer][4] += 1
                                tehaitmp[tehaiplayer][9] -= 1
                            if count == 19 and element == 1:
                                tehaitmp[tehaiplayer][14] += 1
                                tehaitmp[tehaiplayer][19] -= 1
                            if count == 29 and element == 1:
                                tehaitmp[tehaiplayer][24] += 1
                                tehaitmp[tehaiplayer][29] -= 1
                        for count, element in enumerate(tehaitmp[tehaiplayer]): #捨て牌と手牌を合わせてポンできるか確認
                            if element >= 3: #手牌と捨て牌を合わせて3枚以上ある時
                                indexes.append(count)
                        if indexes != []: #3枚以上ある時
                            if self.dorall.index(tmp) in indexes:
                                sendCSV()
                            elif self.dorall.index(tmp) in [9, 19, 29]:
                                if self.tehaiok[tehaiplayer][4] == 2 or self.tehaiok[tehaiplayer][14] == 2 or self.tehaiok[tehaiplayer][24] == 2:
                                    sendCSV()
                    
                    elif self.todo == 2: #チー
                        pass

                    elif self.todo == 3: #カンをしたらgangで削除処理　全プレイヤーの手牌を処理
                        indexes = []
                        #print(tehainakami)
                        for count, element in enumerate(tehaitmp[tehaiplayer]): #赤ドラを移動
                            if count == 9 and element == 1:
                                tehaitmp[tehaiplayer][4] += 1
                                tehaitmp[tehaiplayer][9] -= 1
                            if count == 19 and element == 1:
                                tehaitmp[tehaiplayer][14] += 1
                                tehaitmp[tehaiplayer][19] -= 1
                            if count == 29 and element == 1:
                                tehaitmp[tehaiplayer][24] += 1
                                tehaitmp[tehaiplayer][29] -= 1
                        for count, element in enumerate(tehaitmp[tehaiplayer]): #捨て牌と手牌を合わせてミンカンできるか確認
                            if element == 4: #手牌と捨て牌を合わせて4枚ある時
                                indexes.append(count)
                        if indexes != []: #4枚ある時
                            if self.dorall.index(tmp) in indexes: #捨て牌と手牌を合わせて4枚ある時の中に捨て牌がある時
                                ## ミンカン用csv処理
                                data = []
                                data += self.tehaiok[tehaiplayer] #手牌
                                for j in range(len(self.reach)): #リーチ自分から見て
                                    index = (tehaiplayer + j) % len(self.reach)
                                    #print(index)
                                    data.append(self.reach[index])
                                data += self.dora #ドラ34
                                data.append(self.parentdora) #場風
                                data.append(self.childdora) #自風
                                data.append(self.changbang) #何本場
                                data.append(self.lizhibang) #リーチ棒繰越
                                for k in range(len(self.naki)): #鳴き自分から見て
                                    index = (tehaiplayer + k) % len(self.naki)
                                    data.extend(self.naki[index])
                                for l in range(len(self.discard)): #捨て牌自分から見て
                                    index = (tehaiplayer + l) % len(self.discard)
                                    data.extend(self.discard[index])
                                for m in range(len(self.score)): #点数自分から見て
                                    index = (tehaiplayer + m) % len(self.score)
                                    data.append(self.score[index] // 100)
                                data.append(self.tiles) #残り牌数
                                data.append(0) #0が鳴きなし 1がカン
                                self.csvdata = data
                                ## ミンカン用csv処理終了
                            elif self.dorall.index(tmp) in [9, 19, 29]:
                                if self.tehaiok[tehaiplayer][4] == 3 or self.tehaiok[tehaiplayer][14] == 3 or self.tehaiok[tehaiplayer][24] == 3:
                                    ## ミンカン用csv処理
                                    data = []
                                    data += self.tehaiok[tehaiplayer] #手牌
                                    for j in range(len(self.reach)): #リーチ自分から見て
                                        index = (tehaiplayer + j) % len(self.reach)
                                        #print(index)
                                        data.append(self.reach[index])
                                    data += self.dora #ドラ34
                                    data.append(self.parentdora) #場風
                                    data.append(self.childdora) #自風
                                    data.append(self.changbang) #何本場
                                    data.append(self.lizhibang) #リーチ棒繰越
                                    for k in range(len(self.naki)): #鳴き自分から見て
                                        index = (tehaiplayer + k) % len(self.naki)
                                        data.extend(self.naki[index])
                                    for l in range(len(self.discard)): #捨て牌自分から見て
                                        index = (tehaiplayer + l) % len(self.discard)
                                        data.extend(self.discard[index])
                                    for m in range(len(self.score)): #点数自分から見て
                                        index = (tehaiplayer + m) % len(self.score)
                                        data.append(self.score[index] // 100)
                                    data.append(self.tiles) #残り牌数
                                    data.append(0) #0が鳴きなし 1がカン
                                    self.csvdata = data
                    elif self.todo == 4:
                        pass
                    else:
                        raise ValueError("todoがおかしい")