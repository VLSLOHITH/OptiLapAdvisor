import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering

Overal_Data=pd.read_excel(r"UI/Cleaned_Data.xlsx")
Standardized_Data=pd.read_excel(r"UI/Standardized_Data.xlsx")
Outlier_Data=pd.read_excel(r"UI/Outlier_Data.xlsx")
Standardized_Data.set_index(Standardized_Data.columns[0],inplace=True)
Outlier_Data.set_index(Outlier_Data.columns[0],inplace=True)
Overal_Data.set_index(Overal_Data.columns[0],inplace=True)

st.title("OptiLapAdvisor")

class webpage():
    Gen={"High_Gen":3,"Mid_Gen":2,"Low_Gen":1}
    Gen_option=Gen[st.sidebar.selectbox("Laptop_Generation",["High_Gen","Mid_Gen","Low_Gen"],index=1)]
    RAM_option=st.sidebar.select_slider("RAM (GB)",[4,8,16,32,64],value=8)
    Storage_option=st.sidebar.selectbox("Storage (GB)",[64,128,256,512,1024],index=2)
    Size_option=st.sidebar.slider("Screen Size",0.0,18.0,step=1.5,value=15.6)
    Price_option=st.sidebar.slider("Price",0,100000,step=1000)
x=Standardized_Data.drop(Standardized_Data.columns[[0,1,6,7,8,9,10,11]],axis=1)
scale=StandardScaler()
x=np.array(x)
scale.fit(x)
x=scale.transform(x)
N_cluster=3
Model=AgglomerativeClustering(n_clusters=N_cluster)
Model.fit(x)
Standardized_Data["Cluster"]= Model.labels_
New_data= list(x) 
New_data.append(scale.transform([[webpage().Gen_option,webpage().RAM_option,webpage().Storage_option,webpage().Size_option,webpage().Price_option]])[0])
new_labels=Model.fit_predict(New_data)
New_Prediction_Cluster_Number=new_labels[len(x):]+1
Standardized_Data["Cluster"]=new_labels[:len(x)]+1
Cluster_Number=New_Prediction_Cluster_Number[0]
Outlier_Data["Cluster"]=N_cluster+1
Merged=pd.concat([Standardized_Data,Outlier_Data])
Overal_Data["Cluster"]=Merged["Cluster"]
Result=Overal_Data[Overal_Data["Cluster"]==Cluster_Number]

def Bool_(value,feature):
    if value==0:
        return (Overal_Data[feature]==value)
    return not(value) or (bool(value) and (Overal_Data[feature]==value))

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
def Yes_No(value):
    if value=="Yes":
        return 1
    elif value=="No":
        return 0
    else:
        return None

if st.checkbox("Filter"):
    Brand_filter = st.selectbox("Brand",Overal_Data["Brand"].unique(),index=None)
    Processor_filter= st.selectbox("Processor",Overal_Data["Processor"].unique(),index=None)
    RAM_filter=  st.selectbox("RAM",Overal_Data["RAM"].unique(),index=None)
    Storage_filter=  st.selectbox("Storage",Overal_Data["Storage"].unique(),index=None)
    Size_filter=  st.selectbox("Size",Overal_Data["Size"].unique(),index=None)
    Gaming_filter=  Yes_No(st.selectbox("Gaming",["No","Yes"],index=None))
    FingerPrint_filter= Yes_No(st.selectbox("Finger Print",["No","Yes"],index=None))
    OLED_filter= Yes_No(st.selectbox("OLED",["No","Yes"],index=None))
    SSD_filter= Yes_No(st.selectbox("SSD",["No","Yes"],index=None))
    Renewed_filter= Yes_No(st.selectbox("Renewed",["No","Yes"],index=None))
    flag=st.selectbox("Generation",["High_Gen","Mid_Gen","Low_Gen"],index=None)
    PType_filter= webpage().Gen[flag] if flag else None
    Final_Result=Filter(Brand_filter,Processor_filter,RAM_filter,Storage_filter,Size_filter,Gaming_filter,FingerPrint_filter,OLED_filter,SSD_filter,Renewed_filter,PType_filter,Result)
    st.header("Result")   
    st.dataframe(Final_Result[:][1:])
else:
    st.header("Result")   
    st.dataframe(Result[:][1:])

st.subheader("Explore the laptops below to see if any interest you, even though you haven't requested them")
if st.checkbox("Laptops which are very low or very high conifgurations."):
    st.header("Extream Laptops")
    st.dataframe(Overal_Data[Overal_Data["Cluster"]==4][1:])





