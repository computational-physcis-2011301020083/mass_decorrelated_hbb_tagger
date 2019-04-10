import pandas as pd
import glob
import numpy as np
import argparse,math,os
import matplotlib.pyplot as plt
parser = argparse.ArgumentParser(description="%prog [options]", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--path", dest='path',  default="", help="path")
parser.add_argument("--variable", dest='variable',  default="", help="variable")
parser.add_argument("--outpath", dest='outpath',  default="", help="pathout")
args = parser.parse_args()
path="/global/project/projectdirs/atlas/massDecorrelatedXbb/adversarial-wei1/datasets/"
f=path+"/MergedDatasetsFixed/HbbTopDatasets.h5"

if args.variable=="pt":
 df1 = pd.read_hdf(f)[[args.variable, "weight","signal"]]
if args.variable!="pt":
 df1 = pd.read_hdf(f)[[args.variable,"pt", "weight","signal"]]

df1=df1[df1["pt"]<=2000]
OneVa1=df1[df1["signal"] == 1]
OneVa2=df1[df1["signal"] == 0]
Sumweight1=sum(OneVa1["weight"])
OneVa1["weight_fraction"]=OneVa1["weight"]/Sumweight1
Sumweight2=sum(OneVa2["weight"])
OneVa2["weight_fraction"]=OneVa2["weight"]/Sumweight2



varMax = max([max(OneVa1[args.variable]),max(OneVa2[args.variable])])
varMin = min([min(OneVa1[args.variable]),min(OneVa2[args.variable])])
numBins = 50
bins = np.linspace(varMin, varMax, numBins)

plt.hist(OneVa1[args.variable].values,weights=OneVa1["weight_fraction"].values,bins=bins,label="Hbb",histtype="step")
plt.hist(OneVa2[args.variable].values,weights=OneVa2["weight_fraction"].values,bins=bins,label="Top",histtype="step")

plt.legend(loc='upper right', fontsize="x-small")
plt.xlabel(args.variable)
plt.yscale("log", nonposy="clip")
plt.ylabel("Events Fraction")
plt.savefig("/global/project/projectdirs/atlas/massDecorrelatedXbb/adversarial-wei1/dataprocessing/HbbTopPlotsBeforeReweight/"+args.variable+".pdf")














