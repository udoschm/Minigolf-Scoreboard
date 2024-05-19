import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Minigolf Scoreboard",
    page_icon="⛳️",
    initial_sidebar_state="collapsed",
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.header("Minigolf Scoreboard ⛳️")

# Auswahl der Spieleranzahl
player_count = st.select_slider(
    'Wähle die Anzahl der Spieler',
    options=['2', '3', '4', '5', '6', '7', '8', '9', '10'])

# Umwandlung der Spieleranzahl in eine Ganzzahl
player_count = int(player_count)

# Eingabe der Spielernamen
player_names = []
for i in range(player_count):
    player_name = st.text_input(f'Name von Spieler {i + 1}', key=f'player_name_{i}')
    player_names.append(player_name)

# Initialisierung der Datenstruktur für die Punkte
player_points = {name: [0] * 18 for name in player_names}

# Eingabe der Punkte für jedes Spiel und jeden Spieler
for game in range(18):
    with st.expander(f'Bahn {game + 1}'):
        for player_name in player_names:
            points = st.select_slider(
                f'Versuche für {player_name} auf Bahn {game + 1}',
                options=[1, 2, 3, 4, 5, 6, 7],
                key=f'{player_name}_game_{game}'
            )
            player_points[player_name][game] = points

# Berechnung der Gesamtsumme der Punkte für jeden Spieler
total_points = {player: sum(points) for player, points in player_points.items()}

# Erstellung eines DataFrame zur Darstellung der Gesamtsummen
total_points_df = pd.DataFrame(list(total_points.items()), columns=['Spieler', 'Gesamtpunkte'])

# Schöne Darstellung der Gesamtsumme der Punkte in einer Tabelle
st.header("Gesamtsumme der Punkte:")
st.table(total_points_df)