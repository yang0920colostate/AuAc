# Chiu_AuAc
"A new parameterization for autoconversion rate and accretion rate using **in-situ aircraft observations** and **Machine Learning** techniques"

Please read [Chiu et al., 2020](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2020GL091236) for more information.

Release note
============
**We welcome any feedback and comments.**
A `Fortran` version of the code is planned to be released in January, 2021

- `v1.0.0` (12/11/2020): a `Python` version of the package is released
- `v2.0.0` (expeceted on 12/25/2020): `Keras-Tensoflow` as the backend (another option)
- `v3.0.0` (expected on 01/01/2021): a `Fortran` version of the pacakge will be published

Citation & Contacts
===================
Citation: Chiu, J. C., C. Kevin Yang, Peter Jan van Leeuwen, Graham Feingold, Robert Wood, Yann Blanchard, Fan Mei, and Jian Wang (2020): Observational constraints on warm cloud microphysical processes using machine learning and optimization techniques. Geophys. Res. Lett. doi:10.1029/2020GL091236

* PI: [Dr. Christine Chiu](https://cloud-radiation.atmos.colostate.edu/): `Christine.Chiu@colostate.edu`
* Co-I: C. Kevin Yang: `yang0920@rams.colostate.edu` for any issues related to the source code

Descriptions of Machine-Learning models
=======================================
PLEASE PAY ATTENTION TO THE UNITS!!!

- **Inputs**: 
   - `qc`: cloud water content in `g/m3`
   - `Nc`: cloud droplet number concentration in `/cm3`
   - `qr`: drizzle watar content in `g/m3`
   - `Nr`: drizzle drop number concentration in `/cm3`
   
- **Outputs**: 
   - `Pau`: autoconversion rate in `g/cm3/s`
   - `Pac`: accretion rate in `g/cm3/s`

- **Models**:

   1. `Standard()`:
      - Use four inputs `(qc, Nc, qr, Nr)` to predict both `Pau` and `Pac` in drizzling conditions

   2. `Initiation()`: 
      - Use two inputs `(qc, Nc)` to predict `Pau` in non-drizzling conditions (i.e., `qr` & `Nr` are both zero)

About this package
==================
This package comprises **5** parts:

1. `pkl.zip`: 
   - The zip file contains 4 python pickle files. 'Initiation.pkl' and 'Standard.pkl' contain the weights and the biases for the Artificial Neural Network (ANN) for the initiation and standard model, respectively. The coefficients for scaling the inputs and outputs data are inlcuded in 'Initiation_Coef.pkl' (for the initiation model) and 'Standard_Coef.pkl' (for the standard model). 
   - Used in Chiu_AuAc.py
   - Available in the [Google drive folder](https://drive.google.com/drive/folders/1YQtwRKVPUH_4ptDDk8yXLBmEpVeNT2lY?usp=sharing):

2. `Chiu_AuAc.py`: PLEASE DO NOT MODIFY THE CONTENT!!!
   - This is a `python` module that 
      
   
   - Available in this Github repository.

3. `run_example1.py`:

4. `run_example2.py`:

5. `ExampleData_for_Standard.mat` and `ExampleData_for_Initiation.mat` : 
   - As shown in the end, these two example data sets will be input to Chiu_AuAc.py for predicting Pau and Pac; one for the initiation model, and the other for the standard model
   - Available in this Github repository.

Installation (from scratch)
===========================

- Step 0: for `v1.0.0`, this package can run on `Windows`, `MacOS`, and `Linux` with a appropriate `python` package manager installed in the operation system.

- Step 1: make sure that the following packages are installed in your `Python3` environment:

   - `Numpy`
  
   - `scikit-learn`
     
   - [Pytorch](https://pytorch.org/): click the link to see the corresponding commmands for different operational system (Windows/MacOS/Linux)
   
      using Anaconda3 as the `python` package manager:
      
      ```
      - (Windows) >> conda install pytorch torchvision torchaudio cpuonly -c pytorch 
      -   (MacOS) >> conda install pytorch torchvision torchaudio -c pytorch 
      -   (Linux) >> conda install pytorch torchvision torchaudio cpuonly -c pytorch 
      ```
      
   - `pickle`: this is part of the `Python3` standard library (i.e., you don't have to worry about it)
   
   - (optional; for running the example codes below) `SciPy`
   
- Step 2: put all the necessary files (**5** in total) in the working directory; you should have:
   
   - `Chiu_AuAc.py`
   - `Standard_Coef.pkl`
   - `Standard.pkl`
   - `Initiation_Coef.pkl`
   - `Initiation.pkl` 

- Step 3: an exmaple code showing how to use the models to make predictions

   ```python
   # Load in the necessary libaries
   import Chiu_AuAc 
   from scipy.io import loadmat

   # Use the standard model to make predictions ("Pau" and "Pac")
   Data_Test = loadmat('ExampleData_for_Standard.mat');
   Data_Test = Data_Test['Testing']; 
   Prediction = Chiu_AuAc.Standard(Data_Test);
   
   # Use the initiaion model to make predictions ("Pau" only)
   Data_Test = loadmat('ExampleData_for_Initiation.mat');
   Data_Test = Data_Test['Testing']; 
   Prediction = Chiu_AuAc.Initiation(Data_Test);
   ```

- Notes: 
   - You do not need to have `CUDA` installed in your operational system to use the pacakge
   - The format of the input data should be `ndarray` (click [here](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html) to learn more about what is `ndarray`)
   - You should use no more than 10,000 sample to make predictions at once (memory issue)
   - Our StandardScaler is built from sklearn 0.23.2. If you have another version of sklearn istalled in your python environment, you might get a warning message but it should general cause no harm.
