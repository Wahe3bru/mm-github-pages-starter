---
title: ML Notes- Linear Models
last_modified_at: 2019-09-01
categories:
  - blog
tags:
  - python
  - notes
  - ML Notes
classes: wide
header:
  overlay_image: https://source.unsplash.com/collection/8544654/1024x720
excerpt: "Linear models make a prediction using a linear function of the input features"
---

Linear models make a prediction using a linear function of the input features
### Linear models for regression
The predicted response as a weighted sum of the input features.
The prediction is a line for a single feature, a plane for two features, and a hyperplane for higher dimensions.
There are strong assumptions, like the target variable is a linear combination of features.

For datasets with many features, linear models are very powerful. Especially if there are more features than training points.

There are many different linear models for regression. The difference lies in how the coefficients and intercept of the model is learned, and how model complexity can be controlled.
#### Linear regression (aka ordinary least squares)
Simplest linear model. finds the parameters _w_ and _b_ that minimizes the _least squared error_ between the predictions and the true target (y) on the training set.
Linear regression has no hyperparameters which is a benefit, but also has no way to control model complexity.
On higher dimension data, there is a greater chance of overfitting.
##### Code implementation
``` python
from sklearn.linear_model import LinearRegression
lr = LinearRegression().fit(X_train, t_train)
print("lr.coef_: {}".format(lr.coef_))
print("lr.intercept_: {}".format(lr.intercept_))
```
The `intercept_` is always a single float number while `coeff_` is a NumPy array with one entry per feature.
#### Ridge regression
Same as linear regression model, but the coefficients are also trained to fit an additional constraint.The magnitudes of the coefficients should be as small as possible, meaning that each feature should have as little effect as possible.
Uses L2 regularization; explicitly restricting the model to avoid overfitting.
###### Code implementation
``` python
from sklearn.linear_model import Ridge
ridge = Ridge(alpha=10).fit(X_train, y_train)
```

By tuning the `alpha` parameter, the model places importance on simplicity (near-zero coefficients) versus training set performance. Optimum `alpha` setting depends on the dataset. The less restriction, the closer the model resembles `LinearRegression`
#### Lasso regression
Also restricts the coefficients, but uses L1 regularization. This results in some features being _exactly zero_. This is a form of automatic feature selection, as having coefficients being zero means they have no influence on the dependant variable. Thereby making the model easier to interpret by revealing the most important features.
##### Code implementation
``` python
from sklearn,linear_model import Lasso
lasso = Lasso(alpha=0.01, max_iter=100000).fit(X_train, y_train)
print("Training set score: {:.2f}".format(lasso.score(X_train, y_train)))
print("Test set score: {:.2f}".format(lasso.score(X_test, y_test)))
print("Number of features used: {}".format(np.sum(lasso.coef_ != 0)))
```
### Linear models for classification
The formula is very similar to regression, but the prediction is threshold at 0. If the function is _smaller_ than 0 then the prediction is class -1; otherwise if it's _greater_ than 0 the prediction is class +1.

For Linear models for classification, the __decision boundry__ is a linear function of the input. It separates classes by a line, plane or hyperplane.

The two most common classifiers are _logistic regression_ and _linear support vector machines_
- `from sklearn.linear_model import LogisticRegression`
- `from sklearn.svm import LinearSVC`

by default both models apply L2 regularization. The `C` parameter determines the strength of regularization. The higher the values of `C` corresponds to _less_ regularization.

another aspect of `C`; lower values causes the algorithm to try to fit the _majority_ of data points, while a higher value places importance on each data point.

Similar to the regression models, it might seem restrictive in lower dimensions but are very powerful in higher dimensions.
### Linear models for multiclass classification
Many linear classification models are for binary classification only. A common approach to apply a  binary classification algorithm to a multiclass algorithm is the _one vs rest_ approach. In this approach, a binary model is learned for each class that tries to separate that class from all other classes. which results in as much binary models as there are features. The classifyer with the highest score on its single class "wins", and the class label is returned as the predictor.
### Strengths, Weakness and Parameters
#### Strengths
- Fast to predict and train.
- can scale to large datasets and work well in sparse data
- relatively easy to understand.

#### Weakness
- In lower dimensional spaces other models perform better generalizations.
- there are assumptions that need to be met for linear regression to predict successfully.
- - linear relationship
- - no multicollineararity
- - errors are homoscedascity
- - no correlation between features

#### Parameters
`alpha` for regression and `C` for LinearSVC and LogisticRegression. large values for `alpha` and small values for `C` mean simpler models. These parameters are usually searched for on a logarithmic scale (10,1,0.1,0.01, etc)
