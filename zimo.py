import copy

def zimo(self, i):
    #print("ツモ")
    
    z = "zimo"
    
    self.tiles -= 1
    #print(self.tehaiok[i[z]["l"]])
    self.tehaiok[i[z]["l"]][self.dorall.index(i[z]["p"])] += 1
    
    if self.reach[i[z]["l"]] != 1:
        #カカン処理
        if self.todo == 3:
            tehaitmp = []
            tehaitmp = copy.deepcopy(self.tehaiok[i[z]["l"]])
            indexes = [] #ぽんしている牌
            for count, element in enumerate(self.naki[i[z]["l"]]): #すでにポンをしている中にツモ牌があるか確認
                if element == 3:
                    indexes.append(count)
            if indexes != []: #プレイヤーがポンしている時
                if self.dorall.index((i[z]["p"])) in indexes:
                    #カカンcsv処理
                    data = []
                    data += tehaitmp #手牌
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
                    self.writer.writerow(data)
                    #カカンcsv処理終了
        
    #print(self.tehaiok[i[z]["l"]])
    #アンカン確認処理
    if self.todo == 3:
        tehaitmp = []
        tehaitmp = copy.deepcopy(self.tehaiok[i[z]["l"]])
        indexes = []
        for count, element in enumerate(tehaitmp): #捨て牌と手牌を合わせてミンカンできるか確認
            if element == 4: #手牌と捨て牌を合わせて4枚ある時
                indexes.append(count)
        if indexes != []: #4枚ある時
            if self.dorall.index((i[z]["p"])) in indexes: #ツモ牌と手牌を合わせて4枚ある時の中にツモ牌がある時
                #アンカンcsv処理
                data = []
                data += tehaitmp #手牌
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
                self.writer.writerow(data)
                #アンカンcsv処理終了