# -*- coding: utf-8 -*-
"""NM Project

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wAIHmJTg8_zqFa8AsMpHA5wVBxlZo13t

**Upload the Dataset**
"""

from google.colab import files
import pandas as pd

# Upload the file
uploaded = files.upload()

# Load the dataset
df = pd.read_csv('competition_test_bodies.csv')


# Show the first few rows
df.head()

"""**Load the Dataset**"""

import pandas as pd

# Read the uploaded CSV file
df = pd.read_csv('competition_test_bodies.csv')

# Display the first few rows
print("📌 Preview of the dataset:")
print(df.head())

# Display the shape of the dataset
print("\n✅ Dataset shape:", df.shape)

# Display column names
print("\n🧾 Columns:", df.columns.tolist())

# Display data types and non-null counts
print("\n🔍 Dataset Info:")
df.info()

"""**Data Exploration**"""

# Check for missing values
print("❗ Missing Values:\n", df.isnull().sum())

# Check for duplicate entries
print("\n🔁 Duplicate Rows:", df.duplicated().sum())

# Check unique articleBody lengths
df['text_length'] = df['articleBody'].apply(len)
print("\n📝 Text Length Stats:")
print(df['text_length'].describe())

# Histogram of text lengths
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 5))
sns.histplot(df['text_length'], bins=30, kde=True)
plt.title('Distribution of Article Body Lengths')
plt.xlabel('Text Length (Characters)')
plt.ylabel('Frequency')
plt.show()

"""**Check for Missing Values and Duplicates**"""

# Check for missing values in each column
print("📋 Missing Values:")
print(df.isnull().sum())

# Check for duplicated rows
duplicate_count = df.duplicated().sum()
print(f"\n🔁 Number of duplicate rows: {duplicate_count}")

"""Visualize a Few Features"""

# Add a column for word count
df['word_count'] = df['articleBody'].apply(lambda x: len(str(x).split()))

# Plot histogram of word counts
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 5))
sns.histplot(df['word_count'], bins=30, kde=True)
plt.title('Distribution of Article Word Counts')
plt.xlabel('Word Count')
plt.ylabel('Frequency')
plt.show()

"""
 Identify Target and Features"""

import pandas as pd

df = pd.read_csv('/content/competition_test_bodies.csv')
print(df.columns)

"""**Convert Categorical Columns to Numerical**"""

from sklearn.feature_extraction.text import TfidfVectorizer

# Initialize TF-IDF Vectorizer
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)

# Convert text to numeric features
X_tfidf = vectorizer.fit_transform(df['articleBody'])

# View the shape of the result
print("TF-IDF Matrix shape:", X_tfidf.shape)

"""**One-Hot Encoding**"""

from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Sample news headlines (simplified for demo)
news_headlines = [
    "Fake news spreads fast",
    "Truth will prevail",
    "Detect fake reports",
    "Report the truth"
]

# Step 1: Build vocabulary of unique words
vocab = sorted(set(word.lower() for headline in news_headlines for word in headline.split()))
print("Vocabulary:", vocab)

# Step 2: Encode each headline as a sequence of one-hot vectors for each word
# For simplicity, we'll create one-hot vectors per word, then sum to get headline vector

# Map words to indices
word_to_index = {word: i for i, word in enumerate(vocab)}

# Create one-hot vectors for each headline
def one_hot_encode_headline(headline):
    one_hot_vector = np.zeros(len(vocab))
    for word in headline.lower().split():
        index = word_to_index[word]
        one_hot_vector[index] = 1  # Mark presence of word
    return one_hot_vector

# Encode all headlines
encoded_headlines = np.array([one_hot_encode_headline(headline) for headline in news_headlines])

print("\nOne-hot encoded vectors for headlines:\n", encoded_headlines)

"""**Feature Scaling**"""

from sklearn.preprocessing import MinMaxScaler, StandardScaler
import numpy as np

# Sample features extracted from news articles (e.g., word counts, sentiment score)
features = np.array([
    [10, 0.5],   # Article 1
    [200, -0.1], # Article 2
    [50, 0.0],   # Article 3
    [300, 0.9]   # Article 4
])

print("Original features:\n", features)

# Min-Max Scaling
min_max_scaler = MinMaxScaler()
features_minmax = min_max_scaler.fit_transform(features)
print("\nFeatures after Min-Max Scaling:\n", features_minmax)

# Standardization
standard_scaler = StandardScaler()
features_standard = standard_scaler.fit_transform(features)
print("\nFeatures after Standardization:\n", features_standard)

"""**Train-Test Split**"""

from sklearn.model_selection import train_test_split

# Sample data: headlines and labels (0 = real, 1 = fake)
headlines = [
    "Fake news spreads fast",
    "Truth will prevail",
    "Detect fake reports",
    "Report the truth"
]

labels = [1, 0, 1, 0]

# Split data: 75% train, 25% test
X_train, X_test, y_train, y_test = train_test_split(
    headlines, labels, test_size=0.25, random_state=42
)

print("Training data:", X_train)
print("Training labels:", y_train)
print("\nTesting data:", X_test)
print("Testing labels:", y_test)

"""**Model Building**"""

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Sample dataset: headlines + labels (0 = real, 1 = fake)
headlines = [
    "Fake news spreads fast",
    "Truth will prevail",
    "Detect fake reports",
    "Report the truth",
    "Breaking news: fake story",
    "Verified report confirms facts"
]

labels = [1, 0, 1, 0, 1, 0]

# Step 1: Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    headlines, labels, test_size=0.33, random_state=42
)

# Step 2: Convert text to numeric features (Bag of Words)
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Step 3: Train Logistic Regression model
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Step 4: Predict and evaluate
y_pred = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

""" **Evaluation**"""

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

# Assume y_test and y_pred from your model predictions

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

"""**Make Predictions from New Input**"""

# New headlines to predict
new_headlines = [
    "Fake story uncovered by researchers",
    "Official report confirms the truth",
    "Unbelievable fake news alert"
]

# Step 1: Convert new text data to numeric features using the same vectorizer
new_vec = vectorizer.transform(new_headlines)

# Step 2: Predict using the trained model
predictions = model.predict(new_vec)

# Step 3: Display predictions (0 = real, 1 = fake)
for headline, pred in zip(new_headlines, predictions):
    label = "Fake" if pred == 1 else "Real"
    print(f"Headline: '{headline}' -> Prediction: {label}")

"""**Convert to DataFrame and Encode**"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Sample data with headlines and labels as strings
data = {
    "headline": [
        "Fake news spreads fast",
        "Truth will prevail",
        "Detect fake reports",
        "Report the truth"
    ],
    "label": [
        "fake",
        "real",
        "fake",
        "real"
    ]
}

# Step 1: Create DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Step 2: Encode labels to numbers (fake=1, real=0)
label_encoder = LabelEncoder()
df['label_encoded'] = label_encoder.fit_transform(df['label'])

print("\nDataFrame after encoding labels:\n", df)

"""**Predict the Final Grade**"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Sample dataset
data = {
    'homework_score': [80, 90, 70, 85, 95],
    'exam_score': [75, 88, 65, 90, 92],
    'attendance': [90, 100, 85, 95, 100],
    'final_grade': [78, 92, 70, 88, 95]
}

df = pd.DataFrame(data)

# Features and target
X = df[['homework_score', 'exam_score', 'attendance']]
y = df['final_grade']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

print("Predicted final grades:", y_pred)
print("Actual final grades:", y_test.values)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

"""#  Deployment-Building an Interactive App"""

!pip install Gradio

import gradio as gr
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Sample training data
headlines = [
    "Fake news spreads fast",
    "Truth will prevail",
    "Detect fake reports",
    "Report the truth",
    "Breaking news: fake story",
    "Verified report confirms facts"
]
labels = [1, 0, 1, 0, 1, 0]

# Train model and vectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(headlines)
model = LogisticRegression()
model.fit(X, labels)

# Prediction function
def predict_fake_news(text):
    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]
    return "Fake News" if pred == 1 else "Real News"

# Build Gradio interface
iface = gr.Interface(
    fn=predict_fake_news,
    inputs=gr.Textbox(lines=2, placeholder="Enter a news headline here..."),
    outputs="text",
    title="Fake News Detection",
    description="Enter a news headline to check if it is real or fake."
)

# Launch the app
iface.launch()