from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load your model here
model = joblib.load('C:/Users/Dylan/exoplanets/models/exoplanet_classifier.joblib')
@app.route('/', methods=['GET', 'POST'])

def home():
    prediction = None
    predicted_label = None

    if request.method == 'POST':
        exoplanetmass = float(request.form['exoplanetmass'])
        exoplanetradius = float(request.form['exoplanetradius'])
        exoplanetdensity = float(request.form['exoplanetdensity'])
        unit = request.form['unit']


        # Convert units if needed
        if unit == 'Earths':
            # Convert values based on your conversion logic
            exoplanetmass = exoplanetmass * 0.00314558
            exoplanetradius = exoplanetradius * 0.0892147
            
        
        new_data = pd.DataFrame({
            'pl_radj': [exoplanetradius],
            'pl_bmassj': [exoplanetmass],
            'pl_dens': [exoplanetdensity]
        })

        if not exoplanetdensity:
            exoplanetradius *= 7.149e+9
            exoplanetmass *= 6.99115e+9
            volume = (4/3) * (np.pi) * (exoplanetradius**3)
            exoplanetdensity = exoplanetmass/volume



        # Make prediction using your loaded model
        if exoplanetmass and exoplanetradius and exoplanetdensity and unit:
            predicted_class = model.predict(new_data)
            predicted_label = predicted_class[0]
        # Map predicted class to human-readable format
    
        
    
    return render_template('index.html', prediction=predicted_label)

if __name__ == '__main__':
    app.run(debug=True)
