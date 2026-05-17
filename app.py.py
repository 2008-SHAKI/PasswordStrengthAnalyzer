import streamlit as st
import re

st.title("🔐 Password Strength Analyzer")

password = st.text_input("Enter Password", type="password")

if st.button("Check Password"):

    strength = 0

    if len(password) >= 8:
        strength += 1

    if re.search(r"[A-Z]", password):
        strength += 1

    if re.search(r"[a-z]", password):
        strength += 1

    if re.search(r"[0-9]", password):
        strength += 1

    if re.search(r"[!@#$%^&*]", password):
        strength += 1

    if strength <= 2:
        st.error("🔴 Weak Password")

    elif strength <= 4:
        st.warning("🟡 Medium Password")

    else:
        st.success("🟢 Strong Password")