from .profanity_model import model

class profanity:
    def __init__(self,text):
        self.text = text
        self.SCORE_THRESHOLD = 0.70
        self.model = model()

    def profane_check(self,text):
        return self.model.predict(text)


    def profane_prob(self,text):
        return self.model.predict_prob(text)


    def get_profanity(self):
        results = {}
        results['is_profane'] = self.profane_check([self.text])[0]
        results['profane_score'] = self.profane_prob([self.text])[0][1]
        return results


#get_profanity("I don't give a dam. You fucking piece of shit")
