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

![image](https://github.com/DylanBerger/ExoplanetClassifier/assets/82914031/78f7dc77-719e-440a-8b5a-c55225019f2c)

Therefore to simplify the model I was able to remove the rest of the features

The fifth step on the other hand, involved doing calculations with the data I had, to fill in missing cells. I mainly performed calculations to estimate the orbital period, semi-major axis, and density. Here are the formulas: 

![image](https://github.com/DylanBerger/ExoplanetClassifier/assets/82914031/8f2bb744-7ff2-4801-ac12-6122f7280de1)
 
![image](https://github.com/DylanBerger/ExoplanetClassifier/assets/82914031/0b4bcb34-e313-4829-beda-70cc65f8d9e3)
 
![image](https://github.com/DylanBerger/ExoplanetClassifier/assets/82914031/5c7eb789-cf22-4e75-bf59-2a2febc00d00)

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

![image](https://github.com/DylanBerger/ExoplanetClassifier/assets/82914031/af387158-9d43-405e-9378-f052cc5e0240)

![image](https://github.com/DylanBerger/ExoplanetClassifier/assets/82914031/b76678f2-d6d8-4ee3-b558-a3c69e038cb7)

One thing you might have noticed is the lack of standardization/normalization. The model for some reason did not train well if I normalized/standardized the data. It would overfit and perfer the "Gas Giant" class in every test example. My only guess is that applying these techniques affected the usefulness of the data, perhaps putting it to too much of the same scale. Regardless, it worked extremely well without standardization/normalization.

# The Model

The model is as such: 

![image](https://github.com/DylanBerger/ExoplanetClassifier/assets/82914031/e50d0618-a7c3-4be9-92a4-3f876f8fae5c)


It performed extremely well with every depth and number of trees. Given this, I aimed to simplify it and look for the sweetspot which I found to be around 35 trees and 8 layers of depth.

# Evaluation

The model achieved 98.65% accuracy on the test set (which was 30% of the data)

![image](https://github.com/DylanBerger/ExoplanetClassifier/assets/82914031/055800ed-eb94-437a-81be-cf2601869674)

The confusion matrix showed that the model did a very good job at predicting all classes, and in the rare errors it did make, they were at least reasonable. The model did not ever classify a gas giant as a terrestrial planet for example. 

![image](https://github.com/DylanBerger/ExoplanetClassifier/assets/82914031/8d9aa5eb-cfa4-457e-beff-d20a5af5ac8c)

I then saved the model and tested it on an additional 13 examples. It got all of them correct.

![image](https://github.com/DylanBerger/ExoplanetClassifier/assets/82914031/895538e4-abc4-4674-a2a5-05b2353d8c68)

For all intents and purposes, the model did great!

# Building the site

Building the site involved a lot of trial and error. 

The development process of this entailed:

1. Website design (html and css)
2. Model Integration (python)
3. Debugging

Here is the design of the site and the code, made to be very simple:

![image](https://github.com/DylanBerger/ExoplanetClassifier/assets/82914031/c3854307-4d72-4de8-a3ad-55b56243192f)

All you have to do is enter the density in grams per centimeter cubed and the mass/radius in either Jupiters or Earths (which you can select) and it will output a class. Here is a demonstration: 

https://github.com/DylanBerger/ExoplanetClassifier/assets/82914031/869dfab9-1d28-4e35-9f9c-5a40428d69b1

The only limitation to the website and the model itself is that it relies on an accurate density value. This is because you calculate density from the planets radius and mass so if the density is not accurate, it will mess with the model. 

And of course you can see the code in this repository.

# Running the site

Unfortunately, you can't run the site by just opening the html file, but here's how you can:

- The first step is to go to the command prompt and navigate to the directory that holds all the files. You can achieve this with: cd your/path/right/here

- Once in the directory, all you have to do is type 'python app.py", copy the server address and paste it into your internet browser.

![image](https://github.com/DylanBerger/ExoplanetClassifier/assets/82914031/31fb3a1f-6228-4a0b-b80c-09f6f6630cad)

# Next Steps

The model performed just as we wanted. The next steps would be to make the website look nicer, add more unit options, and make it so it automatically calculates density. But that is for another time. In the mean time, hope you enjoyed this project!
