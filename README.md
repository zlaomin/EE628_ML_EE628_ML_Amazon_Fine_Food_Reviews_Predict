# EE628_ML_TeamProject_Toxic_Content_Detection

One Paragraph of project description goes here

## Introduction

In this project, we will predict wheather a question asked on Quora is sincere or not.
Some characteristics that can signify that a question is insincere:
* Has a non-neutral tone
* Is disparaging or inflammatory
* Isn't grounded in reality
* Uses sexual content
We will use Machine learning to achieve our goal.


### Methods

In this project, we will firstly introduced a RNN model written by Pytorch. And then, according to the result, we would decide if we need to add some BN layers, drop_out layers and some other LSTM cells to improve the model.

Secondly, we want to build a CNN model which can treat the words equally in a sentence when RNN model will ignore some important words information.

Finally, we will show our result of these two different methods.

### Dataset

* [Download Dataset](https://www.kaggle.com/c/quora-insincere-questions-classification/rules) - Dataset

Dataset files:
```
Train.csv 1.31m * 3
Test.csv 376 * 2
Sample_submission.csv
```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
pip3 install -r requirement.txt
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
git clone https://github.com/zlaomin/EE628_ML_TeamProject_toxic_content_detection.git
```


## Deployment

Add additional notes about how to deploy this on a live system


## Authors

* **Yuchen Zeng** [zlaoma](https://github.com/zlaomin)
* **Hanyi Zhang** [HanyiZhang](https://github.com/HanyiZhang)
* **Yarong Liu** [MidgeLiu](https://github.com/MidgeLiu)


## License

This project is licensed under the MIT License

