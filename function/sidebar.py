import streamlit as st
import os


def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Enter your [OpenAI API key](https://platform.openai.com/account/api-keys) below🔑\n"  # noqa: E501
            "2. Ask a question 💬\n"
        )
        api_key_input = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="Paste your OpenAI API key here (sk-...)",
            help="You can get your API key from https://platform.openai.com/account/api-keys.",  # noqa: E501
            value=os.environ.get("OPENAI_API_KEY", None)
                  or st.session_state.get("OPENAI_API_KEY", ""),
        )

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "📖ChatGPT allows you to ask questions about your "
            "documents and get accurate answers with instant citations. "
        )
        st.markdown(
            "This tool is a work in progress. "
            "You can contribute to the project on [GitHub](https://github.com/AndrewCheUA/Image_Classification_Web_App_Team_3) "  # noqa: E501
            "with your feedback and suggestions💡"
        )
        st.markdown("Made by [TEAM_3](https://github.com/AndrewCheUA/Image_Classification_Web_App_Team_3)")
        st.markdown("---")

        return api_key_input
