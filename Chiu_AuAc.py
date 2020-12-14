## A Python module called "Chiu_AuAc" that contains two functions: "Standard()" and "Initiation()"
## ====================Function 1: the "Standard" model====================
def Standard(Input_Data):
    # ----------Step1: load in all the necesssary libraries
    import numpy as np;
    import sklearn;
    import torch;
    import pickle;
    # ----------Step2: define the ANN (a feed-forward and fully-connected) architecture
    class Model(torch.nn.Module):
        def __init__(self):
            super(Model,self).__init__();
            self.l1=torch.nn.Linear(4,1024);
            self.l2=torch.nn.Linear(1024,1024);
            self.l3=torch.nn.Linear(1024,1024);
            self.l4=torch.nn.Linear(1024,1024);
            self.l5=torch.nn.Linear(1024,1024);
            self.l6=torch.nn.Linear(1024,1024);
            self.l7=torch.nn.Linear(1024,1024);
            self.l8=torch.nn.Linear(1024,1024);
            self.l9=torch.nn.Linear(1024,1024);
            self.l10=torch.nn.Linear(1024,2);
            self.activation=torch.nn.LeakyReLU();
        def forward(self, x):
            out1=self.activation(self.l1(x));
            out2=self.activation(self.l2(out1));
            out3=self.activation(self.l3(out2));
            out4=self.activation(self.l4(out3));
            out5=self.activation(self.l5(out4));
            out6=self.activation(self.l6(out5));
            out7=self.activation(self.l7(out6));
            out8=self.activation(self.l8(out7));
            out9=self.activation(self.l9(out8));
            y_pred=self.l10(out9);
            return y_pred;
    # ----------Step3: data prepping
    # Load in the "scaler" for later standardizing the "Input_X" and transform the "Output_Y" to the original scale
    scaler=pickle.load(open('Standard_Coef.pkl','rb'));
    std = scaler.scale_;
    mean = scaler.mean_;
    # Check the dimensions of the "Input_Data", and make sure its shape is in 2-D
    if len(np.shape(Input_Data))==1:
        Input_Data=np.reshape(Input_Data,(1,-1));
    # Transform the data into log10 scale and then standardize the "Input_X" (second dimension needs to be 6)
    xy_scaled=scaler.transform(np.log10(np.hstack((Input_Data,np.full((np.shape(Input_Data)[0],2),10**-15)))));
    # ----------Step4: initialize the model that runs on a CPU device
    trained_model=eval("Model()");
    trained_model.load_state_dict(torch.load('Standard.pkl',torch.device('cpu')));
    # ----------Step5: make predictions
    y_predict=trained_model(torch.autograd.Variable(torch.from_numpy(xy_scaled[:,[0,1,2,3]].astype('float32')))).data.numpy();                
    result=np.concatenate((np.reshape(10**(y_predict[:,0]*std[4]+mean[4]),(-1,1)),np.reshape(10**(y_predict[:,1]*std[5]+mean[5]),(-1,1))),axis=1);
    # ----------Step6: return the results
    return result
## ====================Function 2: the "Intiation" model====================
def Initiation(Input_Data):
    # ----------Step1: load in all the necesssary libraries
    import numpy as np;
    import sklearn;
    import torch;
    import pickle;
    # ----------Step2: define the ANN (a feed-forward and fully-connected) architecture
    class Model(torch.nn.Module):
        def __init__(self):
            super(Model,self).__init__();
            self.l1=torch.nn.Linear(2,1024);
            self.l2=torch.nn.Linear(1024,1024);
            self.l3=torch.nn.Linear(1024,1024);
            self.l4=torch.nn.Linear(1024,1024);
            self.l5=torch.nn.Linear(1024,1024);
            self.l6=torch.nn.Linear(1024,1024);
            self.l7=torch.nn.Linear(1024,1024);
            self.l8=torch.nn.Linear(1024,1024);
            self.l9=torch.nn.Linear(1024,1024);
            self.l10=torch.nn.Linear(1024,1);
            self.activation=torch.nn.LeakyReLU();
        def forward(self, x):
            out1=self.activation(self.l1(x));
            out2=self.activation(self.l2(out1));
            out3=self.activation(self.l3(out2));
            out4=self.activation(self.l4(out3));
            out5=self.activation(self.l5(out4));
            out6=self.activation(self.l6(out5));
            out7=self.activation(self.l7(out6));
            out8=self.activation(self.l8(out7));
            out9=self.activation(self.l9(out8));
            y_pred=self.l10(out9);
            return y_pred;
    # ----------Step3: data prepping
    # Load in the "scaler" for later standardizing the "Input_X" and transform the "Output_Y" to the original scale
    scaler=pickle.load(open('Initiation_Coef.pkl','rb'));
    std = scaler.scale_;
    mean = scaler.mean_;
    # Check the dimensions of the "Input_Data", and make sure its shape is in 2-D
    if len(np.shape(Input_Data))==1:
        Input_Data=np.reshape(Input_Data,(1,-1));
    # Transform the data into log10 scale and then standardize the "Input_X" (second dimension needs to be 6)
    xy_scaled=scaler.transform(np.log10(np.hstack((Input_Data,np.full((np.shape(Input_Data)[0],1),10**-20)))));
    # ----------Step4: initialize the model that runs on a CPU device
    trained_model=eval("Model()");
    trained_model.load_state_dict(torch.load('Initiation.pkl',torch.device('cpu')));
    # ----------Step5: make predictions
    y_predict=trained_model(torch.autograd.Variable(torch.from_numpy(xy_scaled[:,[0,1]].astype('float32')))).data.numpy(); 	
    result=10**(y_predict[:,0]*std[2]+mean[2])
    # ----------Step6: return the results
    return result