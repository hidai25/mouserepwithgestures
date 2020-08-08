
### Team Name: Computer mouse replication with gestures

### Team Members:

Gurel Ari (gurelari.ivy@gmail.com)

Hidai Bar-mor (hidai25@gmail.com)

Vikram Maduskar (vim882@g.harvard.edu)

Nina Tabari ( naz706@g.harvard.edu)

Vasco Meerman (vmeerman.appdev@gmail.com)

#### Project’s website:

http://hidai25.github.io/mouse_project_frontend  

### Runnning instructions

Firstly while your terminal is on the project folder do:  

"pip3 install -r requirements.txt"

in order to make sure you have all the required packages for the project.

Then order to make the project work you first have to have tutorial 1 code running of the link:

"https://sites.google.com/view/ucla-stmicroelectronics-iot/home". The sensortile should send data to your computer. Then you have to do the following:

1. In order to run the project with machine learning, go to the folder "real_time_python_with_ml" and open the file "args_with_ml". Enter inside the file your own computers sensortile port name. Then, while having the file "serial_with_ml" in the same file and the folder sav_files run the file args_with_ml in python and the project will start working.

2. In order to run the project without the machine learning (only mouse controlled by the sensor) go to the folder "mouse-sensor_no_ml" and open the file "args_no_ml". Change the address line to your computer sensortile port and make sur the file "serial_no_ml" is in the same folder. Then run the "args_no_ml" file and the project will start working.

# Project Final Report:

# About the Project:

The inspiration for this project was the movie “Minority Report”, specifically the scene where Tom Cruise is using hand gestures to control the display.
Based on the output from tutorial 1 we know the sensor can tell XYZ dimensions/directions, which means that technically we can capture most of the movements of the mouse.
We are going to reuse parts of the code from tutorial 1 and modify it to create and open a port to submit data as we move the sensor. More clearly, it’ll be passing the data to a python script. There is a package in python called “PYAUTOGUI” that allows you to control the position of the mouse, which means that once the python application receives the information it can identify changes in the data and correlate those to the mouse position. We will try and capture different movements for the mouse. We will try to at the minimum replicate all the movement classes that the PYAUTOGUI package captures.
Motivation:
This pipeline will allow you to transfer the information from the sensor to something that can control the position of the mouse. The motivation for this project is that you can integrate this with any device or display so instead of having to manually select options you can do so via gestures, in other words touch might be augmented or substituted by motion. It could later on be modified to work for people with disabilities or ones who have suffered an injury to their fingers or arms, and allow them to use this as a headband (or similar device) to control the mouse/cursor’s movement.
Additionally, this would also be a better option for interaction in a VR or AR world.
Technology Components (Software and Hardware):
Anaconda Package (Python 3.7, 64 bit including Jupyter notebook, Numpy, panda, scikit-learn, TensorFlow, Keras, Matplotlib, PyAutoGUI), Django
Python package- PYAUTOGUI
We are using the sensortile to collect the data
Possible use of our phones
React

# Workflow:

### Work Plan and Milestones:

#### Week 1 (13-20.07):

* Setting up a laptop developing environment including all the software packages/tools
* Define the set of specific gestures classes to be recognized and passed to the screen for classification
* Define the data collection, data preparation and data modelling approach
* Configure and test the device
* Identify what movements are captured by the device
* Confirm that we can register movements in each direction

#### Week 2 (20-27.07):

* Establish connectivity between the movement and mouse
* Data collection with the sensor for the set of defined gesture classes
* Data preprocessing and cleaning
* Data exploration and feature engineering
* Data modelling
* Model training
* Model evaluation and Optimization
* Model Deployment in device

#### Week 3 (27-03.08):

* Conduct and document motion predictions/classifications by device
* Prepare project report (pdf/word document)
* Prepare project video
* Update and finalized code/content on project in Github
* Prepare powerpoint slides

#### Week 4 (3-03.08):

* Practice for presentation
* Final Class presentation

# Data Collection:

To collect the data, we first had to investigate the “PYAUTOGUI” package to determine the movements and get an idea of how we could compile the code. After some investigation, we decided to use 6 motions, each mapped to a certain movement of the mouse or a click. The movements we chose to collect data on include right swipe, left swipe, upward swipe, downward swipe, spiral, and wave. The swiping movements are used to control the mouse and which direction it will go as we move the sensor, and the spiral and wave gestures are used to imitate the right and left clicks of the mouse. After agreeing on the types of motions, we proceeded with the data collection.  

For each movement, we decided it would be best to use 75% of the data for training and 25% of the data for testing. To do that, we decided to collect data 30 times for each of the gestures, totaling 180 collections. To add variety to our gestures, we decided to use different speeds for the movements: fast, medium, and slow. These little differences were used to create a real-world-model to accommodate for different users and different speeds. After collecting each data, we labeled them according to their speeds and their types. Finally, we uploaded them to our GitHub repository to proceed with data processing.  

# Data Processing, Machine Learning, and Test:

### Data merging, concatenating and cleaning:  

The movement data we collected had a time frame of seconds per movement. The sensory data of each movement was split into 3 separate files for each sensor, so we had 3 different movement files per movement on the exact same time frame with each file consisting of different x, y and z axis corresponding to 1 of the sensors. Also each of the people recording the data, made 15 recordings per movement type. So to split our test/train data, we made a cutoff at the 11th movement per person, which came to approximately 25/75 test/train data. We could not do 30/70, since this would mean we would have to cut some time frames into 2 parts.

So before we could use the data as test and training data to create our machine learning model, we first had to merge each movement’s sensor data into 1 file and then concatenate all the time frames into a training and test dataset. To do this, Vasco created a separate pipenv project, which consisted of these steps:

1. Reading in each separate movement file, per sensor.

![im1](/imgs_fr/im1.png)



a. As you can see here we have 3 different sensor files per each numbered movement per movement type (e.g down)

2. Merging each separate movement into 1 file consisting of all different x,y and z axis for each sensor.
This happened for both the datasets we got simultaneously, so both persons.

3. Then deciding based on our test/train cutoff where each merged movement file was going to be concatenated to.

![im2](/imgs_fr/im2.png)

a. Note that we’re getting the data from both person’s numbered movements (e.g. move_1, move_g_1), at the same time, because we want our test/train data sets to contain an amount of movement data frames from both persons.

4. Now that all the data of a movement is merged and concatenated and separated evenly from both persons into a test and training set, we repeat the process for each movement until we have all or movement separated in test/train.  

5. Lastly we clean and optimize both datasets before saving them to csv files, ready to use with our ML.

![im3](/imgs_fr/im3.png)

These are the stats of the project we just described:

![im4](/imgs_fr/im4.png)

The data was then uploaded to github, so it could be used to generate our Machine Learning models.  

## Machine Learning: Model Training, Evaluation & Optimization  

Our methodology for training, evaluating and optimizing the best performing model selected from among 5 different ML models consisted of the below steps:

* Step 1. Environment Setup
* Step 2. Data Setup
* Step 3. Exploratory Data Analysis
* Step 4. Classifier Model Training & Evaluate Models
* Model 1:Logistic Regression
* Model 2: SVM
* Model 3:Random Forest
* Model 4: AdaBoost
* Model 5: XGBoost
* Step 5. Best Model Selection
* Step 6. Hyper Parameter Tuning Of Selected Model
* Step 7. Save Persistent Finalized Model to Disk

### Summary of ML modelling:  
The performance metrics used as the basis for selecting the best model were: Accuracy, Precision, Recall and Prediction execution time. Of the ML 5 models listed above, our evaluation selected XGBoost to be the best model. We then further tuned the hyper parameters of this model using Grid-search cross validation approach to optimize its performance significantly further. The hyper tuned final model was then saved in a serialized, persistent format whereby it could be deployed and invoked in a live environment anytime for performing classification on new real time sensor data.

A few samples of the EDA data visualization plots from our Jupyter notebook:



![im5](/imgs_fr/im5.png)





![im6](/imgs_fr/im6.png)



![im7](/imgs_fr/im7.png)



![im8](/imgs_fr/im8.png)



![im9](/imgs_fr/im9.png)


![im10](/imgs_fr/im10.png)




* Note: For full details and python code of our ML modelling methodology please refer to the attached Jupyter notebook and our Github repository.

# Real-Time Computer Integration With The Code:

 The real time integration of our model with the sensortile code was done in python. We used two python files that basically got the data from our computer’s usb port and at first just connected it to the pyautogui package to get a live mouse control with no classifier but only with live accelerometer data. Then  we took the  real time data and processed it in the same way our ml data was processed to put it in the exact same format. Once the live data was in the same form of the training data we gave it to the finalized ml model and connected the output (L,R,D,U,S,W) to the pyautogui package again to get a finalized product.

# Final Product:
The goal of this project was to create a script that would react to the movement of the sensor tile in real time and move the mouse cursor accordingly on the screen.  

In order to accomplish this task, the first thing we did was to investigate different machine learning algorithms so that we could differentiate and associate gestures with sensor tile readings.  

This was done through visualization, feature importance, and dimensionality reduction techniques. We further investigated the accuracy of a variety of classification techniques, determining that XGBoost resulted in high quality classifications.
We then created a real time system incorporating C and Python in order to process sensor movements in real time, these sensor readings were then converted into actualized corresponding mouse movements on the screen.

Therefore this project demonstrated and serves as a proof of concept on the feasibility of controlling the computer mouse through wearable sensors.  

We expect this type of technology could be of great interest and benefit for controlling computers remotely without the use of traditional input devices like keyboard and mouse as it’s usually the case in AR and VR environments.


# Summary and Conclusion:

## Next Steps and Future Plans:

### Next Steps:
As part of the future work, we would explore methodologies to reduce the time lag between the sensor and mouse movement, as well as refining and expanding the number of recognized gestures.  

With further development, this technology could be useful for people with disabilities. For example, a paralyzed person could rotate his head to control the direction of his wheelchair. A hat containing a sensor or even glasses with an embedded sensor could be used to control the wheelchair. The chair can be programmed to register the voice commands of the user as starting and stopping the motor and while in action, the user can tilt his head the direction he wants to go. The chair could register this swiping motion and redirect the user in the direction he wants to go. The sensor integration could be taken even one step further with nanochips in the future by embedding the actual sensor inside the eye so that no external sensor is needed to control the chair. Just the eye movements of the user would suffice to control the cart if used this way.
## Web App classification

We were also working on a web app that can live demo our movement classifier by accessing the sensors of phones visiting our website. This was built with a Django backend, React frontend. The latest Django versions above 3.0, supports ASGI which gives developers the possibility to program asynchronously. This made the use of websockets easier to do then previous Django versions where you have to use Django-channels. It works like this:

1. Django opens websocket while opening the frontend app with React
2. Then the React App displays a button to begin the movement classifier, for which it then takes care of getting the required permissions through the Generic Sensor Api.

a. Basically we created a bridge in React with a native JS library through a polyfill to access the motion sensors  library, be able to access and process the data in React.

3. Once it has the permissions, it sends the recorded x,y z data for all 3 required sensors for our ML model directly through the websocket back to Django.

4. Django then formats the data into the correct pandas dataframe object required for our ML model to work.

5. The data is fed to the model and makes the predictions, which are then sent downstream through the websocket to React.

6. React then displays the movement our model classified and with which accuracy.

7. Lastly the user can start again to try another movement.

Project Repository – Github, Video URL, Online Resources:



#### References:

1. https://machinelearningmastery.com/how-to-model-human-activity-from-smartphone-data/
2. http://stanford.edu/class/ee267/Spring2018/report_adu_bran-melendez.pdf
3. https://lembergsolutions.com/blog/motion-gesture-detection-using-tensorflow-android
