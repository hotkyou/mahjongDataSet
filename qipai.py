def qipai(self, i):
    #print("配牌")
    
    a = ""
    q = "qipai"
    
    self.tehaiok = [[0 for i in range(37)] for j in range(4)] # +1で入れてるので初期化しないとバグる
    self.reach = [0, 0, 0, 0]
    self.dora = [0 for i in range(34)] # +1で入れてるので初期化しないとバグる
    self.naki = [[0 for i in range(37)] for j in range(4)]
    self.discard = [[0 for i in range(37)] for j in range(4)]  # 捨て牌
    self.tiles = 70
    
    self.parentdora = i[q]["zhuangfeng"] # 場風
    self.childdora = i[q]["jushu"] # 局数(自風)
    self.changbang = i[q]["changbang"] # 積み棒(１本場)
    self.lizhibang = i[q]["lizhibang"] # リーチ帽
    for j, num in enumerate(i[q]["defen"]): # 点数
        self.score[j] = num
    if i[q]["baopai"] == "m0": #ドラ
        a = "m5"
    elif i[q]["baopai"] == "p0":
        a = "p5"
    elif i[q]["baopai"] == "s0":
        a = "s5"
    else:
        a = i[q]["baopai"]
    self.dora[self.all.index(a)] += 1
    for k, hai in enumerate(i[q]["shoupai"]): # k = 誰の手牌か hai = その人の手牌
        hai = list(hai)
        # print(hai)
        for str in hai:
            if str == "m" or str == "p" or str == "s" or str == "z":
                mpsz = str
            else:
                self.tehaiok[k][self.dorall.index(mpsz + str)] += 1
        # print(self.tehaiok[k])