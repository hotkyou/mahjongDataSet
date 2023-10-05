import csv
import json
import os
import glob
import tqdm
import numpy as np


input_dir = 'json'

os.chdir(input_dir)
json_list = glob.glob('*.json')
w = open("data.csv", mode="w", newline="")
writer = csv.writer(w)

for i in tqdm.tqdm(range(len(json_list))):
    np.pi*np.pi
    #並び替え用配列
    all = ['m1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 'z1', 'z2', 'z3', 'z4', 'z5', 'z6', 'z7']
    
    tehaiok = [[0 for i in range(14)] for j in range(4)] #一人の編集済み手牌

    first = 0 # 1回目の配牌の判定

    with open(json_list[i]) as file:
        for line in file:
            jsondata = json.loads(line)
            # ４人の手牌
            data = jsondata['log'][0][0]['qipai']['shoupai']
            #print(data)
            #一人分の手牌に変換
            for index, tehai in enumerate(data):
                sindex = 0
                #print(list(tehai))
                tehai = list(tehai)
                #一文字ずつ取り出し
                for str in tehai:
                    if str == 'm':
                        mpsz = "m"
                    elif str == 'p':
                        mpsz = "p"
                    elif str == 's':
                        mpsz = "s"
                    elif str == 'z':
                        mpsz = "z"
                    else:
                        tehaiok[index][sindex] = mpsz + str
                        sindex = sindex + 1
                        
            #print(tehaiok)
            
            #列ごとの処理
            #print(len(jsondata['log']))
            
            for makecsv in jsondata['log']:
                #print(makecsv)
                kickplayer = [0, 0, 0, 0]
                for usedata in makecsv:
                    #print(usedata)
                    error = 0
                    if 'zimo' in usedata: #ツモ
                        first = 1
                        if kickplayer[usedata['zimo']['l']] == 0: 
                            #print(usedata['zimo'])
                            #print(tehaiok[usedata['zimo']['l']])
                            for index in range(14):
                                if tehaiok[usedata['zimo']['l']][index] == 0:
                                    tehaiok[usedata['zimo']['l']][index] = usedata['zimo']['p']
                                    error = 1
                                    break
                            if error == 0:
                                print("error1")
                                break
                            #print(usedata['zimo']['l'])
                    elif 'dapai' in usedata: #打牌
                        if kickplayer[usedata['dapai']['l']] == 0:
                            #print(kickplayer)
                            #print(usedata['dapai'])
                            #csv格納用配列
                            gocsv = [0 for i in range(34)]
                            for index in range(14):
                                if tehaiok[usedata['dapai']['l']][index] == usedata['dapai']['p'] or tehaiok[usedata['dapai']['l']][index] + '_' == usedata['dapai']['p']:
                                    if len(usedata['dapai']['p']) == 3: #_がある場合
                                        usedata['dapai']['p'] = usedata['dapai']['p'].removesuffix('_')
                                    for y in tehaiok[usedata['dapai']['l']]:
                                        if y == 'm0': #まさかの赤ドラ０だったので対応
                                            y = 'm5'
                                        elif y == 'p0':
                                            y = 'p5'
                                        elif y == 's0':
                                            y = 's5'
                                        alli = -1
                                        for allindex in all:
                                            #crint(allindex, y)
                                            alli += 1
                                            if y == allindex:
                                                gocsv[alli] += 1
                                                break
                                    gocsv.append(usedata['dapai']['p'])
                                    writer.writerow(gocsv) #csvに書き込み
                                    tehaiok[usedata['dapai']['l']].append(usedata['dapai']['p'])
                                    #writer.writerow(tehaiok[usedata['dapai']['l']]) #csvに書き込み
                                    del tehaiok[usedata['dapai']['l']][-1]
                                    
                                    tehaiok[usedata['dapai']['l']][index] = 0
                                    error = 1
                                    break
                                elif tehaiok[usedata['dapai']['l']][index] + '*' == usedata['dapai']['p'] or tehaiok[usedata['dapai']['l']][index] + '_*' == usedata['dapai']['p']:
                                    kickplayer[usedata['dapai']['l']] = 1
                                    error = 1
                                    #print('リーチ')
                            if error == 0:
                                #print(usedata['dapai']['p'])
                                print("error2")
                                break
                    elif 'fulou' in usedata:
                        #print(usedata['fulou']['l'])
                        kickplayer[usedata['fulou']['l']] = 1
                    elif 'gang' in usedata:
                        #print(usedata['gang']['l'])
                        kickplayer[usedata['gang']['l']] = 1
                    elif 'qipai' in usedata: #配牌
                        if first == 1:
                            #print('配牌')
                            kickplayer = [0, 0, 0, 0]
                            tehaiok = [[0 for i in range(14)] for j in range(4)] #一人の編集済み手牌
                            data = usedata['qipai']['shoupai']
                            #print(data)
                            for index, tehai in enumerate(data):
                                sindex = 0
                                #print(list(tehai))
                                tehai = list(tehai)
                                #一文字ずつ取り出し
                                for str in tehai:
                                    if str == 'm':
                                        mpsz = "m"
                                    elif str == 'p':
                                        mpsz = "p"
                                    elif str == 's':
                                        mpsz = "s"
                                    elif str == 'z':
                                        mpsz = "z"
                                    else:
                                        tehaiok[index][sindex] = mpsz + str
                                        sindex = sindex + 1
                        
                    #print(tehaiok)
                #print("段落終わり")