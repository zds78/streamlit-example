import streamlit as st
import pandas as pd
import numpy as np

st.sidebar.success("sl1...")

st.title('zds page 11111')


img_file = st.sidebar.file_uploader(label='Upload a file', type=['png', 'jpg'])
if img_file:
    bytes_data = img_file.getvalue()
    fl = open(img_file.name, 'wb')
    fl.write(bytes_data)
    fl.close()
    st.write('write file:', img_file.name)


