import csv
import json
import os
import glob
import tqdm
import numpy as np
import enviroment as env
import dapai, fulou, kaigang, hule, pingju, gang, gangzimo, zimo, error, qipai

class DataControl:
    def __init__(self):
        # jsonのファイル指定 (仮置き)
        self.url = env.json

        self.input_dir = 'json'
        self.json_list = glob.glob('*.json')
        self.writter = csv.writer(open("csv/data.csv", mode="w", newline=""))
        self.all = ['m1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7',
                    'p8', 'p9', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 'z1', 'z2', 'z3', 'z4', 'z5', 'z6', 'z7']
        self.dorall = ['m1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm0', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6',
                    'p7', 'p8', 'p9', 'p0', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's0', 'z1', 'z2', 'z3', 'z4',
                    'z5', 'z6', 'z7']

    def createArray(self):
        self.tehaiok = [[0 for i in range(14)] for j in range(4)]  # 手牌4人分用意
        self.reach = [0, 0, 0, 0]  # リーチの有無
        self.dora = [0 for i in range[34]]  # ドラ
        self.parentdora = [0, 0]
        self.childdora = [0, 0, 0, 0]
        self.naki = [[0 for i in range(34)] for j in range(4)]  # 鳴きの有無
        self.discard = [[0 for i in range(34)] for j in range(4)]  # 捨て牌
        self.score = [25000, 25000, 25000, 25000]  # 点数
        self.tiles = 69  # 残り牌数

    def loadJson(self):
        # os.chdir(self.input_dir)
        # for i in tqdm.tqdm(range(len(self.json_list))):
        #  np.pi*np.pi
        #  with open(self.json_list[i]) as file:
        with open(self.url) as file:
            for line in file:
                jsondata = json.loads(line)
                self.data = jsondata["log"]
                # print(self.data)
                for data in self.data:
                    for i in data:
                        if ("qipai" in i):
                            qipai.qipai(self, i)
                        elif ("zimo" in i):
                            zimo.zimo(self, i)
                        elif ("dapai" in i):
                            dapai.dapai(self, i)
                        elif ("fulou" in i):
                            fulou.fulou(self, i)
                        elif ("gang" in i):
                            gang.gang(self, i)
                        elif ("gangzimo" in i):
                            gangzimo.gangzimo(self, i)
                        elif ("kaigang" in i):
                            kaigang.kaigang(self, i)
                        elif ("hule" in i):
                            hule.hule(self, i)
                        elif ("pingju" in i):
                            pingju.pingju(self, i)
                        else:
                            error.error(self, i)

    def dataControl(self):
        pass

    def writeCSV(self):
        pass


DataControl = DataControl()
DataControl.loadJson()
