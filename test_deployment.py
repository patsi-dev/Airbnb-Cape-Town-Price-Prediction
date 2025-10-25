# Simple test to verify model can be loaded and used
import joblib
import numpy as np
import pandas as pd

def test_deployment():
    """Test that the deployed model works correctly"""
    try:
        # Load model
        model = joblib.load('saved_models/airbnb_price_predictor_{timestamp}.joblib')
        print("✅ Model loaded successfully")
        
        # Create test input
        test_input = pd.DataFrame({
            'accommodates': [4],
            'bedrooms': [2],
            'bathrooms': [1],
            'room_type': ['Entire home/apt'],
            'property_type': ['Apartment'],
            'neighbourhood_cleansed': ['City Bowl'],
            'latitude': [-33.9258],
            'longitude': [18.4232],
            'minimum_nights': [2],
            'host_is_superhost': [True],
            'instant_bookable': [True],
            'amenities_count': [5],
            'luxury_score': [2],
            'dist_to_table_mountain': [2.5],
            'dist_to_v_a_waterfront': [1.2],
            'dist_to_camps_bay': [4.1]
            
        })
        
        # Make prediction
        prediction = model.predict(test_input)
        price = np.expm1(prediction[0])
        print(f"✅ Test prediction successful: ZAR {price:.2f}")
        return True
        
    except Exception as e:
        print(f"❌ Deployment test failed: {e}")
        return False

if __name__ == "__main__":
    test_deployment()