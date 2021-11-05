from pandas.io.formats import style
import streamlit as st
import numpy as np
import pandas as pd

st.title('超入門')

st.write('DataFrame')

df = pd.DataFrame(
    np.random.read(20, 3, 5),
    columns=['a', 'b', 'c']
)

st.line_chart(df)

st.area_chart(df)


st.write('test')

num = 0

try:
    print(f'計算結果：{10/num}')
except ZeroDivisionError as e:
    print(e)

https://www.youtube.com/watch?v=DkqGC8Jf6Mc

df = pd.read_csv('AAA')
    


#動的な表を作成したい場合
st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)

#static(静的)な表を作成したい場合
st.table(df.style.highlight_max(axis=0)

st.table(df.style.highlight_max(axis=0)

#フットサルのデータを作成する
#データ読込
#Pandas
#グラフ化
#Git

