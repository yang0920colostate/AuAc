## ------------------------------README------------------------------
# A Python script named "run_example1.py": demonsrate how to run the "Standard()" or "Initiation()" model  
# with the "ExampleData_for_Standard.mat" or "ExampleData_for_Initiation" respectively.
# ----------Step1: load in the all the necessary libraries
import Chiu_AuAc;
import numpy as np;
import pandas as pd;
from scipy.io import loadmat;
# ----------Step2: run the "Standard()" model with the "ExampleData_for_Standard.mat" to make predictions ("Pau" and "Pac")
Input_Data=loadmat('ExampleData_for_Standard.mat')['Testing']; # 4 columns in the "Input_Data"-> (qc,Nc,qr,Nr)
Output_Data=Chiu_AuAc.Standard(Input_Data);                    # 2 columns in the "Output_Data" -> (Pau,Pac)
# ----------Step3: a Pandas dataframe to summarize the "Input_Data" & "Output_Data" in a table
df=pd.DataFrame(data=np.hstack((Input_Data,Output_Data)),\
                columns=["qc (g/m3)","Nc (#/cm3)","qr (g/m3)","Nr (/cm3)","Pau (g/cm3/s)","Pac (g/cm3/s)"]);
print('-> Success in running the "Standard()" model!!!');
print('-> Here are the "Input_Data" (qc,Nc,qr,Nr) and the "predicted Pau and Pac":\n');
print(df);
print('==========================================================================================');
# ----------Step4: run the "Initiation()" model with the "ExampleData_for_Initiation.mat" to make predictions ("Pau" only)
Input_Data = loadmat('ExampleData_for_Initiation.mat')['Testing']; # 2 columns in the "Input_Data"-> (qc,Nc)
Output_Data=Chiu_AuAc.Initiation(Input_Data);                      # 1 column in the "Output_Data" -> (Pau)
# ----------Step5: a Pandas dataframe to summarize the "Input_Data" & "Output_Data" in a table
df=pd.DataFrame(data=np.hstack((Input_Data,np.reshape(Output_Data,(-1,1)))),\
                columns=["qc (g/m3)","Nc (#/cm3)","Pau (g/cm3/s)"]);
print('-> Success in running the "Initiation()" model!!!');
print('-> Here are the "Input_Data" (qc,Nc) and the "predicted Pau":\n');
print(df);
print('==========================================================================================');