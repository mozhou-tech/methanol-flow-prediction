import pandas as pd


def read_flow_speed():
    df = pd.read_excel("../datasets/flowspeeds.xlsx")
    return df
