# model testing

## emotion_detection  
```
              precision    recall  f1-score   support

       anger       0.01      0.40      0.01       110
     boredom       0.00      0.00      0.00       179
       empty       0.00      0.00      0.00       827
  enthusiasm       0.00      0.00      0.00       759
        fear       0.00      0.00      0.00         0
         fun       0.00      0.00      0.00      1776
   happiness       0.00      0.00      0.00      5209
        hate       0.00      0.00      0.00      1323
         joy       0.00      0.00      0.00         0
        love       0.38      0.09      0.14      3842
     neutral       0.00      0.00      0.00      8638
    painting       0.00      0.00      0.00         0
    patience       0.00      0.00      0.00         0
        rain       0.00      0.00      0.00         0
      relief       0.00      0.00      0.00      1526
     sadness       0.30      0.38      0.34      5165
    surprise       0.15      0.03      0.05      2187
       worry       0.00      0.00      0.00      8459

    accuracy                           0.06     40000
   macro avg       0.05      0.05      0.03     40000
weighted avg       0.08      0.06      0.06     40000

confusion matrix
[	   [  44,    0,    0,    0,   18,    0,    0,    0,   27,    0,    0, 0,    0,    0,    0,   21,    0,    0],
       [  60,    0,    0,    0,   20,    0,    0,    0,   43,    3, 0,    0,    0,    0,    0,   53,    0,    0],
       [ 276,    0,    0,    0,  111,    0,    0,    0,  314,   12, 0,    0,    0,    0,    0,  111,    3,    0],
       [ 106,    0,    0,    0,   55,    0,    0,    0,  521,   10, 0,    0,    0,    0,    0,   60,    7,    0],
       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 0,    0,    0,    0,    0,    0,    0,    0],
       [ 256,    0,    0,    0,   99,    0,    0,    0, 1222,   39, 0,    0,    0,    0,    0,  115,   45,    0],
       [ 420,    0,    0,    0,  185,    0,    0,    0, 4170,  119, 0,    0,    0,    0,    0,  234,   81,    0],
       [ 653,    0,    0,    0,  110,    0,    0,    0,  247,   10, 0,    0,    0,    0,    0,  296,    7,    0],
       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 0,    0,    0,    0,    0,    0,    0,    0],
       [ 324,    0,    0,    0,   90,    0,    0,    0, 2824,  341, 0,    0,    0,    0,    0,  208,   55,    0],
       [2284,    0,    0,    0, 1009,    0,    0,    0, 4400,  118, 0,    1,    1,    1,    0,  776,   48,    0],
       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 0,    0,    0,    0,    0,    0,    0,    0],
       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 0,    0,    0,    0,    0,    0,    0,    0],
       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 0,    0,    0,    0,    0,    0,    0,    0],
       [ 215,    0,    0,    0,   79,    0,    0,    0, 1032,   20, 0,    0,    0,    0,    0,  168,   12,    0],
       [1303,    0,    0,    0,  378,    0,    0,    0, 1414,   71, 0,    0,    0,    0,    0, 1965,   34,    0],
       [ 540,    0,    0,    0,  204,    0,    0,    0, 1070,   40, 0,    0,    0,    0,    0,  271,   62,    0],
       [2150,    0,    0,    0, 1068,    0,    0,    0, 2810,  109, 0,    0,    0,    0,    0, 2265,   57,    0]]
```

## RacismDetection 
colab notebook link : https://colab.research.google.com/drive/1qoedjMD6LdXyqL9YRN6MWG8YPSK-00jK?usp=sharing
```
              precision    recall  f1-score   support

           0       0.00      0.00      0.00         0
           1       1.00      0.47      0.64       945

    accuracy                           0.47       945
   macro avg       0.50      0.24      0.32       945
weighted avg       1.00      0.47      0.64       945

confusion matrix
[[  0   0]
 [497 448]]
```
## SexualHarrasment 
dataset link : https://www.kaggle.com/datasets/munkialbright/classified-tweets
### Model not performing well as it is predicting all as False. Since the dataset is unbalanced hence accuracy is high but performnace not good. 
```
with tokenization of sentences : 
           precision    recall  f1-score   support

       False       0.86      0.71      0.78     17256
        True       0.12      0.26      0.17      2678

    accuracy                           0.65     19934
   macro avg       0.49      0.48      0.47     19934
weighted avg       0.76      0.65      0.69     19934

confusion matrix
[[12166  5090]
 [ 1974   704]]

without tokenization of sentences : 
              precision    recall  f1-score   support

       False       0.87      1.00      0.93     17256
        True       0.00      0.00      0.00      2678

    accuracy                           0.87     19934
   macro avg       0.43      0.50      0.46     19934
weighted avg       0.75      0.87      0.80     19934

confusion matrix
[[17256     0]
 [ 2678     0]]

```

## profanity_model  
```
              precision    recall  f1-score   support

           0       0.86      0.57      0.68     30000
           1       0.51      0.83      0.63     16225

    accuracy                           0.66     46225
   macro avg       0.68      0.70      0.66     46225
weighted avg       0.74      0.66      0.66     46225

confusion matrix
[[16980, 13020],
 [ 2742, 13483]]
       
```
## SentimentAnalysis
link to the dataset : https://www.kaggle.com/datasets/kazanova/sentiment140
link to the notebook : https://www.kaggle.com/code/shaurysrivastava/notebook0c26169fc7
```
             precision    recall  f1-score   support

    negative       0.68      0.81      0.74     24949
    positive       0.76      0.62      0.68     25051

    accuracy                           0.71     50000
   macro avg       0.72      0.71      0.71     50000
weighted avg       0.72      0.71      0.71     50000

[[20135  4814]
 [ 9567 15484]]
```
## HATE_SPEECH
```
```
## PeersConflict
```
```
## TextualAbuse
```
```
## InsultDetection
```
```
## MoraleDetection  
```
```

