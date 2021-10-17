import streamlit as st
import numpy as np
import pandas as pd

st.title('超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [1, 2, 3, 4]
})


st.write(df)