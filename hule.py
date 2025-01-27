def hule(self, i):
    #print("和了")
    #print(i)
    player = i["hule"]["l"]
    yaku_dict = {
        '立直': 0, '一発': 1, '赤ドラ': 2, '裏ドラ': 3, '役牌 白': 4, '役牌 發': 5, '役牌 中': 6,
        '三色同刻': 7, '三色同順': 8, '混老頭': 9, '対々和': 10, '断幺九': 11, '場風 東': 12,
        '場風 南': 13, '自風 北': 14, '自風 東': 15, '自風 西': 16, '自風 南': 17, '平和': 18,
        '一盃口': 19, '七対子': 20, 'ドラ': 21, '一気通貫': 22, '混一色': 23, '三暗刻': 24,
        '流局': 25, '小三元': 26, '三貫子': 27, '清一色': 28, '四暗刻': 29, '大三元': 30,
        '小四喜': 31, '字一色': 32, '緑一色': 33, '九蓮宝燈': 34, '河底撈魚': 35, '九種九牌': 36,
        '門前清自摸和': 37, '場風 西': 38, '場風 北': 39, '四暗刻単騎': 40, '純全帯幺九': 41,
        '混全帯幺九': 42, '嶺上開花': 43, '海底摸月': 44, '槍槓': 45, '両立直': 46, '二盃口': 47,
        '国士無双': 48, '清老頭': 49, '天和': 50, '地和': 51, '三槓子': 52, '大四喜': 53,
        '純正九蓮宝燈': 54, '国士無双１３面': 55
    }
    yaku_list = [0] * len(yaku_dict)
    # print(yaku_list)
    # print(len(yaku_list))

    # JSONデータ内の役をループで確認
    

    if self.todo == 5 and self.dapaitile[0] == 1: #ロンされた時のみ学習させるので
        dataiplayer = self.dapaitile[2] #ロンされた人
        dtile = self.dapaitile[1]   #ロンされた牌
        
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

        
    if self.todo == 6:
        data = []
        data += self.tehaiok[player] #手牌
        for j in range(len(self.reach)): #リーチ自分から見て
            index = (player + j) % len(self.reach)
            data.append(self.reach[index])
        data += self.dora #ドラ34
        data.append(self.parentdora) #場風
        data.append(self.childdora) #自風
        data.extend(self.naki[player]) #鳴き自分だけ
        data.extend(self.discard[player]) #捨て牌自分だけ
        data.append(self.tiles) #残り牌数
        
        for item in i["hule"]["hupai"]:
            yaku_name = item["name"]
            if yaku_name in yaku_dict:  # 役が辞書に存在する場合のみ処理
                index = yaku_dict[yaku_name]
                #print(index)
                yaku_list[index] = 1  # 該当位置に1をセット
                #print(f"役名: {yaku_name}, インデックス: {index}")
            else:
                print(f"無効なインデックス: {index}, 役名: {yaku_name}")

        data.extend(yaku_list)
        self.writer.writerow(data)
        # デバッグ用出力
        #print("役リスト:", yaku_list)
        #print("dataに追加後:", data)