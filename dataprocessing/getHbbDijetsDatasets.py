import os

with open("./dataprocessing/hbbDijetsSourceDatasets.csv", "rU") as f:
    lines = f.readlines()

sourceDatasetsWithFlags = [x.strip() for x in lines]

for sourceDatasetWithFlag in sourceDatasetsWithFlags:

    sourceDatasetAndFlag = sourceDatasetWithFlag.split(",")

    sourceDataset = sourceDatasetAndFlag[0]
    flag = sourceDatasetAndFlag[1]

    dsid = sourceDatasetWithFlag.split(".")[2]

    print "processing " +  sourceDataset
    output = os.popen("rucio list-file-replicas " + sourceDataset +" --rse NERSC_LOCALGROUPDISK")

    for line in output.readlines():
        if "/projecta/projectdirs/atlas/" in line:
            filepath = "/projecta/" + line.split("projecta/")[1].split(" |")[0]

            os.popen("cp " + filepath + " ./hbbDijetsDatasets/")

            oldFileName = filepath.split("/")[-1]
            newFileName = oldFileName.split('.h5')[0] + "_" + dsid + "_" + flag + ".h5"

            os.popen("mv ./hbbDijetsDatasets/" + oldFileName + " ./hbbDijetsDatasets/" + newFileName)

