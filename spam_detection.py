# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
import gradio as gr

# Load and preprocess the dataset
df = pd.read_csv(r'D:/Email_Spam_detection/email.csv')

# Rename columns for clarity
df.columns = ['label', 'message']  # Renaming 'Category' to 'label' and 'Message' to 'message'

# Encode labels: 'spam' = 1, 'ham' = 0
label_encoder = LabelEncoder()
df['label'] = label_encoder.fit_transform(df['label'])

# Split the dataset into training and testing sets (70% training, 30% testing)
X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.3, random_state=42)

# Convert text data into numerical data using TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words='english')
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

# Train the Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Define a prediction function
def predict_spam(message):
    # Preprocess and predict
    message_tfidf = tfidf.transform([message])  # Convert input text to TF-IDF vector
    prediction = model.predict(message_tfidf)   # Predict using the trained model
    return "Spam" if prediction[0] == 1 else "Ham"  # Return label

# Create the Gradio interface using updated syntax
interface = gr.Interface(
    fn=predict_spam,  # Function to call for prediction
    inputs=gr.Textbox(lines=2, placeholder="Enter your message here..."),  # Input text box
    outputs=gr.Textbox(),  # Output text box
    title="Spam Detection",
    description="Enter a message and the model will classify it as spam or not spam (ham)."
)

# Launch the interface
interface.launch()
