from collections import Counter

def fulou(self, i):
    #print("鳴き")
    #print(i)
    player = i["fulou"]["l"]
    tile = i["fulou"]["m"]
    mpsz = ""

    if self.todo == 1: #ぽん

        if any(value == 3 for value in Counter([t.replace('0', '5') for t in tile]).values()):#ぽん
            if self.csvdata != []:
                self.csvdata[-1] = 1
                self.writer.writerow(self.csvdata)
                self.csvdata = []

    elif self.todo == 2: #チー
        if all(value == 1 for value in Counter([t.replace('0', '5') for t in tile]).values()):#ぽん
            # print(i)
            result = self.dorall.index(tile[:2])
            if self.csvdata != []:
                # print(result)
                # print(self.csvdata)
                self.csvdata[-1] = result
                self.writer.writerow(self.csvdata)
                self.csvdata = []
            else:
                data = []
                data += self.tehaiok[player] #手牌
                for j in range(len(self.reach)): #リーチ自分から見て
                    index = (player + j) % len(self.reach)
                    #print(index)
                    data.append(self.reach[index])
                data += self.dora #ドラ34
                data.append(self.parentdora) #場風
                #data.append(self.childdora) #自風
                data.append(player) #自風
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
                data.append(result) #37が鳴きなし それ以外が鳴き
                self.csvdata = data
        
    elif self.todo == 3: #カン
        if any(value == 4 for value in Counter([t.replace('0', '5') for t in tile]).values()): #カン
            if self.csvdata != []:
                self.csvdata[-1] = 1
                self.writer.writerow(self.csvdata)
                self.csvdata = []
            else:
                raise ValueError("カン用csv処理エラー")
            #カン用csv処理終了
    
    for num in range(len(tile)):
        if tile[num] == "m" or tile[num] == "p" or tile[num] == "s" or tile[num] == "z":
            mpsz = tile[num]
        elif tile[num] == "+" or tile[num] == "=" or tile[num] == "-":
            pass
        else:
            if mpsz + tile[num] in self.dorall:
                #print(tile[num])
                #print(num)
                self.naki[player][self.dorall.index(mpsz + tile[num])] += 1
                if num < len(tile) - 1: # なぜかこれないとエラー(なぜかこれでうまくいってる)
                    if tile[num + 1] == "+" or tile[num + 1] == "=" or tile[num + 1] == "-": #鳴かれた人の捨て牌から削除処理
                        if tile[num + 1] == "+":
                            nakaretaplayer = player + 1
                            if nakaretaplayer == 4:
                                nakaretaplayer = 0
                        elif tile[num + 1] == "=":
                            nakaretaplayer = player + 2
                            if nakaretaplayer >= 4:
                                nakaretaplayer = nakaretaplayer - 4
                        else:
                            nakaretaplayer = player -1
                            if nakaretaplayer == -1:
                                nakaretaplayer = 3
                        if self.discard[nakaretaplayer][self.dorall.index(mpsz + tile[num])] >= 1:
                            self.discard[nakaretaplayer][self.dorall.index(mpsz + tile[num])] -= 1
                        else:
                            raise ValueError("鳴かれた人の捨て牌配列から捨てようとしたが捨て牌配列になかった")
                    else:
                        if self.tehaiok[player][self.dorall.index(mpsz + tile[num])] -1 >= 0:
                            self.tehaiok[player][self.dorall.index(mpsz + tile[num])] -= 1
                        else:
                            raise ValueError("手配がマイナスに!fulou")
                else:
                    if self.tehaiok[player][self.dorall.index(mpsz + tile[num])] -1 >= 0:
                            self.tehaiok[player][self.dorall.index(mpsz + tile[num])] -= 1
                    else:
                        raise ValueError("手配がマイナスに!fulou2")
            else:
                print(mpsz + tile[num])
                raise ValueError("鳴きチェックエラー:" + i)
