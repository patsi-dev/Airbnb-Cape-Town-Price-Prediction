# 🚀 Cape Town Airbnb Price Optimizer - Deployment Guide

## Prerequisites
- Python 3.8+
- Streamlit installed
- Saved model files in 'saved_models/' directory

## Quick Start
1. Install required packages:
```bash
pip install streamlit pandas numpy scikit-learn xgboost folium streamlit-folium joblib
```

2. Run the Streamlit app:
```bash
streamlit run capetown_airbnb_predictor.py
```

3. Open your browser to the local URL (typically http://localhost:8501)

## Features Included
✅ Property characteristic input form
✅ Interactive Cape Town map
✅ Real-time price predictions
✅ Neighborhood comparisons
✅ Pricing insights and tips
✅ Mobile-responsive design

## Production Deployment Options

### Option 1: Streamlit Sharing (Recommended)
1. Push code to GitHub repository
2. Connect repository to Streamlit Sharing
3. Deploy with one click

### Option 2: Heroku
1. Create Procfile and requirements.txt
2. Deploy using Heroku CLI
3. Scale as needed

### Option 3: AWS/Azure/GCP
1. Containerize app with Docker
2. Deploy to cloud platform
3. Set up auto-scaling

## Model Updates
- Retrain model quarterly with new data
- Monitor prediction accuracy
- Update saved model files
- Test thoroughly before deployment

## Monitoring & Maintenance
- Track user engagement metrics
- Monitor prediction performance
- Gather user feedback
- Regular security updates