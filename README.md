# HEALTHY AI 🍽️

##### In this project, we developed and implemented a robust wellness platform aimed at empowering users to optimize their health through a personalized approach. The platform incorporates innovative features such as personalized diet suggestions, a cutting-edge recipe generator, and advanced food image identification technology.

## DATA SOURCE 📊
  I created this dataset by utilizing the Beautiful Soup library in Python for web scraping. [Web scraping documentation](https://beautiful-soup-4.readthedocs.io/en/latest/)
- [Food decommendation dataset ](https://drive.google.com/file/d/1dOGy_vMtQU3YqETamp2CNo78w8-ckLWN/view?usp=drive_link)
- [Food Image Classification dataset](https://drive.google.com/file/d/1lky7C3LipwPKv46QEjpTVHDTfrxEtXew/view?usp=sharing)




## How to use 💻

- Food Recommendation system ==> Input your height, weight, age, gender, physical activity level, and set your health goal. For instance, if your aim is to gain weight, this model can forecast healthy food options for breakfast, lunch, snacks, and dinner

- Food image Classification system ==> If an image of food is uploaded, the system has the capability to predict the type of food and provide information about its nutritional content

- Recipe generator  ==> When you input a collection of ingredients, the recipe generator will not only generate instructions on how to prepare the food but also determine the appropriate quantities for a healthy dish. It ensures that each step is provided with clear instructions for creating a nutritious meal



## How to run locally 🛠️

- Before the following steps make sure you have [git](https://git-scm.com/download), [Anaconda](https://www.anaconda.com/) or [miniconda](https://docs.conda.io/en/latest/miniconda.html) installed on your system
- Clone the complete project with `git clone https://github.com/ItzmeAkash/Healthy.ai` or you can just download the code and unzip it
- **Note:** The master branch doesn't have the updated code used for deployment, to download the updated code used for deployment you can use the following command
  ```
  ❯ git clone -b deploy https://github.com/ItzmeAkash/Healthy.ai/
  ```
- `deploy` branch has only the code required for deploying the app (rest of the code that was used for training the models, data preparation can be accessed on `master` branch)
- It is highly recommended to clone the deploy branch for running the project locally (the further steps apply only if you have the deploy branch cloned)
- Once the project is cloned, open anaconda prompt in the directory where the project was cloned and paste the following block

```bash
# To Create the environment
conda create -n healthyai python=3.10.13 -y
```
```bash
# To activate the environment
conda activate healthyai
```

```bash
# To install all the requirements
pip install -r requirements.txt
```

```bash
- And finally run the project with
# Finally run the following command
python main.py
```

- Open the localhost url provided after running `app.py` and now you can use the project locally in your web browser.


### MLflow
- MFlow is capable of monitoring models to determine which one achieves high accuracy by leveraging different parameters. Moreover, it can compare all the models and choose the most suitable one

```bash
# cmd
mlflow ui
```


### DVC Cmd
- DVC assists in executing pipelines more efficiently by allowing us to skip already executed pipelines. This speeds up the overall execution process, enabling us to reach our model as quickly as possible

```bash
# cmd
1. dvc init
2. dvc repo
3. dvc dag
```


## Further Improvements 📈
Ongoing Project Enhancements 📈

- Consider building the frontend with React.js for improved user interface
- Explore the creation of RESTful APIs using Django Rest Framework



## License 📝
This project is licensed under [GNU (GENERAL PUBLIC LICENSE)](https://github.com/ItzmeAkash/Healthy.ai/blob/main/LICENSE).

## Contact 📞

#### If you have any doubt or want to contribute feel free to email me or hit me up on [LinkedIn](www.linkedin.com/in/itzmeakash)
