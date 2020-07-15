Please submit your proposal with the following content:
1. Team Name:
Computer mouse replication with gestures
2. Team Members and Roles: (Depending on the strengths of each member as an example)

Gurel Ari (gurelari.ivy@gmail.com) => Data Collection

Hidai Bar-mor (hidai25@gmail.com) => Data Processing

Vikram Maduskar (vim882@g.harvard.edu) => Data Modeling and Machine Learning

Nina Tabari ( naz706@g.harvard.edu) => Project Lead and writing the python script

Vasco Meerman (vmeerman.appdev@gmail.com) => BE development  

3. Goal of the Project: (Describe here which problem are you solving and your motivation)
The inspiration for this project was the movie “Minority Report”, specifically the scene where Tom Cruise is using hand gestures to control the display.
Based on the output from tutorial 1 we know the sensor can tell XYZ dimensions/directions, which means that technically we can capture most of the movements of the mouse.
We are going to reuse parts of the code from tutorial 1 and modify it to create and open a port to submit data as we move the sensor. More clearly, it’ll be passing the data to a python script. There is a package in python called “PYAUTOGUI” that allows you to control the position of the mouse, which means that once the python application receives the information it can identify changes in the data and correlate those to the mouse position. We will try and capture different movements for the mouse. We will try to at the minimum replicate all the movement classes that the PYAUTOGUI package captures.
This pipeline will allow you to transfer the information from the sensor to something that can control the position of the mouse. The motivation for this project is that you can integrate this with any device or display so instead of having to manually select options you can do so via gestures, in other words touch might be augmented or substituted by motion. It could later on be modified to work for people with disabilities or ones who have suffered an injury to their fingers or arms, and allow them to use this as a headband (or similar device) to control the mouse/cursor’s movement.
Additionally, this would also be a better option for interaction in a VR or AR world.


4. Software and Developing tools:
Python package- PYAUTOGUI
Anaconda Package (Python 3.7, 64 bit including Jupyter notebook, Numpy, panda, scikit-learn, TensorFlow, Keras, Matplotlib, PyAutoGUI), Django
a. include a GitHub repository
https://github.com/hidai25/mouserepwithgestures
b. any other tools? (example: dropbox, google drive, slack, google collab, etc.)
Trello, Google Drive, slack
5. Hardware used:
We are going to base our work on one sensortile in order to acquire data.
6. Team Meeting Schedule: (tentative hours to meet with your team every week)
Twice a week on sunday and wednesday
7. List of Milestones, week by week:
Week 1 (13-20.07):
Setting up a laptop developing environment including all the software packages/tools
Define the set of specific gestures classes to be recognized and passed to the screen for classification
Define the data collection, data preparation and data modelling approach
Configure and test the device
Identify what movements
Week 2 (20-27.07):
Data collection with the sensor for the set of defined gesture classes
Data preprocessing and cleaning
Data exploration and feature engineering
Data modelling
Model training
Model evaluation and Optimization
Model Deployment in device
Week 3 (27-03.08):
Conduct and document motion predictions/classifications by device
Prepare project report (pdf/word document)
Prepare project video
Update and finalized code/content on project in Github
Prepare powerpoint slides
Week 4 (3-03.08):
Practice for presentation
Final Class presentation
8. Other comments:
As a stretch goal we might create an interactive web application for this project.
