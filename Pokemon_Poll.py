import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Pokémon Starter Poll")

# List of starter Pokémon and their associated colors (based on iconic colors)
starter_colors = {
    "Bulbasaur": "#66C6A1",  # Green
    "Charmander": "#F07F00",  # Orange
    "Squirtle": "#6DB1F7",  # Blue
    "Chikorita": "#A4D36C",  # Light Green
    "Cyndaquil": "#F08000",  # Orange
    "Totodile": "#00B5E2",  # Blue
    "Treecko": "#1B5B2F",  # Dark Green
    "Torchic": "#F5A000",  # Yellow-Orange
    "Mudkip": "#4A90A4",  # Blue
    "Turtwig": "#6E9D3B",  # Green
    "Chimchar": "#FF5A00",  # Orange
    "Piplup": "#00A7D8",  # Blue
    "Snivy": "#A0C88C",  # Green
    "Tepig": "#F08C37",  # Orange
    "Oshawott": "#65AEDD",  # Blue
    "Chespin": "#8B9F4D",  # Green
    "Fennekin": "#F9A000",  # Yellow-Orange
    "Froakie": "#64A9D1",  # Blue
    "Rowlet": "#7F7F3F",  # Green
    "Litten": "#9C3A2D",  # Red
    "Popplio": "#2E88A0",  # Blue
    "Grookey": "#7AC74C",  # Green
    "Scorbunny": "#F4A300",  # Orange
    "Sobble": "#68B0D2",  # Blue
    "Sprigatito": "#6A9A3A",  # Green
    "Fuecoco": "#F18F2B",  # Orange
    "Quaxly": "#4F9ACF"  # Blue
}

# List of starter Pokémon
starters = list(starter_colors.keys())

# Create or load poll results
if "poll_results" not in st.session_state:
    st.session_state.poll_results = {pokemon: 0 for pokemon in starters}

# Let the user vote
selected_pokemon = st.radio("Which is your favorite starter Pokémon?", starters)

if st.button("Vote"):
    st.session_state.poll_results[selected_pokemon] += 1
    st.success(f"You voted for {selected_pokemon}!")

# Display results as a dataframe
st.subheader("Poll Results")
poll_df = pd.DataFrame(list(st.session_state.poll_results.items()), columns=["Pokémon", "Votes"])

# Customize colors for the bar chart
colors = [starter_colors[pokemon] for pokemon in poll_df['Pokémon']]

# Plotting the bar chart with custom colors
fig, ax = plt.subplots()
ax.bar(poll_df['Pokémon'], poll_df['Votes'], color=colors)
ax.set_xticklabels(poll_df['Pokémon'], rotation=90)

# Display the chart
st.pyplot(fig)

