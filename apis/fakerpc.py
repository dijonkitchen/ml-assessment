import math

func = lambda x: 1 / (math.exp(x / 20))


def rpc1(arg: str):
    return {
        "hits": [
            {"label": "foo", "weight": 1 - func(len(arg))},
            {"label": "bar", "weight": func(len(arg))},
        ]
    }


func2 = lambda x: len([c for c in x if c in "aeiou"]) / len(x)


def rpc2(arg: str):
    return {
        "hits": [
            {"label": "foo", "weight": 1 - func(len(arg))},
            {"label": "bar", "weight": func(len(arg))},
            {"label": "baz", "weight": func2(arg)},
        ]
    }
