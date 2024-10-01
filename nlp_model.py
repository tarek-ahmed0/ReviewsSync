# Model Used Libraries
import spacy
from sklearn import svm
import pickle

# Setup Our Dictionary 
sentences = [
    "The shoes are super comfortable, definitely worth the price!",  
    "Amazing laptop, fast performance and sleek design!",  
    "The quality of the jacket exceeded my expectations, highly recommend!",  
    "Great camera! The picture quality is stunning, would buy again!",  
    "Very happy with this phone, excellent battery life and features!",  
    "The headphones stopped working after a week, really disappointing.",  
    "Horrible experience! The material feels cheap and flimsy.",  
    "Product arrived damaged, very poor packaging.",  
    "Not as advertised, the product broke within days.",  
    "The customer service was terrible, and the product didn’t match the description."
]

# Categorizing Sentences
class Categories :
    POSITIVE = 'Satisfied Customer'
    NEGATIVE = 'Un Satisfied Customer'

# Mapping Our Sentence Into Categories
sentences_list = [
    Categories.POSITIVE, Categories.POSITIVE, Categories.POSITIVE, 
    Categories.POSITIVE, Categories.POSITIVE, Categories.NEGATIVE, 
    Categories.NEGATIVE, Categories.NEGATIVE, Categories.NEGATIVE, 
    Categories.NEGATIVE
]

# Load NLP Model
nlp_model = spacy.load(r'en_core_web_md')

# Process Sentences 
dictionary = [ nlp_model(sen) for sen in sentences ]

# Dictionary Vetcors Extraction 
dict_vectors = [ proc_sen.vector for proc_sen in dictionary ]

# Machine Learning Classification Model 
clf_model = svm.SVC(kernel = 'linear')
clf_model.fit(dict_vectors, sentences_list)

# Model Evaluation Prediction
testing_reviews = ['highly recommended']
testing_doc = [ nlp_model(review) for review in testing_reviews ]
testing_vectors = [ proc_review.vector for proc_review in testing_doc ]

predicted_class = clf_model.predict(testing_vectors)
print(predicted_class)

# Model Saving
with open('semantic_model.pkl', 'wb') as saved_model :
    pickle.dump({'model': clf_model}, saved_model)