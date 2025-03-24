from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import random
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)
class CropRequest(BaseModel):
    year: int
    month: int
    region: str
    temperature: float
    rainfall: float
    humidity: float
    soil_pH: float
    soil_nitrogen: float
    soil_phosphorus: float
    soil_potassium: float
    soil_organic_matter: float
    fertilizer_use: float
    pesticide_use: float
    previous_year_yield: float
    sowing_to_harvest_days: int
    farm_size_acres: float
    irrigation_available: int
    supply_tons: float
    import_tons: float
    export_tons: float
    crops: List[str]

class CropRankingResponse(BaseModel):
    crop: str
    score: float

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/rank_crops")
def rank_crops(request: CropRequest) -> List[CropRankingResponse]:
    ranked_crops = [
        CropRankingResponse(crop=crop, score=random.uniform(0, 1))
        for crop in request.crops
    ]
    ranked_crops.sort(key=lambda x: x.score, reverse=True)
    return ranked_crops

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
