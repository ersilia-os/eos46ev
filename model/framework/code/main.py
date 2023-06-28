import joblib
import sys
import os
import sklearn
import xgboost as xgb
import warnings
import pandas as pd
import numpy as np
from PyBioMed.PyMolecule import fingerprint
from rdkit import Chem
from rdkit.Chem import MACCSkeys
from rdkit.Chem import AllChem
from descriptastorus.descriptors.DescriptorGenerator import MakeGenerator
from descriptastorus.descriptors import rdNormalizedDescriptors
from numpy import savetxt

warnings.filterwarnings("ignore")

ROOT = os.path.dirname(os.path.abspath(__file__))

smiles_file = str(sys.argv[1])
results_file = str(sys.argv[2])

## load data

# sml = pd.read_csv(smiles_file, names=['Smiles'])
# smiles = sml['Smiles'].to_numpy()
# print("smiles",smiles)
# print("Len of smiles",len(smiles))
# mol = [Chem.MolFromSmiles(x) for x in smiles]
# print("mol",mol)

smiles_df = pd.read_csv(smiles_file)
smiles = smiles_df[smiles_df.columns[0]].tolist()
mol = [Chem.MolFromSmiles(x) for x in smiles]

## produce RDKit 2D descriptors
generator = rdNormalizedDescriptors.RDKit2DNormalized()
des = [generator.process(x) for x in smiles]
des = np.array(des)
des_ = des[:,1:201]

## produce ECFP fingerprint
ecfp = np.array(fingerprint.CalculateECFP4Fingerprint(mol[0])[0])
for i in range(1,len(mol)):
    fp = fingerprint.CalculateECFP4Fingerprint(mol[i])
    fp = np.array(fp[0])
    ecfp = np.vstack((ecfp,fp))
ecfp = ecfp.astype('float64')

if(len(smiles) == 1):
    input_des = np.append(des_, ecfp) 
    input_des = input_des.reshape(1, -1)
else:
    input_des = np.concatenate((des_, ecfp), axis=1) 

## Load Model and make predictions
model = joblib.load(os.path.join(ROOT, "..", "stack.joblib"))
pred = model.predict_proba(input_des)
pred = pred[:,1]

## Write output to csv file
np.savetxt(results_file, pred,header='Probability',delimiter=",",comments='')
