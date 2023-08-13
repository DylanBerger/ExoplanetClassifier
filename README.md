# Overview
The purpose of this classifier was to create a machine learning model which could classify planets. I ended up using a random forest classifier which achieved 98.65% accuracy with just three parameters. Note: before running the site, look for the instructions in this page to properly set it up. 

# Repository Summary 

- "data" which holds the original dataset, the cleaned dataset, and a third dataset to see my model in action after everything is done.
- "models" which holds the random forest model
- "static" which holds the css file of my site
- "templates" which holds the html file
- "app.py" which configures the website
- "classification" which is the code of the machine learning part of the project

# Data

All of the data originates from NASAs exoplanet archive (https://exoplanetarchive.ipac.caltech.edu/) and NASAs exoplanet catalog (https://exoplanets.nasa.gov/discovery/exoplanet-catalog/). 

Making the cleaned dataset involved several steps:

1. Downloading the dataset from the exoplanet archive (one dataset)
2. Gathering planet classes with data scaping techniques (another dataset)
3. Merging the two datasets
4. Deciding which features are relevant
5. Filling in null values

The two last steps were the most difficult. The fourth one involved extensive research into which features were most relavant, narrowing them down to seven, and then running the model with them.  

After training the model, I performed a feature test to see which ones were most relevant to the model, of which mass, radius, and density were the most relevant by a fair margin as you can see. ![image](https://github.com/DylanBerger/Exoplanet-Classifier/assets/82914031/6d3bf77e-ded6-4ad0-a4a0-f146b78363d9). 

Therefore to simplify the model I was able to remove them.

The fifth step on the other hand, involved doing calculations with the data I had, to fill in missing cells. I mainly performed calculations to estimate the orbital period, semi-major axis, and density.

These steps resulted in a cleaned dataset ideal for machine learning!

# Data Preprocessing

Processing the data involved several steps:

1. Loading the model
2. Dropping irrelevant columns/features
3. Dropping rows with null values (if calculations couldn't be made)
4. Label Encoding (assigning a value to each class)
5. Shuffling the dataset (eliminate accidental bias)
6. Balancing the dataset (making sure the model learns from all classes equally)
7. Running the model with it

To balance the dataset I used undersampling because the dataset was relatively large. Here is the before and after: 
![image](https://github.com/DylanBerger/Exoplanet-Classifier/assets/82914031/0a4d8f5f-c74d-4d44-b146-60a1c655690f) ![image](https://github.com/DylanBerger/Exoplanet-Classifier/assets/82914031/78263d0e-dcce-4f9c-8c20-b4cbb5248601)

One thing you might have noticed is the lack of standardization/normalization. The model for some reason did not train well if I normalized/standardized the data. It would overfit and perfer the "Gas Giant" class in every test example. My only guess is that applying these techniques affected the usefulness of the data, perhaps putting it to too much of the same scale. Regardless, it worked extremely well without standardization/normalization.

# The Model

The model is as such: 

![image](https://github.com/DylanBerger/Exoplanet-Classifier/assets/82914031/b01c6fee-6e47-4103-8d1a-5670984eae10)


It performed extremely well with every depth and number of trees. As such I aimed to simplify it and look for the sweetspot which I found to be around 35 trees and 8 layers of depth.

# Evaluation



