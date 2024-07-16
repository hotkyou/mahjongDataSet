from collections import Counter
import copy

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
       for tehaiplayer, tehainakami in enumerate(tehaitmp):
        tmp = tile[:-2]
        tile_index=self.dorall.index(tmp)
        tehaitmp = copy.deepcopy(self.tehaiok)
        print(tile)
        if tile_index< 27:
            mod = tile_index % 9
            if mod >= 2 and tehaitmp[tehaiplayer][tile_index - 2] > 0 and tehaitmp[tehaiplayer][tile_index - 1] > 0:
                print(mod)
                self.csvdata[-1] = tile_index-2
                self.writer.writerow(self.csvdata)
                self.csvdata = []
            if mod >= 1 and mod <= 7 and tehaitmp[tehaiplayer][tile_index - 1] > 0 and tehaitmp[tehaiplayer][tile_index + 1] > 0:
                self.csvdata[-1] = tile_index-1
                self.writer.writerow(self.csvdata)
                self.csvdata = []
            if mod <= 6 and tehaitmp[tehaiplayer][tile_index + 1] > 0 and tehaitmp[tehaiplayer][tile_index + 2] > 0:
                self.csvdata[-1] = tile_index
                self.writer.writerow(self.csvdata)
                self.csvdata = []
            
        # if ?:
            #raise ValueError("ポン")
                #print(tile)
        
        
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
