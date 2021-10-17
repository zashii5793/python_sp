import streamlit as st
import numpy as np
import pandas as pd

st.title('超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

#動的な表を作成したい場合
st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)

#static(静的)な表を作成したい場合
st.table(df.style.highlight_max(axis=0)

"""
# 章
## 節
### 項

'''python
import streamlit as st
import numpy as np
import pandas as pd
'''
"""