import pandas as pd
import glob
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

paths = glob.glob("./xbbScorePtWeightExtractedHbbDijetsWithCalculatedWeights/*_N_*.h5")

pathByJzw = {}
for path in paths:
    fileName = path.split('/')[-1]
    jzwNum = int(fileName.split('_')[2]) - 361020

    if jzwNum in pathByJzw.keys():
        pathByJzw[jzwNum].append(path)
    else:
        pathByJzw[jzwNum] = [path]

bins = np.linspace(0, 8000, 320)

colors = ["#800000", "#e6194B", "#9A6324", "#f58231", "#ffe119", "#bfef45", "#3cb44b", "#42d4f4", "#4363d8", "#000075", "#911eb4", "#f032e6", "#a9a9a9"]

jzwSize = 0
allJzwDf = pd.DataFrame(columns=["pt", "weight_test"])
for jzw in pathByJzw.keys():
    filePaths = pathByJzw[jzw]

    jzwDf = pd.DataFrame(columns=["pt", "weight_test"])
    for filePath in filePaths:
        df = pd.read_hdf(filePath)[["pt", "weight_test"]]

        if jzw == 0:
            df = df[df["pt"] < 2000]
        jzwSize = jzwSize + len(df.index)
        
        print "{}".format(filePath)
        jzwDf = pd.concat([jzwDf, df], ignore_index=True)

    allJzwDf = pd.concat([allJzwDf, jzwDf], ignore_index=True)


    plt.hist(jzwDf["pt"].values, weights= jzwDf["calculatedWeight"].values, bins=bins, label="JZ{}W".format(jzw), color=colors[jzw], histtype="step")

plt.hist(allJzwDf["pt"].values, weights= allJzwDf["calculatedWeight"].values, bins=bins, label="All", histtype="step", color="k")

plt.legend(loc='upper right', fontsize="x-small")
plt.yscale("log", nonposy="clip")
plt.ylim(0, 1E9)
plt.xlim(0, 8000)
plt.xlabel("Large R jet pT (GeV)")
plt.ylabel("Weighted Dijets")
plt.savefig("./figures/ptWeight_hbbDijets.pdf")