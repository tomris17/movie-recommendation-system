# 🎬 Movie Recommendation System

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Library-Scikit_Learn-orange.svg)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Library-Pandas-yellow.svg)](https://pandas.pydata.org/)
[![Streamlit](https://img.shields.io/badge/App-Streamlit-red.svg)](https://streamlit.io/)

This repository contains a content-based movie recommendation system built using Python. By analyzing movie metadata (genres, keywords, cast, crew, and overviews), the system suggests similar movies tailored to user preferences.

---

## 📊 Project Overview
* **Objective:** Build an intelligent recommendation engine that suggests relevant movies based on textual metadata similarity.
* **Key Steps:**
  * Exploratory Data Analysis (EDA) and data merging across multiple relational datasets (credits and movies).
  * Feature extraction and text preprocessing (combining tags, overview, genres, and cast into a unified feature bag).
  * Vectorization using **TF-IDF** and computing similarity scores via **Cosine Similarity**.
  * Interactive web dashboard deployment via **Streamlit** for real-time movie recommendations.

---

## 🛠️ Tech Stack & Libraries
* **Python**
* **Pandas & NumPy** (Data Processing)
* **Scikit-Learn** (Cosine Similarity & TF-IDF Vectorizer)
* **Streamlit** (Interactive Recommendation Dashboard)

---

## 🚀 Getting Started & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/tomris17/movie-recommendation-system.git](https://github.com/tomris17/movie-recommendation-system.git)
   cd movie-recommendation-system
