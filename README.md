# Duplito 

**Duplito** is a result of the Analytics Assignment of HackerCamp Summer 2018 where the main aim is to create a robust model which can Identify Variation in names and identifying a unique person and hence solve deduplication of records comming from multiple sources.

## Getting Started

Following are the instruction to you need to follow to get this project up and running into your local machine for testing and development purporse.

Following are the steps to create Python virtual environment for this project. This is recommended so that this project and other project can have its own dependencies, regardless of what dependencies every other project has.


### Installing

Following are the step by step to get a development env running

    1. Visit the Anaconda homepage.
    2. Click “Anaconda” from the menu and click “Download” to go to the download page.
    3. Choose the download suitable for your platform (Windows, OSX, or Linux):
    4. Follow the Installation wizard.
    5. Open the Anaconda Prompt and enter the following to create a python env
```
conda create -n myenv python=3.5
```
    6. Then enter the following commands to install the required dependencies for this project. 
```
conda install -n myenv scikit-learn
conda install -n myenv pandas
```

## Running the Code 

1. Download/Clone this repository.
2. Go the location and open Anaconda Prompt/Termial and start the environment by 
```
activate myenv
```
3. After this you can run the program by executing the following line.
```
python Duplito.py
```

Note: The program would pick the database from database directory and remove all the duplicate values from it and output it in Result.csv 
## Program I/O

For program *input/output* please check *dataset file* in dataset directory of this *repository* for **input** and **result.csv** for the output on that dataset.

## FAQ
Q: Why this repository named Duplito ?

Just like Magneto in X-Men is able to attract all the **magnetic substances** towards himself, same way this program is able to attract all the **duplicate sample** and leaves only original samples in *result.csv*


## Built With

* [scikit-learn](http://scikit-learn.org/) - Python Machine Learning Framework
* [Pandas](https://pandas.pydata.org/) - Python Data Analysis Library


## Authors

* **Dhruvraj Singh Rawat** - [LinkedIn](https://github.com/PurpleBooth)

## Acknowledgments

* Inspiration



