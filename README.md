# Image Biolab
**Image Biolab** is an accessible resource database of images of cells, capturing a wide diversity of organisms, cell types, and cellular processes. It enables the user to explore the galleries or test his/her knowledge through a variety of tests!

# Current features
Image Biolab is a Django application with the following features:
* You can **exlpore** the beauty of living systems through unique images recovered from the cell image library.
* You can **test** your knowledge on microscopy and cellular biology through four quiz categories:
  * Identify the type of the organism in the shown images.
  * Identify the cellular type shown in the images.
  * Identify which type of microscopy was used to acquire the images.
  * Determine the common features between the shown images.

# Installing and running the application

## 1. Installing and running the application on a local server
*It is recommended to run the commands on a Linux distribution terminal*

* Run the following to clone the repository
~~~~
git clone https://github.com/yorgomoubayed/quizapp.git
~~~~

* Run the following to install the conda package and dependencies: 
~~~~
conda env create --file djangoenv.yml
~~~~
Check the requirements.txt file for any missing packages and install them if needed.

* Run the following to launch the application: 
~~~~
python manage.py runserver
~~~~

* Copy the following link **http://127.0.0.1:8000/quizapp/** into your navigator (Chrome is recommended). You should have access to the **Image Biolab** website home page.

## 3. Running the application on a remote server
The application was **deployed using Heroku**, a container-based cloud Platform as a Service (PaaS).
Follow this link for access **https://imagebiolab.herokuapp.com/quizapp/**

# Credits
Image Biolab was **created by Yorgo EL MOUBAYED**. This project was given for master's degree students majoring in Bioinformatics at the University of Aix-Marseille for the web development module.
