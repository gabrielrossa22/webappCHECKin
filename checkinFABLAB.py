#libraries
import streamlit as st
from PIL import Image
from io import BytesIO
import requests
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import qrcode
import base64


#from urllib.error import URLError
#DATA CHECK-IN
rD = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vTN00fNo-fKTaMHme6ed2fTMkmqvoCxUA_u1PmkL9bADZ-OXrVcTvmw4o3yrgRjGdP09vOd51Za2uPE/pub?gid=0&single=true&output=csv')
dataD = rD.content
dfD = pd.read_csv(BytesIO(dataD), index_col=0)
selecao = dfD['Aprovado']=='X'
df01 = dfD[selecao]
NregD = len(df01)

#Data LINKS
rD2 = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vQhjoG-Sgj_9A1n6PAbwuJ6saRnyw1DW-q6KwEi_i3KxGxXrWGVcTk_daQ_Zpq4RwP8LApufF7l0lVm/pub?gid=0&single=true&output=csv')
dataD2 = rD2.content
dfD2 = pd.read_csv(BytesIO(dataD2), index_col=0)
NregD2 = len(dfD2)

# eliminar as colunas com valores ausentes
summary = df01.dropna(subset=['Mensagem'], axis=0)['Mensagem']
# concatenar as palavras
all_summary = " ".join(s for s in summary)
# lista de stopword
stopwords = set(STOPWORDS)
stopwords.update(["de", "ao", "o", "nao", "para", "da", "meu", "em", "você", "ter", "um", "ou", "os", "ser", "só"])
# gerar uma wordcloud
wordcloud = WordCloud(stopwords=stopwords,
                      background_color="white",
                      width=1280, height=720).generate(all_summary)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('FabLabBackground.PNG')  
    

col1, col2, col3, col4 = st.columns((1, 1, 1, 1))
with col1:
    st.image('LOGO - FabLLab.JPG', width=150, output_format='auto')
with col2: 
    st.write(" ") 
with col3: 
    st.subheader("Como está sendo a sua experiência no FabLab?")
with col4: 
    st.image('AppsheetCheck-inQRCode.png', width=150, output_format='auto')    
    
#st.markdown("<h1 style='text-align: center; color: black;'>Como está sendo a sua experiência?</h1>", unsafe_allow_html=True)
#st.video("https://www.youtube.com/watch?v=IYJKM3ie9sE&list=PLMQP5Jy3lKrMVgnuGfCCldqOjo_lGksM4")

# mostrar a imagem final
#fig, ax = plt.subplots(figsize=(10,6))
#ax.imshow(wordcloud, interpolation='bilinear')
#ax.set_axis_off()
plt.imshow(wordcloud);
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
#st.pyplot()
wordcloud.to_file("Mensagens_dos_Visitantes.png")

st.video("https://www.youtube.com/watch?v=IYJKM3ie9sE&list=PLMQP5Jy3lKrMVgnuGfCCldqOjo_lGksM4")
with st.sidebar:
  st.sidebar.button('0')
  if st.sidebar.button(0):
    st.video(str(dfD2['link'][0])) 

st.pyplot() #Este método faz exibirt a nuvem de palavras
st.set_option('deprecation.showPyplotGlobalUse', False)
st.info(" Desenvolvido em Linguagem Python | Equipe FabLab/Programador: prof. Massaki de O. Igarashi")


