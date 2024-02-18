import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering

Data_dup=pd.read_excel(r"/workspaces/OptiLapAdvisor/UI/Standardized_Data.xlsx")
outlier_data=pd.read_excel(r"/workspaces/OptiLapAdvisor/UI/Outlier_Data.xlsx")
Data=pd.read_excel(r"/workspaces/OptiLapAdvisor/UI/Cleaned_Data.xlsx")
Data_dup.set_index(Data_dup.columns[0],inplace=True)
outlier_data.set_index(outlier_data.columns[0],inplace=True)
Data.set_index(Data.columns[0],inplace=True)

class webpage():
    Gen={"High_Gen":3,"Mid_Gen":2,"Low_Gen":1}
    Gen_option=Gen[st.sidebar.selectbox("Laptop_Generation",["High_Gen","Mid_Gen","Low_Gen"],index=1)]
    RAM_option=st.sidebar.select_slider("RAM (GB)",[4,8,16,32,64],value=8)
    Storage_option=st.sidebar.selectbox("Storage (GB)",[64,128,256,512,1024],index=2)
    Size_option=st.sidebar.slider("Screen Size",0.0,18.0,step=1.5,value=15.6)
    Price_option=st.sidebar.slider("Price",0,100000,step=1000)
x=Data_dup.drop(Data_dup.columns[[0,1,6,7,8,9,10,11]],axis=1)
scale=StandardScaler()
x=np.array(x)
scale.fit(x)
x=scale.transform(x)
N_cluster=3
Model=AgglomerativeClustering(n_clusters=N_cluster)
Model.fit(x)
Data_dup["Cluster"]= Model.labels_
New_data= list(x) 
New_data.append(scale.transform([[webpage().Gen_option,webpage().RAM_option,webpage().Storage_option,webpage().Size_option,webpage().Price_option]])[0])
new_labels=Model.fit_predict(New_data)
New_Prediction_Cluster_Number=new_labels[len(x):]+1
Data_dup["Cluster"]=new_labels[:len(x)]+1
Cluster_Number=New_Prediction_Cluster_Number[0]
outlier_data["Cluster"]=N_cluster+1
Merged=pd.concat([Data_dup,outlier_data])
Data["Cluster"]=Merged["Cluster"]
Result=Data[Data["Cluster"]==Cluster_Number]

def Bool_(value,feature):
    return not(value) or (bool(value) and (Data[feature]==value))

def Filter(Brand_,Processor_,RAM_,Storage_,Size_,Gaming_,FingerPrint_,OLED_,SSD_,Renewed_,PType_,data):
    Values=[Brand_,Processor_,RAM_,Storage_,Size_,Gaming_,FingerPrint_,OLED_,SSD_,Renewed_,PType_]
    Variables=["Brand","Processor","RAM","Storage","Size","Gaming","FingerPrint","OLED","SSD","Renewed","PType"]
    Bool_flag=True
    for i,j in zip(Values,Variables):
        Bool_flag = Bool_flag & Bool_(i,j)
    try: 
        return data[Bool_flag][:] 
    except: 
        return data
if st.checkbox("Filter"):
    Brand_filter = st.selectbox("Brand",Data["Brand"].unique(),index=None)
    Processor_filter= st.selectbox("Processor",Data["Processor"].unique(),index=None)
    RAM_filter=  st.selectbox("RAM",Data["RAM"].unique(),index=None)
    Storage_filter=  st.selectbox("Storage",Data["Storage"].unique(),index=None)
    Size_filter=  st.selectbox("Size",Data["Size"].unique(),index=None)
    Gaming_filter=  st.selectbox("Gaming",[False,True],index=None)
    FingerPrint_filter= st.selectbox("Finger Print",[False,True],index=None)
    OLED_filter= st.selectbox("OLED",[False,True],index=None)
    SSD_filter= st.selectbox("SSD",[False,True],index=None)
    Renewed_filter= st.selectbox("Renewed",[False,True],index=None)
    flag=st.selectbox("Generation",["High_Gen","Mid_Gen","Low_Gen"],index=None)
    PType_filter= webpage().Gen[flag] if flag else None
    Final_Result=Filter(Brand_filter,Processor_filter,RAM_filter,Storage_filter,Size_filter,Gaming_filter,FingerPrint_filter,OLED_filter,SSD_filter,Renewed_filter,PType_filter,Result)
    Final_Result
else:
    Result




