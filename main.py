%%writefile main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from joblib import load
import pandas as pd
import os

# Define the path to the trained model
MODEL_PATH = "calorie_model.joblib"

# Initialize FastAPI app
app = FastAPI(
    title="Nutrition ML API",
    description="API for predicting calories based on macronutrients using a pre-trained ML model.",
    version="1.0.0"
)

# Load the model globally to ensure it's loaded only once on startup
# and not reloaded for every request.
try:
    # Check if the model file exists
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}. Please run train_model.py first.")
    model = load(MODEL_PATH)
    print(f"Model loaded successfully from {MODEL_PATH}")
except Exception as e:
    model = None # Set model to None if loading fails
    print(f"Error loading the model: {e}")
    # Optionally, you might want to raise an error or exit if the model is crucial
    # raise RuntimeError(f"Failed to load ML model: {e}")


# Define Pydantic model for request body validation
class NutritionInput(BaseModel):
    protein: float = Field(..., gt=-0.1, description="Protein in grams (cannot be negative)")
    carbs: float = Field(..., gt=-0.1, description="Carbohydrates in grams (cannot be negative)")
    fat: float = Field(..., gt=-0.1, description="Fat in grams (cannot be negative)")
    fiber: float = Field(..., gt=-0.1, description="Fiber in grams (cannot be negative)")

    # Example values for API documentation
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "protein": 40,
                    "carbs": 200,
                    "fat": 50,
                    "fiber": 20
                }
            ]
        }
    }

# Define the prediction endpoint
@app.post("/predict", summary="Predict total calories", response_model=dict)
async def predict_calories(nutrition_input: NutritionInput):
    """
    Predicts the total calories based on the provided macronutrient values.

    - **protein**: Grams of protein (e.g., 40)
    - **carbs**: Grams of carbohydrates (e.g., 200)
    - **fat**: Grams of fat (e.g., 50)
    - **fiber**: Grams of fiber (e.g., 20)

    Returns the predicted calories.
    """
    if model is None:
        raise HTTPException(status_code=500, detail="ML model not loaded. Please check server logs.")

    # Create a Pandas DataFrame from the input data
    # The model expects a 2D array or DataFrame with feature names
    input_df = pd.DataFrame([{
        'protein': nutrition_input.protein,
        'carbs': nutrition_input.carbs,
        'fat': nutrition_input.fat,
        'fiber': nutrition_input.fiber
    }])

    try:
        # Make prediction
        predicted_calories = model.predict(input_df)[0]
        return {"predicted_calories": round(predicted_calories, 2)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

# Root endpoint for health check or basic info
@app.get("/", summary="Health Check")
async def root():
    return {"message": "Welcome to the Nutrition ML API! Visit /docs for API documentation."}

