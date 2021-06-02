from utils.preprocessing_model import ModellingData

mod = ModellingData()

print(mod.prediction_saved_model("xgb_reg.pkl", mod.X_test))
print(mod.load_model("xgb_reg.pkl").score(mod.X_test, mod.y_test))