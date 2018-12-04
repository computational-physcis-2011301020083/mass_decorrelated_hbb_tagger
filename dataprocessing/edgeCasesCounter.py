import pandas as pd

with open("./dataprocessing/HiggsDatasets.txt", "rU") as f:
    lines = f.readlines()

sourceDatasets = [x.strip() for x in lines]

numAllTotal = 0
numEdgeTotal = 0

for sourceDataset in sourceDatasets:
    filePath = "./datasets/" + sourceDataset
    key = "fat_jet"

    df = pd.read_hdf(filePath, key)

    numAll = len(df.index)

    hCountKey = "GhostHBosonsCount"
    bCountKey = "GhostBHadronsFinalCount"

    # Signal cases: (1H, >= 2b) or (2H, >= 2b)
    signalDf = df[((df[hCountKey] == 1) & (df[bCountKey] >= 2)) | ((df[hCountKey] == 2) & (df[bCountKey] >= 2))]
    numSignal = len(signalDf.index)

    # QCD cases: no H
    qcdDf = df[(df[hCountKey] == 0)]
    numQcd = len(qcdDf.index)

    # Edge cases: (1H, < 2b) or (2H, < 2b)
    edgeDf = df[((df[hCountKey] == 1) & (df[bCountKey] < 2)) | ((df[hCountKey] == 2) & (df[bCountKey] < 2))]
    numEdge = len(edgeDf.index)

    numAllTotal = numAllTotal + numAll
    numEdgeTotal = numEdgeTotal + numEdge

print float(numEdgeTotal)/float(numAllTotal)





