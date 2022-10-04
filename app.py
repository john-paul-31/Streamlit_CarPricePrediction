#from copyreg import pickle
import pandas as pd
import streamlit as st
import pickle
import sklearn

master_data = pd.read_csv("./cars24-car-price.csv") #Importing master data

#Encoding categorical variables with integers
encodings = {               
    "fuel_type": {"Diesel":1,"Petrol":2,"CNG":3,"LPG":4,"Electric":5},
    "seller_type": {"Dealer":1,"Individial":2,"Trustmark Dealer":3},
    "transmission_type": {"Manual":1,"Automatic":2}
}

#Defining the Predict Function
def predict(fuel_type,transmission_type,engine,seats): #Define the arguments
    
    with open("car_pred",'rb') as file: #Open the model file in read format using pickle
        reg_model = pickle.load(file)   #Loading the file 


    input_features = [[2018.0, 1, 40000, fuel_type, transmission_type, 19.7, engine, 86.30, seats]] #Setting the input values for prediction
    
    return reg_model.predict(input_features) #Predicting the Car Price 



#### Page Setting in Streamlit ####

st.set_page_config("layout = 'wide") #Setting the layout of the webpage

st.title("Car Price Prediction") #Setting the Title for the webpage

col1, col2 = st.columns(2) #Setting the number of columns in the layout

fuel_type = col1.selectbox("Select Fuel type",  #Setting the label/header for the dropdown
                           ['Diesel','Petrol','CNG','LPG','Electric']) #Setting values for the dropdown

engine = col1.slider("Select Engine Power", #Setting the label/header for the slider
                    500,5000,100) #Setting the range and step size

transmission_type = col2.selectbox("Select Transmission Type", #Setting the label/header for the dropdown
                                   ['Manual','Automatic']) #Setting values for the dropdown

seats = col2.selectbox("No. of seats",  #Setting the label/header for the dropdown
                       [4,5,6,7,8]) #Setting values for the dropdown

if (st.button("Predict Price")): #If the Button is clicked
    fuel_type = encodings['fuel_type'][fuel_type] #Set the fuel type from the encodings
    transmission_type = encodings['transmission_type'][transmission_type] #Set the fuel type from the encodings
    
    price = predict(fuel_type,transmission_type,engine,seats) #Predicting the Price of the car
    st.text("Predicted Price for given inputs is: "+ str(price)+" Lakhs") #Display the Price on the webpage
    



    
     