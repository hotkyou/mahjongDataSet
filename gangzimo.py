def gangzimo(self, i):
    #print("カンツモ")
    self.tiles -= 1
    #print(self.tehaiok[i[z]["l"]])
    #if self.reach[i["gangzimo"]["l"]] != 1: #これがいるか怪しい csvで手牌が14になってるかチェック
    self.tehaiok[i["gangzimo"]["l"]][self.dorall.index(i["gangzimo"]["p"])] += 1
