import pandas as pd
import streamlit as st

# DEFINIR NOTAS

TONES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def generate_scale(tone, intervals):
    notes = TONES * 2
    start = notes.index(tone)
    end = start + len(intervals)
    scale = [notes[start]]
    for i in intervals:
        start += i
        scale.append(notes[start])
    return scale


def show_scale_page():
    st.write("# Generador de Escalas")

    SCALE_FORMULAS = {
        "Major": [2, 2, 1, 2, 2, 2, 1],
        "Minor": [2, 1, 2, 2, 1, 2, 2],
        "Harmonic Minor": [2, 1, 2, 2, 1, 3, 1],
        "Melodic Minor (Ascending)": [2, 1, 2, 2, 2, 2, 1],
        "Natural Minor": [2, 1, 2, 2, 1, 2, 2],
        "Dorian": [2, 1, 2, 2, 2, 1, 2],
        "Phrygian": [1, 2, 2, 2, 1, 2, 2],
        "Lydian": [2, 2, 2, 1, 2, 2, 1],
        "Mixolydian": [2, 2, 1, 2, 2, 1, 2],
        "Locrian": [1, 2, 2, 1, 2, 2, 2],
        "Major Pentatonic": [2, 2, 3, 2, 3],
        "Minor Pentatonic": [3, 2, 2, 3, 2],
        "Blues": [3, 2, 1, 1, 3, 2],
        "Diminished (H-W)": [1, 2, 1, 2, 1, 2, 1, 2],
        "Diminished (W-H)": [2, 1, 2, 1, 2, 1, 2, 1],
        "Whole Tone": [2, 2, 2, 2, 2, 2],
        "Augmented": [3, 1, 3, 1, 3, 1],
        "Double Harmonic": [1, 3, 1, 2, 1, 3, 1],
        "Neapolitan Minor": [1, 2, 2, 2, 1, 3, 1],
        "Neapolitan Major": [1, 2, 2, 2, 2, 2, 1],
        "Harmonic Major": [2, 2, 1, 2, 1, 3, 1],
        "Altered Scale": [1, 2, 1, 2, 2, 2, 2]
    }

    ADDITIONAL_SCALE_FORMULAS = {
        "Hungarian Gypsy": [2, 1, 3, 1, 1, 2, 2],
        "Persian": [1, 3, 1, 1, 2, 3, 1],
        "Arabian": [2, 2, 1, 1, 2, 2, 2],
        "Japanese": [1, 4, 2, 1, 4],
        "Enigmatic": [1, 3, 2, 2, 2, 1, 1],
        "Spanish 8 Tone": [1, 2, 1, 1, 1, 2, 2, 2],
        "Bebop Dominant": [2, 2, 1, 2, 2, 1, 1, 1],
        "Bebop Major": [2, 2, 1, 2, 1, 1, 2, 1],
        "Bebop Minor": [2, 1, 2, 2, 1, 1, 2, 1],
        "Dominant Pentatonic": [2, 2, 3, 3, 2],
        "Blues b5 Scale": [3, 2, 1, 1, 1, 2, 2],
        "Blues Scale": [3, 2, 1, 1, 1, 3, 1],
        "Major b6 Pentatonic": [2, 2, 3, 1, 4],
        "Minor Major Pentatonic": [3, 2, 2, 1, 4],
        "Harmonic Minor b6": [2, 1, 2, 2, 1, 2, 2],
        "Dorian b2": [1, 2, 2, 2, 1, 2, 2],
        "Lydian Augmented": [2, 2, 2, 2, 1, 2, 1],
        "Lydian b7": [2, 2, 2, 1, 2, 1, 2],
        "Mixolydian b13": [2, 2, 1, 2, 1, 2, 2],
        "Locrian Natural 2": [2, 1, 2, 1, 2, 2, 2],
        "Super Locrian": [1, 2, 1, 2, 2, 2, 2],
        "Hindu": [2, 2, 1, 2, 1, 2, 2],
        "Ionian Augmented": [2, 2, 2, 1, 2, 2, 1],
        "Dorian #4": [2, 1, 3, 1, 2, 2, 1]
    }

    escalas = list(SCALE_FORMULAS.keys()) + list(ADDITIONAL_SCALE_FORMULAS.keys())

    tone = st.sidebar.selectbox("Elige un tono", TONES)
    scale_type = st.sidebar.selectbox("Elige un tipo de escala", escalas)

    if scale_type in SCALE_FORMULAS:
        scale_formula = SCALE_FORMULAS[scale_type]
    else:
        scale_formula = ADDITIONAL_SCALE_FORMULAS[scale_type]

    scale = generate_scale(tone, scale_formula)
    scale_text = ", ".join(scale)
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(f"La escala {scale_type} de {tone} es:")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.markdown(f"<p style='font-size:24px;line-height:1.5;'><strong>{scale_text}</strong></p>", unsafe_allow_html=True)

...

if __name__ == "__main__":
    page = st.sidebar.selectbox("Elige una página", ["Progresiones modales", "Funcionalidad 2", "Generador de Escalas"])
    if page == "Progresiones modales":
        show_modal_chord_page()
    elif page == "Funcionalidad 2":
        pass
    elif page == "Generador de Escalas":
        show_scale_page()
