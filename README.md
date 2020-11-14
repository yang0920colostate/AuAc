# Chiu_AuAc
"A warm rain parameterization using aircraft observation and Machine Learning techniques"

Please read [Chiu et al., 2020]() for more information

Citation & Contacts
===================
Citation: ???

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

   1. `Initiation()`: 
      - Uses two inputs `(qc, Nc)` for predicting `Pau` in drizzle-absent conditions (i.e., `qr` & `Nr` are both zero)

   2. `Standard()`:
      - Uses four inputs `(qc, Nc, qr, Nr)` for predicting `Pau` and `Pac` jointly in drizzling conditions

About this package
==================
This package comprises **3** parts:

* In this Github repository:

   1. `Chiu_AuAc.py`: the main source code 
   2. Two example data files: `Data_for_Initiation.mat` and `Data_for_Standard.mat`

* In the [Google drive folder](https://drive.google.com/drive/folders/1YQtwRKVPUH_4ptDDk8yXLBmEpVeNT2lY?usp=sharing):
   
   3. `pkl.zip`: the weights and biases for the Artificial Neural Network (ANN), and the coefficients for scaling the input and output data

Installation (from scratch)
===========================

- Step 1: make sure that the following packages are installed in your `Python3` environment: 

   - `Numpy`: 
      > conda install -c anaconda numpy
      
   - `scikit-learn`: 
      > conda install -c anaconda scikit-learn
      
   - [Pytorch](https://pytorch.org/): click the link to see the corresponding commmands for different operational system (MacOS vs. Windows)
   
   - `pickle`: this is part of the `Python3` standard library
   
   - (optional) `SciPy`: for running the example codes below' 
      > conda install -c anaconda scipy

- Step 2: put all the necessary files (**5** in total) in the working directory; you should have:
   
   - `Chiu_AuAc.py`
   - `Initiation_Coef.pkl`
   - `Initiation.pkl`
   - `Standard_Coef.pkl`
   - `Standard.pkl`

- Step 3: an exmaple code using the model to make predictions

   ```python
   # Load in the necessary libaries
   import Chiu_AuAc 
   from scipy.io import loadmat

   # Use the initiaion model to make predictions ("Pau" only)
   Data_Test = loadmat('Data_for_Reduced.mat');
   Data_Test = Data_Test['Testing']; 
   Prediction = Chiu_AuAc.Initiation(Data_Test);

   # Use the standard model to make predictions ("Pau" and "Pac")
   Data_Test = loadmat('Data_for_Standard.mat');
   Data_Test = Data_Test['Testing']; 
   Prediction = Chiu_AuAc.Standard(Data_Test);
   ```

- Notes: 

   - The format of the input data should be `ndarray` (click [here](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html) to learn more about what is `ndarray`)
