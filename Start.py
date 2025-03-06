import streamlit as st
import pandas as pd

from utils.data_manager import DataManager

# initialize data manager and load persistent data
# data_manager = DataManager()  # for local use
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="db_bmld")  # switch drive 

# the session state key has to be bmi_df for the data to be loaded correctly
data_manager.load_app_data(
    session_state_key='bmi_df', 
    file_name='database.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
    )

st.title('BMI Rechner')

name = st.session_state.get('name')
st.markdown(f"✨ Hallo {name}! ✨")
st.markdown("🏃 Die Anwendung ermöglicht es Ihnen, Ihren BMI zu berechnen und im Zeitverlauf zu verfolgen 📊")
        
# Add some health advice
st.info("""Der BMI ist ein Screening-Tool, aber keine Diagnose für Körperfett oder Gesundheit. 
Bitte konsultieren Sie einen Arzt für eine vollständige Beurteilung.""")

st.write("Diese App wurde von Samuel Wehrli im Rahmen des Moduls 'BMLD Informatik 2' an der ZHAW entwickelt.")