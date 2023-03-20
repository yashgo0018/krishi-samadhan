# build the lightgbm model
import lightgbm as lgb
import numpy as np
from fastapi import FastAPI, UploadFile, HTTPException
from .schemas import SuggestCropBody
import tensorflow_hub as hub
import PIL
import PIL.Image
import io

crop_suggestion_classes = ['apple', 'banana', 'blackgram', 'chickpea', 'coconut', 'coffee', 'cotton',
                           'grapes', 'jute', 'kidneybeans', 'lentil', 'maize', 'mango', 'mothbeans',
                           'mungbean', 'muskmelon', 'orange', 'papaya', 'pigeonpeas', 'pomegranate',
                           'rice', 'watermelon']

disease_detector_classes = ['Tomato Healthy', 'Tomato Septoria Leaf Spot', 'Tomato Bacterial Spot', 'Tomato Blight', 'Cabbage Healthy', 'Tomato Spider Mite', 'Tomato Leaf Mold',
                            'Tomato_Yellow Leaf Curl Virus', 'Soy_Frogeye_Leaf_Spot', 'Soy_Downy_Mildew', 'Maize_Ravi_Corn_Rust', 'Maize_Healthy', 'Maize_Grey_Leaf_Spot', 'Maize_Lethal_Necrosis', 'Soy_Healthy', 'Cabbage Black Rot']

bst = lgb.Booster(model_file='crop_suggestion_lgb_model.txt')

hub_url = "https://tfhub.dev/agripredict/disease-classification/1"
disease_detector_model = hub.KerasLayer(hub_url)


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


[0.7, 0.2, 0.1]


@app.post("/suggest-crop")
async def suggest_crop(x: SuggestCropBody):
    probabilities = bst.predict([[
        x.N,
        x.P,
        x.K,
        x.temperature,
        x.humidity,
        x.ph,
        x.rainfall,
    ]])[0]
    predictions = []
    for i in range(len(probabilities)):
        predictions.append((crop_suggestion_classes[i], probabilities[i]))
    predictions.sort(key=lambda x: x[1], reverse=True)
    return {"prediction": predictions}


@app.post("/detect-disease")
async def detect_disease(file: UploadFile):
    if "image" not in file.content_type:
        raise HTTPException(400, detail="Invalid document type")
    request_object_content = await file.read()
    img = PIL.Image.open(io.BytesIO(request_object_content))
    img = img.resize((300, 300)).convert('RGB')
    img = np.asarray(img) / 255
    probabilities = disease_detector_model([img])[0]
    predictions = []
    for i in range(len(probabilities)):
        predictions.append(
            (disease_detector_classes[i], float(probabilities[i])))
    predictions.sort(key=lambda x: x[1], reverse=True)
    return {"prediction": predictions}


@app.get("/disease")
def get_all_disease():
    return {"diseases": []}


@app.get("/disease/:id")
def get_disease(id: int):
    return {"disease": ""}


@app.get("/crops")
def get_all_crops():
    return {"crops": []}


@app.get("/crops/:id")
def get_crop(id: int):
    return {"crop": ""}
