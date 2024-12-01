import streamlit as st
from io import StringIO
import os
import base64
# import speech_recognition as sr
# import text2audio as ta
from transformers import AutoTokenizer , AutoModelForSeq2SeqLM, pipeline
import readfiles


class translate():
    def __init__(self) -> None:
        t = '../model/tokenizers'
        m = '../model/model'
        self.tokenizer = AutoTokenizer.from_pretrained(t)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(m)

    def getres(self, sentence, src, dest):
        translator = pipeline('translation',model=self.model, tokenizer=self.tokenizer, src_lang=src,tgt_lang=dest,max_length = 2000)
        res = translator(sentence)[0]
        print(res)
        return res

def load_view():
    st.markdown("<h1 style='text-align: left; color: Black;'>Offline Translator</h1>", unsafe_allow_html=True)

    option_src = st.selectbox(
    'Select Languge you want to translate',
    ('Kannada', 'Hindi', 'Marati', 'Telugu', 'French', 'English'))

    iotype = st.radio(
        "Input Type",
    ('File', 'Text'))

    if iotype == 'File':
        uploaded_file = st.file_uploader("Choose a file")
        sentence = readfiles.readfile(uploaded_file)
        if sentence == False:
            st.write("Wrong input file or loading failed.")
    else:
        sentence = st.text_input(label='Enter Text')
    
    option_dest = st.selectbox(
    'Select Languge you want to translate to',
    ('Kannada', 'Hindi', 'Marati', 'Telugu', 'French', 'English'))

    
    lang_code = {
        'Kannada' : 'kan_Knda',
        
        'Hindi' : 'hin_Deva',
        'Marati' : 'mar_Deva',
        'Telugu' : 'tel_Telu',
        'French' : 'fra_Latn',
        'English' : 'eng_Latn'        
    }

    st.write("Convert Your File to Text [link](https://pdftotext.com/)")

    src = lang_code[option_src]
    dest = lang_code[option_dest]
    if st.button('Translate'):
        res = trans.getres(sentence,src,dest)
        res = res['translation_text']
        st.text_area(value=res, height=300, max_chars=None, key=None,label="Result")

trans = translate()