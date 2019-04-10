import pandas as pd
import glob
import argparse,math,os
parser = argparse.ArgumentParser(description="%prog [options]", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--path", dest='path',  default="", help="path")
args = parser.parse_args()

#tCountKey = "GhostTQuarksFinalCount"
hCountKey = "GhostHBosonsCount"
bCountKey = "GhostBHadronsFinalCount"



'''
def label_row(row, isTopSample):
    if isTopSample:
      if  row[tCountKey] >= 2:
        return "Zprimett"
      else:
        return "ignore"
    else :
      if  row[tCountKey] >= 2:
        return "ignore"
      else :
        return "qcd"
'''

def label_row(row, isTopSample):
    if isTopSample:
      if row[hCountKey] >= 1 and row[bCountKey] >= 2:
        return "ignore"
      else:
        return "Zprimett"
    else :
      if row[hCountKey] >= 1 and row[bCountKey] >= 2:
        return "ignore"
      else :
        return "Zprimett"


#filePath = args.path
filePaths = glob.glob(args.path+"/TopDatasets/*.h5")

list1=['Split12', 'Split23', 'Qw', 'PlanarFlow', 'Angularity', 'Aplanarity', 'ZCut12', 'KtDR', 'HbbScore', 'XbbScoreQCD', 'XbbScoreTop', 'XbbScoreHiggs', 'JSSTopScore', 'pt', 'eta', 'GhostHBosonsCount', 'GhostWBosonsCount', 'GhostZBosonsCount', 'GhostTQuarksFinalCount', 'GhostBHadronsFinalCount', 'GhostCHadronsFinalCount', 'mcEventWeight', 'eventNumber', 'mass', 'C2', 'D2', 'e3', 'Tau21_wta', 'Tau32_wta', 'FoxWolfram20']
list2=['MV2c10_discriminant', 'DL1_pu', 'DL1_pc', 'DL1_pb', 'DL1rnn_pu', 'DL1rnn_pc', 'DL1rnn_pb', 'IP2D_pu', 'IP2D_pc', 'IP2D_pb', 'IP3D_pu', 'IP3D_pc', 'IP3D_pb', 'SV1_pu', 'SV1_pc', 'SV1_pb', 'rnnip_pu', 'rnnip_pc', 'rnnip_pb', 'rnnip_ptau', 'JetFitter_energyFraction', 'JetFitter_mass', 'JetFitter_significance3d', 'JetFitter_deltaphi', 'JetFitter_deltaeta', 'JetFitter_massUncorr', 'JetFitter_dRFlightDir', 'SV1_masssvx', 'SV1_efracsvx', 'SV1_significance3d', 'SV1_dstToMatLay', 'SV1_deltaR', 'SV1_Lxy', 'SV1_L3d', 'JetFitter_nVTX', 'JetFitter_nSingleTracks', 'JetFitter_nTracksAtVtx', 'JetFitter_N2Tpair', 'SV1_N2Tpair', 'SV1_NGTinSvx', 'secondaryVtx_nTrks', 'IP2D_nTrks', 'IP3D_nTrks', 'IP2D_isDefaults', 'IP3D_isDefaults', 'JetFitter_isDefaults', 'SV1_isDefaults', 'secondaryVtx_isDefaults', 'rnnip_isDefaults', 'GhostBHadronsFinalCount', 'GhostCHadronsFinalCount','pt', 'eta', 'deta', 'dphi', 'dr']
list3={}
list4={}
for i in list2:
  list3[i]=i+"_1"
  list4[i]=i+"_2"

for filePath in filePaths:
  #print pd.read_hdf(filePath, "fat_jet")[list1]
  sourceDataset=filePath.split("/")[-1]
  isTopSample = "_T" in sourceDataset
  h1=pd.read_hdf(filePath, "subjet_VRGhostTag_1")[list2]
  h1.rename(columns=list3,inplace=True)
  #print h1
  h2=pd.read_hdf(filePath, "subjet_VRGhostTag_2")[list2]
  h2.rename(columns=list4,inplace=True)
  #print h2
  newDf =  pd.concat([pd.read_hdf(filePath, "fat_jet")[list1], h1,h2], axis=1)
  newDf.dropna(inplace=True)
  newDf["label"] = newDf.apply(lambda row: label_row(row, isTopSample), axis=1)
  newDf["pt"] = (newDf["pt"]/1000.0).astype("float64")
  newDf["mass"] = (newDf["mass"]/1000.0).astype("float64")
  newDf["weight_test"]=newDf["mcEventWeight"]
  newDf["weight"]=newDf["weight_test"]
  newDf=newDf[newDf["label"]!="ignore"]
  newDf["signal"]=0
  newDf["data"]=sourceDataset
  newDf["dsid"]=sourceDataset.split("_")[2]
  
  print "ready"
  newDfFilePath = "/global/project/projectdirs/atlas/massDecorrelatedXbb/adversarial-wei1/datasets/ReducedTopDatasets/" + sourceDataset
  newDf.to_hdf(newDfFilePath, "dataset", format="table", data_columns=True)








