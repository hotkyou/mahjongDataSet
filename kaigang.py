def kaigang(self, i):
    #print("カンドラ")
    #print(i)
    tmp = i["kaigang"]["baopai"]
    if tmp == "m0":
        tmp = "m5"
    elif tmp == "p0":
        tmp = "p5"
    elif tmp == "s0":
        tmp = "s5"
    self.dora[self.all.index(tmp)] += 1