# Chiu_AuAc
"A warm rain parameterization using **in-situ aircraft observation** and **Machine Learning** techniques"

Please read [Chiu et al., 2020](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2020GL091236) for more information.

Release note
============
**This is a relatively new method, and we would appreciate any feedback from the users**.
A `Fortran` version of the code would be soon released in January, 2021

- `v1.0.0` (11/?/2020): a `Python` version of the package is released
- `v2.0.0` (expeceted on 12/25/2020): `Keras-Tensoflow` as the backend (another option)
- `v3.0.0` (expected on 01/01/2021): a `Fortran` version of the pacakge will be published

Citation & Contacts
===================
Citation: ???

* [Dr. Christine Chiu](https://www.atmos.colostate.edu/people/faculty/chiu/): `Christine.Chiu@colostate.edu`
* C. Kevin Yang: `yang0920@rams.colostate.edu` for any issues related to the source code

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

   1. `Initiation()`: 
      - Use two inputs `(qc, Nc)` to predict `Pau` in drizzle-absent conditions (i.e., `qr` & `Nr` are both zero)

   2. `Standard()`:
      - Use four inputs `(qc, Nc, qr, Nr)` to predict `Pau` and `Pac` jointly in drizzling conditions

About this package
==================
This package comprises **3** parts:

* In this Github repository:

   1. `Chiu_AuAc.py`: the main source code 
   2. Two example data files: `Data_for_Initiation.mat` and `Data_for_Standard.mat`

* In the [Google drive folder](https://drive.google.com/drive/folders/1YQtwRKVPUH_4ptDDk8yXLBmEpVeNT2lY?usp=sharing):
   
   3. `pkl.zip`: the weights and the biases for the Artificial Neural Network (ANN), and the coefficients for scaling the inputs and outputs data

Installation (from scratch)
===========================

- Step 1: make sure that the following packages are installed in your `Python3` environment:

   - `Numpy`
  
   - `scikit-learn`
     
   - [Pytorch](https://pytorch.org/): click the link to see the corresponding commmands for different operational system (MacOS vs. Windows)
   
   - `pickle`: this is part of the `Python3` standard library (i.e., you don't have to worry about it)
   
   - (optional) `SciPy`: for running the example codes below

- Step 2: put all the necessary files (**5** in total) in the working directory; you should have:
   
   - `Chiu_AuAc.py`
   - `Initiation_Coef.pkl`
   - `Initiation.pkl`
   - `Standard_Coef.pkl`
   - `Standard.pkl`

- Step 3: an exmaple code showing how to use the models to make predictions

   ```python
   # Load in the necessary libaries
   import Chiu_AuAc 
   from scipy.io import loadmat

   # Use the initiaion model to make predictions ("Pau" only)
   Data_Test = loadmat('Data_for_Initiation.mat');
   Data_Test = Data_Test['Testing']; 
   Prediction = Chiu_AuAc.Initiation(Data_Test);

   # Use the standard model to make predictions ("Pau" and "Pac")
   Data_Test = loadmat('Data_for_Standard.mat');
   Data_Test = Data_Test['Testing']; 
   Prediction = Chiu_AuAc.Standard(Data_Test);
   ```

- Notes: 

   - The format of the input data should be `ndarray` (click [here](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html) to learn more about what is `ndarray`)
   - You should use no more than 10,000 sample to make predictions at once (memory issue)
