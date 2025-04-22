import joblib
import sys
import os
import warnings
import csv
import numpy as np
from PyBioMed.PyMolecule import fingerprint
from rdkit import Chem
from descriptastorus.descriptors import rdNormalizedDescriptors
from numpy import savetxt

warnings.filterwarnings("ignore")

ROOT = os.path.dirname(os.path.abspath(__file__))

input_file = str(sys.argv[1])
output_file = str(sys.argv[2])

## load data

with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]
mol = [Chem.MolFromSmiles(x) for x in smiles_list]

## produce RDKit 2D descriptors
generator = rdNormalizedDescriptors.RDKit2DNormalized()
des = [generator.process(x) for x in smiles_list]
des = np.array(des)
des_ = [row[1:201] for row in des]

## produce ECFP fingerprint
ecfp = np.array(fingerprint.CalculateECFP4Fingerprint(mol[0])[0])
for i in range(1,len(mol)):
    fp = fingerprint.CalculateECFP4Fingerprint(mol[i])
    fp = np.array(fp[0])
    ecfp = np.vstack((ecfp,fp))
ecfp = ecfp.astype('float64')

if(len(smiles_list) == 1):
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
model = joblib.load(os.path.join(ROOT, "..", "..","checkpoints", "stack.joblib"))
pred = model.predict_proba(input_des)
pred = pred[:,1]

## Write output to csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["proba_chemtb"])  # header with column names
    for p in pred:
        writer.writerow([p])