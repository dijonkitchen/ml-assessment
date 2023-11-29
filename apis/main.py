from fastapi import FastAPI
from pydantic import BaseModel
from fakerpc import rpc1, rpc2

app = FastAPI()


class PredRequest(BaseModel):
    message: str


class PredResponse(BaseModel):
    status: str
    prediction: list


@app.post("/predict")
def predict(req: PredRequest):
    try:
        pred = rpc1(req.message)
        return {
            "status": "ok",
            "prediction": sorted(pred["hits"], key=lambda x: x["weight"], reverse=True),
        }
    except:
        return {"status": "error", "prediction": ""}
