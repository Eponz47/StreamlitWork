import streamlit as st
import requests
import json

def get_random_dog_image():
    """Fetches a random dog image URL from the API."""
    try:
        response = requests.get("https://random.dog/woof.json",verify=False)
        response.raise_for_status()  
        data = response.json()
        return data["url"]
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching dog image: {e}")
        return None
    except (KeyError, json.JSONDecodeError) as e:
        st.error(f"Error parsing API response: {e}")
        return None

def main():
    st.title("Random Dog Image Generator")

    if st.button("Show me a dog!"):
        dog_image_url = get_random_dog_image()

        if dog_image_url:
            st.image(dog_image_url, caption="A random dog!", use_container_width=True)
        else:
            st.write("Failed to load dog image. Please try again.")

if __name__ == "__main__":
    main()
