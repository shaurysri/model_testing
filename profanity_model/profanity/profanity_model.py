import joblib
path = './profanity/training'
class model:
	def __init__(self):
		self.vectorizer = joblib.load(path+'/vectorizer.joblib')
		self.model = joblib.load(path+'/model.joblib')
	
	def predict(self,text):
		self.text = self.vectorizer.transform(text)
		return self.model.predict(self.text)

	def predict_prob(self,text):
		self.text = self.vectorizer.transform(text)
		return self.model.predict_proba(self.text)