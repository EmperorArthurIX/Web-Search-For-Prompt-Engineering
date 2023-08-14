import streamlit as st
import pandas as pd
from utility_functions import BingWebSearchAPI, convert_to_selectable_df, get_selected_rows, get_text_contents

st.set_page_config(page_title="Web Search for Prompt Engineering",
                   layout="centered")

st.title("Web Search for Prompt Engineering")

with st.sidebar.expander(label="Disclaimer"):
     st.caption("None of the data appearing on this app is claimed to be generated here, it is simply a tool to optimise search times for examples to give while prompt engineering")

already_searched = False
search_query = st.sidebar.text_input(label="Enter your search query")
api_key = st.sidebar.text_input(label="Search Engine Service API Key",
                                type='password',
                                help="Eg. Bing Search API Key")
api_endpoint = st.sidebar.text_input(label="Search API Endpoint URL",
                                     value="https://api.bing.microsoft.com/",
                                     help="URL from where we fetch search results")

if search_query:
    if not already_searched:
        if st.sidebar.button("Refresh Search"):
                already_searched = False
        try:
                response = BingWebSearchAPI().get_search_results(search_query, api_key, api_endpoint)
                response = convert_to_selectable_df(response)
                already_searched = True
        except Exception as exp:
                st.error(exp.args[0])

        st.header("Search Results - Available Content Sources")
        editing_df = st.data_editor(response,
                                hide_index=True,
                                disabled=response.columns[1:],
                                column_config={"Select":st.column_config.CheckboxColumn(required=True)}
                                )
        selected_df = get_selected_rows(editing_df)
        if len(selected_df) > 0:
                st.header("Selected Sources to Fetch Content")
                st.dataframe(selected_df[['Title']], hide_index=True)
        st.header("Content Parsed from Sources")
        st.subheader("Usable as examples for content generation via an LLM")
        for text in get_text_contents(selected_df):
                st.code(text)
