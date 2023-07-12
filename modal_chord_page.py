import pandas as pd
import streamlit as st

def load_data(modo):
    if modo == 'Jónico':
        data = pd.read_csv('jonico.csv')
    elif modo == 'Dórico':
        data = pd.read_csv('dorico.csv')
    elif modo == 'Frigio':
        data = pd.read_csv('frigio.csv')
    elif modo == 'Lidio':
        data = pd.read_csv('lidio.csv')
    elif modo == 'Mixolidio':
        data = pd.read_csv('mixolidio.csv')
    elif modo == 'Eólico':
        data = pd.read_csv('eolico.csv')

    # Eliminar los espacios al final de los strings en la columna 'Tono'
    data['Tono'] = data['Tono'].str.rstrip()
    return data

def show_modal_chord_page():
    
    st.write("# Progresiones modales")

    modes = ["Lidio", "Mixolidio", "Dórico", "Frigio", "Jónico", "Eólico"]
    tones = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]

    lidian_data = load_data('Lidio')
    dorian_data = load_data('Dórico')
    phrygian_data = load_data('Frigio')
    ionian_data = load_data('Jónico')
    aeolian_data = load_data('Eólico')
    myxolydian_data = load_data('Mixolidio')
    data_dict = {"Lidio": lidian_data, "Dórico": dorian_data, "Frigio": phrygian_data, "Jónico": ionian_data, "Eólico": aeolian_data, "Mixolidio": myxolydian_data}

    def get_row_by_tone(data, tone):
        return data.loc[data['Tono'] == tone]

    st.markdown("""

    1. **Elige un modo y un tono** en la barra lateral a la izquierda.
    2. **Explora** la información que se muestra sobre la progresión modal.
    3. **Diviértete** explorando y experimentando con diferentes combinaciones. 
    """, unsafe_allow_html=True)



    def present_info(data, tone):
        row = get_row_by_tone(data, tone)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"<h2 style='text-align: left; font-size: 16px; color: rgb(20, 150, 200);'>Nota seleccionada: {row['Tono'].values[0]}</h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: left; font-size: 16px;'>Acordes de tónica: {row['Tónica'].values[0]}</h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: left; font-size: 16px;'>Acordes de cadencia: {row['Cadencia'].values[0]}</h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: left; font-size: 16px;'>Acordes condicionales de cadencia: {row['Cadencia cond'].values[0]}</h2>", unsafe_allow_html=True)

        with col2:
            st.markdown(f"<h2 style='text-align: left; font-size: 16px;'>Acordes de enlace: {row['Enlaces'].values[0]}</h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: left; font-size: 16px; color:red;'>Acordes a evitar: {row['Evitar'].values[0]}</h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: left; font-size: 16px; color: rgb(0, 121, 121);'>Nota característica primaria: {row['Primaria'].values[0]}</h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: left; font-size: 16px; color: rgb(0, 121, 121);'>Nota característica secundaria: {row['Secundaria'].values[0]}</h2>", unsafe_allow_html=True)




    mode = st.sidebar.selectbox("Elige un modo", modes)
    tone = st.sidebar.selectbox("Elige un tono", tones)

    data = data_dict[mode]
    present_info(data, tone)

if __name__ == "__main__":
    show_modal_chord_page()
