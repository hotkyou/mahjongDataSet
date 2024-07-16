import csv
import json
import os
import glob
import tqdm
import numpy as np
import pandas as pd
import dapai, fulou, kaigang, hule, pingju, gang, gangzimo, zimo, error, qipai

class DataControl:
    def __init__(self):

        self.todo = 4 # 0:捨て牌 1:ポン 2:チー 3:カン 4:リーチ
        self.folder_path = "/Users/hotkyou/dev/git/mahjongDataSet/json1"
        self.json_files = glob.glob(os.path.join(self.folder_path, '**/*.json'), recursive=True)
        self.writer = csv.writer(open(f"reach.csv", mode="w", newline="", encoding="utf-8"))
        self.input_dir = 'json'
        self.json_list = glob.glob('json1/*.json')
        self.all = ['m1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8',
                    'p9', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 'z1', 'z2', 'z3', 'z4', 'z5', 'z6', 'z7']
        self.dorall = ['m1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm0', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6',
                    'p7', 'p8', 'p9', 'p0', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's0', 'z1', 'z2', 'z3',
                    'z4', 'z5', 'z6', 'z7']
        
        self.tehaiok = [[0 for i in range(37)] for j in range(4)]  # 手牌4人分用意
        self.reach = [0, 0, 0, 0]  # リーチの有無
        self.dora = [0 for i in range(34)]  # ドラ
        self.parentdora = 0 #場風
        self.childdora = 0 #自風
        self.changbang = 0 #何本場
        self.lizhibang = 0 #リーチ棒繰越
        self.naki = [[0 for i in range(37)] for j in range(4)]  # 鳴きの有無
        self.discard = [[0 for i in range(37)] for j in range(4)]  # 捨て牌
        self.score = [0, 0, 0, 0]  # 点数
        self.tiles = 70  # 残り牌数
        
        self.csvdata = []
        
    def loadJson(self):
        for i in tqdm.tqdm(range(len(self.json_files))):
            np.pi*np.pi
            with open(self.json_files[i], encoding="utf-8") as file:
                for line in file:
                    jsondata = json.loads(line)
                    self.data = jsondata["log"]
                    title = jsondata["title"]
                    if "三" in title:
                        print(title)
                        break
                    else:
                        # print(self.data)
                        for data in self.data:
                            for i in data:
                                #print(i)
                                if self.todo == 3:
                                    if self.csvdata != []:
                                        if not "fulou" in i and not "gang" in i and not "kaigang" in i:
                                            self.writer.writerow(self.csvdata)
                                            self.csvdata = []
                                elif self.todo == 1:
                                    if self.csvdata != []:
                                        if not "fulou" in i:
                                            self.writer.writerow(self.csvdata)
                                            self.csvdata = []
                                            
                                if "qipai" in i:
                                    qipai.qipai(self, i)
                                elif "zimo" in i:
                                    zimo.zimo(self, i)
                                elif "dapai" in i:
                                    dapai.dapai(self, i)
                                elif "fulou" in i:
                                    fulou.fulou(self, i)
                                elif "gang" in i:
                                    gang.gang(self, i)
                                elif "gangzimo" in i:
                                    gangzimo.gangzimo(self, i)
                                elif "kaigang" in i:
                                    kaigang.kaigang(self, i)
                                elif "hule" in i:
                                    hule.hule(self, i)
                                elif "pingju" in i:
                                    pingju.pingju(self, i)
                                else:
                                    error.error(self, i)
                                    raise ValueError("aaa")

DataControl = DataControl()
DataControl.loadJson()
