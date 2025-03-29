import streamlit as st 
import requests 

def get_random_joke():
    """Fetch a random joke from the API"""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")

        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']} \n\n {joke_data['punchline']}"
        else:
            return "Failed to fetch a joke. Please try again later."
    except:
        return "Why did the programmer quit his job? \n because he didn't get array"


def main():
    """Main function to run the Streamlit app"""

    st.title("Random Joke Generator")
    st.write("Click the button below to generate a random Joke")

    if st.button("Generate Joke"):
        joke = get_random_joke()
        st.success(joke)
    st.divider()

    st.markdown(
        """
    <div style='text-align:center;'>
        <p>Joke from Official Joke API</p>
        <p>Build with ❤️ by <a href='https://github.com/Kafil99'>Kafeel Ahmed</a> using Streamlit</p>
    </div>
""", 
        unsafe_allow_html=True
    )


# Run main function when script is executed directly
if __name__ == "__main__":
    main()