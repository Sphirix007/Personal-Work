import streamlit as st
import pandas as pd

# Title of the app with a custom background
st.markdown("""
    <style>
        .stApp {
            background-color: #F0F8FF;  /* Light Blue Background */
        }
    </style>
""", unsafe_allow_html=True)

# Title with an emoji and a gradient
st.markdown("""
    <h1 style="text-align: center; color: #FF6347; font-family: 'Helvetica';">
        Pokémon Starter Poll 🗳️
    </h1>
    <p style="text-align: center; font-size: 18px; color: #FF4500;">Vote for your favorite Pokémon starter!</p>
""", unsafe_allow_html=True)

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

# Custom vote button styling with gradient background
vote_button_style = """
    <style>
    .stButton>button {
        background: linear-gradient(to right, #Ff6961, #89CFF0, #50C878);
        color: white;
        font-size: 16px;
        padding: 10px 50px;
        border-radius: 20px;
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        background: linear-gradient(to right, #FF4500, #FF6347);
        box-shadow: 0 4px 10px rgba(255, 69, 0, 0.5);
    }
    </style>
"""
st.markdown(vote_button_style, unsafe_allow_html=True)

# Let the user vote
selected_pokemon = st.radio(
    "Which is your favorite starter Pokémon?", 
    starters, 
    index=0, 
    key="pokemon_radio",
    help="Click to select your favorite Pokémon starter! 🌟"
)

# Vote action with custom button color
if st.button("Vote"):
    st.session_state.poll_results[selected_pokemon] += 1
    st.success(f"🎉 **You voted for {selected_pokemon}!**", icon="✅")

# Display results with colorful styling
st.subheader("Poll Results", anchor="results")
poll_df = pd.DataFrame(list(st.session_state.poll_results.items()), columns=["Pokémon", "Votes"])
poll_df = poll_df.sort_values("Votes", ascending=False)

# Custom table styling with background and color
st.write(
    poll_df.style.set_table_styles([
        {'selector': 'thead th', 'props': [('background-color', '#FFEB3B'), ('color', 'black'), ('font-weight', 'bold')]},
        {'selector': 'tbody td', 'props': [('background-color', '#E0FFFF')]},
        {'selector': 'tr:nth-child(odd)', 'props': [('background-color', '#F5F5F5')]},
        {'selector': 'tr:nth-child(even)', 'props': [('background-color', '#FFFFFF')]},
    ])
)

# Display results in a colorful bar chart
st.bar_chart(poll_df.set_index("Pokémon")["Votes"], color="#FFFFFF")

# A cool footer with a background color and emoji
st.markdown("""
    <style>
        .footer {
            text-align: center;
            font-size: 16px;
            background-color: #FF6347;
            padding: 10px;
            color: white;
            border-radius: 8px;
            box-shadow: 0px 5px 15px rgba(255, 69, 0, 0.3);
        }
    </style>
    <div class="footer">
        Made with ❤️ by me :)
    </div>
""", unsafe_allow_html=True)





