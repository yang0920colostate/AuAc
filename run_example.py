## =================README=================
# -> A Python script named "run_example.py": demonstrate how to use the 
#    "Chiu_AuAc_Standard_2022_module" in "Chiu_AuAc_Standard_2022_module.py"
## ========================================
# ----------Step1: load in the all the necessary libraries----------
import Chiu_AuAc_Standard_2022_module
import scipy.io as sio
import numpy as np
# ----------Step 2: load in example field----------
# -> example "reflectance field"----------
example_INPUT=sio.loadmat('ExampleData.mat');
example_INPUT=example_INPUT['TestingData_INPUT'];
# ----------Step 3: do the aerosol retrieval----------
Predicted_Pau_Pac=Chiu_AuAc_Standard_2022_module.Chiu_AuAc_Standard_2022(example_INPUT);
sio.savemat('Predicted_Pau_Pac.mat',{'Predicted_Pau_Pac':Predicted_Pau_Pac});