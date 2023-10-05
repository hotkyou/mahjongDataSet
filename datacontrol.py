import csv
import json
import os
import glob
import tqdm
import numpy as np


class DataControl:
  def __init__(self):
    self.url = "json/2012010100gm-00a9-0000-9b9687d3.json" # jsonのファイル指定 (仮置き)
    
    self.input_dir = 'json'
    self.json_list = glob.glob('*.json')
    self.writter = csv.writer(open("data.csv", mode="w", newline=""))
    pass
  
  def createArray(self):
    
    pass

  def loadJson(self):
    #os.chdir(self.input_dir)
    #for i in tqdm.tqdm(range(len(self.json_list))):
    #  np.pi*np.pi
    #  with open(self.json_list[i]) as file:
      with open(self.url) as file:
        for line in file:
          jsondata = json.loads(line)
          self.data = jsondata["log"]

  def dataControl(self):
    pass

  def writeCSV(self):
    pass

DataControl = DataControl()
DataControl.loadJson()