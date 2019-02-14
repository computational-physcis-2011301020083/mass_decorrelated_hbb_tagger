import pandas as pd
import glob

paths = glob.glob("./processedDatasets_xbbscore_reformat_hbbDijets/*.h5")

extractedDf = pd.read_hdf("./reweightDatasets/data_2M_20M_xbbscoreHbbDijetsWithCalculatedWeights.h5")

featuresToAppend = [u"Tau32", u"e3", u"Qw", u"eta", u"Tau21", u"C2", u'D2', u'Angularity', u'Aplanarity', u'FoxWolfram20',u'KtDR', u'PlanarFlow', u'Split12', u'ZCut12', u'label', u'm', u'MV2c10_discriminant_1', u'MV2c10mu_discriminant_1', u'MV2c10rnn_discriminant_1', u'DL1_pu_1', u'DL1_pc_1', u'DL1_pb_1', u'DL1rnn_pu_1', u'DL1rnn_pc_1', u'DL1rnn_pb_1', u'IP2D_pb_1', u'IP2D_pc_1', u'IP2D_pu_1',u'IP3D_pb_1', u'IP3D_pc_1', u'IP3D_pu_1', u'JetFitter_dRFlightDir_1',u'JetFitter_deltaeta_1', u'JetFitter_deltaphi_1',u'JetFitter_energyFraction_1', u'JetFitter_mass_1',u'JetFitter_massUncorr_1', u'JetFitter_significance3d_1', u'SV1_L3d_1',u'SV1_Lxy_1', u'SV1_deltaR_1', u'SV1_dstToMatLay_1', u'SV1_efracsvx_1',u'SV1_masssvx_1', u'SV1_significance3d_1', u'deta_1', u'dphi_1',u'dr_1', u'eta_1', u'pt_1', u'rnnip_pb_1', u'rnnip_pc_1',u'rnnip_ptau_1', u'rnnip_pu_1', u'JetFitter_nSingleTracks_1',u'JetFitter_nTracksAtVtx_1', u'JetFitter_nVTX_1',u'JetFitter_N2Tpair_1', u'SV1_N2Tpair_1', u'SV1_NGTinSvx_1', u'MV2c10_discriminant_2', u'MV2c10mu_discriminant_2', u'MV2c10rnn_discriminant_2', u'DL1_pu_2', u'DL1_pc_2', u'DL1_pb_2', u'DL1rnn_pu_2', u'DL1rnn_pc_2', u'DL1rnn_pb_2', u'IP2D_pb_2', u'IP2D_pc_2', u'IP2D_pu_2', u'IP3D_pb_2', u'IP3D_pc_2',u'IP3D_pu_2', u'JetFitter_dRFlightDir_2', u'JetFitter_deltaeta_2',u'JetFitter_deltaphi_2', u'JetFitter_energyFraction_2',u'JetFitter_mass_2', u'JetFitter_massUncorr_2',u'JetFitter_significance3d_2', u'SV1_L3d_2', u'SV1_Lxy_2',u'SV1_deltaR_2', u'SV1_dstToMatLay_2', u'SV1_efracsvx_2',u'SV1_masssvx_2', u'SV1_significance3d_2', u'deta_2', u'dphi_2',u'dr_2', u'eta_2', u'pt_2', u'rnnip_pb_2', u'rnnip_pc_2',u'rnnip_ptau_2', u'rnnip_pu_2', u'JetFitter_nSingleTracks_2',u'JetFitter_nTracksAtVtx_2', u'JetFitter_nVTX_2',u'JetFitter_N2Tpair_2', u'SV1_N2Tpair_2', u'SV1_NGTinSvx_2']

for featureToAppend in featuresToAppend:
	extractedDf[featureToAppend] = 0

i = 0
for path in paths:
	fileName = path.split('/')[-1]
	i = i + 1
	print "Processing {}: {}".format(i, fileName)

	indexOfExtractedDf = extractedDf["datasource"] == fileName

	if(indexOfExtractedDf.sum() > 0):
		indexOfOriginalDf = extractedDf[indexOfExtractedDf]["index"]
		originalDf = pd.read_hdf(path).loc[indexOfOriginalDf]

		tmpDf = extractedDf[indexOfExtractedDf]
		tmpDf[featuresToAppend] = originalDf[featuresToAppend].values

		extractedDf[indexOfExtractedDf] = tmpDf

extractedDf.to_hdf("./reweightDatasets/data_2M_20M_xbbscore_alldataHbbDijetsCalculatedWeights.h5", "dataset")
print "Done!"
	


