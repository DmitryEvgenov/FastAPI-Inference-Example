from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
# Здесь должен быть ваш код для загрузки модели

app = FastAPI()

class Item(BaseModel):
    data: list

@app.post("/predict/")
async def predict(item: Item):
    try:
        # Преобразуйте данные из запроса для вашей модели
        data = np.array(item.data)
        # Здесь ваш код для предсказания
        prediction = "здесь результат инференса модели"
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
