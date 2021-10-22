import streamlit as st
import numpy as np
import pandas as pd

st.title('超入門')

st.write('DataFrame')

df = pd.DataFrame(
    np.random.read(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(df)

#動的な表を作成したい場合
st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)

#static(静的)な表を作成したい場合
st.table(df.style.highlight_max(axis=0)

