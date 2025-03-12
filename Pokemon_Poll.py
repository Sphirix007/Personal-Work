import streamlit as st
import pandas as pd

# Title of the app
st.title("Pokémon Starter Poll")

# List of starter Pokémon
starters = [
    "Bulbasaur", "Charmander", "Squirtle", 
    "Chikorita", "Cyndaquil", "Totodile", 
    "Treecko", "Torchic", "Mudkip", 
    "Turtwig", "Chimchar", "Piplup", 
    "Snivy", "Tepig", "Oshawott", 
    "Chespin", "Fennekin", "Froakie", 
    "Rowlet", "Litten", "Popplio", 
    "Grookey", "Scorbunny", "Sobble", 
    "Sprigatito", "Fuecoco", "Quaxly"
]

# Create or load poll results
if "poll_results" not in st.session_state:
    st.session_state.poll_results = {pokemon: 0 for pokemon in starters}

# Let the user vote
selected_pokemon = st.radio("Which is your favorite starter Pokémon?", starters)

if st.button("Vote"):
    st.session_state.poll_results[selected_pokemon] += 1
    st.success(f"You voted for {selected_pokemon}!")

# Display results as a dataframe and chart
st.subheader("Poll Results")
poll_df = pd.DataFrame(list(st.session_state.poll_results.items()), columns=["Pokémon", "Votes"])
st.bar_chart(poll_df.set_index("Pokémon"))
