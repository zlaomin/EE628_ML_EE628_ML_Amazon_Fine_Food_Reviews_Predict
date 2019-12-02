# EE628_ML_Amazon_Fine_Food_Reviews_Predict

One Paragraph of project description goes here

## Introduction

This dataset consists of reivew of fine foods from amazon. Reviews include product and user information, ratings, and a plain text review. It also includes reviews from all other Amazon categories.

We will use the user information, reviews and etc to pridict the rating.
* [amazon-fine-food-reviews](https://www.kaggle.com/snap/amazon-fine-food-reviews)

### Methods

In this project, we will firstly introduced a RNN model written by Pytorch. And then, according to the result, we would decide if we need to add some BN layers, drop_out layers and some other LSTM cells to improve the model.

Secondly, we want to build a CNN model which can treat the words equally in a sentence when RNN model will ignore some important words information. Stopword is also an important way to improve the accuracy of model.

Finally, we will show our result of these two different methods--seq2seq and KNN.

### Dataset

* [Download Dataset](https://www.kaggle.com/snap/amazon-fine-food-reviews/download) - Dataset

Dataset files:
```
Data includes:
- Reviews from Oct 1999 - Oct 2012
- 568,454 reviews
- 256,059 users
- 74,258 products
- 260 users with > 50 reviews
```
* [Here is the training, validation and test data](https://drive.google.com/drive/folders/1CNXHHPrlgKYVqdQ3WUHy1uKAv7PazUOw)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Filesystem hierarchy

```
- Trend_chat: The Trend chart of our data produced by report.py
- test_result: output of all our experiment
- error_stopwords.py: it contained the frequency of stopwords in the failed simple.
  We are trying to use this to find out the relationshop between stopwords map and performence. 
- report.py: 
```
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
********




## License

This project is licensed under the MIT License

