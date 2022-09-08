def Chiu_AuAc_Standard_2022(INPUT):
    ## =================README=================
    # -> Description: an updated version of the Standard model, trained and tested with different days
	#                 of in-situ aircraft measurements. For more information, please refer to 
	#                 Dr. Christine Chiu's talk (https://ams.confex.com/ams/CMM2022/meetingapp.cgi/Paper/406848) 
	#                 at the AMS's Collective Madison Meeting (2022 summer).
	#                
	# -> INPUT variables: 
	#                   qc: cloud water content in g/m3
	#                   Nc: cloud droplet number concentration in /cm3
	#                   qr: drizzle watar content in g/m3
	#                   Nr: drizzle drop number concentration in /cm3
	#
    # -> OUTPUT variables 
	#                   Pau: autoconversion rate in g/cm3/s
	#                   Pac: accretion rate in g/cm3/s
	#
	## ========================================
	# ----------step 1: load in all the necessary libraries----------
    from tensorflow import keras
    import scipy.io as sio
    import numpy as np
    # ----------step 2: load in the "Chiu_AuAc_Standard_2022_modell"----------
    trained_model=keras.models.load_model('Chiu_AuAc_Standard_2022_model.hdf5');
	# ----------step 3: load in the "scaler"----------
    scaler=sio.loadmat('scaler.mat');
    scaler_mean=np.squeeze(scaler['mean']);
    scaler_std=np.squeeze(scaler['std']);
    # ----------step : scale the INPUT variable----------
    input=(np.log10(INPUT)-scaler_mean[0:4])/scaler_std[0:4];
    # ----------step 4: make prediction----------
    output=trained_model.predict(input);
    # ----------step 5: transform the OUTPUT variable to original scale----------
    Pau_Pac=10**(output*scaler_std[4:6]+scaler_mean[4:6]);
    return Pau_Pac