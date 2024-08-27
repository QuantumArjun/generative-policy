# Beyond Stereotypes, Accurately Representing Personas

## Repo Instructions

### Download Repo
To clone this repo, simply go to your terminal and clone type `git clone <giturl>`

To verify that the repo is working, simply cd into the repo, and run `python main.py`. This should result in the following output: "My Code is Running!". If so, yay! You've succesfully cloned the repository. 

### Set-up Python Environment 
Next, you'll want to set up your Python environment to ensure that there is no package conflicts during the development process.

Step 1 - Create a Virtual Environment `python -m venv venv`

Step 2 - Activate the Virtual Environment `source venv/bin/activate`

Step 3 - In your repo, after the virtual environment has been activated, run the following: `pip install -r requirements.txt`

This should verify that your repository packages have been set up properly! To check that it worked, run the following and make sure it's not empty: `pip list`

As always, if something doesn't work, ping me and we can figure it out! 

### Code Instructions 

The code is setup in the following manner

- experimentation.py: This is the main function of the program, and takes in all the arguments to run an experiment. If you simply wish to run the experiment from beginning to end, run experimentation.py 

- data_procesor.py: This function reads in the data (currently, ANES 2012, 2016, and 2020), and processes it so that it is readable by our program. It then saves this information in an external JSON. 

- create_participant.py: This function takes in the participant information from the aforementioned JSON, samples n participants, and creates a GPT prompt using the participants' information. 

- simulate_participant.py: This function takes in a cosntructed human participant and simulates them using GPT, giving in both the identity and the desired question 




