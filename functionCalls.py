from datetime import datetime
import os
import platform
import logging
import pandas as pd
import settings

def checkSavePath():
    if not os.path.exists(settings.savePath):
       os.mkdir(settings.savePath)
       print("Created:", settings.savePath)

def checkSaveFile():
    summaryFilePath = os.path.join(settings.savePath, settings.safeFile)
    if not os.path.isfile(summaryFilePath):
        with open(summaryFilePath, 'w') as f:
            f.write('')
            f.close()
            print("Created:", settings.safeFile)
        os.chdir(settings.savePath)


def checkDate(saveData):
    start = buildDate(settings.startDate)
    end = buildDate(settings.endDate, True)
    filtered = saveData[(pd.to_datetime(saveData['Date']) >= start) & (pd.to_datetime(saveData['Date']) <= end)]
    return filtered

def prepareAndSortData(saveData):
    if saveData.empty:
        exit()
    saveData.drop_duplicates(inplace=True)
    saveData.sort_values(by=["Date", "LOC Time"], inplace=True)
    saveData.drop(labels="Record", axis=1, inplace=True)
    saveData = checkDate(saveData)
    saveData.reset_index(drop=True, inplace=True)
    saveData.to_csv(os.path.join(settings.savePath, settings.safeFile))


def openFileAndCreateDataFrame():
    saveData = pd.DataFrame()
    for it in os.scandir(settings.rootPath):
        if it.is_dir():
            for i in range(0, 5):
                if platform.system() == "Windows":
                    dirName = it.path.rsplit('\\', 1)[-1]
                else:
                    dirName = it.path.rsplit('/', 1)[-1]
                filePath = os.path.join(settings.rootPath, dirName, "D" + str(i) + "_" + dirName + ".csv")
                if os.path.isfile(filePath):
                    try:
                        data = pd.read_csv(filePath)
                        saveData = pd.concat([saveData, data], axis=0)
                    except:
                        logging.basicConfig(filename='File.log', encoding='utf-8', level=logging.INFO)
                        logdata = str(datetime.now()) + ' '+ filePath + ' is empty'
                        logging.info(logdata)
    return saveData


def buildDate(datesting, end=False):
    if end:
        date = pd.Timestamp(int(datesting.split(".")[2]), int(datesting.split(".")[1]), int(datesting.split(".")[0]), 23, 59, 59)
    else:
        date = pd.Timestamp(int(datesting.split(".")[2]),int(datesting.split(".")[1]), int(datesting.split(".")[0]))
    return date