import math

from pydantic import BaseModel


class Prediction(BaseModel):
    label: str
    weight: float


class Hits(BaseModel):
    hits: list[Prediction]


def bar_weight(length: int) -> float:
    return 1 / math.exp(length / 20)


def baz_weight(string: str) -> float:
    return len([c for c in string if c in "aeiou"]) / len(string)


def rpc1(arg: str) -> Hits:
    """
    Remote procedure call for the prediction hits of a given string.

    Predictions include only `foo` or `bar` labels and their respective weights.
    """
    return Hits(
        hits=[
            Prediction(label="foo", weight=1 - bar_weight(len(arg))),
            Prediction(label="bar", weight=bar_weight(len(arg))),
        ]
    )


def rpc2(arg: str) -> Hits:
    """
    Remote procedure call for the prediction hits of a given string.

    Predictions include labels (e.g., `foo`, `bar`, `baz`, or others) and their respective weights.
    """
    return Hits(
        hits=[
            Prediction(label="foo", weight=1 - bar_weight(len(arg))),
            Prediction(label="bar", weight=bar_weight(len(arg))),
            Prediction(label="baz", weight=baz_weight(arg)),
        ]
    )
