import pandas as pd

hCountKey = "GhostHBosonsCount"
bCountKey = "GhostBHadronsFinalCount"


def label_row(row, isHiggsSample):
    if row[hCountKey] >= 1:
        if row[bCountKey] >= 2:
            return "Hbb"
        else:
            return "ignore"
    else:
        if row[bCountKey] >=2 and not isHiggsSample:
            return "gbb"
        else:
            return "qcd"


def isHbb(row_label):
    if row_label == "Hbb":
        return 1
    else:
        return 0


def isGbb(row_label):
    if row_label == "gbb":
        return 1
    else:
        return 0


def isQcd(row_label):
    if row_label == "qcd":
        return 1
    else:
        return 0


with open("./dataprocessing/expandedDatasets.txt", "rU") as f:
    lines = f.readlines()

sourceDatasets = [x.strip() for x in lines]

totalNumEvent = 0
totalNumSignal = 0

for sourceDataset in sourceDatasets:
    print "processing " + sourceDataset

    filePath = "./datasets/" + sourceDataset
    key = "fat_jet"

    df = pd.read_hdf(filePath, key)

    isHiggsSample = "H" in sourceDataset

    df["label"] = df.apply(lambda row: label_row(row, isHiggsSample), axis=1)

    newDf = df[df["label"] != "ignore"]
    newDf = newDf[["Tau21_wta", "C2", "D2", "Angularity", "Aplanarity", "FoxWolfram20", "KtDR", "PlanarFlow", "Split12", "ZCut12", "mcEventWeight", "mass", "pt", "label"]]

    newDf["pt"] = (newDf["pt"]/1000.0).astype("float64")

    newDf["m"] = (newDf["mass"]/1000.0).astype("float64")
    newDf = newDf.drop("mass", axis=1)

    newDf["Tau21"] = newDf["Tau21_wta"]
    newDf = newDf.drop("Tau21_wta", axis=1)

    newDf["weight_test"] = newDf["mcEventWeight"]
    newDf = newDf.drop("mcEventWeight", axis=1)

    newDf["signal"] = newDf.apply(lambda row: isHbb(row["label"]), axis=1)

    # will need these in the future
    # newDf["IsHbb"] = newDf["signal"]
    # newDf["IsGbb"] = newDf.apply(lambda row: isGbb(row["label"]), axis=1)
    # newDf["IsQcd"] = newDf.apply(lambda row: isQcd(row["label"]), axis=1)

    numEvent = len(newDf.index)
    numSignal = newDf["signal"].sum()

    totalNumEvent = totalNumEvent + numEvent
    totalNumSignal = totalNumSignal + numSignal

    newDfFilePath = "./processedDatasets/" + sourceDataset.split(".h5")[0] + "_"+ str(numEvent) + "_" + str(numSignal) + ".h5"

    print "saving " + newDfFilePath
    print "total number of events: " + str(totalNumEvent)
    print "total number of signal: " + str(totalNumSignal)
    newDf.to_hdf(newDfFilePath, "dataset", format="table", data_columns=True)

print "total number of events: " + str(totalNumEvent)
print "total number of signal: " + str(totalNumSignal)







