import pandas as pd
import glob
import argparse,math,os
parser = argparse.ArgumentParser(description="%prog [options]", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--path", dest='path',  default="", help="path")
parser.add_argument("--outname", dest='outname',  default="", help="outname")
args = parser.parse_args()

paths=sorted(glob.glob(args.path+"/*.h5"))
h0=pd.read_hdf(paths[0])
h1=pd.read_hdf(paths[1])
print paths
print "Processing first two files"
SumH=pd.concat([h0, h1], ignore_index=True)
Index=len(h0.index)+len(h1.index)
paths.remove(paths[0])
paths.remove(paths[0])
print paths,len(paths)
j=0
for f in paths:
  j=j+1
  print j,f
  hi=pd.read_hdf(f)
  Index=Index+len(hi.index)
  SumH=pd.concat([SumH, hi], ignore_index=True)


print SumH
print len(SumH.index),Index


newDfFilePath="/global/project/projectdirs/atlas/massDecorrelatedXbb/adversarial-wei1/datasets/ReweightedDatasetsFixed/"+args.outname
SumH.to_hdf(newDfFilePath, "dataset")



