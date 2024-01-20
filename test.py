import streamlit as st
#import flag

#st.radio('Test flag icon :smile:', (flag.flag('BR'), flag.flag('US'), flag.flag('GBENG') ))


langugae_option = {
    'US': 'American English',
    'GB': 'British English',
    'BR': 'Português',
}

selected_language = st.radio('Language choice:', options=langugae_option)
st.write(f'Selected language: {langugae_option[selected_language]}')
