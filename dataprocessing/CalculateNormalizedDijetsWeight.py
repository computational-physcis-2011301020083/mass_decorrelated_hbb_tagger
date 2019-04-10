import pandas as pd
import glob
import numpy as np
import h5py
import argparse,math,os
parser = argparse.ArgumentParser(description="%prog [options]", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--path", dest='path',  default="", help="path")
args = parser.parse_args()

filterEff = np.array([1.0240E+00, 6.7198E-04, 3.3264E-04, 3.1953E-04, 5.3009E-04, 9.2325E-04, 9.4016E-04, 3.9282E-04, 1.0162E-02, 1.2054E-02, 5.8935E-03, 2.7015E-03, 4.2502E-04])
xsec = np.array([7.8420E+13, 7.8420E+13, 2.4334E+12, 2.6454E+10, 2.5464E+08, 4.5536E+06, 2.5752E+05, 1.6214E+04, 6.2505E+02, 1.9640E+01, 1.1961E+00, 4.2260E-02, 1.0370E-03])
dsid=np.array(["361020","361021","361022","361023","361024","361025","361026","361027","361028","361029","361030","361031","361032",])
filterEffTimesXsec = filterEff*xsec
events=[]
for i in range(0,13):
  events.append(0)

for i in range(0,13):
  paths= glob.glob(args.path+"/*"+dsid[i]+"*.h5")
  print i,paths
  for f in paths:
    hf= h5py.File(f, "r")
    events[i]=events[i]+hf["metadata"]["nEventsProcessed"]
  print events[i]
list1={}

for i in range(0,13):
  print dsid[i],filterEffTimesXsec[i]/float(events[i])
  list1[dsid[i]]=100000.0*filterEffTimesXsec[i]/float(events[i])
print list1
