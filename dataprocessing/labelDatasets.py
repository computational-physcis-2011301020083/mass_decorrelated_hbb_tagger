import pandas as pd
import glob

hCountKey = "GhostHBosonsCount"
bCountKey = "GhostBHadronsFinalCount"


def label_row(row, isHiggsSample):
    if row[hCountKey] >= 1:
        if row[bCountKey] >= 2:
            return "Hbb"
        else:
            return "ignore"
    else:
        if row[bCountKey] >=2 and not isHiggsSample:
            return "gbb"
        else:
            return "qcd"


def isHbb(row_label):
    if row_label == "Hbb":
        return 1
    else:
        return 0


def isGbb(row_label):
    if row_label == "gbb":
        return 1
    else:
        return 0


def isQcd(row_label):
    if row_label == "qcd":
        return 1
    else:
        return 0

filePaths = glob.glob("./hbbDijetsDatasets/*.h5")

totalNumEvent = 0
totalNumSignal = 0

for filePath in filePaths:

    sourceDataset = filePath.split('/')[2]

    print "processing " + sourceDataset

    fatjet_key = "fat_jet"
    fatjet_columns = ["Tau32_wta", "e3", "Qw", "eta", "Tau21_wta", "C2", "D2", "Angularity", "Aplanarity", "FoxWolfram20", "KtDR", "PlanarFlow", "Split12", "ZCut12", "mcEventWeight", "eventNumber", "mass", "pt", "label"]

    df = pd.read_hdf(filePath, fatjet_key)

    isHiggsSample = "_H" in sourceDataset

    df["label"] = df.apply(lambda row: label_row(row, isHiggsSample), axis=1)

    ignore_msk = df["label"] != "ignore"

    newDf = df[ignore_msk][fatjet_columns]

    newDf["pt"] = (newDf["pt"]/1000.0).astype("float64")

    newDf["m"] = (newDf["mass"]/1000.0).astype("float64")
    newDf = newDf.drop("mass", axis=1)

    newDf.rename(columns={"Tau21_wta": "Tau21", "Tau32_wta": "Tau32", "mcEventWeight": "weight_test"}, inplace=True)

    newDf["signal"] = newDf.apply(lambda row: isHbb(row["label"]), axis=1).astype("int32")

    float_subjet_columns = ['MV2c10_discriminant', 'MV2c10mu_discriminant', 'MV2c10rnn_discriminant', 'DL1_pu', 'DL1_pc', 'DL1_pb', 'DL1rnn_pu', 'DL1rnn_pc', 'DL1rnn_pb', 'IP2D_pb', 'IP2D_pc', 'IP2D_pu', 'IP3D_pb', 'IP3D_pc', 'IP3D_pu', 'JetFitter_dRFlightDir', 'JetFitter_deltaeta','JetFitter_deltaphi', 'JetFitter_energyFraction', 'JetFitter_mass', 'JetFitter_massUncorr', 'JetFitter_significance3d','SV1_L3d', 'SV1_Lxy', 'SV1_deltaR', 'SV1_dstToMatLay', 'SV1_efracsvx', 'SV1_masssvx', 'SV1_significance3d', 'deta', 'dphi', 'dr', 'eta', 'pt', 'rnnip_pb', 'rnnip_pc', 'rnnip_ptau', 'rnnip_pu']

    int_subjet_columns = ['JetFitter_nSingleTracks','JetFitter_nTracksAtVtx', 'JetFitter_nVTX', 'JetFitter_N2Tpair', 'SV1_N2Tpair', 'SV1_NGTinSvx']
    for i in [1, 2]:
        subjet_key = "subjet_VRGhostTag_{}".format(i)

        column_name_dict = {}
        for subjet_column in float_subjet_columns + int_subjet_columns:
            newColumnName = "{}_{}".format(subjet_column, i)
            column_name_dict[subjet_column] = newColumnName

        df_subjet =  pd.concat([pd.read_hdf(filePath, subjet_key)[ignore_msk][float_subjet_columns].astype("float32"), pd.read_hdf(filePath, subjet_key)[ignore_msk][int_subjet_columns].astype("int32")], axis=1)
        newDf = pd.concat([newDf, df_subjet.rename(columns=column_name_dict)], axis=1)

    newDf.dropna(inplace=True)
    # will need these in the future
    # newDf["IsHbb"] = newDf["signal"]
    # newDf["IsGbb"] = newDf.apply(lambda row: isGbb(row["label"]), axis=1)
    # newDf["IsQcd"] = newDf.apply(lambda row: isQcd(row["label"]), axis=1)

    numEvent = len(newDf.index)
    numSignal = newDf["signal"].sum()

    totalNumEvent = totalNumEvent + numEvent
    totalNumSignal = totalNumSignal + numSignal

    newDfFilePath = "./labelledHbbTopDatasets/" + sourceDataset.split(".h5")[0] + "_"+ str(numEvent) + "_" + str(numSignal) + ".h5"

    print "saving " + newDfFilePath
    print "total number of events: " + str(totalNumEvent)
    print "total number of signal: " + str(totalNumSignal)
    newDf.to_hdf(newDfFilePath, "dataset", format="table", data_columns=True)

print "total number of events: " + str(totalNumEvent)
print "total number of signal: " + str(totalNumSignal)






