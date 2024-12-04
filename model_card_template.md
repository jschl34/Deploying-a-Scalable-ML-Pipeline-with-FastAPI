# Model Card
For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Model type is RandomForestClassifier
Framework is scikit-learn
Developed using Python 3.10 and scikit-learn 1.5.1
The sample split=25

## Intended Use
The model is designed to predict whether an individaul's income is greater than $50k in 1994 based on the Census Bureau data. 

## Training Data
The source of the data is UCI Census Income Dataset
The data can be found here: https://archive.ics.uci.edu/dataset/20/census+income.
The size of the dataset is 32,561 rows
Features:
    Categorical: workclass, education, marital-status, occupation, relationship, race, sex, mative-country
    Continuous: age, fnlgt, education-num, capital-gain, capital-loss, hours-per-week
Data split:
    Training - 80% approximately 26,049 rows
    Test - 20% approximately 6,512 rows

## Evaluation Data
The source of the data is the same as the training data.
The size of the dataset is 6,512.
The categorical and continuous feature processed consistently with training data.

## Metrics
Precison: 0.7905 - meaning that nearly 8 out of 10 predictions for >50k are correct.
Recall: 0.6339 - indicates the model identifies about 6 out of 10 high-income individuals.
F1: 0.7035 - This shows a moderate balance between precision and recall. 

## Ethical Considerations
The dataset has serveral imblances: 
sex: male constituting 66.92% and females 33.08%
race: white makes up 85% of the data, while other groups are underrepresented.
salary groups: 
    male make up 61.20% earning <=50K and 84.96% earning >50K
    females are underrepresented earning 38.80 <=50K and 15.04 earning >50K
This dataset may lead to biased predictions, as the model could perform better for one group over another.
Users should exercise caution and consider reblancing or adjusting the dataset.

## Caveats and Recommendations
Caveats
    Prediction are based on 1994 Census data, which may not relect current socioeconomic conditions.
Recommendations
    Retain the model with updated, balanced dataset before applying it to real-workd tasks.
    Evaluate model performance on underrepresented groups and address disparities if used in critical applications.
