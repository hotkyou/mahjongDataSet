from collections import Counter

def fulou(self, i):
    #print("鳴き")
    #print(i)
    player = i["fulou"]["l"]
    tile = i["fulou"]["m"]
    mpsz = ""
    
    # csv出力処理
    if self.todo == 1 or self.todo == 2 or self.todo == 3:
        print(tile)
        if any(value == 4 for value in Counter(tile).values()): #カン
            #raise ValueError("カン")
            
            pass
        elif any(value >= 2 for value in Counter(tile).values()): #ぽん
            #raise ValueError("ポン")
            
            pass
        else:   #チー
            #raise ValueError("チー")
            pass
    
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
