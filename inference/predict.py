import pandas as pd

def predict(model, scaler, sample, FEATURES):
    df = pd.DataFrame([sample])
    pred = model.predict(scaler.transform(df[FEATURES]))[0]
    return pred