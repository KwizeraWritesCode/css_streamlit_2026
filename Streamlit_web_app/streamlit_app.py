# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 20:01:44 2026

@author: 240106051
"""

import streamlit as st

st.set_page_config(
    page_title="My Portfolio",
    page_icon="🐝",
    layout="wide"
)

col2 = st.columns([1])


with col2:
    st.markdown("""
    ### Kwizera Mpilonhle Rwarinda

    I am a **Computer Science Honours graduate and machine learning researcher**
    with a strong focus on **audio-based classification, bioacoustics, and
    intelligent decision-support systems**.

    My work explores how **machine learning can be applied to real-world
    ecological and health challenges**, including bee swarming detection
    and multimodal medical diagnosis.

    #### 🔬 What I Do
    - Machine Learning & Data Science
    - Audio Signal Processing (MFCC, LPC, Spectral Features)
    - Applied AI for Agriculture & Healthcare
    - Research-focused system development

    #### 🚀 Current Aspirations
    I aim to pursue **postgraduate research (MSc/PhD)** in Artificial Intelligence,
    focusing on **interpretable, real-time ML systems** that create measurable
    impact in sustainability, healthcare, and smart agriculture.
    """)

st.markdown(
    """
    <style>
    /* App background */
    .stApp {
        background-color: #0a1a2f;
        color: #f0f2f6;
    }

    /* Top header / toolbar */
    header[data-testid="stHeader"] {
        background-color: #0a1a2f;
    }

    /* Remove white divider under header */
    header[data-testid="stHeader"]::after {
        background: none;
    }

    /* Main block container */
    section.main > div {
        background-color: #0a1a2f;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #081427;
    }

    [data-testid="stSidebar"] * {
        color: #f0f2f6 !important;
    }

    /* Text */
    h1, h2, h3, p, li, span, label {
        color: #f0f2f6;
    }

    h1, h2, h3 {
        color: #ffd700;
    }

    </style>
    """,
    unsafe_allow_html=True
)



