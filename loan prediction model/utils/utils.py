
import numpy as np
import joblib

def preprocessdata(income, age, experience, married_single, house_ownership, car_ownership, profession, city, state, current_job_yrs, current_house_yrs):
    # Encode the categorical features
    label_encoder = joblib.load("label_encoder.pkl")
    married_single_enc = label_encoder.fit_transform([married_single])[0]
    house_ownership_enc = label_encoder.fit_transform([house_ownership])[0]
    car_ownership_enc = label_encoder.fit_transform([car_ownership])[0]
    profession_enc = label_encoder.fit_transform([profession])[0]
    city_enc = label_encoder.fit_transform([city])[0]
    state_enc = label_encoder.fit_transform([state])[0]

    test_data = np.array([[income, age, experience, married_single_enc, house_ownership_enc, car_ownership_enc, profession_enc, city_enc, state_enc, current_job_yrs, current_house_yrs]])

    trained_model = joblib.load("extra_trees_model.pkl")
    standard_scaler = joblib.load("standard_scaler.pkl")

    scaled_numerical_features = standard_scaler.transform([[income, age, experience, married_single_enc, house_ownership_enc, car_ownership_enc, profession_enc, city_enc, state_enc, current_job_yrs, current_house_yrs]])

    # Combine the scaled numerical features and encoded categorical features
    # combined_test_data = np.concatenate([scaled_numerical_features, test_data], axis=1)

    prediction = trained_model.predict(scaled_numerical_features)

    return prediction














