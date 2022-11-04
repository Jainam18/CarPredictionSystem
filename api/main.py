from tokenize import Double
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pickle

# Load The Model 
model = pickle.load(open('..\model\car_price_predictor.pkl','rb'))

# Creating a FastAPI instance
app = FastAPI()

# Creating Input Schema using Pydantic BaseModel 
class Input(BaseModel):
    Make:int
    Model:int
    Year:float
    Engine_Fuel_Type:int
    Engine_HP:float
    Engine_Cylinders:float
    Transmission_Type:int
    Driven_Wheels:int
    Number_of_Doors:float
    Market_Category:int
    Vehicle_Size:int
    Vehicle_Style:int
    highway_MPG:float
    city_mpg:float
    Popularity:float

# Creating Routes 

# Home Route will just Return Car Prediction Message 
@app.get('/')
def read_root():
    return {'msg':'Car Price Predictor'}

# Predict Route will output the prediction of model provided the input 
@app.post('/predict')
def predict_price(input:Input):
    data = input.dict()
    data_in = [[data['Make'], data['Model'], data['Year'], data['Engine_Fuel_Type'], data['Engine_HP'],
       data['Engine_Cylinders'], data['Transmission_Type'], data['Driven_Wheels'],
       data['Number_of_Doors'], data['Market_Category'], data['Vehicle_Size'], data['Vehicle_Style'],
       data['highway_MPG'], data['city_mpg'], data['Popularity']]]
    prediction = model.predict(data_in)
    return{
        'prediction':prediction[0]
    }

# Run the Uvicorn Server 
if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)
    print("Executed Sucessfully")
    
