# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 20:01:44 2026

@author: 240106051
"""

import streamlit as st

st.title("👤 About Me")

col1, col2 = st.columns([1, 3])

with col1:
    st.markdown(
        """
        <div style="
            width:180px;
            height:180px;
            border-radius:50%;
            background-color:#081427;
            border:4px solid #FFD700;
            display:flex;
            align-items:center;
            justify-content:center;
            font-size:64px;
            color:#FFD700;
            margin:auto;
        ">
            KM
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown("""
    ### Kwizera Mpilonhle Rwarinda

    I am a Computer Science Honours graduate and machine learning researcher
    with a strong focus on audio-based classification, bioacoustics, and
    applied artificial intelligence.

    #### 🔬 What I Do
    - Machine Learning & Data Science  
    - Audio Signal Processing (MFCC, LPC, Spectral Features)  
    - Intelligent systems for agriculture & healthcare  
    - Research-driven model evaluation and deployment  

    #### 🚀 Current Aspirations
    I aim to pursue postgraduate research (MSc/PhD) in Artificial Intelligence,
    focusing on **interpretable, real-time ML systems with measurable
    impact in sustainability, healthcare, and smart agriculture.
    """)



