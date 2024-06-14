import copy

def zimo(self, i):
    #print("ツモ")
    
    z = "zimo"
    
    self.tiles -= 1
    #print(self.tehaiok[i[z]["l"]])
    self.tehaiok[i[z]["l"]][self.dorall.index(i[z]["p"])] += 1
    
    #カカン処理
    if self.todo == 3:
        nakitmp = copy.deepcopy(self.naki[i[z]["l"]])
        indexes = [] #ぽんしている牌
        for count, element in enumerate(nakitmp): #赤ドラを移動 (ここにnakitmpを移動させてcsvにはself.naki[i[z]["l"]]を入れる)
            if count == 9 and element == 1:
                nakitmp[4] += 1
                nakitmp[9] -= 1
            if count == 19 and element == 1:
                nakitmp[14] += 1
                nakitmp[19] -= 1
            if count == 29 and element == 1:
                nakitmp[24] += 1
                nakitmp[29] -= 1
        for count, element in enumerate(nakitmp): #すでにポンをしている中にツモ牌があるか確認
            if element == 3:
                indexes.append(count)
        if indexes != []: #プレイヤーがポンしている時
            if self.dorall.index((i[z]["p"])) in indexes:
                #カカンcsv処理
                data = []
                data += self.tehaiok[i[z]["l"]] #手牌
                for j in range(len(self.reach)): #リーチ自分から見て
                    index = (i[z]["l"] + j) % len(self.reach)
                    #print(index, tehaitmp[i[z]["l"]])
                    data.append(self.reach[index])
                data += self.dora #ドラ34
                data.append(self.parentdora) #場風
                data.append(self.childdora) #自風
                data.append(self.changbang) #何本場
                data.append(self.lizhibang) #リーチ棒繰越
                for k in range(len(self.naki)): #鳴き自分から見て
                    index = (i[z]["l"] + k) % len(self.naki)
                    data.extend(self.naki[index])
                for l in range(len(self.discard)): #捨て牌自分から見て
                    index = (i[z]["l"] + l) % len(self.discard)
                    data.extend(self.discard[index])
                for m in range(len(self.score)): #点数自分から見て
                    index = (i[z]["l"] + m) % len(self.score)
                    data.append(self.score[index] // 100)
                data.append(self.tiles) #残り牌数
                data.append(0) #0が鳴きなし 1がカン
                #self.writer.writerow(data)
                self.csvdata = data
                #print(self.csvdata)
                #カカンcsv処理終了
            elif self.dorall.index((i[z]["p"])) in [9, 19, 29]: # 赤ドラをカカンする時用
                if self.naki[i[z]["l"]][4] == 3 or self.naki[i[z]["l"]][14] == 3 or self.naki[i[z]["l"]][24] == 3: # 赤ドラをカカンする時用
                    data = []
                    data += self.tehaiok[i[z]["l"]] #手牌
                    for j in range(len(self.reach)): #リーチ自分から見て
                        index = (i[z]["l"] + j) % len(self.reach)
                        #print(index, tehaitmp[i[z]["l"]])
                        data.append(self.reach[index])
                    data += self.dora #ドラ34
                    data.append(self.parentdora) #場風
                    data.append(self.childdora) #自風
                    data.append(self.changbang) #何本場
                    data.append(self.lizhibang) #リーチ棒繰越
                    for k in range(len(self.naki)): #鳴き自分から見て
                        index = (i[z]["l"] + k) % len(self.naki)
                        data.extend(self.naki[index])
                    for l in range(len(self.discard)): #捨て牌自分から見て
                        index = (i[z]["l"] + l) % len(self.discard)
                        data.extend(self.discard[index])
                    for m in range(len(self.score)): #点数自分から見て
                        index = (i[z]["l"] + m) % len(self.score)
                        data.append(self.score[index] // 100)
                    data.append(self.tiles) #残り牌数
                    data.append(0) #0が鳴きなし 1がカン
                    self.csvdata = data
        
    #print(self.tehaiok[i[z]["l"]])
    #アンカン確認処理
    if self.todo == 3:
        tehaitmp = []
        tehaitmp = copy.deepcopy(self.tehaiok[i[z]["l"]])
        indexes = []
        for count, element in enumerate(tehaitmp): #赤ドラを移動 (ここにnakitmpを移動させてcsvにはself.naki[i[z]["l"]]を入れる)
            if count == 9 and element == 1:
                tehaitmp[4] += 1
                tehaitmp[9] -= 1
            if count == 19 and element == 1:
                tehaitmp[14] += 1
                tehaitmp[19] -= 1
            if count == 29 and element == 1:
                tehaitmp[24] += 1
                tehaitmp[29] -= 1
        for count, element in enumerate(tehaitmp): #捨て牌と手牌を合わせてミンカンできるか確認
            if element == 4: #手牌と捨て牌を合わせて4枚ある時
                indexes.append(count)
        if indexes != []: #4枚ある時
            if self.dorall.index((i[z]["p"])) in indexes: #ツモ牌と手牌を合わせて4枚ある時の中にツモ牌がある時
                #アンカンcsv処理
                data = []
                data += self.tehaiok[i[z]["l"]] #手牌
                for j in range(len(self.reach)): #リーチ自分から見て
                    index = (i[z]["l"] + j) % len(self.reach)
                    #print(index, tehaitmp[i[z]["l"]])
                    data.append(self.reach[index])
                data += self.dora #ドラ34
                data.append(self.parentdora) #場風
                data.append(self.childdora) #自風
                data.append(self.changbang) #何本場
                data.append(self.lizhibang) #リーチ棒繰越
                for k in range(len(self.naki)): #鳴き自分から見て
                    index = (i[z]["l"] + k) % len(self.naki)
                    data.extend(self.naki[index])
                for l in range(len(self.discard)): #捨て牌自分から見て
                    index = (i[z]["l"] + l) % len(self.discard)
                    data.extend(self.discard[index])
                for m in range(len(self.score)): #点数自分から見て
                    index = (i[z]["l"] + m) % len(self.score)
                    data.append(self.score[index] // 100)
                data.append(self.tiles) #残り牌数
                data.append(0) #0が鳴きなし 1がカン
                #self.writer.writerow(data)
                self.csvdata = data
                #アンカンcsv処理終了
            elif self.dorall.index((i[z]["p"])) in [9, 19, 29]: # 赤ドラをアンカンする時用
                if self.tehaiok[i[z]["l"]][4] == 3 or self.tehaiok[i[z]["l"]][14] == 3 or self.tehaiok[i[z]["l"]][24] == 3:
                    data = []
                    data += self.tehaiok[i[z]["l"]] #手牌
                    for j in range(len(self.reach)): #リーチ自分から見て
                        index = (i[z]["l"] + j) % len(self.reach)
                        #print(index, tehaitmp[i[z]["l"]])
                        data.append(self.reach[index])
                    data += self.dora #ドラ34
                    data.append(self.parentdora) #場風
                    data.append(self.childdora) #自風
                    data.append(self.changbang) #何本場
                    data.append(self.lizhibang) #リーチ棒繰越
                    for k in range(len(self.naki)): #鳴き自分から見て
                        index = (i[z]["l"] + k) % len(self.naki)
                        data.extend(self.naki[index])
                    for l in range(len(self.discard)): #捨て牌自分から見て
                        index = (i[z]["l"] + l) % len(self.discard)
                        data.extend(self.discard[index])
                    for m in range(len(self.score)): #点数自分から見て
                        index = (i[z]["l"] + m) % len(self.score)
                        data.append(self.score[index] // 100)
                    data.append(self.tiles) #残り牌数
                    data.append(0) #0が鳴きなし 1がカン
                    self.csvdata = data
