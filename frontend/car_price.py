import streamlit as st
import requests
import json


# WebPage 
def main():
    st.title("CAR PRICE PREDICTOR")
    make = st.number_input('Make')
    model = st.number_input('Model')
    Year = st.number_input('Year')
    engineFuel = st.number_input('Engine_Fuel_Type')
    engineHP = st.number_input('Engine_HP')
    engineCylinder = st.number_input('Engine_Cylinder')
    Transmission_Type = st.number_input('Transmission_Type')
    Driven_Wheels = st.number_input('Driven_Wheels')
    Number_of_Doors = st.number_input('Number_of_Doors')
    Market_Category = st.number_input('Market_Category')
    Vehicle_Size = st.number_input('Vehicle_Size')
    Vehicle_Style = st.number_input('Vehicle_Style')
    highway_MPG = st.number_input('Highway_MPG')
    city_mpg = st.number_input('City_MPG')
    Popularity = st.number_input('Popularity')

    # Creating a dictionary of all values input 
    input_data={
        "Make":make,
        "Model":model,
        "Year":Year,
        "Engine_Fuel_Type":engineFuel,
        "Engine_HP":engineHP,
        "Engine_Cylinders":engineCylinder,
        "Transmission_Type":Transmission_Type,
        "Driven_Wheels":Driven_Wheels,
        "Number_of_Doors":Number_of_Doors,
        "Market_Category":Market_Category,
        "Vehicle_Size":Vehicle_Size,
        "Vehicle_Style":Vehicle_Style,
        "highway_MPG":highway_MPG,
        "city_mpg":city_mpg,
        "Popularity":Popularity
    }   

    # CALL THE API request Module with POST Method 
    price = 0
    if st.button('Predict'):
        price = requests.post(url='http://127.0.0.1:8000/predict',data=json.dumps(input_data))
        price = price.json()
        p = price['prediction']
        st.success(f'The Price Of Car is {p} lacks.')


if __name__=="__main__":
    main()