import joblib
import sys
import os
import sklearn
import xgboost as xgb
import warnings
import pandas as pd
import csv
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

smiles = []
with open(smiles_file, "r") as f:
    reader = csv.reader(f)
    for r in reader:
        smiles += [r[0]]
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

# Handling NAN inputs
for i in range(len(input_des)):
    problematic_values = np.isnan(input_des[i]) | np.isinf(input_des[i]) | (np.abs(input_des[i]) > np.finfo(np.float64).max)
    if np.any(problematic_values):
        problematic_indices = np.where(problematic_values)[0]
        problematic_data = input_des[i][problematic_values]
    # Handle NaN, replacing NAN with 0.0
    nan_indices = np.isnan(input_des[i])
    input_des[i][nan_indices] = 0.0

## Load Model and make predictions
model = joblib.load(os.path.join(ROOT, "..", "stack.joblib"))
pred = model.predict_proba(input_des)
pred = pred[:,1]

## Write output to csv file
np.savetxt(results_file, pred,header='Probability',delimiter=",",comments='')
