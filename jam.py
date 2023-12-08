from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(page_title="DIY CRAFTS",page_icon=":tada:",layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>',  unsafe_allow_html=True)

local_css("style/style.css")

lottie_coding = "https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json"
img_contact_form = Image.open("images/yy.jpg")
img_github = Image.open("images/hh.jpg")

 

with st.container():
    st.subheader('Hi, I am JAMAICA I. VALDEZ')
    st.title('This Is My Webpage')
    st.write('This page is all about my business.')
    st.write('WHEN YOU BY A HANDMADE YOU SUPPORT A DREAM.')
    st.write('[Learn More >](https://www.facebook.com/profile.php?id=100094332801323)')

with st.container():
    st.write('---')
    left_column, right_column =st.columns(2)
    with left_column:
        st.header("What to know?")
        st.write("##")
        st.write(
            """
            I am currently studying at SNSU 
            under CEIT department with BSCpE 1B course. 
            """
        )
        
    st.write("[For more information >](https://www.youtube.com/watch?v=VqgUkExPvLY)")
with right_column:
    st_lottie(lottie_coding, height=300, key='coding')

with st.container():
    st.write("---")
    st.write("My product")
    st.write("##")
    image_column, text_column = st.columns((1,2))

with image_column:
    st.image(img_contact_form)

with text_column:
    st.subheader("DIY BOUQUET")
    st.write(
        """
        This bouquet cost 190 pesos, this handly made by me and my companion.
        """     
        )
    st.markdown("[watch the video...](https://www.facebook.com/permalink.php?story_fbid=pfbid036HpR6GGFDH5ujjsdTswfBvDMnWFti5YoQg9snrzuJNF87ah1F1fKbsgp7qv9Crwkl&id=61554510924778)")

with st.container():
    st.write("---")
    st.write("my product")
    st.write("##")
    image_column, text_column = st.columns((1,2))

with image_column:
    st.image(img_github)

with text_column:
    st.subheader("DECORATION")
    st.write(
        """
         The primary reason to opt for balloon decoration is the excitement it brings.
        """     
        )
    st.markdown("[watch the video...](https://www.facebook.com/61554510924778/posts/pfbid02eZTnW3T4svGRPmqgwbkfHdaG5aT57oMVUMQF7asUAWvR9HEwDbnoCDCABR3Dn6DPl/?app=fbl)")

with st.container():
    st.write("---")
    st.header('For ORDERS:')
    st.write("##")
    
    contact_form = """
    <form action="https://formsubmit.co/vjamaica314@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="your email" required>
     <textarea name="message" placeholder="your message  here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
