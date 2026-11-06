import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
model = joblib.load("model_knn.pkl")

class PassengerFeatures(BaseModel):
    Pclass: int
    Age: float
    SibSp: int
    Parch: int
    Fare: float

@app.post("/predict")
def predict(passenger: PassengerFeatures):
    # Respect strict de l'ordre des colonnes numériques entraînées
    data = [[
        passenger.Pclass, 
        passenger.Age, 
        passenger.SibSp, 
        passenger.Parch, 
        passenger.Fare
    ]]
    prediction = int(model.predict(data))
    status = "A survécu" if prediction == 1 else "N'est pas survivant"
    return {"prediction": prediction, "status": status}
