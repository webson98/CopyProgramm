from functionCalls import *
from settings import getConfig

getConfig()

checkSavePath()

checkSaveFile()

dataFrame = openFileAndCreateDataFrame()

prepareAndSortData(dataFrame)
