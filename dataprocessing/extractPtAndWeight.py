import pandas as pd
import glob

paths = glob.glob("./labelledHbbTopDatasets/*.h5")

i = 0
for path in paths:
	i = i + 1
	print "Processing {}: {}".format(i, path)
	df = pd.read_hdf(path)[["pt","signal","weight_test", "eventNumber"]]

	df["pt"] = df["pt"].astype("float64")
	df["signal"] = df["signal"].astype("int32")
	df["weight_test"] = df["weight_test"].astype("float32")

	fileName = path.split('/')[-1]
	df["datasource"] = fileName
	df["datasource"] = df["datasource"].astype('S80')

	df["dsid"] = fileName.split('_')[2]
	df["dsid"] = df["dsid"].astype('int32')

	newFilePath = "./extractedHbbTopDatasets/" + fileName
	df.to_hdf(newFilePath, "dataset", format="table", data_columns=True)
