import os
import json
import platform
#Hier könenn die Pfade zu den zu kopierenden Dateien, sowie der Ordner und Name des Zielfiles festgelegt werden

def find(name):
    if(platform.system() == "Linux"):
        path = "/root"
    elif(platform.system() == "Darwin"):
        path = "/Users"
    elif(platform.system() == "Windows"):
        path = "C:"

    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def getConfig():
    global savePath, safeFile, rootPath, startDate, endDate
    #settingsFile = find("CopyConfig.json")
    settingsFile = "CopyConfig.json"
    with open(settingsFile, "r") as read_file:
        data = json.load(read_file)
    #Angabe des Pfads unter welchem die neue .csv Datei gespeichert wird
    #Hinweis: Für Windows muss r vor dem Pfad ergänzt werden z.B. r"C:\User\...\"
    savePath = os.path.realpath(data["savePath"])

    #Name der .csv Datei
    #Endung .csv nicht editieren
    safeFile = data["safeFile"] + ".csv"

    #Angabe des Pfads zu den gespeicherten Dateien
    #Hinweis: Für Windows muss r vor dem Pfad ergänzt werden z.B. r"C:\User\...\"
    rootPath = os.path.realpath(data["rootPath"])

    startDate = data['startDate']
    endDate = data['endDate']


