# Mengimpor library
import pandas as pd
import streamlit as st
import pickle

# Menghilangkan warning
import warnings
warnings.filterwarnings("ignore")

# Menulis judul
st.markdown("<h1 style='text-align: center; '> Model HPH Level</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; '>Indonesia Power</h1>", unsafe_allow_html=True)

# Pilihan utama
pilihan = st.sidebar.selectbox('Apa yang ingin Anda lakukan?', ('Prediksi HPH 1', 'Prediksi HPH 2', 'Prediksi HPH 3'))
#pilihan = st.selectbox('Apa yang ingin Anda lakukan?',['Prediksi HPH 1', 'Prediksi HPH 2', 'Prediksi HPH 3'])

if pilihan == 'Prediksi HPH 1':

    st.markdown('---'*10)

    st.markdown("<h3 style='text-align: center; '>HPH #1</h3>", unsafe_allow_html=True)
        
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            ngmp = st.number_input('NET GENERATOR MEASURED POWER', value=192.75)
        with col2:
            ttd = st.number_input('TTD HPH #1', value=0.34)
        with col3:
           dca = st.number_input('DCA HPH #1', value=4.71)
        
        
    data1 = {
        'NET GENERATOR MEASURED POWER': ngmp,
        'TTD HPH #1': ttd,
        'DCA HPH #1': dca,
        }
        
    kolom = list(data1.keys())
        
    df_final = pd.DataFrame([data1.values()],columns=kolom)
        
    # load model
    my_model1 = pickle.load(open('model_regresi_hph_level_new.pkl', 'rb'))
        
    # Predict
    result = round(float(my_model1.predict(df_final)),2)
        
    st.write('<center><b><h4>HPH #1 Level= ', str(result),'</b></h4>', unsafe_allow_html=True)

    st.markdown('---'*10)

elif pilihan == 'Prediksi HPH 2':
    
    st.markdown('---'*10)
    
    st.markdown("<h3 style='text-align: center; '>HPH #2</h3>", unsafe_allow_html=True)
        
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            gmp = st.number_input('GENERATOR MEASURED POWER', value=192.75)
        with col2:
            ttd = st.number_input('TTD HPH #2', value=0.34)
        with col3:
           dca = st.number_input('DCA HPH #2', value=4.71)
        
        
    data2 = {
        'GENERATOR MEASURED POWER': gmp,
        'TTD HPH #2': ttd,
        'DCA HPH #2': dca,
        }
        
    kolom2 = list(data2.keys())
        
    df_final2 = pd.DataFrame([data2.values()],columns=kolom2)
        
    # load model
    my_model2 = pickle.load(open('model_regresi_hph_level2_new.pkl', 'rb'))
        
    # Predict
    result2 = round(float(my_model2.predict(df_final2)),2)
        
    st.write('<center><b><h4>HPH #2 Level= ', str(result2),'</b></h4>', unsafe_allow_html=True)

    st.markdown('---'*10)

else:
    st.markdown('---'*10)
    
    st.markdown("<h3 style='text-align: center; '>HPH #3</h3>", unsafe_allow_html=True)
        
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            gmp = st.number_input('GENERATOR MEASURED POWER', value=192.75)
        with col2:
            ttd = st.number_input('TTD HPH #3', value=0.34)
        with col3:
           dca = st.number_input('DCA HPH #3', value=4.71)
        
        
    data3 = {
        'GENERATOR MEASURED POWER': gmp,
        'TTD HPH #3': ttd,
        'DCA HPH #3': dca,
        }
        
    kolom3 = list(data3.keys())
        
    df_final3 = pd.DataFrame([data3.values()],columns=kolom3)
        
    # load model
    my_model3 = pickle.load(open('model_regresi_hph_level3_new.pkl', 'rb'))
        
    # Predict
    result3 = round(float(my_model3.predict(df_final3)),2)
        
    st.write('<center><b><h4>HPH #2 Level= ', str(result3),'</b></h4>', unsafe_allow_html=True)

    st.markdown('---'*10)

