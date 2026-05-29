# Nutrition Calories Prediction API

A Machine Learning-powered REST API built using FastAPI that predicts total calorie intake from macronutrient values.

## Overview

This project demonstrates a complete Machine Learning deployment workflow:

* Synthetic nutrition dataset generation
* Model training using Scikit-Learn
* Model serialization using Joblib
* FastAPI backend development
* Input validation using Pydantic
* Interactive API documentation using Swagger UI

The API predicts calories based on:

* Protein (grams)
* Carbohydrates (grams)
* Fat (grams)
* Fiber (grams)

---

## Project Structure

```text
nutrition_api/
│
├── main.py
├── calorie_model.joblib
├── requirements.txt
├── README.md
└── .venv/
```

---

## Technologies Used

* Python 3.11+
* FastAPI
* Uvicorn
* Scikit-Learn
* Joblib
* NumPy
* Pandas
* Pydantic

---

## Installation

### Clone Repository

```bash
git clone <your-repository-url>
cd nutrition_api
```

### Create Virtual Environment using UV

```bash
uv venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
uv pip install -r requirements.txt
```

---

## Running the API

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Server will be available at:

```text
http://127.0.0.1:8000
```

---

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## Prediction Endpoint

### POST /predict

Predict total calories from nutrition values.

### Request

```json
{
  "protein": 40,
  "carbs": 200,
  "fat": 50,
  "fiber": 20
}
```

### Response

```json
{
  "predicted_calories": 1410
}
```

---

## Machine Learning Model

### Input Features

| Feature       | Unit  |
| ------------- | ----- |
| Protein       | grams |
| Carbohydrates | grams |
| Fat           | grams |
| Fiber         | grams |

### Target

| Target   |
| -------- |
| Calories |

### Model Storage

The trained model is stored as:

```text
calorie_model.joblib
```

and loaded during API startup.

---

## Validation

The API validates incoming requests using Pydantic.

Checks include:

* Missing values
* Negative values
* Invalid data types

Invalid requests return appropriate HTTP error responses.

---

## Example cURL Request

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{
  "protein": 40,
  "carbs": 200,
  "fat": 50,
  "fiber": 20
}'
```

---

## Future Improvements

* Food recommendation engine
* Indian food nutrition database
* Barcode scanning integration
* Weight prediction model
* Nutrition deficiency detection
* User authentication
* Flutter mobile application integration
* Cloud deployment using Render or Railway

---

## Author

SK

Machine Learning & Backend Development Project

---

## License

This project is intended for educational and portfolio purposes.
