import csv
from collections import Counter

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
                self.dora[player] = 1
                self.score[player] -= 1000
            elif tile[2] == "_": # 同じ牌を捨てる
                tmp = tile[:-1]
            elif tile[2] == "*": # リーチした時
                tmp = tile[:-1]
                self.dora[player] = 1
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
                data.append(self.score[index])
            data.append(self.tiles) #残り牌数
            data.append(self.dorall.index(tmp)) #何を捨てたか
            self.writer.writerow(data)
        # -- CSV処理終了 --
        
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
    tehaitmp = self.tehaiok.copy()
    print(self.tehaiok)
    for tehaiplayer, tehainakami in enumerate(tehaitmp):
        #print(tehaiplayer, tehainakami)
        if tehaiplayer != player:   #捨て牌を捨てた本人は鳴けないのでスキップ
            if self.reach[tehaiplayer] != 1: #立直してない人のみ
                tehaitmp[tehaiplayer][self.dorall.index(tmp)] += 1

    if self.todo == 1: #ぽん
        for n, o in enumerate(self.tehaiok):
            #print(n, o)
            if n != player:
                pass
    elif self.todo == 2: #チー
        for n, o in enumerate(self.tehaiok):
            #print(n, o)
            if n != player:
                pass
    elif self.todo == 3: #カンをしたらgangで削除処理　全プレイヤーの手牌を処理
        #print(player)
        for n, o in enumerate(self.tehaiok):
            #print(n, o)
            if n != player: #鳴いた人以外のカンできるかチェック
                if Counter(o)[3] >= 1:  # 明カン
                    #print(Counter(o))
                    #raise ValueError("カン3")
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
                        data.append(self.score[index])
                    data.append(self.tiles) #残り牌数
                    data.append(0) #0が鳴きなし 1がカン
                if Counter(o)[4] >= 1:  # 手牌に4枚持っているがカンしていない時
                    pass
            else:
                if Counter(o)[4] >= 1:  # 暗カン
                    #print(Counter(o))
                    #print(self.naki[player])
                    pass
                    #raise ValueError("カン４")
    else:
        pass