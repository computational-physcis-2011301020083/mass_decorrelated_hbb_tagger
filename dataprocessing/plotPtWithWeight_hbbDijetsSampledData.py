import pandas as pd
import numpy as np

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt


df = pd.read_hdf("./usedDatasets/data_2M_20M_xbbscore_hbbDijets.h5")[["signal", "pt", "weight_test", "weight_adv", "train"]]

hbbDf = df[(df["signal"] == 1)]
dijetsDf = df[(df["signal"] == 0)]

bins = np.linspace(0, 8000, 320)

plt.hist(hbbDf["pt"].values, weights=hbbDf["weight_adv"].values, bins=bins, label="Hbb", histtype="step", color="b")
plt.hist(dijetsDf["pt"].values, weights=dijetsDf["weight_adv"].values, bins=bins, label="Dijets", histtype="step", color="g")


plt.legend(loc='upper right', fontsize="x-small")
plt.yscale("log", nonposy="clip")
plt.ylim(0, 1E8)
plt.xlim(0, 8000)
plt.xlabel("Large R jet pT (GeV)")
plt.ylabel("Reweighted jets")
plt.savefig("./figures/ptWeight_hbbDijetsSample_ReweightedTrain.pdf")

