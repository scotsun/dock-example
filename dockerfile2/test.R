require(xgboost)
library(ggplot2)
library(pROC)

data(agaricus.train, package='xgboost')
data(agaricus.test, package='xgboost')
train <- agaricus.train
test <- agaricus.test

dtrain <- xgb.DMatrix(data = train$data, label = train$label)
bst <- xgboost(data = dtrain, max.depth = 2, eta = 1, nthread = 2, nrounds = 2, objective = "binary:logistic", verbose = 2)
pred <- predict(bst, test$data)

rocobj <- roc(test$label, pred)
ggroc(rocobj)