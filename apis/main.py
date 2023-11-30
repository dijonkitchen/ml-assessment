import uvicorn
from fakerpc import rpc1, rpc2
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class PredRequest(BaseModel):
    message: str


class Prediction(BaseModel):
    label: str
    weight: float


class PredResponse(BaseModel):
    status: str
    prediction: list[Prediction]


@app.post("/predict")
def predict(req: PredRequest) -> PredResponse:
    """
    For a non-empty `message`, returns the label hits sorted from highest to lowest weights.

    Examples of `label` may be `foo`, `bar`, `baz` or other strings in the future.

    Examples of `weight` are: 0.0001, 0.24765, or another number from 0 to 1.
    """
    try:
        pred = rpc2(req.message)

        return {
            "status": "ok",
            "prediction": sorted(pred["hits"], key=lambda x: x["weight"], reverse=True),
        }
    except Exception:
        return {"status": "error", "prediction": []}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
