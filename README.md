# Overview
The purpose of this classifier was to create a machine learning model which could classify planets. I ended up using a random forest classifier which achieved 98.65% accuracy with just three parameters. Note: before running the site, look for the instructions on the bottom of the page to properly set it up. 

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

The two last steps were the most difficult. The fourth one involved extensive research into which features were most relavant, narrowing them down to six, and then running the model with them.  

After training the model, I performed a feature test to see which ones were most relevant to the model, of which mass, radius, and density were the most relevant by a fair margin as you can see:

![image](https://github.com/DylanBerger/Exoplanet-Classifier/assets/82914031/6d3bf77e-ded6-4ad0-a4a0-f146b78363d9). 

Therefore to simplify the model I was able to remove the rest of the features

The fifth step on the other hand, involved doing calculations with the data I had, to fill in missing cells. I mainly performed calculations to estimate the orbital period, semi-major axis, and density. Here are the formulas: 

![image](https://github.com/DylanBerger/Exoplanet-Classifier/assets/82914031/617f2ab9-8715-4383-8ec3-ee94804fbed5) 

![image](https://github.com/DylanBerger/Exoplanet-Classifier/assets/82914031/4084b19a-f202-4f5e-988d-aeafcdff4d39) 

![image](https://github.com/DylanBerger/Exoplanet-Classifier/assets/82914031/b5b6aaef-4893-4a26-9cbf-b45adf725fbf)

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

To balance the dataset I used undersampling because the dataset was relatively large and the Terrestrial class was massively underrepresented. Here is the before and after: 
![image](https://github.com/DylanBerger/Exoplanet-Classifier/assets/82914031/0a4d8f5f-c74d-4d44-b146-60a1c655690f) ![image](https://github.com/DylanBerger/Exoplanet-Classifier/assets/82914031/78263d0e-dcce-4f9c-8c20-b4cbb5248601)

One thing you might have noticed is the lack of standardization/normalization. The model for some reason did not train well if I normalized/standardized the data. It would overfit and perfer the "Gas Giant" class in every test example. My only guess is that applying these techniques affected the usefulness of the data, perhaps putting it to too much of the same scale. Regardless, it worked extremely well without standardization/normalization.

# The Model

The model is as such: 

![image](https://github.com/DylanBerger/Exoplanet-Classifier/assets/82914031/b01c6fee-6e47-4103-8d1a-5670984eae10)

It performed extremely well with every depth and number of trees. Given this, I aimed to simplify it and look for the sweetspot which I found to be around 35 trees and 8 layers of depth.

# Evaluation

The model achieved 98.65% accuracy on the test set (which was 30% of the data)

![image](https://github.com/DylanBerger/Exoplanet-Classifier/assets/82914031/9077a73c-b18d-4c03-baa5-cd071e387df6)

The confusion matrix showed that the model did a very good job at predicting all classes, and in the rare errors it did make, they were at least reasonable. The model did not ever classify a gas giant as a terrestrial planet for example. 

![image](https://github.com/DylanBerger/Exoplanet-Classifier/assets/82914031/20fef540-4511-409d-8cf4-a2eac8a7d2e0)

I then saved the model and tested it on an additional 13 examples. It got all of them correct.

![image](https://github.com/DylanBerger/Exoplanet-Classifier/assets/82914031/a4edf3e5-11dd-45f4-a104-639692e0257c)

For all intents and purposes, the model did great!

# Building the site

Building the site involved a lot of trial and error. 

The development process of this entailed:

1. Website design (html and css)
2. Model Integration (python)
3. Debugging

Here is the design of the site and the code, made to be very simple:

![image](https://github.com/DylanBerger/Exoplanet-Classifier/assets/82914031/696cddf1-8f0a-49cb-bab0-2f2233cca78d)

All you have to do is enter the density in grams per centimeter cubed and the mass/radius in either Jupiters or Earths (which you can select) and it will output a class. Here is a demonstration: 

https://github.com/DylanBerger/Exoplanet-Classifier/assets/82914031/654d1048-c068-4039-9354-2027f65b9685

The only limitation to the website and the model itself is that it relies on an accurate density value. This is because you calculate density from the planets radius and mass so if the density is not accurate, it will mess with the model. 

And of course you can see the code in this repository.

# Running the site

Unfortunately, you can't run the site by just opening the html file, but here's how you can:

- The first step is to go to the command prompt and navigate to the directory that holds all the files. You can achieve this with: cd your/path/right/here

- Once in the directory, all you have to do is type 'python app.py", copy the server address and paste it into your internet browser.

![image](https://github.com/DylanBerger/Exoplanet-Classifier/assets/82914031/1001d168-2d63-4ec2-81cf-627ba940f40e)

# Next Steps

The model performed just as we wanted. The next steps would be to make the website look nicer, add more unit options, and make it so it automatically calculates density. But that is for another time. In the mean time, hope you enjoyed this project!
