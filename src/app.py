# Libraries
import os
import toml

import streamlit as st

#from github import Github

CONFIG_PATH = os.path.join(".streamlit", "config.toml")
config = toml.load(CONFIG_PATH)

def chat_interface():
    st.text_area(label = "Paste Link Here")
    st.button(label = "Submit")

def main():
    """
    """
    st.set_page_config(
        page_title = config["PAGES"]["HOME"]["NAME"],
        page_icon = config["IMAGES"]["LOGO"],
        layout = "centered"
    )
    st.title(config["PAGES"]["HOME"]["TITLE"])
    #st.write(config["PAGES"]["HOME"]["SUBTITLE"])

    chat_interface()

if __name__ == "__main__":
    main()



