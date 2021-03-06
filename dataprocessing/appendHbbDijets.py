import pandas as pd
import glob
import argparse,math,os
parser = argparse.ArgumentParser(description="%prog [options]", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--path", dest='path',  default="", help="path")
args = parser.parse_args()


valist1=['Split12', 'Split23', 'Qw', 'PlanarFlow', 'Angularity', 'Aplanarity', 'ZCut12', 'KtDR', 'HbbScore', 'XbbScoreQCD', 'XbbScoreTop', 'XbbScoreHiggs', 'JSSTopScore', 'pt', 'eta', 'GhostHBosonsCount', 'GhostWBosonsCount', 'GhostZBosonsCount', 'GhostTQuarksFinalCount', 'GhostBHadronsFinalCount', 'GhostCHadronsFinalCount', 'mcEventWeight', 'eventNumber', 'mass', 'C2', 'D2', 'e3', 'Tau21_wta', 'Tau32_wta', 'FoxWolfram20', 'MV2c10_discriminant_1', 'DL1_pu_1', 'DL1_pc_1', 'DL1_pb_1', 'DL1rnn_pu_1', 'DL1rnn_pc_1', 'DL1rnn_pb_1', 'IP2D_pu_1', 'IP2D_pc_1', 'IP2D_pb_1', 'IP3D_pu_1', 'IP3D_pc_1', 'IP3D_pb_1', 'SV1_pu_1', 'SV1_pc_1', 'SV1_pb_1', 'rnnip_pu_1', 'rnnip_pc_1', 'rnnip_pb_1', 'rnnip_ptau_1', 'JetFitter_energyFraction_1', 'JetFitter_mass_1', 'JetFitter_significance3d_1', 'JetFitter_deltaphi_1', 'JetFitter_deltaeta_1', 'JetFitter_massUncorr_1', 'JetFitter_dRFlightDir_1', 'SV1_masssvx_1', 'SV1_efracsvx_1', 'SV1_significance3d_1', 'SV1_dstToMatLay_1', 'SV1_deltaR_1', 'SV1_Lxy_1', 'SV1_L3d_1', 'JetFitter_nVTX_1', 'JetFitter_nSingleTracks_1', 'JetFitter_nTracksAtVtx_1', 'JetFitter_N2Tpair_1', 'SV1_N2Tpair_1', 'SV1_NGTinSvx_1', 'secondaryVtx_nTrks_1', 'IP2D_nTrks_1', 'IP3D_nTrks_1', 'IP2D_isDefaults_1', 'IP3D_isDefaults_1', 'JetFitter_isDefaults_1', 'SV1_isDefaults_1', 'secondaryVtx_isDefaults_1', 'rnnip_isDefaults_1', 'GhostBHadronsFinalCount_1', 'GhostCHadronsFinalCount_1', 'pt_1', 'eta_1', 'deta_1', 'dphi_1', 'dr_1', 'MV2c10_discriminant_2', 'DL1_pu_2', 'DL1_pc_2', 'DL1_pb_2', 'DL1rnn_pu_2', 'DL1rnn_pc_2', 'DL1rnn_pb_2', 'IP2D_pu_2', 'IP2D_pc_2', 'IP2D_pb_2', 'IP3D_pu_2', 'IP3D_pc_2', 'IP3D_pb_2', 'SV1_pu_2', 'SV1_pc_2', 'SV1_pb_2', 'rnnip_pu_2', 'rnnip_pc_2', 'rnnip_pb_2', 'rnnip_ptau_2', 'JetFitter_energyFraction_2', 'JetFitter_mass_2', 'JetFitter_significance3d_2', 'JetFitter_deltaphi_2', 'JetFitter_deltaeta_2', 'JetFitter_massUncorr_2', 'JetFitter_dRFlightDir_2', 'SV1_masssvx_2', 'SV1_efracsvx_2', 'SV1_significance3d_2', 'SV1_dstToMatLay_2', 'SV1_deltaR_2', 'SV1_Lxy_2', 'SV1_L3d_2', 'JetFitter_nVTX_2', 'JetFitter_nSingleTracks_2', 'JetFitter_nTracksAtVtx_2', 'JetFitter_N2Tpair_2', 'SV1_N2Tpair_2', 'SV1_NGTinSvx_2', 'secondaryVtx_nTrks_2', 'IP2D_nTrks_2', 'IP3D_nTrks_2', 'IP2D_isDefaults_2', 'IP3D_isDefaults_2', 'JetFitter_isDefaults_2', 'SV1_isDefaults_2', 'secondaryVtx_isDefaults_2', 'rnnip_isDefaults_2', 'GhostBHadronsFinalCount_2', 'GhostCHadronsFinalCount_2', 'pt_2', 'eta_2', 'deta_2', 'dphi_2', 'dr_2', 'label', 'weight', 'signal', 'data', 'dsid']
valist2=['index', 'dsid','weight_test', 'weight_train', 'weight_adv', 'train']
path="/global/project/projectdirs/atlas/massDecorrelatedXbb/adversarial-wei1/datasets/"
path1=path+"MergedDatasetsFixed/HbbDijetsDatasets"
path2=path+"ReweightedDatasetsFixed/ExtractedHbbDijetsPt2TeV/HbbDijetsDatasets.h5"

path=sorted(glob.glob(path1+"/*.h5"))
print path

h2=pd.read_hdf(path2)[valist2]

'''
#print h2.dtypes
hHbb=h2[((h2["dsid"] != "361024") & (h2["dsid"] != "361025") & (h2["dsid"] != "361026") & (h2["dsid"] != "361027")& (h2["dsid"] != "361028")& (h2["dsid"] != "361029")& (h2["dsid"] != "361030"))]
#print hHbb

h=h1.loc[hHbb["index"].tolist()]
#print h

for i in valist2:
  if i!="dsid":
    h[i]=hHbb[i].values  
  else:
    h["DSID"]=hHbb[i].values
print h

'''

path.remove(path[7])
print path
Index=0.0
for f in path:
  print f
  hf=pd.read_hdf(f)[valist1]
  ID=f.split("/")[-1].split(".")[1]
  hDijet=h2[h2["dsid"]==ID]
  h0=hf.loc[hDijet["index"].tolist()]
  for i in valist2:
    if i!="dsid":
      h0[i]=hDijet[i].values
    else:
      h0["DSID"]=hDijet[i].values
  print h0
  Index=Index+len(h0.index)

  newDfFilePath = "/global/project/projectdirs/atlas/massDecorrelatedXbb/adversarial-wei1/datasets/ReweightedDatasetsFixed/HbbDijetsDatasets/"+f.split("/")[-1]
  h0.to_hdf(newDfFilePath, "dataset") 
print Index














