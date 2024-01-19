import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import os
import base64

np.set_printoptions(suppress=True)
st.set_page_config(page_title="Halal Logo Classifier")


model = tf.keras.models.load_model(r'C:\Users\VICTUS\Documents\barang\sem6\ftyp2\halal\code\THIRDTRY.h5', compile=False)
nonMalaysiaClass = {0: 'ARGENTINA', 1: 'AUSTRALIA', 2: 'AUSTRIA', 3: 'BANGLADESH', 4: 'BELGIUM', 5: 'BOSNIA & HERZEGOVINA', 6: 'BRAZIL', 7: 'BRUNEI', 8: 'CANADA', 9: 'CHILE', 10: 'CHINA', 11: 'CROATIA', 12: 'EGYPT', 13: 'FRANCE', 14: 'GERMANY', 15: 'INDIA', 16: 'INDONESIA', 17: 'IRAN', 18: 'IRELAND', 19: 'ITALY', 20: 'JAPAN', 21: 'KAZAKHSTAN', 22: 'KENYA', 23: 'LITHUANIA', 24: 'MALDIVES', 25: 'MOROCCO', 26: 'NETHERLANDS & HOLLAND', 27: 'NEW ZEALAND', 28: 'PAKISTAN', 29: 'PHILIPPINES', 30: 'POLAND', 31: 'PORTUGAL', 32: 'SINGAPORE', 33: 'SOUTH AFRICA', 34: 'SOUTH KOREA', 35: 'SPAIN', 36: 'SRI LANKA', 37: 'SWITZERLAND', 38: 'TAIWAN', 39: 'THAILAND', 40: 'TUNISIA', 41: 'TURKEY', 42: 'UKRAINE', 43: 'UNITED KINGDOM', 44: 'UNITED STATES OF AMERICA', 45: 'VIETNAM'}




def run():
    img1 = Image.open(r'C:\Users\VICTUS\Documents\barang\sem6\ftyp2\halal\code\gambar untuk ui\logoterbaru.png')
    img1 = img1.resize((50, 50))

    img_style = """
    <style>
        .centered-image {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .centered-image img {
            max-width: 25%;
            max-height: 25%;
        }
        .centered-title {
            display: flex;
            justify-content: center;
            align-items: center;
        }
    </style>
    """
    st.markdown(img_style, unsafe_allow_html=True)
    with open(r'C:\Users\VICTUS\Documents\barang\sem6\ftyp2\halal\code\gambar untuk ui\logobaru.png', "rb") as image_file:
        img_data = base64.b64encode(image_file.read()).decode("utf-8")

    st.markdown('<div class="centered-image">' + f'<img src="data:image/png;base64,{img_data}">' + '</div>', unsafe_allow_html=True)
    st.markdown('''<h1 style='text-align: center; color: #000000;'>WEB-BASED HALAL LOGO DETECTION SYSTEM</h4>''',unsafe_allow_html=True)


    option = st.sidebar.selectbox("", ["Choose", "Malaysia Halal Logo", "Foreign Halal Logo"], index=0)

    if option != "Select an option":
        if option == "Malaysia Halal Logo":
            st.markdown('''<h4 style='text-align: left; color: green;'>This option will help users to determine if the Malaysian halal logo they uploaded is genuine or fake.</h4>''',unsafe_allow_html=True)
            tepi = Image.open(r"C:\Users\VICTUS\Documents\barang\sem6\ftyp2\halal\code\gambar untuk ui\MalaysiahalallogoSide.png")
            st.sidebar.image(tepi, caption="", use_column_width=True)
            st.sidebar.write("Example of the Malaysia Halal Logo, if the logo does not look like this, choose the Overseas option ", use_column_width=False)

            model = tf.keras.models.load_model(r'C:\Users\VICTUS\Documents\barang\sem6\ftyp2\halal\code\yangBaru.h5', compile=False)
            #model = tf.keras.models.load_model(r'C:\Users\VICTUS\Documents\barang\sem6\ftyp2\halal\code\semua.h5', compile=False)
            #model = tf.keras.models.load_model(r'C:\Users\VICTUS\Documents\barang\sem6\ftyp2\halal\code\Documents\barang\sem6\ftyp2\halal\model teachebal machine\31.7\keras_model.h5', compile=False)
            img_file = st.file_uploader("Upload an Image of Malaysia Halal Logo", type=["jpg", "png", "jpeg"])

            if img_file is not None:

                image = Image.open(img_file).convert("RGB")
                size = (224, 224)
                image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
                st.image(image, caption="Uploaded Image after resizing process", use_column_width=True)

                save_image_path = './upload_images/' + img_file.name
                os.makedirs(os.path.dirname(save_image_path), exist_ok=True)
                with open(save_image_path, "wb") as f:
                    f.write(img_file.getbuffer())

                if st.button("SUBMIT"):
                    ind, scoreUploaded = getResult(img_file, model, image)
                    if(ind == 0):
                        resultLast = "Fake"
                        st.markdown(f'<h1 style="color: red;">{resultLast}</h1>', unsafe_allow_html=True)
                    elif(ind == 2):
                        resultLast = "Original"
                        st.markdown(f'<h1 style="color: green;">{resultLast}</h1>', unsafe_allow_html=True)
                    else:
                        resultLast = "Invalid Input"
                        st.markdown(f'<h1 style="color: red;">{resultLast}</h1>', unsafe_allow_html=True)
                        red_subheader = "<h3 style='color: red;'>The image you uploaded does not contain any halal logo</h3>"
                        st.markdown(red_subheader, unsafe_allow_html=True)

                    #st.subheader("The confident score is: {:.2f}".format(scoreUploaded))
                    if resultLast == "Fake":
                        penerangan = Image.open(r"C:\Users\VICTUS\Documents\barang\sem6\ftyp2\halal\code\gambar untuk ui\resultFake.png")
                        st.image(penerangan, caption="The logo you uploaded is fake because it does not have these 7 features as shown in the above image.", use_column_width=True)
        elif option == "Foreign Halal Logo":
            tepi = Image.open(r"C:\Users\VICTUS\Documents\barang\sem6\ftyp2\halal\code\gambar untuk ui\jakim.jpg")
            st.sidebar.image(tepi, caption="", use_column_width=True)
            st.sidebar.write("Jakim recognizes 46 countries' Halal certification bodies, resulting in 84 different Halal logos. This promotes global Halal trade and assures consumers of products' adherence to Islamic dietary laws. ", use_column_width=False)
            st.sidebar.markdown("[Consumers can access the PDF list of recognized certification bodies by clicking here](https://www.halal.gov.my/v4/ckfinder/userfiles/files/cb2/CB_LIST_FEBRUARY_5TH_2020.pdf)")


            st.markdown('''<h4 style='text-align: left; color: green;'>This option will help users to classify the country of origin for the uploaded halal logo.</h4>''',unsafe_allow_html=True)
            model = tf.keras.models.load_model(r'C:\Users\VICTUS\Documents\barang\sem6\ftyp2\halal\code\firstNonMalaysia.h5', compile=False)
            img_file = st.file_uploader("Upload an Image of Non Malaysia Halal Logo", type=["jpg", "png", "jpeg"])

            if img_file is not None:

                image = Image.open(img_file).convert("RGB")
                size = (224, 224)
                image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
                st.image(image, caption="Uploaded Image after resizing process", use_column_width=True)

                save_image_path = './upload_images/' + img_file.name
                os.makedirs(os.path.dirname(save_image_path), exist_ok=True)
                with open(save_image_path, "wb") as f:
                    f.write(img_file.getbuffer())

                if st.button("SUBMIT"):
                    ind, scoreUploaded = getResult(img_file, model, image)
                    jawapan = "The Origin of Uploaded halal Logo is " + nonMalaysiaClass[ind]
                    st.header(jawapan)
                    #st.subheader("The confident score is: {:.2f}".format(scoreUploaded))


def getResult(img_file, model, image):
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    index = np.argmax(prediction)
    confidence_score = prediction[0][index]

    return index, confidence_score;



run()
