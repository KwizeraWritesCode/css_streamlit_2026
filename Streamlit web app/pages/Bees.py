# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 23:29:03 2026

@author: 240106051
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("🐝 Bee Swarming Detection Research Summary")

st.markdown("""
### 📌 Research Focus
This research investigated non-invasive honeybee swarming detection
using machine learning applied to bee audio signals.

Swarming is preceded by an increase in **drone bee activity**, which can be
identified acoustically. Instead of manual hive inspections, this study
evaluated whether audio features + ML classifiers can reliably
distinguish worker bees from drone bees.

### 🔍 Methodology
- Audio dataset: 11,700 samples (10,000 workers, 1,700 drones)
- Feature extraction:
  - MFCC
  - LPC
  - Spectral Centroid
  - ZCR
  - Spectral Contrast
  - AMM
  - Spectral Variability
- Machine Learning models:
  - Random Forest
  - Decision Tree
  - Logistic Regression
  - Bernoulli Naive Bayes
  - Gaussian Naive Bayes

### 🏆 Key Findings
- Random Forest, Decision Tree, and Gaussian Naive Bayes
  achieved **up to 100% accuracy** on several feature sets.
- LPC and MFCC-based features** were the most discriminative.
- A 15% drone threshold** can be used as an early indicator of swarming.

This confirms that audio-based ML systems are viable for real-time
bee swarm detection, enabling smarter and safer beekeeping.
""")

results = {
    "LPC (10 features)": {
        "Random Forest": {"Accuracy": 100, "Precision": 100, "Recall": 100, "F1": 100},
        "Decision Tree": {"Accuracy": 100, "Precision": 100, "Recall": 100, "F1": 100},
        "Logistic Regression": {"Accuracy": 99.74, "Precision": 99.85, "Recall": 99.12, "F1": 99.48},
        "Bernoulli NB": {"Accuracy": 99.91, "Precision": 93.70, "Recall": 98.78, "F1": 96.02},
        "Gaussian NB": {"Accuracy": 100, "Precision": 100, "Recall": 100, "F1": 100},
    },
    "MFCC + ZCR + Spectral Contrast + Centroid": {
        "Random Forest": {"Accuracy": 100, "Precision": 100, "Recall": 100, "F1": 100},
        "Decision Tree": {"Accuracy": 100, "Precision": 100, "Recall": 100, "F1": 100},
        "Logistic Regression": {"Accuracy": 100, "Precision": 100, "Recall": 100, "F1": 100},
        "Bernoulli NB": {"Accuracy": 99.36, "Precision": 97.77, "Recall": 99.63, "F1": 98.68},
        "Gaussian NB": {"Accuracy": 100, "Precision": 100, "Recall": 100, "F1": 100},
    },
    "Spectral Variability (1 feature)": {
        "Random Forest": {"Accuracy": 100, "Precision": 100, "Recall": 100, "F1": 100},
        "Decision Tree": {"Accuracy": 100, "Precision": 100, "Recall": 100, "F1": 100},
        "Logistic Regression": {"Accuracy": 85.47, "Precision": 42.74, "Recall": 50.00, "F1": 46.08},
        "Bernoulli NB": {"Accuracy": 85.47, "Precision": 42.74, "Recall": 50.00, "F1": 46.08},
        "Gaussian NB": {"Accuracy": 100, "Precision": 100, "Recall": 100, "F1": 100},
    }
}
st.title("📈 Model Classification Performance")

feature_set = st.selectbox(
    "Select Feature Set",
    list(results.keys())
)

model = st.selectbox(
    "Select Machine Learning Model",
    list(results[feature_set].keys())
)

metrics = results[feature_set][model]

df = pd.DataFrame(
    metrics.values(),
    index=metrics.keys(),
    columns=["Score (%)"]
)

st.subheader(f"Performance Metrics – {model}")
st.dataframe(df)

# ---- Dynamic Bar Chart ----
fig, ax = plt.subplots()
df.plot(kind="bar", ax=ax)
ax.set_ylim(0, 105)
ax.set_ylabel("Percentage (%)")
ax.set_title(f"{model} Performance using {feature_set}")
plt.xticks(rotation=0)

st.pyplot(fig)