import streamlit as st
import cv2
from webcam import webcam
from fer import FER
import matplotlib.pyplot as plt


st.title('Face Detection - Application')

captured_image = webcam()
if captured_image is None:
    st.write("Waiting for capture...")
else:
    st.write("Got your amazing face from the camera! :smile: :")
    st.image(captured_image)

    cap = captured_image.convert("RGB")
    cap.save('cam.jpg')

    read_img = plt.imread("cam.jpg")
    #
    detector = FER(mtcnn=True)
    emotion, score = detector.top_emotion(read_img)

    if emotion == "happy":
        st.title(f"What a day, for a wonderful SMILE!! :smile:")

    elif emotion == "sad":
        st.title(f"NEXT SAALA CUP NAMDE :disappointed:")

    elif emotion == 'angry':
        st.title("Indiranagar ka Gunda hum MAIN!! :angry:")

    elif emotion == 'neutral':
        st.title("..Seems very normal... :neutral:")

    elif emotion == "surprise":
        st.title("WHAT!! YOU HAVEN'T HEARD OF TUBER SIMULATOR??!? ")

