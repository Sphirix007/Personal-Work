import streamlit as st
import pandas as pd

# Title of the app
st.title("Pokémon Starter Poll 🗳️")

# Add a custom heading and description
st.markdown("""
### Vote for your favorite Pokémon starter!
Choose your favorite from the options below. Let's see which one reigns supreme! 😎
""")

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

# Custom vote button styling
vote_button_style = """
    <style>
    .stButton>button {
        background-color: #FFFFFF;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #FF6347;
    }
    </style>
"""
st.markdown(vote_button_style, unsafe_allow_html=True)

# Let the user vote
selected_pokemon = st.radio(
    "Which is your favorite starter Pokémon?", 
    starters, 
    index=0, 
    key="pokemon_radio"
)

# Vote action
if st.button("Vote"):
    st.session_state.poll_results[selected_pokemon] += 1
    st.success(f"🎉 You voted for **{selected_pokemon}**!")

# Display results as a styled dataframe and bar chart
st.subheader("Poll Results")
poll_df = pd.DataFrame(list(st.session_state.poll_results.items()), columns=["Pokémon", "Votes"])
poll_df = poll_df.sort_values("Votes", ascending=False)

# Style the DataFrame
st.write(
    poll_df.style.set_table_styles([
        {'selector': 'thead th', 'props': [('background-color', '#FFEB3B'), ('color', 'black')]},
        {'selector': 'tbody td', 'props': [('background-color', '#F4F4F4')]},
        {'selector': 'tr:nth-child(odd)', 'props': [('background-color', '#EEEEEE')]},
    ])
)

# Display results in a colorful bar chart
st.bar_chart(poll_df.set_index("Pokémon")["Votes"])

# A cool footer
st.markdown("---")
st.markdown("Made with ❤️ by Me :) | Pokémon Fan")

