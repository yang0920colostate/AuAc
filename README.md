# Chiu_AuAc
"A new parameterization for autoconversion rate and accretion rate using **in-situ aircraft observations** and **Machine Learning** techniques"

Please read [Chiu et al., 2021](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2020GL091236) for more information.

This `README.md` and all the codes can be found in https://github.com/yang0920colostate/AuAc as well, except the `training and testing dataset` for the machine learning model.

Release note
============
***We welcome any feedback and comments***

A `Fortran` version of the code is planned to be released in January, 2022

- `v1.0.0` (12/11/2020): a `Python` version of the package is released
- `v2.0.0` (expeceted on 09/01/2022): `Keras-Tensoflow` as the backend (another option)
- `v3.0.0` (expected on 09/01/2022): a `Fortran` version of the pacakge will be published

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
This package comprises **4** parts:

1. `pkl.zip`: 

   - The zip file contains 4 `python` pickle files. `Standard.pkl` and `Initiation.pkl` contain the weights and the biases for the Artificial Neural Network (ANN) for the `Standard()`  and `Initiation()` model, respectively. The coefficients for scaling the inputs and outputs data are inlcuded in `Standard_Coef.pkl` (for the `Standard()` model) and `Initiation_Coef.pkl` (for the `Initiation()` model). 
   - Used in Chiu_AuAc.py
   - Available in the [Google drive folder](https://drive.google.com/drive/folders/1YQtwRKVPUH_4ptDDk8yXLBmEpVeNT2lY?usp=sharing)

2. `Chiu_AuAc.py`: ***PLEASE DO NOT MODIFY THE CONTENT***

   - This is a `python` module that contains two functions: `Standard()` and `Initiation()`. Each function performs the following tasks:
      
      - Inititialze the Artificial Neural Network (ANN) with the trained weights and bias loaded from the `.pkl` file
      
      - Scale the "Input_Data" with the scaling information obtained from the training dataset
      
      - Make predictions with the Artificial Neural Network (ANN) 
   
   - Available in this Github repository.

3. `ExampleData_for_Standard.mat` and `ExampleData_for_Initiation.mat` : 

   - These two example datasets will be used in `run_example1.py` for predicting Pau and Pac; one for the `Standard()` model, an the other for the `Initiation()` model
   
   - Available in this Github repository.
   
4. Example scripts:

   - `run_example1.py`: demonsrate how to run the `Standard()` or `Initiation()` model  with the `ExampleData_for_Standard.mat` or `ExampleData_for_Initiation` respectively.
   
   - `run_example2.py`: demonsrate how to use part of the testing dataset from `Chiu_etal_GRL2020_AuAc.nc` for evaluating the performance of the `Standard()` model. 
   
   - `Chiu_etal_GRL2020_AuAc.nc` contains the `training dataset` and `testing dataset` and is under a zip file called `PIProduct-Chiu-etal-GRL2020-AuAc.zip` stored in the [ARM Archive](https://sso.arm.gov/arm/login?service=https%3A%2F%2Fiop.archive.arm.gov%2Farm-iop%2F0pi-data%2Fchiu%2Faceena-ml%2F) (you will need to set up a free ARM account by using this [link](https://adc.arm.gov/discovery/#/account) before accessing the data).
   
Installation (from scratch)
===========================

- Step 0: for `v1.0.0`, this package can run on `Windows`, `MacOS`, and `Linux` with a appropriate `python` package manager installed in the operation system.

- Step 1: make sure that the following packages are installed in your `Python3` environment:

   - `Numpy`
  
   - `scikit-learn`
     
   - [Pytorch](https://pytorch.org/): click the link to see the corresponding commmands for different operational system (Windows/MacOS/Linux)
   
      for example: using `Anaconda3` as the `python` package manager:
      
      ```
      - (Windows) >> conda install pytorch torchvision torchaudio cpuonly -c pytorch 
      -   (MacOS) >> conda install pytorch torchvision torchaudio -c pytorch 
      -   (Linux) >> conda install pytorch torchvision torchaudio cpuonly -c pytorch 
      ```
      
   - `pickle`: this is part of the `Python3` standard library (i.e., you don't have to worry about it)
   
   - (optional; for `run_example1.py`) `SciPy`
   
   - (optional; for `run_example2.py`) `netCDF4`
   
- Step 2: put all the necessary files (**5** in total) in the working directory; you should have:
   
   - `Chiu_AuAc.py`
   - `Standard_Coef.pkl`
   - `Standard.pkl`
   - `Initiation_Coef.pkl`
   - `Initiation.pkl` 
   
   ***YOU ARE ALL SET FOR RUNNING THIS MODULE***

- Notes: 
   - You do not need to have `CUDA` installed in your operational system to use the pacakge
   - The format of the "Input_Data" should be `ndarray` (click [here](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html) to learn more about what is `ndarray`)
   - You should use no more than 10,000 samples to make predictions at once (it's likely that you will run out of memory on a typical PC)
   - Our `StandardScaler` is built from `sklearn 0.23.2`. If you have another version of the `sklearn` installed in your `python` environment, you might get a warning message but it should be fine.
