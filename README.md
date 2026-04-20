# 🎬 Movie Recommendation System

A simple yet powerful **content-based movie recommendation web app** built using Python and Streamlit.  
The system suggests movies similar to a user’s input based on **overview and genre similarity** using machine learning techniques.

---

## 🚀 Live Demo
*(Optional: Add your Streamlit Cloud link here once deployed)*  
`https://your-app-link.streamlit.app`

---

## 📌 Features

- 🎥 Recommend movies based on user input
- 🧠 Uses Machine Learning (Content-Based Filtering)
- ⚡ Fast and lightweight recommendation system
- 🖥️ Interactive web interface using Streamlit
- 📊 Simple and clean UI for easy usage

---

## 🧠 How It Works

The recommendation system follows these steps:

1. Loads movie dataset (title, overview, genres)
2. Combines features into a single text field
3. Converts text into numerical vectors using **CountVectorizer**
4. Computes similarity between movies using **Cosine Similarity**
5. Returns top 5 most similar movies based on input

---

## 🛠️ Tech Stack

- Python 🐍
- Pandas 📊
- Scikit-learn 🤖
- Streamlit 🌐

