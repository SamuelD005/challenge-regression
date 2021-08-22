# Price Prediction Model App Streamlit



[![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/samuel-dodet/)


![Logo](https://github.com/SamuelDodet/Scrapping_RealEstate_Belgium/blob/main/image/logo.png)
<!-- PROJECT LOGO -->
<br />
<p align="center">
    

  <h3 align="center">Price Prediction Model App Streamlit</h3>

  <p align="center">
    Project done during BeCode Bootcamp.
    <br />
    <a href="https://becode.org/learn/ai-bootcamp/"><strong> BeCode BootCamp </strong></a>
    <br />
    <br />

  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Conclusion</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


### Mission objectives
- Be able apply a linear regression in a real context
- Be able to preprocess data for machine learning

### Project steps:
- #### Data Cleaning
  * Using given Dataset
    * Dataset link: https://raw.githubusercontent.com/JulienAlardot/challenge-collecting-data/main/Data/database.csv
    * Note: We have created our own more complete dataset by a different scrapping approach. 
      Check it on: https://github.com/SamuelDodet/Scrapping_RealEstate_Belgium
    * Cleaned Dataset : ./dataset.csv
    

- #### Data formatting
  * Creating pipeline for numerical and categorical features
  * Split Dataset into Train / Test
  * Normalize Data
    

- #### Model:
    * Selection of Model ( XGBoost)
    * Training Model
    * Model Saving (Pickle)
    * Model Evaluation

- #### Application Platform:
    * Streamlit
    
#### Objective:
Create a program capable of scraping one (or more ?) real estate websites while respecting all constraints.


### Built With

To achieve this challenge, here are the main framework use in it:

* [Pandas](https://pandas.pydata.org/)
* [Sklearn](https://scikit-learn.org/stable/)
* [XGBoost](https://xgboost.readthedocs.io/en/latest/)
* [StreamLit](https://streamlit.io/)




<!-- GETTING STARTED -->
## Getting Started



### Installation


1. Clone the repo
   ```sh
   git clone git@github.com:SamuelDodet/House_Pricing_Prediction.git
   ```
2. Install required packages
   ```sh
   pip install requirement.txt
   ```
   or
   ```sh
   pip3 install requirement.txt
   ```
3.Install streamlit
   ```sh
   pip install streamlit
   ```

4. Data Source
   
    * https://raw.githubusercontent.com/JulienAlardot/challenge-collecting-data/main/Data/database.csv



<!-- USAGE EXAMPLES -->
## Usage

#### Data Cleaning:
* Using Pandas Profiling to have a good overview of the data
* Drop rows without prices / Area / Type of properties as it is our target, and our main features
* delete row with outlier value (1€/house, unnatural area, ...)
* Delete columns with too many NaN 
* Delete duplicate

Done Outside this project but final dataset in repository
    
#### Data Formatting:

run model_use.py --> Preprocessing and Model Creation

Here in details the elements:

  * Pipeline
    * Categorical:
        * ['Type of property','Fully equipped kitchen', 'Furnished', 'Open fire',
                                    'Number of facades','Swimming pool', 'State of the building', 'Province', 'Region'
                                     ]
    * Numerical:
        * ['Locality', 'Number of rooms', 'Area', 'Terrace Area', 'Garden Area',
                                   'Surface of the land']
          
    
  * Normalizing Data : 
    * Categorical:
        * Standard Scaler
    * Numerical:
        * Most Frequent / One Hot Encoder
    
    
  *  Split DataSet:
        * SkLearn train_test_split Module
    

#### Model

Model will be saved in a pickle file for easy loading purpose

Model Score : 74%

#### Streamlit

In terminal ''' steamlit app_streamlit.py
''' to execute streamlit app visualisation





<!-- ROADMAP -->
## Conclusion

The database generated is a good base to construct a model of price prediction or 
to analyse the state of Belgian Market




<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

### Team Members
Samuel Dodet - [@Linkedin](https://www.linkedin.com/in/samuel-dodet/) - samuel.dodet3@gmail.com

Jeremy Lipszic - [@Linkedin](https://www.linkedin.com/in/jeremy-lipszyc/) - jeremylipszyc@gmail.com

Yolann Sabaux - [@Linkedin](https://www.linkedin.com/in/samuel-dodet/) - samuel.dodet3@gmail.com

Clement Hannecourt - [@Linkedin](https://www.linkedin.com/in/haenecour/) - cl.haenecour@gmail.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/SamuelDodet/Scrapping_RealEstate_Belgium)

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555


