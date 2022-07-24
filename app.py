import streamlit as st

st.title('文字起こしアプリ')
st.caption('セイセイ')

with st.form(key='profile_form'):
    name = st.text_input('名前')
    adress = st.text_input('住所')

    submit_btn = st.form_submit_button('送信')
    submit_cancel = st.form_submit_button('キャンセル')

    if submit_btn:
        st.text(f'ようこそ!!! {adress}にお住まいの{name}さん')

