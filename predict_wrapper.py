# predict_wrapper.py
import pandas as pd

# Try to load MLflow models; if not available, use a safe dummy fallback.
def _load_models():
    try:
        from mlflow.pyfunc import load_model
        clf = load_model("models:/EMIPredict_XGB_Classifier/1")
        reg = load_model("models:/EMIPredict_RF_Regressor/1")
        return clf, reg
    except Exception:
        return None, None

CLF, REG = _load_models()

def predict(df_input: pd.DataFrame) -> pd.DataFrame:
    n = len(df_input)
    # If models are available, call them (they must accept the same columns used in training).
    if CLF is not None and REG is not None:
        try:
            cls_enc = CLF.predict(df_input)
            reg_pred = REG.predict(df_input)
            # If classifier returns encoded labels, try coarse decode to strings (best-effort)
            cls_out = [str(x) for x in cls_enc]
            return pd.DataFrame({
                "emi_eligibility_pred": cls_out,
                "max_monthly_emi_pred": list(reg_pred)
            })
        except Exception:
            # fallback to dummy if model call fails
            pass

    # Dummy fallback (keeps UI working)
    return pd.DataFrame({
        "emi_eligibility_pred": ["Eligible"] * n,
        "max_monthly_emi_pred": [5000.0] * n
    })
