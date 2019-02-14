import pandas as pd
import glob
import numpy as np
import h5py

filterEff = np.array([1.0240E+00, 6.7198E-04, 3.3264E-04, 3.1953E-04, 5.3009E-04, 9.2325E-04, 9.4016E-04, 3.9282E-04, 1.0162E-02, 1.2054E-02, 5.8935E-03, 2.7015E-03, 4.2502E-04])
xsec = np.array([7.8420E+13, 7.8420E+13, 2.4334E+12, 2.6454E+10, 2.5464E+08, 4.5536E+06, 2.5752E+05, 1.6214E+04, 6.2505E+02, 1.9640E+01, 1.1961E+00, 4.2260E-02, 1.0370E-03])

filterEffTimesXsec = filterEff*xsec

paths = glob.glob("./xbbScorePtWeightExtractedHbbDijets/*_N_*.h5")

i = 0
for path in paths:
	i = i + 1
	print "processing {}: {}".format(i, path)

	fileName = path.split('/')[-1]

	jzwNum = int(fileName.split('_')[2])-361020

	df = pd.read_hdf(path)

	splitFileName = fileName.split("_")
	h5FileName = "{}_{}_{}_{}.h5".format(splitFileName[0], splitFileName[1], splitFileName[2], splitFileName[3])
	
	hf= h5py.File("./hbbDijetsDatasets/{}".format(h5FileName), "r")
	nEventsProcessed = hf["metadata"]["nEventsProcessed"]
	df["calculatedWeight"] = df["weight_test"] * filterEffTimesXsec[jzwNum]/float(nEventsProcessed)

	newFilePath = "./xbbScorePtWeightExtractedHbbDijetsWithCalculatedWeights/" + fileName
	df.to_hdf(newFilePath, "dataset", format="table", data_columns=True)

print "DONE!"