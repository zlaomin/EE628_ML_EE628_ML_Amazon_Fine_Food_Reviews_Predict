# EE628_ML_Amazon_Fine_Food_Reviews_Predict

One Paragraph of project description goes here

## Introduction

This dataset consists of reivew of fine foods from amazon. Reviews include product and user information, ratings, and a plain text review. It also includes reviews from all other Amazon categories.

We will use the user information, reviews and etc to pridict the rating.
* [amazon-fine-food-reviews](https://www.kaggle.com/snap/amazon-fine-food-reviews)

### Methods

In this project, we will firstly introduced a RNN model written by Pytorch. And then, according to the result, we would decide if we need to add some BN layers, drop_out layers and some other LSTM cells to improve the model.

Secondly, we want to build a CNN model which can treat the words equally in a sentence when RNN model will ignore some important words information.

Finally, we will show our result of these two different methods.

### Dataset

* [Download Dataset](https://www.kaggle.com/snap/amazon-fine-food-reviews/download) - Dataset

Dataset files:
```
TData includes:
- Reviews from Oct 1999 - Oct 2012
- 568,454 reviews
- 256,059 users
- 74,258 products
- 260 users with > 50 reviews
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
********
## Acknowledgements

See this SQLite query for a quick sample of the dataset.

If you publish articles based on this dataset, please cite the following paper:

J. McAuley and J. Leskovec. [From amateurs to connoisseurs: modeling the evolution of user expertise through online reviews](http://i.stanford.edu/~julian/pdfs/www13.pdf). WWW, 2013.


## License

This project is licensed under the MIT License

