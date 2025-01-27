import re

def hule(self, i):
    #print("和了")
    #print(i)
    player = i["hule"]["l"]
    if self.todo == 5 :
        if i["hule"]["baojia"] is not None:
            dataiplayer = i["hule"]["baojia"]
            shoupai=i["hule"]["shoupai"]
            match = re.search(r"(..),(?=\S)", shoupai)
            if match:
                 # 出力: "s5"
                index= match.group(1)
            else:
                match = re.search(r"..$", shoupai)
                index= match.group(0)
            dtile= self.dorall.index(index)
            print(dtile)

            data = []
            data += self.tehaiok[dataiplayer] #手牌
            for j in range(len(self.reach)): #リーチ自分から見て
                index = (dataiplayer + j) % len(self.reach)
                #print(index)
                data.append(self.reach[index])
            data += self.dora #ドラ34
            data.append(self.parentdora) #場風
            data.append(dataiplayer) #自風
            data.append(self.changbang) #何本場
            data.append(self.lizhibang) #リーチ棒繰越
            for k in range(len(self.naki)): #鳴き自分から見て
                index = (dataiplayer + k) % len(self.naki)
                data.extend(self.naki[index])
            for l in range(len(self.discard)): #捨て牌自分から見て
                index = (dataiplayer + l) % len(self.discard)
                data.extend(self.discard[index])
            for m in range(len(self.score)): #点数自分から見て
                index = (dataiplayer + m) % len(self.score)
                data.append(self.score[index] // 100)
            data.append(self.tiles) #残り牌数
            data.append(dtile) #37が鳴きなし それ以外が鳴き
            self.writer.writerow(data)

    #and self.dapaitile[0] == 1: #ロンされた時のみ学習させるので
            #dataiplayer = self.dapaitile[2] #ロンされた人
            #dtile = self.dapaitile[1]   #ロンされた牌
            
            
            # data = []
            # data += self.tehaiok[dataiplayer] #手牌
            # for j in range(len(self.reach)): #リーチ自分から見て
            #     index = (dataiplayer + j) % len(self.reach)
            #     #print(index)
            #     data.append(self.reach[index])
            # data += self.dora #ドラ34
            # data.append(self.parentdora) #場風
            # data.append(dataiplayer) #自風
            # data.append(self.changbang) #何本場
            # data.append(self.lizhibang) #リーチ棒繰越
            # for k in range(len(self.naki)): #鳴き自分から見て
            #     index = (dataiplayer + k) % len(self.naki)
            #     data.extend(self.naki[index])
            # for l in range(len(self.discard)): #捨て牌自分から見て
            #     index = (dataiplayer + l) % len(self.discard)
            #     data.extend(self.discard[index])
            # for m in range(len(self.score)): #点数自分から見て
            #     index = (dataiplayer + m) % len(self.score)
            #     data.append(self.score[index] // 100)
            # data.append(self.tiles) #残り牌数
            # data.append(dtile) #37が鳴きなし それ以外が鳴き
            # self.writer.writerow(data)