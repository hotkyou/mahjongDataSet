def zimo(self, i):
    #print("ツモ")
    
    z = "zimo"
    
    self.tiles -= 1
    #print(self.tehaiok[i[z]["l"]])
    if self.reach[i[z]["l"]] != 1:
        self.tehaiok[i[z]["l"]][self.dorall.index(i[z]["p"])] += 1
    #print(self.tehaiok[i[z]["l"]])