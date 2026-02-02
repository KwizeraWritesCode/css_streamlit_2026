# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 23:20:02 2026

@author: 240106051
"""

import streamlit as st

st.set_page_config(
    page_title="About Me",
    page_icon="👤",
    layout="wide"
)
# --- CENTERED HEADER ---
st.markdown(
    """
    <div style="text-align: center;">
        <h1>Kwizera Mpilonhle Rwarinda</h1>
        <h3>Computer Science | Machine Learning | Data Science</h3>
        <p>
            📍 Empangeni, KwaZulu-Natal <br>
            📧 Mpilorwar@gmail.com <br>
            📞 078 602 1304
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# --- PROFILE SUMMARY ---
st.header("Profile")
st.write(
    """
I am a Computer Science graduate and current MSc Computer Science student with strong
interests in **Machine Learning, Data Science, and High-Performance Computing**.
I have hands-on experience in technical support, Linux systems, web development,
and supporting academic research environments.
"""
)

# --- EDUCATION ---
st.header("Education")

st.markdown(
    """
**MSc in Computer Science (In Progress)**  
University of Zululand | 2025 – Present  
• Deep Learning  
• Research  

**BSc Honours in Computer Science**  
University of Zululand | 2024  
• Data Engineering  
• Machine Learning Research  

**Bachelor of IT – Business Systems**  
Rosebank College | 2019 – 2022  
• Databases  
• Information Systems Strategy  
"""
)

# --- EXPERIENCE ---
st.header("Work & Leadership Experience")

st.markdown(
    """
**Laboratory Technician Intern**  
University of Zululand | Aug 2025 – Present  
• Technical support for computer science laboratories  
• Hardware repair and software troubleshooting  
• Website management for Science departments  
• Asset management system development  
• High-Performance Computing (HPC) system setup  
• Linux support for students and repositories  

**Computer Literacy Tutor**  
University of Zululand | Mar 2024 – Nov 2024  
• Trained first-year students in computer usage  
• Microsoft Word, Excel, PowerPoint, and Access  
• Troubleshooting hardware and software issues  

**Floor Representative**  
Rage Distribution | Oct 2022 – Feb 2023  
• Customer support and account assistance  
• Inventory checks and system updates  
• Operational and team support  
"""
)

# --- SKILLS ---
st.header("Skills")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
**Technical Skills**
- Python
- SQL
- Data Analysis
- Machine Learning
- Data Science
- Linux
- IT Troubleshooting
"""
    )

with col2:
    st.markdown(
        """
**Languages**
- English (Very Proficient)
- IsiZulu (Native)

**Certifications**
- IBM Data Science & AI Certifications
- AWS Data Analytics Fundamentals
"""
    )

# --- REFERENCES ---
with st.expander("References"):
    st.markdown(
        """
**University of Zululand**
- Dr P. Tarwireyi – HOD Computer Science  
- Mr S. Fatyi – Senior Laboratory Technician  
- Mr N. Nene – Computer Literacy Lecturer  
- Mr NB Khumalo – IT Specialist  

**Rage Distribution**
- Mr Nkosi – Manager  
"""
    )

st.divider()
st.caption("© 2026 | Kwizera Mpilonhle Rwarinda")

# --- CV DOWNLOAD ---
st.download_button(
    label="📄 Download My CV",
    data=open("Mpilo CV.pdf", "rb"),
    file_name="Kwizera_Mpilonhle_Rwarinda_CV.pdf",
    mime="application/pdf"
)

