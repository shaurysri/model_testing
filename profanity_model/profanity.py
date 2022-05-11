from profanity.Profanity_check import profanity
import pandas as pd
import numpy as np


# problem in the library : 
# 1) no module named sklearn.joblib - changed to import joblib
# 2) no model sklearn.svm.classes 

text = 'Fuck you bitch!!'

model = profanity(text)

print(model.get_profanity())
