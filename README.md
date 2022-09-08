# Chiu_AuAc_Standard_2022
"An updated version of the `Chiu_AuAC_2021` parameterization for autoconversion rate and accretion rate using **in-situ aircraft observations** and **Machine Learning** techniques"

To find `Chiu_AuAC_2021` with `Standard()` and the `Initiation()` model described in [Chiu et al., 2021](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2020GL091236), select the branch named `Chiu_AuAc_2021` (use the 
drop down menu located at the upper left corner of the page).

Release note
============
***We welcome any feedback and comments***

A `Fortran` version of the code is planned to be released in January, 2023

- `v1.0.0` (09/09/2022): a `Python` version using `Keras-Tensoflow` backend of the package is released
- `v2.0.0` (expected on 01/01/2023): a `Fortran` version of the pacakge will be published

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

About this package
==================
This package comprises **5** parts:

1. `Chiu_AuAc_Standard_2022_model.hdf5`:

   - Contain the weights and the biases for the Artificial Neural Network (ANN) for the `Chiu_AuAc_Standard_2022()` model.

   - Used in `Chiu_AuAc_Standard_2022_module.py`
   
   - Available in this Github repository.

2. `Scaler.mat`:
  
   - Contain the scaling used to normalize the INPUT and OUTPUT variables in the training dataset.

   - Used in `Chiu_AuAc_Standard_2022_module.py`

   - Available in this Github repository.

3. `Chiu_AuAc_Standard_2022_module.py`: ***PLEASE DO NOT MODIFY THE CONTENT***

   - This is a `python` module that contains one function: `Chiu_AuAc_Standard_2022()`. The function performs the following tasks:
   
      - Inititialze the Artificial Neural Network (ANN) with the trained weights and bias loaded from the `Chiu_AuAc_Standard_2022_model.hdf5` file

      - Scale the "Input_Data" with the scaling information obtained from the training dataset

      - Make predictions with the Artificial Neural Network (ANN)
   
   - Available in this Github repository.

4. `ExampleDatad.mat`: 

   - This example dataset will be used in `run_example.py` for predicting Pau and Pac

   - Available in this Github repository.

5. `run_example.py`:

   - An example script that demonsrates how to run the `Chiu_AuAc_Standard_2022()`model  with the `ExampleData.mat`.

   - Available in this Github repository.

Installation (from scratch)
===========================

- Step 0: for `v1.0.0`, this package can run on `Windows`, `MacOS`, and `Linux` with a appropriate `python` package manager installed in the operation system.

- Step 1: make sure that the following packages are installed in your `Python3` environment:

   - `Tensorflow`
   
   - `Keras`
   
   - `Numpy`

   - (optional; for `run_example.py`) `SciPy`

- Step 2: put all the necessary files (**5** in total) in the working directory; you should have:

   - `Chiu_AuAc_Standard_2022_model.hdf5`
   - `Scaler.mat`
   - `Chiu_AuAc_Standard_2022_module.py`
   - `ExampleData.mat`
   - `run_example.py`
  
   ***YOU ARE ALL SET FOR RUNNING THIS MODULE***

- Notes:
   - You do not need to have `CUDA` installed in your operational system to use the pacakge
   - The format of the "Input_Data" should be `ndarray` (click [here](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html) to learn more about what is `ndarray`)
