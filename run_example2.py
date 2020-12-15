## ------------------------------README------------------------------
# A Python script named "run_example2.py": demonsrate how to use part of the testing dataset ('Chiu_etal_GRL2020_AuAc.nc')
# for evaluating the performance of the "Standard()" model.
# ----------Step1: load in the all the necessary libraries
import Chiu_AuAc; 
import numpy as np;
import numpy.ma as ma;
import netCDF4;
import time;
# ----------Step2: load in all the necessary variables from the netCDF4 file
f = netCDF4.Dataset('Chiu_etal_GRL2020_AuAc.nc');
qc_sm = ma.getdata(f.variables['cloud_water_content_sm_test'][:]);       
nc_sm = ma.getdata(f.variables['cloud_number_concentration_sm_test'][:]);    
qr_sm = ma.getdata(f.variables['rain_water_content_sm_test'][:]);    
nr_sm = ma.getdata(f.variables['rain_number_concentration_sm_test'][:]);
Pau_sm = ma.getdata(f.variables['autoconversion_rate_sm_test'][:]);
Pac_sm = ma.getdata(f.variables['accretion_rate_sm_test'][:]);
Input_Data_sm = np.transpose(np.vstack((qc_sm,nc_sm,qr_sm,nr_sm)));
# ----------Step3: make predictions ("Pau" and "Pac") using the "Standard()" model with 1% of the testing dataset (because of the required memory and time for a typical PC)
tic=time.time(); # start making predictions
Output_Data_sm = Chiu_AuAc.Standard(Input_Data_sm[0:2500000:100,:]);
toc=time.time(); # finish making predictions
print('-> Using the "Standard()" model...');
print('-> Time elpased for predicting 25,000 data points:',np.round(toc-tic,0),'seconds');
print('-> Mean error for predicting "Pau":',np.round(np.mean(((Output_Data_sm[:,0]-Pau_sm[0:2500000:100])/Pau_sm[0:2500000:100])*100),0),'% (with 1% of the testing dataset)')
print('-> Mean error for predicting "Pac":',np.round(np.mean(((Output_Data_sm[:,1]-Pac_sm[0:2500000:100])/Pac_sm[0:2500000:100])*100),0),'% (with 1% of the testing dataset)')