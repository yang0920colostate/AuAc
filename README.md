# Chiu_AuAc
"A warm rain parameterization using aircraft observation and Machine Learning techniques"

Please read [Chiu et al., 2020]() for more information.

Citation & Contacts
===================

*Citation: 

* [Christine Chiu](https://www.atmos.colostate.edu/people/faculty/chiu/): `Christine.Chiu@colostate.edu`
* C.Kevin Yang: `yang0920@rams.colostate.edu` for any issues related to the source codes or pacakge

Models
======

1. `Initiation model`: 
   * Uses two inputs `(qc, Nc)` for predicting `Pau` in drizzle-absent (i.e., qr & Nr are both zero) conditions

2. `Standard model`:


Installation from scratch
=========================
In this package, there are three components:

* In this Github repository:
1. `Chiu_AuAc.py`: the main source code 
2. Two example data files: `Data_for_Reduced.mat` and `Data_for_Standard.mat`

* In the Google drive folder:
3. `pkl.zip`: the weights and biases for the Artificial Neural Network (ANN), and 


1. Download Anaconda
2. Open the Anaconda prompt
3. make sure all the necessary libarires are installed: numpy, sklearn, pytorch, pickle? (using xxx command to check)
4. the source code and the related files should be stored in the working directory
5. >>> load Chiu_AuAc
6. >>> ....the input data has to be numpy array and the output data is also a numpy array, can input one sample or up to a thousand sample (for this version, and depemnds on your RAM)
7. >>> 
