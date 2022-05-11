import pandas as pd 
import numpy as np
import joblib
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.calibration import CalibratedClassifierCV
from joblib import dump

#training on offensive tweets dataset
df = pd.read_csv(dataset_path,index_col='Unnamed: 0')

#data cleaning
df['profane'] = df['class'].map(lambda x: True if(x<2) else False)

def preprocessing(x):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",x).split())

df['clean_tweets'] = df['tweet'].map(preprocessing)

texts = df["clean_tweets"].astype(str)
y = df["profane"]

#vectorizer instance
vectorizer = TfidfVectorizer(stop_words="english", min_df=0.0001)
X = vectorizer.fit_transform(texts)

#svm model instance 
model = LinearSVC(class_weight="balanced", dual=False, tol=1e-2, max_iter=1e5)
cclf = CalibratedClassifierCV(base_estimator=model)
cclf.fit(X, y)

dump(vectorizer, "./vectorizer.joblib")
dump(cclf, "./model.joblib")


