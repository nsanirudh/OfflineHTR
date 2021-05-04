import streamlit as st
import easyocr
import pyttsx3
from PIL import Image
import cv2
import numpy as np


def display_text(bounds):
    text = []
    for x in bounds:
        t = x[1]
        text.append(t)
    text = ' '.join(text)
    return text


st.sidebar.title('Language Selection Menu')
st.sidebar.subheader('Select...')
src = st.sidebar.selectbox("From Language", ['English','Assamesse', 'Bihari','Bhojpuri', 'Bengali', 'Hindi', 'Maithili',
                                             'Marathi', 'Nagpuri', 'Tamil', 'Telugu', 'Urdu'])


helper = {'English':'en', 'Assamesse':'as', 'Bihari':'bh', 'Bhojpuri':'bho', 'Bengali':'bn', 'Hindi':'hi', 'Maithili':'mai',
          'Marathi':'mr','Nagpuri':'sck', 'Tamil':'ta', 'Telugu':'te', 'Urdu':'ur'}
# dst = helper[destination]
source = helper[src]


st.set_option('deprecation.showfileUploaderEncoding', False)
st.title('Megdap Offline Handwriting Recognition')
st.subheader('Optical Character Recognition using AI')
st.text('Select Language from the Sidebar.')

image_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg', 'JPG'])

if st.button("Convert"):

    if image_file is not None:
        img = Image.open(image_file)
        img = np.array(img)

        st.subheader('Image you Uploaded...')
        st.image(image_file, width=450)

        if src == 'English':
            st.text('Im trying to read english')
            with st.spinner('Extracting Text from given Image'):
                eng_reader = easyocr.Reader(['en'])
                detected_text = eng_reader.readtext(img)
            st.subheader('Extracted text is ...')
            text = display_text(detected_text)
            st.write(text)

        elif src == 'Assamese':
            with st.spinner('Extracting Text from given Image'):
                assamese_reader = easyocr.Reader(['as'])
                detected_text = assamese_reader.readtext(img)
            st.subheader('Extracted text is ...')
            text = display_text(detected_text)
            st.write(text)

        elif src == 'Bihari':
            with st.spinner('Extracting Text from given Image'):
                bihari_reader = easyocr.Reader(['bh'])
                detected_text = bihari_reader.readtext(img)
            st.subheader('Extracted text is ...')
            text = display_text(detected_text)
            print(text)
            st.write(text)

        elif src == 'Bhojpuri':
            with st.spinner('Extracting Text from given Image'):
                bhoj_reader = easyocr.Reader(['bho'])
                detected_text = bhoj_reader.readtext(img)
            st.subheader('Extracted text is ...')
            text = display_text(detected_text)
            print(text)
            st.write(text)

        elif src == 'Bengali':
            with st.spinner('Extracting Text from given Image'):
                bengali_reader = easyocr.Reader(['bn'])
                detected_text = bengali_reader.readtext(img)
            st.subheader('Extracted text is ...')
            text = display_text(detected_text)
            print(text)
            st.write(text)

        elif src == 'Hindi':
            with st.spinner('Extracting Text from given Image'):
                hindi_reader = easyocr.Reader(['hi'])
                detected_text = hindi_reader.readtext(img)
            st.subheader('Extracted text is ...')
            text = display_text(detected_text)
            print(text)
            st.write(text)

        elif src == 'Maithili':
            with st.spinner('Extracting Text from given Image'):
                mai_reader = easyocr.Reader(['mai'])
                detected_text = mai_reader.readtext(img)
            st.subheader('Extracted text is ...')
            text = display_text(detected_text)
            print(text)
            st.write(text)

        elif src == 'Marathi':
            with st.spinner('Extracting Text from given Image'):
                mar_reader = easyocr.Reader(['mr'])
                detected_text = mar_reader.readtext(img)
            st.subheader('Extracted text is ...')
            text = display_text(detected_text)
            print(text)
            st.write(text)

        elif src == 'Nagpuri':
            with st.spinner('Extracting Text from given Image'):
                nag_reader = easyocr.Reader(['sck'])
                detected_text = nag_reader.readtext(img)
            st.subheader('Extracted text is ...')
            text = display_text(detected_text)
            print(text)
            st.write(text)

        elif src == 'Tamil':
            with st.spinner('Extracting Text from given Image'):
                tamil_reader = easyocr.Reader(['ta'])
                detected_text = tamil_reader.readtext(img)
            st.subheader('Extracted text is ...')
            text = display_text(detected_text)
            print(text)
            st.write(text)

        elif src == 'Telugu':
            with st.spinner('Extracting Text from given Image'):
                tel_reader = easyocr.Reader(['te'])
                detected_text = tel_reader.readtext(img)
            st.subheader('Extracted text is ...')
            text = display_text(detected_text)
            print(text)
            st.write(text)

        elif src == 'Urdu':
            with st.spinner('Extracting Text from given Image'):
                urdu_reader = easyocr.Reader(['ur'])
                detected_text = urdu_reader.readtext(img)
            st.subheader('Extracted text is ...')
            text = display_text(detected_text)
            print(text)
            st.write(text)

        st.balloons()


    else:
        st.subheader('Image not found! Please Upload an Image.')