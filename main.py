from fastapi import Security, Depends, FastAPI, HTTPException
from fastapi.security.api_key import APIKeyQuery, APIKey
from starlette.status import HTTP_403_FORBIDDEN
from pydantic import BaseModel
import uvicorn
import pickle

API_KEY = "pau_al_cuadrado"
API_KEY_NAME = "password"

api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)

app = FastAPI(
    title = "Título",
    description = "Esta API recibe un parámetro tipo body con variables sobre una película para predecir si"
                  "ganará un premio Óscar o no.",
    version = "0.0.1"
)


def get_api_key(api_key_query: str = Security(api_key_query)):
    if api_key_query == API_KEY:
        return api_key_query
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Acceso denegado."
        )


class Oscar(BaseModel):
    Production: float
    Time_taken: float
    Avg_age_actors: float
    Hashtags: float
    Marketing: float
    Budget: float
    Collection: float
    Trailer_views: float
    Movie_length: float
    Lead_Actor_Rating: float
    Genre_Comedy: int
    Genre_Drama: int
    Genre_Thriller: int
    third_D: int


@app.on_event("startup")
def load_model():
    global model_rf
    with open("model/rf_classifier.pkl", "rb") as openfile:
        model_rf = pickle.load(openfile)


@app.get("/secure_endpoint", tags=["test"])
async def get_open_api_endpoint(api_key: APIKey = Depends(get_api_key)):
    response = {'description': "You have access to this endpoint."}
    return response


@app.get("/api/v1/classify")
async def classify_oscar(oscar: Oscar, api_key: APIKey = Depends(get_api_key)):
    params = [[oscar.Production,
               oscar.Time_taken,
               oscar.Avg_age_actors,
               oscar.Hashtags,
               oscar.Marketing,
               oscar.Budget,
               oscar.Collection,
               oscar.Trailer_views,
               oscar.Movie_length,
               oscar.Lead_Actor_Rating,
               oscar.Genre_Comedy,
               oscar.Genre_Drama,
               oscar.Genre_Thriller,
               oscar.third_D]]
    pred = model_rf.predict(params)
    dict_oscar = {0: 'Did not win an Oscar Award.',
                 1: 'Won an Oscar Award.'}
    return {"Oscar Award": dict_oscar.get(pred[0]),
            'Description': "Prediction correctly executed"}


@app.get("/")
def home():
    return {"Desc": "Health Check"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)

# documentación: http://localhost:8000/docs
