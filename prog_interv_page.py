import streamlit as st

def show_prog_interv_page():

    # Las tonalidades y sus correspondientes acordes
    acordes = {
        'C': ['C', 'Dm7', 'Em7', 'Fmaj7', 'G', 'Am7', 'Bm7(b5)'],
        'D': ['D', 'Em7', 'F#m7', 'Gmaj7', 'A', 'Bm7', 'C#m7(b5)'],
        'E': ['E', 'F#m7', 'G#m7', 'Amaj7', 'B', 'C#m7', 'D#m7(b5)'],
        'F': ['F', 'Gm7', 'Am7', 'Bbmaj7', 'C', 'Dm7', 'Em7(b5)'],
        'G': ['G', 'Am7', 'Bm7', 'Cmaj7', 'D', 'Em7', 'F#m7(b5)'],
        'A': ['A', 'Bm7', 'C#m7', 'Dmaj7', 'E', 'F#m7', 'G#m7(b5)'],
        'B': ['B', 'C#m7', 'D#m7', 'Emaj7', 'F#', 'G#m7', 'A#m7(b5)']
    }

    def generar_progresion(tonalidad, num_notas, intervalo_intra, intervalo_inter, tam_progr, resolver, tipo_resolucion):
        progresion = []

        indice_actual = 0
        tonica_primera_celula = 0 # variable para guardar la tónica del primer acorde
        for i in range(tam_progr):
            if i % num_notas == 0: # estamos en la tónica de una nueva célula
                tonica_primera_celula = indice_actual
            progresion.append(acordes[tonalidad][indice_actual])

            if i % num_notas != num_notas - 1: # si estamos dentro de una célula
                indice_actual += intervalo_intra
            else: # si estamos en el último acorde de una célula
                indice_actual = tonica_primera_celula + intervalo_inter
            indice_actual = indice_actual % 7

        if resolver:
            if tipo_resolucion == 'II-V':
                progresion[-2:] = [acordes[tonalidad][1], acordes[tonalidad][4]]
            else: # 'IV-V'
                progresion[-2:] = [acordes[tonalidad][3], acordes[tonalidad][4]]

        return progresion



    # Sidebar para los controles
    st.sidebar.text("Controles de progresión")

    tonalidad = st.sidebar.selectbox("Tonalidad", list(acordes.keys()), index=0)
    num_notas = st.sidebar.slider("Cantidad de notas en la célula", 1, 4, 2)
    intervalo_intra = st.sidebar.selectbox("Intervalo intracélula", ['Segunda', 'Tercera', 'Cuarta', 'Quinta', 'Sexta', 'Séptima'], index=1)
    intervalo_inter = st.sidebar.selectbox("Intervalo intercélula", ['Segunda', 'Tercera', 'Cuarta', 'Quinta', 'Sexta', 'Séptima'], index=1)
    tam_progr = st.sidebar.slider("Tamaño de la progresión", 1, 64, 8)
    tipo_resolucion = st.sidebar.selectbox('Tipo de resolución', ['No', 'II-V', 'IV-V'])

    # Convertir los intervalos seleccionados a enteros para la función generar_progresion
    intervalo_intra = ['Segunda', 'Tercera', 'Cuarta', 'Quinta', 'Sexta', 'Séptima'].index(intervalo_intra) + 1
    intervalo_inter = ['Segunda', 'Tercera', 'Cuarta', 'Quinta', 'Sexta', 'Séptima'].index(intervalo_inter) + 1

    resolver = tipo_resolucion != 'No'

    progresion = generar_progresion(tonalidad, num_notas, intervalo_intra, intervalo_inter, tam_progr, resolver, tipo_resolucion)

    font_size_slider = st.slider("Tamaño de fuente", 1, 7, 2)
    font_sizes = {1: 1, 2: 1.5, 3: 2, 4: 2.5, 5: 3, 6: 3.5, 7: 4}


    # Mostrar la progresión 
    font_size = font_sizes[font_size_slider]
    st.markdown(f'<h2 style="font-size:{font_size}em;"><b> ||: {" | ".join(progresion)} :|| </b></h2>', unsafe_allow_html=True)
