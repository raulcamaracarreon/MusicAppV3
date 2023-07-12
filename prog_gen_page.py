import streamlit as st
import random
import pandas as pd
import numpy as np

def show_prog_gen_page():

    st.title('Generador de Progresiones de Acordes para Armonía Funcional')
    st.markdown('''
        ¡Bienvenido!
        
        Este generador crea progresiones armónicas efectivas y atractivas con solo unos pocos clics. 

        1. Selecciona una tonalidad.
        2. Elige cuántos acordes deseas en tu progresión.
        3. Selecciona la complejidad de la progresión
        4. Agrega u oculta las progresiones con dominantes secundarios y con cadenas II-V-I que se generan a partir de tu progresión.
        5. Presiona 'Enter'

    ''')


    # Define un diccionario con los acordes y los movimientos fuertes asociados.

    acordes_naturales_c = {
        'C': ['Am', 'F'],
        'Dm': ['Bdim', 'G7'],
        'Em': ['C', 'Am'],
        'F': ['Dm', 'Bdim'],
        'G7': ['Em', 'C'],
        'Am': ['F', 'Dm'],
        'Bdim': ['G7', 'Em']
    }

    sustitutos_naturales_c = {
        'C': ['Am', 'F'],
        'Dm': ['Bdim', 'G7'],
        'Em': ['C', 'Am'],
        'F': ['Dm', 'Bdim'],
        'G7': ['Em', 'C', 'Am'],
        'Am': ['F', 'Dm'],
        'Bdim': ['G7', 'Em']
    }

    intercambio_modal_c = {
        'C': ['Am', 'F'],
        'Dm': ['Bdim', 'G7', 'Fm7', 'Abmaj7', 'Bbmaj7'],
        'Em': ['C', 'Am'],
        'F': ['Dm', 'Bdim'],
        'G7': ['Em', 'C', 'Am'],
        'Am': ['F', 'Dm'],
        'Bdim': ['G7', 'Em', 'Fm7', 'Abmaj7', 'Bbmaj7'],
        'Fm7' : ['C', 'Em'],
        'Abmaj7': ['C', 'Em'],
        'Bbmaj7' :  ['C', 'Em', 'Am']
    }

    sustitutos_tritonales_c = {
        'C': ['Am', 'F'],
        'Dm': ['Bdim', 'G7', 'Fm7', 'Abmaj7', 'Bbmaj7', 'Dbmaj7'],
        'Em': ['C', 'Am'],
        'F': ['Dm', 'Bdim'],
        'G7': ['Em', 'C', 'Am'],
        'Am': ['F', 'Dm'],
        'Bdim': ['G7', 'Em', 'Fm7', 'Abmaj7', 'Bbmaj7', 'Dbmaj7'],
        'Fm7' : ['C', 'Em'],
        'Abmaj7': ['C', 'Em'],
        'Bbmaj7' :  ['C', 'Em', 'Am'],
        'Dbmaj7': ['C','Em', 'Am']
    }

    acordes_naturales_d = {
        'D': ['Bm', 'G'],
        'Em': ['C#dim', 'A7'],
        'F#m': ['D', 'Bm'],
        'G': ['Em', 'C#dim'],
        'A7': ['F#m', 'D'],
        'Bm': ['G', 'Em'],
        'C#dim': ['A7', 'F#m'],
        'Gm7' : ['D', 'F#m'],
        'Bbmaj7': ['D', 'F#m'],
        'Cmaj7' :  ['D', 'F#m'],
        'Ebmaj7': ['D', 'F#m']
    }

    sustitutos_naturales_d = {
        'D': ['Bm', 'G'],
        'Em': ['C#dim', 'A7'],
        'F#m': ['D', 'Bm'],
        'G': ['Em', 'C#dim'],
        'A7': ['F#m', 'D', 'Bm'],
        'Bm': ['G', 'Em'],
        'C#dim': ['A7', 'F#m'],
        'Gm7' : ['D', 'F#m'],
        'Bbmaj7': ['D', 'F#m'],
        'Cmaj7' :  ['D', 'F#m', 'Bm'],
        'Ebmaj7': ['D', 'F#m', 'Bm']
    }

    intercambio_modal_d = {
        'D': ['Bm', 'G'],
        'Em': ['C#dim', 'A7', 'Gm7', 'Bbmaj7', 'Cmaj7'],
        'F#m': ['D', 'Bm'],
        'G': ['Em', 'C#dim'],
        'A7': ['F#m', 'D'],
        'Bm': ['G', 'Em'],
        'C#dim': ['A7', 'Gm7', 'Bbmaj7', 'Cmaj7', 'F#m'],
        'Gm7' : ['D', 'F#m'],
        'Bbmaj7': ['D', 'F#m'],
        'Cmaj7' :  ['D', 'F#m'],
        'Ebmaj7': ['D', 'F#m']
    }

    sustitutos_tritonales_d = {
        'D': ['Bm', 'G'],
        'Em': ['C#dim', 'A7', 'Gm7', 'Bbmaj7', 'Cmaj7', 'Ebmaj7'],
        'F#m': ['D', 'Bm'],
        'G': ['Em', 'C#dim'],
        'A7': ['F#m', 'D'],
        'Bm': ['G', 'Em'],
        'C#dim': ['A7', 'Gm7', 'Bbmaj7', 'Cmaj7', 'F#m', 'Ebmaj7'],
        'Gm7' : ['D', 'F#m'],
        'Bbmaj7': ['D', 'F#m'],
        'Cmaj7' :  ['D', 'F#m'],
        'Ebmaj7': ['D', 'F#m']
    }

    acordes_naturales_e = {
        'E': ['C#m', 'A'],
        'F#m': ['D#dim', 'B7'],
        'G#m': ['E', 'C#m'],
        'A': ['F#m', 'D#dim'],
        'B7': ['G#m', 'E'],
        'C#m': ['A', 'F#m'],
        'D#dim': ['B7', 'G#m'],
        'Am7' : ['E', 'G#m'],
        'Cmaj7': ['E', 'G#m'],
        'Dmaj7' :  ['E', 'G#m'],
        'Fmaj7': ['E', 'G#m']
    }

    sustitutos_naturales_e = {
        'E': ['C#m', 'A'],
        'F#m': ['D#dim', 'B7'],
        'G#m': ['E', 'C#m'],
        'A': ['F#m', 'D#dim'],
        'B7': ['G#m', 'E', 'C#m'],
        'C#m': ['A', 'F#m'],
        'D#dim': ['B7', 'G#m'],
        'D#dim': ['B7', 'G#m'],
        'Am7' : ['E', 'G#m'],
        'Cmaj7': ['E', 'G#m'],
        'Dmaj7' :  ['E', 'G#m', 'C#m'],
        'Fmaj7': ['E', 'G#m', 'C#m']
    }

    intercambio_modal_e = {
        'E': ['C#m', 'A'],
        'F#m': ['D#dim', 'B7', 'Am7', 'Cmaj7', 'Dmaj7'],
        'G#m': ['E', 'C#m'],
        'A': ['F#m', 'D#dim'],
        'B7': ['G#m', 'E', 'C#m'],
        'C#m': ['A', 'F#m'],
        'D#dim': ['B7', 'G#m'],
        'D#dim': ['B7', 'Am7', 'Cmaj7', 'Dmaj7', 'G#m'],
        'Am7' : ['E', 'G#m'],
        'Cmaj7': ['E', 'G#m'],
        'Dmaj7' :  ['E', 'G#m', 'C#m'],
        'Fmaj7': ['E', 'G#m', 'C#m']
    }

    sustitutos_tritonales_e = {
        'E': ['C#m', 'A'],
        'F#m': ['D#dim', 'B7', 'Am7', 'Cmaj7', 'Dmaj7', 'Fmaj7'],
        'G#m': ['E', 'C#m'],
        'A': ['F#m', 'D#dim'],
        'B7': ['G#m', 'E', 'C#m'],
        'C#m': ['A', 'F#m'],
        'D#dim': ['B7', 'G#m'],
        'D#dim': ['B7', 'Am7', 'Cmaj7', 'Dmaj7', 'G#m', 'Fmaj7'],
        'Am7' : ['E', 'G#m'],
        'Cmaj7': ['E', 'G#m'],
        'Dmaj7' :  ['E', 'G#m', 'C#m'],
        'Fmaj7': ['E', 'G#m', 'C#m']
    }

    acordes_naturales_f = {
        'F': ['Dm', 'Bb'],
        'Gm': ['Edim', 'C7'],
        'Am': ['F', 'Dm'],
        'Bb': ['Gm', 'Edim'],
        'C7': ['Am', 'F'],
        'Dm': ['Bb', 'Gm'],
        'Edim': ['C7', 'Am'],
        'Bbm7' : ['F', 'Am'],
        'Dbmaj7': ['F', 'Am'],
        'Ebmaj7' :  ['F', 'Am'],
        'Gbmaj7': ['F', 'Am']
    }

    sustitutos_naturales_f = {
        'F': ['Dm', 'Bb'],
        'Gm': ['Edim', 'C7'],
        'Am': ['F', 'Dm'],
        'Bb': ['Gm', 'Edim'],
        'C7': ['Am', 'F', 'Dm'],
        'Dm': ['Bb', 'Gm'],
        'Edim': ['C7', 'Am'],
        'Bbm7' : ['F', 'Am'],
        'Dbmaj7': ['F', 'Am'],
        'Ebmaj7' :  ['F', 'Am', 'Dm'],
        'Gbmaj7': ['F', 'Am', 'Dm']
    }

    intercambio_modal_f = {
        'F': ['Dm', 'Bb'],
        'Gm': ['Edim', 'C7', 'Bbm7', 'Dbmaj7', 'Ebmaj7'],
        'Am': ['F', 'Dm'],
        'Bb': ['Gm', 'Edim'],
        'C7': ['Am', 'F', 'Dm'],
        'Dm': ['Bb', 'Gm'],
        'Edim': ['C7', 'Am', 'Bbm7', 'Dbmaj7', 'Ebmaj7'],
        'Bbm7' : ['F', 'Am'],
        'Dbmaj7': ['F', 'Am'],
        'Ebmaj7' :  ['F', 'Am', 'Dm'],
        'Gbmaj7': ['F', 'Am', 'Dm']
    }

    sustitutos_tritonales_f = {
        'F': ['Dm', 'Bb'],
        'Gm': ['Edim', 'C7', 'Bbm7', 'Dbmaj7', 'Ebmaj7', 'Gbmaj7'],
        'Am': ['F', 'Dm'],
        'Bb': ['Gm', 'Edim'],
        'C7': ['Am', 'F', 'Dm'],
        'Dm': ['Bb', 'Gm'],
        'Edim': ['C7', 'Am', 'Bbm7', 'Dbmaj7', 'Ebmaj7','Gbmaj7'],
        'Bbm7' : ['F', 'Am'],
        'Dbmaj7': ['F', 'Am'],
        'Ebmaj7' :  ['F', 'Am', 'Dm'],
        'Gbmaj7': ['F', 'Am', 'Dm']
    }


    acordes_naturales_g = {
        'G': ['Em', 'C'],
        'Am': ['F#dim', 'D7'],
        'Bm': ['G', 'Em'],
        'C': ['Am', 'F#dim'],
        'D7': ['Bm', 'G'],
        'Em': ['C', 'Am'],
        'F#dim': ['D7', 'Bm'],
        'Cm7' : ['G', 'Bm'],
        'Ebmaj7': ['G', 'Bm'],
        'Fmaj7' :  ['G', 'Bm'],
        'Abmaj7': ['G', 'Bm']
    }

    sustitutos_naturales_g = {
        'G': ['Em', 'C'],
        'Am': ['F#dim', 'D7'],
        'Bm': ['G', 'Em'],
        'C': ['Am', 'F#dim'],
        'D7': ['Bm', 'G', 'Em'],
        'Em': ['C', 'Am'],
        'F#dim': ['D7', 'Bm'],
        'Cm7' : ['G', 'Bm'],
        'Ebmaj7': ['G', 'Bm'],
        'Fmaj7' :  ['G', 'Bm', 'Em'],
        'Abmaj7': ['G', 'Bm', 'Em']
    }

    intercambio_modal_g = {
        'G': ['Em', 'C'],
        'Am': ['F#dim', 'D7', 'Cm7', 'Ebmaj7', 'Fmaj7'],
        'Bm': ['G', 'Em'],
        'C': ['Am', 'F#dim'],
        'D7': ['Bm', 'G', 'Em'],
        'Em': ['C', 'Am'],
        'F#dim': ['D7', 'Bm', 'Cm7', 'Ebmaj7', 'Fmaj7'],
        'Cm7' : ['G', 'Bm'],
        'Ebmaj7': ['G', 'Bm'],
        'Fmaj7' :  ['G', 'Bm', 'Em'],
        'Abmaj7': ['G', 'Bm', 'Em']
    }

    sustitutos_tritonales_g = {
        'G': ['Em', 'C'],
        'Am': ['F#dim', 'D7', 'Cm7', 'Ebmaj7', 'Fmaj7', 'Abmaj7'],
        'Bm': ['G', 'Em'],
        'C': ['Am', 'F#dim'],
        'D7': ['Bm', 'G', 'Em'],
        'Em': ['C', 'Am'],
        'F#dim': ['D7', 'Bm', 'Cm7', 'Ebmaj7', 'Fmaj7','Abmaj7'],
        'Cm7' : ['G', 'Bm'],
        'Ebmaj7': ['G', 'Bm'],
        'Fmaj7' :  ['G', 'Bm', 'Em'],
        'Abmaj7': ['G', 'Bm', 'Em']
    }

    acordes_naturales_a = {
        'A': ['F#m', 'D'],
        'Bm': ['G#dim', 'E7'],
        'C#m': ['A', 'F#m'],
        'D': ['Bm', 'G#dim'],
        'E7': ['C#m', 'A'],
        'F#m': ['D', 'Bm'],
        'G#dim': ['E7', 'C#m'],
        'Dm7' : ['A', 'C#m'],
        'Fmaj7': ['A', 'C#m'],
        'Gmaj7' :  ['A', 'C#m'],
        'Bbmaj7': ['A', 'C#m']
    }

    sustitutos_naturales_a = {
        'A': ['F#m', 'D'],
        'Bm': ['G#dim', 'E7'],
        'C#m': ['A', 'F#m'],
        'D': ['Bm', 'G#dim'],
        'E7': ['C#m', 'A', 'F#m'],
        'F#m': ['D', 'Bm'],
        'G#dim': ['E7', 'C#m'],
        'Dm7' : ['A', 'C#m'],
        'Fmaj7': ['A', 'C#m'],
        'Gmaj7' :  ['A', 'C#m', 'F#m'],
        'Bbmaj7': ['A', 'C#m', 'F#m']
    }

    intercambio_modal_a = {
        'A': ['F#m', 'D'],
        'Bm': ['G#dim', 'E7', 'Dm7', 'Fmaj7', 'Gmaj7'],
        'C#m': ['A', 'F#m'],
        'D': ['Bm', 'G#dim'],
        'E7': ['C#m', 'A', 'F#m'],
        'F#m': ['D', 'Bm'],
        'G#dim': ['E7', 'C#m', 'Dm7', 'Fmaj7', 'Gmaj7'],
        'Dm7' : ['A', 'C#m'],
        'Fmaj7': ['A', 'C#m'],
        'Gmaj7' :  ['A', 'C#m', 'F#m'],
        'Bbmaj7': ['A', 'C#m', 'F#m']
    }

    sustitutos_tritonales_a = {
        'A': ['F#m', 'D'],
        'Bm': ['G#dim', 'E7', 'Dm7', 'Fmaj7', 'Gmaj7', 'Bbmaj7'],
        'C#m': ['A', 'F#m'],
        'D': ['Bm', 'G#dim'],
        'E7': ['C#m', 'A', 'F#m'],
        'F#m': ['D', 'Bm'],
        'G#dim': ['E7', 'C#m', 'Dm7', 'Fmaj7', 'Gmaj7','Bbmaj7'],
        'Dm7' : ['A', 'C#m'],
        'Fmaj7': ['A', 'C#m'],
        'Gmaj7' :  ['A', 'C#m', 'F#m'],
        'Bbmaj7': ['A', 'C#m', 'F#m']
    }

    acordes_naturales_b = {
        'B': ['G#m', 'E'],
        'C#m': ['A#dim'],
        'D#m': ['B', 'G#m'],
        'E': ['C#m', 'A#dim'],
        'F#7': ['D#m', 'B'],
        'G#m': ['E', 'C#m'],
        'A#dim': ['F#7', 'D#m'],
        'Em7' : ['B', 'D#m'],
        'Gmaj7': ['B', 'D#m'],
        'Amaj7' :  ['B', 'D#m', 'G#m'],
        'Cmaj7': ['B', 'D#m', 'G#m']
    }

    sustitutos_naturales_b = {
        'B': ['G#m', 'E'],
        'C#m': ['A#dim', 'F#7'],
        'D#m': ['B', 'G#m'],
        'E': ['C#m', 'A#dim'],
        'F#7': ['D#m', 'B', 'G#m'],
        'G#m': ['E', 'C#m'],
        'A#dim': ['F#7', 'D#m'],
        'Em7' : ['B', 'D#m'],
        'Gmaj7': ['B', 'D#m'],
        'Amaj7' :  ['B', 'D#m', 'G#m'],
        'Cmaj7': ['B', 'D#m', 'G#m']
    }

    intercambio_modal_b = {
        'B': ['G#m', 'E'],
        'C#m': ['A#dim', 'F#7', 'Em7', 'Gmaj7', 'Amaj7'],
        'D#m': ['B', 'G#m'],
        'E': ['C#m', 'A#dim'],
        'F#7': ['D#m', 'B', 'G#m'],
        'G#m': ['E', 'C#m'],
        'A#dim': ['F#7', 'D#m', 'Em7', 'Gmaj7', 'Amaj7'],
        'Em7' : ['B', 'D#m'],
        'Gmaj7': ['B', 'D#m'],
        'Amaj7' :  ['B', 'D#m', 'G#m'],
        'Cmaj7': ['B', 'D#m', 'G#m']
    }

    sustitutos_tritonales_b = {
        'B': ['G#m', 'E'],
        'C#m': ['A#dim', 'F#7', 'Em7', 'Gmaj7', 'Amaj7', 'Cmaj7'],
        'D#m': ['B', 'G#m'],
        'E': ['C#m', 'A#dim'],
        'F#7': ['D#m', 'B', 'G#m'],
        'G#m': ['E', 'C#m'],
        'A#dim': ['F#7', 'D#m', 'Em7', 'Gmaj7', 'Amaj7','Cmaj7'],
        'Em7' : ['B', 'D#m'],
        'Gmaj7': ['B', 'D#m'],
        'Amaj7' :  ['B', 'D#m', 'G#m'],
        'Cmaj7': ['B', 'D#m', 'G#m']
    }


    # Define un diccionario con las tonalidades y sus respectivos diccionarios de acordes.
    tonalidades_naturales = {
        'C': acordes_naturales_c,
        'D': acordes_naturales_d,
        'E': acordes_naturales_e,
        'F': acordes_naturales_f,
        'G': acordes_naturales_g,
        'A': acordes_naturales_a,
        'B': acordes_naturales_b,
    }

    tonalidades_sustitutos_naturales = {
        'C': sustitutos_naturales_c,
        'D': sustitutos_naturales_d,
        'E': sustitutos_naturales_e,
        'F': sustitutos_naturales_f,
        'G': sustitutos_naturales_g,
        'A': sustitutos_naturales_a,
        'B': sustitutos_naturales_b,
    }


    tonalidades_intercambio_modal = {
        'C': intercambio_modal_c,
        'D': intercambio_modal_d,
        'E': intercambio_modal_e,
        'F': intercambio_modal_f,
        'G': intercambio_modal_g,
        'A': intercambio_modal_a,
        'B': intercambio_modal_b,
    }

    tonalidades_sustitutos_tritonales = {
        'C': sustitutos_tritonales_c,
        'D': sustitutos_tritonales_d,
        'E': sustitutos_tritonales_e,
        'F': sustitutos_tritonales_f,
        'G': sustitutos_tritonales_g,
        'A': sustitutos_tritonales_a,
        'B': sustitutos_tritonales_b,
    }


    # Define un diccionario con las tonalidades y sus quintos grados asociados.
    quinto_grado = {
        'A': 'E7',
        'A7': 'E7',
        'Ab': 'Eb7',
        'Abmaj7':'Eb7',
        'Ab7': 'Eb7',
        'Abm': 'Eb7',
        'Abm7': 'Eb7',
        'Am': 'E7',
        'Am7': 'E7',
        'B': 'E#(F)7',
        'B7': 'F#7',
        'Bb': 'F7',
        'Bbmaj7': 'F7',
        'Bb7': 'F7',
        'Bbm': 'F7',
        'Bbm7': 'F7',
        'Bm': 'F#7',
        'Bm7': 'F#7',
        'C': 'G7',
        'Cmaj7': 'G7',
        'C7': 'G7',
        'Cb': 'Gb7',
        'Cbmaj7': 'Gb7',
        'Cb7': 'Gb7',
        'Cbm': 'Gb7',
        'Cbm7': 'Gb7',
        'Cm': 'G7',
        'Cm7': 'G7',
        'C#': 'G#7',
        'C#7': 'G#7',
        'C#m': 'G#7',
        'C#m7': 'G#7',
        'D': 'A7',
        'D7': 'A7',
        'Db': 'Ab7',
        'Dbmaj7': 'Ab7',
        'Db7': 'Ab7',
        'Dbm': 'Ab7',
        'Dbm7': 'Ab7',
        'Dm': 'A7',
        'Dm7': 'A7',
        'D#': 'A#7',
        'D#7': 'A#7',
        'D#m': 'A#7',
        'D#m7': 'A#7',
        'E': 'B7',
        'E7': 'B7',
        'Eb': 'Bb7',
        'Eb7': 'Bb7',
        'Ebm': 'Bb7',
        'Ebm7': 'Bb7',
        'Em': 'B7',
        'Em7': 'B7',
        'F': 'C7',
        'Fmaj7': 'C7',
        'F7': 'C7',
        'Fm': 'C7',
        'Fm7': 'C7',
        'F#': 'C#7',
        'F#7': 'C#7',
        'F#m': 'C#7',
        'F#m7': 'C#7',
        'G': 'D7',
        'G7': 'D7',
        'Gb': 'Db7',
        'Gbmaj7': 'Db7',
        'Gb7': 'Db7',
        'Gbm': 'Db7',
        'Gbm7': 'Db7',
        'Gm': 'D7',
        'Gm7': 'D7',
        'G#': 'D#7',
        'G#7': 'D#7',
        'G#m': 'D#7',
        'G#m7': 'D#7',
    }

    # Define un diccionario con los acordes II-V7 asociados.
    II_V7 = {
        'A': 'Bm7-E7',
        'A7': 'Bm7-E7',
        'Ab': 'Bbm7-Eb7',
        'Ab7': 'Bbm7-Eb7',
        'Abm': 'Bbm(b5)-Eb7',
        'Abm7': 'Bbm(b5)-Eb7',
        'Am': 'Bm7(b5)-E7',
        'Am7': 'Bm7(b5)-E7',
        'B': 'C#m7-F#7',
        'B7': 'C#m7-F#7',
        'Bb': 'Cm7-F7',
        'Bb7': 'Cm7-F7',
        'Bbm': 'Cm7(b5)-F7',
        'Bbm7': 'Cm7(b5)-F7',
        'Bm': 'C#m7(b5)-F#7',
        'Bm7': 'C#m7(b5)-F#7',
        'C': 'Dm7-G7',
        'Cmaj7': 'Dm7-G7',
        'C7': 'Dm7-G7',
        'Cb': 'Ebm7-Gb7',
        'Cb7': 'Ebm7-Gb7',
        'Cbm': 'Ebm7(b5)-Gb7',
        'Cbm7': 'Ebm7(b5)-Gb7',
        'Cm': 'Dm7(b5)-G7',
        'Cm7': 'Dm7(b5)-G7',
        'C#': 'D#m7-G#7',
        'C#7': 'D#m7-G#7',
        'C#m': 'D#m7(b5)-G#7',
        'C#m7': 'D#m7(b5)-G#7',
        'D': 'Em7-A7',
        'D7': 'Em7-A7',
        'Db': 'Ebm7-Ab7',
        'Db7': 'Ebm7-Ab7',
        'Dbm': 'Ebm7(b5)-Ab7',
        'Dbm7': 'Ebm7(b5)-Ab7',
        'Dm': 'Em7(b5)-A7',
        'Dm7': 'Em7(b5)-A7',
        'D#': 'E#(F)m7-A#7',
        'D#7': 'E#(F)m7-A#7',
        'D#m': 'E#(F)m7(b5)-A#7',
        'D#m7': 'E#(F)m7(b5)-A#7',
        'E': 'F#m7-B7',
        'E7': 'F#m7-B7',
        'Eb': 'Fm7-Bb7',
        'Eb7': 'Fm7-Bb7',
        'Ebm': 'Fm7(b)-Bb7',
        'Ebm7': 'Fm7(b)-Bb7',
        'Em': 'F#m7(b5)-B7',
        'Em7': 'F#m7(b5)-B7',
        'F': 'Gm7-C7',
        'Fmaj7': 'Gm7-C7',
        'F7': 'Gm7-C7',
        'Fm': 'Gm7(b5)-C7',
        'Fm7': 'Gm7(b5)-C7',
        'F#': 'G#m7-C#7',
        'F#7': 'G#m7-C#7',
        'F#m': 'G#m7(b5)-C#7',
        'F#m7': 'G#m7(b5)-C#7',
        'G': 'Am7-D7',
        'G7': 'Am7-D7',
        'Gb': 'Abm7-Db7',
        'Gb7': 'Abm7-Db7',
        'Gbm': 'Abm7(b5)-Db7',
        'Gbm7': 'Abm7(b5)-Db7',
        'Gm': 'Am7(b5)-D7',
        'Gm7': 'Am7(b5)-D7',
        'G#': 'A#m7-D#7',
        'G#7': 'A#m7-D#7',
        'G#m': 'A#m7(b5)-D#7',
        'G#m7': 'A#m7(b5)-D#7',
    }
    #Evitar generación no solicitada de progresiones:

    #GENERACIÓN DE LA PROGRESIÓN BÁSICA

    def generate_chord_progression(tonalidad, num_acordes):
        acordes_movimientos = tonalidades[tonalidad]
        progresion = [tonalidad]

        for i in range(num_acordes - 1):
            ultimo_acorde = progresion[-1]
            if len(progresion) >= 4 and progresion[-4] == quinto_grado[tonalidad]:
                progresion.append(quinto_grado[tonalidad])
            else:
                siguiente_acorde = random.choice(acordes_movimientos[ultimo_acorde])
                progresion.append(siguiente_acorde)
        return progresion

    #GENERACIÓN DE LA PROGRESIÓN CON DOMINANTES SECUNDARIOS

    def agregar_dominantes(progresion, quinto_grado):
        nueva_progresion = []

        for acorde in progresion:
            # No agregamos dominante al primer acorde
            if acorde == progresion[0]:
                nueva_progresion.append(acorde)
            else:
                # Asegurarse de que el acorde actual tenga un quinto grado definido
                if acorde in quinto_grado:
                    quinto_de_acorde = quinto_grado[acorde]
                    nueva_progresion.append(quinto_de_acorde)
                nueva_progresion.append(acorde)

        return nueva_progresion

    # GENERACIÓN DE LA PROGRESIÓN CON CADENAS II-V-I

    def agregar_II_V7(progresion, II_V7):
        nueva_progresion = []
        for acorde in progresion:
            # No agregamos II-V7 al primer acorde
            if acorde == progresion[0]:
                nueva_progresion.append(acorde)
            else:
                # Asegurarse de que el acorde actual tenga un II-V7 definido
                if acorde in II_V7:
                    II_V7_de_acorde = II_V7[acorde]
                    nueva_progresion.append(II_V7_de_acorde)
                nueva_progresion.append(acorde)
        return nueva_progresion


    # Inicializar 'tonalidades' a tonalidades_naturales por defecto
    tonalidades = tonalidades_naturales

    # Pide al usuario que elija una tonalidad y un número de acordes.
    tonalidad = st.sidebar.selectbox('Elige una tonalidad', list(tonalidades.keys()))
    num_acordes = st.sidebar.slider('Elige el número de compases', 1, 64, 8)

    # Permitir al usuario seleccionar un estilo de progresión de acordes.

    estilos = ['Acordes naturales', 'Sustitutos naturales', 'Intercambio modal', 'Sustitutos tritonales']

    estilo = st.sidebar.select_slider('Selecciona la complejidad de la progresión', options=estilos)

    st.sidebar.write(f"Complejizar añadiendo: {estilo}")

    # Define 'tonalidades' en base a la elección del usuario.
    if estilo == 'Acordes naturales':
        tonalidades = tonalidades_naturales
    elif estilo == 'Sustitutos naturales':
        tonalidades = tonalidades_sustitutos_naturales
    elif estilo == 'Intercambio modal':
        tonalidades = tonalidades_intercambio_modal
    elif estilo == 'Sustitutos tritonales':
        tonalidades = tonalidades_sustitutos_tritonales
    else:  
        tonalidades = tonalidades_naturales  # por defecto



    # Comprueba si ya hay una progresión de acordes en el estado de la sesión y si la tonalidad, el número de acordes, o el estilo ha cambiado.
    if 'progresion' not in st.session_state or tonalidad != st.session_state['tonalidad'] or num_acordes != st.session_state['num_acordes'] or estilo != st.session_state['estilo']:

        # Selecciona el diccionario de movimientos armónicos correcto en función de la tonalidad elegida.
        acordes_movimientos = tonalidades[tonalidad]

        # Comienza la progresión en la tónica elegida.
        progresion = [tonalidad]

        # Para cada acorde restante en la progresión...
        for i in range(num_acordes - 1):
            # Si esta es la última posición de acorde, elige el quinto grado.
            if i == num_acordes - 2:
                progresion.append(quinto_grado[tonalidad])
            else:
                # Si no, elige aleatoriamente un acorde que represente un movimiento fuerte desde el acorde actual.
                ultimo_acorde = progresion[-1]
                siguiente_acorde = random.choice(acordes_movimientos[ultimo_acorde])

                # Agrega el nuevo acorde a la progresión.
                progresion.append(siguiente_acorde)

        # Guarda la progresión, la tonalidad, el número de acordes y el estilo en el estado de la sesión
        st.session_state['progresion'] = progresion
        st.session_state['tonalidad'] = tonalidad
        st.session_state['num_acordes'] = num_acordes
        st.session_state['estilo'] = estilo

    else:
        # Usa la progresión de acordes guardada
        progresion = st.session_state['progresion']



    # Muestra la progresión generada.
    st.write("Progresión generada:")
    progresion_str = '||: ' + ' | '.join(progresion) + ' :||'
    st.markdown(f'## **{progresion_str}**')

    if st.sidebar.checkbox('Agregar dominantes secundarios'):
        progresion_con_dominantes = agregar_dominantes(progresion, quinto_grado)  # pasamos progresion como una lista
        # Muestra la progresión generada.
        st.write("Progresión generada enriquecida con dominantes secundarios:")
        progresion_con_dominantes_str ='||: ' + ' | '.join(progresion_con_dominantes) + ' :||'
        st.markdown(f'## **{progresion_con_dominantes_str}**')


    if st.sidebar.checkbox('Agregar secuencias II-V-I'):
        progresion_con_II_V7 = agregar_II_V7(progresion, II_V7)
        # Muestra la progresión generada.
        st.write("Progresión generada enriquecida con secuencias II-V7-I:")
        progresion_con_II_V7_str ='||: ' + ' | '.join(progresion_con_II_V7) + ' :||'
        st.markdown(f'## **{progresion_con_II_V7_str}**')

    # Boton de Información

    readme_text = """
    # Generador de Progresiones de Acordes

    El Generador de Acordes Mágico es una aplicación diseñada para crear progresiones armónicas efectivas y atractivas de una manera simple y divertida.

    ## ¿Cómo funciona?

    La aplicación se basa en principios de composición musical, en particular, en los movimientos armónicos de los acordes. Seleccionas una tonalidad y el número de acordes que deseas en tu progresión, y la aplicación genera una progresión de acordes. 

    Para entender el funcionamiento de esta aplicación es necesario entender básicamente el concepto de:

    ## Los movimientos armónicos

    Los movimientos armónicos son de tres clases:

    1. Movimiento débil: en el cambio de un acorde tríada a otro, una o dos notas cambian, pero no se mantiene la tónica del primer acorde.

    2. Movimiento medio: todas las notas cambian.

    3. Movimiento fuerte: una o dos notas cambian, pero se mantiene la tónica del primer acorde.

    La aplicación utiliza principalmente los movimientos fuertes para generar las progresiones de acordes en la modalidad más simple de generación de progresiones con los acordes naturales. 

    Este tipo de movimiento es frecuente en las progresiones famosas. Por ejemplo, en la secuencia C-Am-Dm-G, cada cambio de acorde implica un movimiento fuerte.

    ## Compliquemos las cosas

    La generación de progresiones, además de los movimientos fuertes como principal recurso para el movimiento de los acordes generados aleatoriamente, se puede personalizar agregando:

    * los acordes sustitutos naturales del primer grado para los casos donde un quinto grado dominante resuelve al primer grado.

    * los acordes de intercambio modal pertenecientes al modo menor cuya función armónica es de subdominante menor y que se "toman prestados" para su uso en la tonalidad mayor como sustituto del quinto grado dominante.

    * los acordes sustitutos del quinto grado dominante que comparten el tritono que contiene el quinto grado natural (5b7 de V).

    ## Compliquemos las cosas aún más

    Si el nivel de complejidad aún no es suficiente, podemos además:

    ***Agregar Dominantes Secundarios***

    Los dominantes secundarios, son acordes que funcionan como dominantes (V grado) a los acordes diatónicos de la tonalidad, sin ser el V grado de la tónica. Estos acordes pueden ayudar a darle un toque de color y complejidad a tu progresión, generando un mayor sentido de movimiento y dirección hacia el próximo acorde. Por ejemplo, en la tonalidad de C mayor, el acorde D7 sería un dominante secundario que resuelve al acorde G.

    ***Agregar secuencias II-V-I***

    La secuencia II-V-I es una de las progresiones más comunes en la música occidental, especialmente en el jazz. Compuesta por un acorde de segundo grado (II, que es un acorde de menor séptima), un acorde de quinto grado (V, que es un acorde de séptima dominante) y un acorde de primer grado (I, que es un acorde mayor o menor), esta secuencia proporciona una fuerte sensación de resolución y se utiliza frecuentemente para establecer o reafirmar la tonalidad principal. Cada cambio de acorde en una secuencia II-V-I implica un movimiento fuerte.

    ## Uso de la aplicación

    Para utilizar la aplicación, sigue estos pasos:

    1. Selecciona una tonalidad.
    2. Elige cuántos compases deseas en tu progresión (dispones de hasta 64 compases).
    3. Selecciona la complejidad de la progresión: conforme pase el deslizador hacia la derecha, la progresión se complejizará:

    | Menos complejo | **Acordes naturales** | **Sustitutos naturales** | **Intercambio modal** | **Sustitutos tritonales** | Más complejo |
    | ------------------ | ----------------- | -------------------- | ----------------- | --------------------- | ---------------- |

    4. Para agregar dominantes secundarios a tu progresión, simplemente marca la casilla "Agregar dominantes secundarios". La aplicación automáticamente añadirá acordes de dominante secundarios donde sea aplicable en tu progresión generada.
    5. Para agregar secuencias II-V-I que anteceden a cada acorde de tu progresión, simplemente marca la casilla "Agregar secuencias II-V7-I". La aplicación automáticamente añadirá estas secuencias donde sea aplicable en tu progresión generada.

    6. Presiona 'Enter' y visualiza la progresión generada.

    Las opciones son acumulativas, por ejemplo: "Sustitutos" tritonales" contiene los acordes de intercambio modal, sustitutos naturales y acordes naturales; la opción "Intercambio modal" contiene, además de los acordes de intercambio modal, todas las opciones de la opción anterior: Sustitutos naturales y los acordes naturales. De igual forma, la progresión generada con secuencias II-V7-I contiene los acordes dominantes de la progresión generada con acordes dominantes secundarios, y esta progresión contiene las anteriores, consecutivamente.


    *Nota: Si bien, cada opción abre la posibilidad de aparición de sus acordes correspondientes, esto no garantiza que se muestren en todas las progresiones, ya que la progresión generada se construye tomando decisiones aleatorias de las distintas opciones que tiene cada acorde según la teoría musical que hemos descrito*

    """

    # Muestra el checkbox "Encuentra las 7 llaves"
    if st.checkbox('Acerca de este generador de progresiones'):
        st.markdown(readme_text, unsafe_allow_html=False)

    #Evitar generaciones de progresiones no solicitadas:

    def generate_chord_progression(tonalidad, num_acordes):
        acordes_movimientos = tonalidades[tonalidad]
        progresion = [tonalidad]

        for i in range(num_acordes - 1):
            ultimo_acorde = progresion[-1]
            if len(progresion) >= 4 and progresion[-4] == quinto_grado[tonalidad]:
                progresion.append(quinto_grado[tonalidad])
            else:
                siguiente_acorde = random.choice(acordes_movimientos[ultimo_acorde])
                progresion.append(siguiente_acorde)
        return progresion

