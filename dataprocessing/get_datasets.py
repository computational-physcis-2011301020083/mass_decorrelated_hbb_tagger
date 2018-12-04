import os

with open("./dataprocessing/datasets.csv", "rU") as f:
    lines = f.readlines()

sourceDatasetsWithFlags = [x.strip() for x in lines]

for sourceDatasetWithFlag in sourceDatasetsWithFlags:

    sourceDatasetAndFlag = sourceDatasetWithFlag.split(",")

    sourceDataset = sourceDatasetAndFlag[0]
    flag = sourceDatasetAndFlag[1]

    print "processing " +  sourceDataset
    output = os.popen("rucio list-file-replicas " + sourceDataset +" --rse NERSC_LOCALGROUPDISK")

    for line in output.readlines():
        if "/projecta/projectdirs/atlas/" in line:
            filepath = "/projecta/" + line.split("projecta/")[1].split(" |")[0]

            os.popen("cp " + filepath + " ./datasets/")

            oldFileName = filepath.split("/")[-1]
            newFileName = oldFileName.split('.h5')[0] + "_" + flag + ".h5"

            os.popen("mv ./datasets/" + oldFileName + " ./datasets/" + newFileName)


