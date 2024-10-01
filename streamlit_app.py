import streamlit as st
import pickle
import nlp_model
from PIL import Image

# Load Our ML Classification Model
with open('semantic_model.pkl', 'rb') as saved_model :
    ml_model_file = pickle.load(saved_model)
    clf_model = ml_model_file['model']

st.title('Review:orange[Sync] 💡')
st.markdown(':violet[ReviewIQ] :gray[is a user-friendly app that classifies product reviews as] :green[Positive] or :red[Negative] or :orange[Neutral] :gray[It helps businesses understand customer feedback quickly and allows shoppers to make informed decisions based on sentiment analysis.]')
st.divider()

user_review = st.text_input(':blue[We would love to hear your feedback on our products. What are your thoughts ?]')

if user_review:
    review_doc = nlp_model.nlp_model(user_review)  
    review_vector = review_doc.vector.reshape(1, -1)  
    predicted_class = clf_model.predict(review_vector)[0]  
    st.divider()
    pos_image  = Image.open(r"Signs\Positive Sign.png")
    neg_image  = Image.open(r"Signs\Negative Sign.png")

    if predicted_class == 'Satisfied Customer':
            st.image(pos_image, caption = 'Satisfied Customer')
    elif predicted_class == 'Un Satisfied Customer':
        st.image(neg_image, caption = 'Un Satisfied Customer')
