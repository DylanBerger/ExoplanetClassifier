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

The model achieved 98.65% accuracy on the test set (which was 30% of the total amount of data)

![image](https://github.com/DylanBerger/Exoplanet-Classifier/assets/82914031/9077a73c-b18d-4c03-baa5-cd071e387df6)

The confusion matrix showed that the model did a very good job at predicting all classes 

![image](https://github.com/DylanBerger/Exoplanet-Classifier/assets/82914031/20fef540-4511-409d-8cf4-a2eac8a7d2e0)

I then saved the model and tested it on an additional 13 examples. It got all of them correct.

![image](https://github.com/DylanBerger/Exoplanet-Classifier/assets/82914031/a4edf3e5-11dd-45f4-a104-639692e0257c)

For all intents and purposes, the model did great!

# Building the site

Building the site was a lot of trial and error - made with css, html, and python.

The design of the site was very simple, nothing complicated:

![image](https://github.com/DylanBerger/Exoplanet-Classifier/assets/82914031/696cddf1-8f0a-49cb-bab0-2f2233cca78d)

All you have to do is enter the density in grams per centimeter cubed and the mass/radius in either Jupiters or Earths (which you can select). The site then outputs the class below. Here is a demonstration: 

https://github.com/DylanBerger/Exoplanet-Classifier/assets/82914031/654d1048-c068-4039-9354-2027f65b9685

And of course you can see the code in this repository.

# Running the site

Unfortunately, you can't run the site by just opening the html file, but here's how you can.

The first step is to go to the command prompt and navigate to the directory that holds all the files. You can achieve this with: cd your/path/right/here

Once your in the directory, all you have to do is type 'python app.py" and then copy the server address.

![image](https://github.com/DylanBerger/Exoplanet-Classifier/assets/82914031/1001d168-2d63-4ec2-81cf-627ba940f40e)
