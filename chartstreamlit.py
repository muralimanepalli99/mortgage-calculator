import streamlit as st
import pandas as pd
import numpy as np

st.write("# My cool Chart")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "C"]

)

st.bar_chart(chart_data)
st.line_chart(chart_data)
