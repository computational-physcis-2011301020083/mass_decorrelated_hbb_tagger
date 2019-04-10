import os

with open("/global/project/projectdirs/atlas/massDecorrelatedXbb/adversarial-wei1/dataprocessing/HbbDatasets1.csv", "rU") as f:
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
              if flag=="N":
                dirname="/global/project/projectdirs/atlas/massDecorrelatedXbb/adversarial-wei1/datasets/DijetsDatasets"
                os.popen("cp " + filepath + "   /global/project/projectdirs/atlas/massDecorrelatedXbb/adversarial-wei1/datasets/DijetsDatasets")
    
        
                oldFileName = filepath.split("/")[-1]
                newFileName = oldFileName.split('.h5')[0] + "_" + dsid + "_" + flag + ".h5"

                os.popen("mv " +dirname+"/"+ oldFileName + "   "+dirname+"/"+ newFileName)

              if flag=="T":
                dirname="/global/project/projectdirs/atlas/massDecorrelatedXbb/adversarial-wei1/datasets/TopDatasets"
                os.popen("cp " + filepath + "    /global/project/projectdirs/atlas/massDecorrelatedXbb/adversarial-wei1/datasets/TopDatasets")
     
        
                oldFileName = filepath.split("/")[-1]
                newFileName = oldFileName.split('.h5')[0] + "_" + dsid + "_" + flag + ".h5"
               
                os.popen("mv " +dirname+"/"+ oldFileName + "   "+dirname+"/"+ newFileName)
              

              if flag=="H":
                dirname="/global/project/projectdirs/atlas/massDecorrelatedXbb/adversarial-wei1/datasets/HbbDatasets"
                os.popen("cp " + filepath + "    /global/project/projectdirs/atlas/massDecorrelatedXbb/adversarial-wei1/datasets/HbbDatasets")
               
        
                oldFileName = filepath.split("/")[-1]
                newFileName = oldFileName.split('.h5')[0] + "_" + dsid + "_" + flag + ".h5"

         
                os.popen("mv " +dirname+"/"+ oldFileName + "   "+dirname+"/"+ newFileName)




