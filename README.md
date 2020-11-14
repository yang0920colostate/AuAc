# Chiu_AuAc
"A warm rain parameterization using aircraft observation and Machine Learning techniques"

Please read [Chiu et al., 2020]() for more information

Citation & Contacts
===================

* Citation: ??? 

* [Christine Chiu](https://www.atmos.colostate.edu/people/faculty/chiu/): `Christine.Chiu@colostate.edu`
* C. Kevin Yang: `yang0920@rams.colostate.edu` for any issues related to the source codes

Description
===========

- **Inputs**: 
   - `qc`: cloud droplet liquid water content in `g/m3`
   - `Nc`: cloud droplet number concentration in `/cm3`
   - `qr`: drizzle drop liquid watar content in `g/m3`
   - `Nr`: drizzle drop number concentration in `/cm3`
   
- **Outputs**: 
   - `Pau`: autoconversion rate in `g/cm3/s`
   - `Pac`: accretion rate in `g/cm3/s`

- **Models**:

   1. `Initiation model`: 
      - Uses two inputs `(qc, Nc)` for predicting `Pau` in drizzle-absent conditions (i.e., `qr` & `Nr` are both zero)

   2. `Standard model`:
      - Uses four inputs `(qc, Nc, qr, Nr)` for predicting `Pau` and `Pac` jointly in drizzling conditions

About this package
==================
This package composed **3** parts.

* In this Github repository:
1. `Chiu_AuAc.py`: the main source code 
2. Two example data files: `Data_for_Initiation.mat` and `Data_for_Standard.mat`

* In the [Google drive folder]()https://drive.google.com/drive/folders/1YQtwRKVPUH_4ptDDk8yXLBmEpVeNT2lY?usp=sharing:
3. `pkl.zip`: the weights and biases for the Artificial Neural Network (ANN), and the coefficients for scaling the input data

Installation from scratch
=========================

-Step 1: make sure that the following packages are installed in your `Python3` environment:

   - `Numpy`
   - `scikit-learn`
   - `Pytorch`
   - `pickle`
   - (optional) `SciPy`: for running the below example codes

- Step 2: put all the necessary files (**5** in total) in the working directories, you should have:
   
   - `Chiu_AuAc.py`
   - `Reduced_Coef.pkl`
   - `Reduced.pkl`
   - `Standard_Coef.pkl`
   - `Standard.pkl`

- Step 3: an exmaple code

```python
# Load in the necessary libaries
import Chiu_AuAc 
from scipy.io import loadmat
# Use the initiaion model to make prediction
Data_Test=loadmat('Data_for_Reduced.mat');
Data_Test=Data_Test['Testing']; 
Pred=Chiu_AuAc.Reduced(Data_Test);
# Use the standard model to make prediction
Data_Test = loadmat('Data_for_Standard.mat');
Data_Test = Data_Test['Testing']; 
Pred=Chiu_AuAc.Standard(Data_Test);
```
