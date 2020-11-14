# Chiu_AuAc module
# Function 1: the "Intiation" model    
def Initiation(Testing_dataset):
    # Sec1: load in the necesssary libraries
    import numpy as np
    import sklearn
    import torch
    from torch.autograd import Variable
    import pickle
    # Sec2: define the ANN architecture
    class Model10(torch.nn.Module):
        def __init__(self):
            hid_size=hid_size_node;
            super(Model10, self).__init__();
            self.l1=torch.nn.Linear(number_of_feature,hid_size);
            self.l2=torch.nn.Linear(hid_size,hid_size);
            self.l3=torch.nn.Linear(hid_size,hid_size);
            self.l4=torch.nn.Linear(hid_size,hid_size);
            self.l5=torch.nn.Linear(hid_size,hid_size);
            self.l6=torch.nn.Linear(hid_size,hid_size);
            self.l7=torch.nn.Linear(hid_size,hid_size);
            self.l8=torch.nn.Linear(hid_size,hid_size);
            self.l9=torch.nn.Linear(hid_size,hid_size);
            self.l10=torch.nn.Linear(hid_size,number_of_output);
            self.activation=activation;
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
    # Sec3: data prepping
    scaler=pickle.load(open('Initiation_Coef.pkl','rb'));
    if len(np.shape(Testing_dataset))==1:
        Testing_dataset=np.reshape(Testing_dataset,(1,-1));
    xy_load_Test=np.empty([np.shape(Testing_dataset)[0],3],dtype=float)
    xy_load_Test[:,2]=1*10**-20; 
    xy_load_Test[:,[0,1]]=Testing_dataset;
    xy_load_Test_log10_std=scaler.transform(np.log10(xy_load_Test));
    xy_load_Test_log10_std=xy_load_Test_log10_std[:,[0,1]];
    std = scaler.scale_;
    mean = scaler.mean_;
    # Sec4: initialize the model
    number_of_feature=2;
    number_of_output=1;
    hid_size_node=1024;
    activation=torch.nn.LeakyReLU();
    trained_model=eval("Model10()");
    trained_model.load_state_dict(torch.load('Initiation.pkl'));
    # Sec5: making predictions
    x_data_Test=torch.from_numpy(xy_load_Test_log10_std.astype('float32'));
    y_pred_Test=trained_model(Variable(x_data_Test));
    y_predict=y_pred_Test.data.numpy();                
    Auto_pred=y_predict[:,0]; Auto_pred=10**(Auto_pred*std[2]+mean[2]);
    result=Auto_pred;
	# Sec6: output the result
    return result    
# Function 2: the "Standard" model 
def Standard(Testing_dataset):
    # Sec1: load in the necesssary libraries
    import numpy as np
    import sklearn
    import torch
    from torch.autograd import Variable
    import pickle
    # Sec2: define the ANN architecture
    class Model10(torch.nn.Module):
        def __init__(self):
            hid_size=hid_size_node;
            super(Model10, self).__init__();
            self.l1=torch.nn.Linear(number_of_feature,hid_size);
            self.l2=torch.nn.Linear(hid_size,hid_size);
            self.l3=torch.nn.Linear(hid_size,hid_size);
            self.l4=torch.nn.Linear(hid_size,hid_size);
            self.l5=torch.nn.Linear(hid_size,hid_size);
            self.l6=torch.nn.Linear(hid_size,hid_size);
            self.l7=torch.nn.Linear(hid_size,hid_size);
            self.l8=torch.nn.Linear(hid_size,hid_size);
            self.l9=torch.nn.Linear(hid_size,hid_size);
            self.l10=torch.nn.Linear(hid_size,number_of_output);
            self.activation=activation;
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
    # Sec3: data prepping
    scaler=pickle.load(open('Standard_Coef.pkl','rb'));
    if len(np.shape(Testing_dataset))==1:
        Testing_dataset=np.reshape(Testing_dataset,(1,-1));
    xy_load_Test=np.empty([np.shape(Testing_dataset)[0],6],dtype=float)
    xy_load_Test[:,4]=1*10**-15; 
    xy_load_Test[:,5]=1*10**-15;
    xy_load_Test[:,[0,1,2,3]]=Testing_dataset;
    xy_load_Test_log10_std=scaler.transform(np.log10(xy_load_Test));
    xy_load_Test_log10_std=xy_load_Test_log10_std[:,[0,1,2,3]];
    std = scaler.scale_;
    mean = scaler.mean_;
    # Sec4: initialize the model
    number_of_feature=4;
    number_of_output=2;
    hid_size_node=1024;
    activation=torch.nn.LeakyReLU();
    trained_model=eval("Model10()");
    trained_model.load_state_dict(torch.load('Standard.pkl'));
    # Sec5: making predictions
    x_data_Test=torch.from_numpy(xy_load_Test_log10_std.astype('float32'));
    y_pred_Test=trained_model(Variable(x_data_Test));
    y_predict=y_pred_Test.data.numpy();                
    Auto_pred=y_predict[:,0]; Auto_pred=10**(Auto_pred*std[4]+mean[4]);
    Accr_pred=y_predict[:,1]; Accr_pred=10**(Accr_pred*std[5]+mean[5]);
    result=np.concatenate((np.reshape(Auto_pred,(-1,1)),np.reshape(Accr_pred,(-1,1))),axis=1);
	# Sec6: output the result
    return result