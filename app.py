import pandas as pd  # --- NEW CODE: add pandas to the imports ---
import streamlit as st

# --- NEW CODE: initialize empty data frame if not already present ---
if 'data_df' not in st.session_state:
    st.session_state['data_df'] = pd.DataFrame()
# --- END OF NEW CODE ---

st.set_page_config(page_title="BMI Rechner", page_icon=":material/monitor_weight:")

pg_home = st.Page("views/home.py", title="Home", icon=":material/home:", default=True)
pg_second = st.Page("views/calculator.py", title="BMI-Rechner", icon=":material/calculate:")

pg = st.navigation([pg_home, pg_second])
pg.run()
