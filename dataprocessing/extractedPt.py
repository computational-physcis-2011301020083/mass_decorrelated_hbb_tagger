import pandas as pd
import argparse,math,os,glob
parser = argparse.ArgumentParser(description="%prog [options]", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--path", dest='path',  default="", help="path")
args = parser.parse_args()

outpath="/global/project/projectdirs/atlas/massDecorrelatedXbb/adversarial-wei1/datasets/MergedDatasetsFixed/ExtractedHbbDijetsPt2TeV/"
paths=glob.glob(args.path+"/*.h5")
for f in paths:
  print f
  name=f.split("/")[-1]
  df = pd.read_hdf(f)[["dsid","pt","signal","weight_test"]]
  df=df[df["pt"]<=2000] 
  path=outpath+name
  df.to_hdf(path, "dataset", format="table", data_columns=True)

print "Done"





