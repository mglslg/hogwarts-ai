import time

import pandas as pd
import altair as alt
import numpy as np
import streamlit as st


def write_eg1():
    data_frame = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 60],
    })
    st.write(data_frame)


def write_eg2():
    data_frame = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 60],
    })
    st.write('1 + 1 = ', 2)
    st.write('Below is a DataFrame:', data_frame, 'Above is a dataframe.')


def write_eg3():
    df = pd.DataFrame(
        np.random.randn(200, 3),
        columns=['a', 'b', 'c'])

    c = alt.Chart(df).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

    st.write(c)


def stream_data_eg():
    _LOREM_IPSUM = """
    Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
    nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    """

    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)

    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )

    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)


def fibonacci(n):
    temp1, temp2 = 0, 1
    total = 0
    while total < n:
        yield temp1
        time.sleep(0.02)
        temp3 = temp1 + temp2
        temp1 = temp2
        temp2 = temp3
        total += 1


def get_data_frame():
    df = pd.DataFrame(
        np.random.randn(200, 3),
        columns=['a', 'b', 'c'])
    return df


def line_chart_demo():
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.line_chart(chart_data)


def slider_demo():
    x = st.slider('x')  # 👈 this is a widget
    st.write(x, 'squared is', x * x)


def show_dataframe():
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.write(chart_data)


def progress_bar():
    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i + 1}')
        bar.progress(i + 1)
        time.sleep(0.1)


if __name__ == '__main__':
    # magic content below
    '''
    # This is my title
    ## First Step :smile:
    '''

    st.write('**Hello World!** :smile:')

    if st.button("write stream"):
        st.write_stream(stream_data_eg)

    if st.button("data frame"):
        st.dataframe(get_data_frame())

    if st.button("line chart"):
        line_chart_demo()

    if st.button("slider"):
        slider_demo()

    # 侧边栏
    add_select_box = st.sidebar.selectbox(
        'How would you like to be contacted?',
        ('Email', 'Home phone', 'Mobile phone')
    )

    # 在Streamlit应用中插入原始的HTML和CSS代码
    st.markdown("""
        <style>
        .css-1d391kg {
            width: 100px;
        }
        </style>
        """, unsafe_allow_html=True)
