import streamlit as st
from utility_functions import BingWebSearchAPI

st.title("Web Search for Promt Engineering")

search_query = st.sidebar.text_input(label="Enter your search query")
api_key = st.sidebar.text_input(label="Search Engine Service API Key", type='password', help="Eg. Bing Search API Key")
api_endpoint = st.sidebar.text_input(label="Search API Endpoint URL", value="https://api.bing.microsoft.com/", help="URL from where we fetch search results")
response = None
if search_query:
    # st.write(search_query)
    # response = BingWebSearchAPI().get_search_results(search_query, api_key)
    response = [{'content_snippet': 'Amity University Mumbai Aug 2020 - Present3 years 1 '
                     'month Mumbai, Maharashtra, India Summer Intern Flex Jul '
                     '2022 - Aug 20222 months Mumbai, Maharashtra, India - '
                     'Implementation: Analysed weekly...',
  'name': 'Ishaan Pandita - Summer Intern - EY | LinkedIn',
  'url': 'https://in.linkedin.com/in/ishaan-sunita-pandita'},
 {'content_snippet': 'Ishan Pandita (born 26 May 1998) is an Indian '
                     'professional footballer who plays as a forward for '
                     'Indian Super League club Kerala Blasters and the Indian '
                     'national team . Club career Early and youth career '
                     'Pandita left India and arrived in the Philippines, where '
                     'he attended British school in Manila and first took '
                     'football training. [2]',
  'name': 'Ishan Pandita - Wikipedia',
  'url': 'https://en.wikipedia.org/wiki/Ishan_Pandita'},
 {'content_snippet': 'Ishan Pandita - Player profile | Transfermarkt #9 Ishan '
                     'Pandita 1 1 Without Club Last club: Jamshedpur FC '
                     'Without Club since: Jun 1, 2023 ISLmedia + Date of '
                     'birth/Age: May 26, 1998 (25) Place of birth: New Delhi, '
                     'Delhi Citizenship: India Height: 1,83 m Position: '
                     'Centre-Forward National player: India Caps/Goals: 6 / 1 '
                     '₹ 1.8 Cr',
  'name': 'Ishan Pandita - Player profile 23/24 | Transfermarkt',
  'url': 'https://www.transfermarkt.co.in/ishan-pandita/profil/spieler/664564'},
 {'content_snippet': "Ishaan Pandita Placement Secretary, AUM | GDSC Lead '22 "
                     "| Beta MLSA '22 | Using Words To Make Art 1w Hello "
                     "#connections ! I've been working on understanding the "
                     'Microsoft Power Platform and how...',
  'name': 'Ishaan Pandita on LinkedIn: Microsoft Power Platform',
  'url': 'https://www.linkedin.com/posts/ishaan-sunita-pandita_microsoft-power-platform-activity-7092539054616969216-gY75'},
 {'content_snippet': 'Ishaan Sunita Pandita Living life and becoming better '
                     'than who I was yesterday. My Portfolio My Medium Page '
                     'GitHub',
  'name': 'Ishaan Sunita Pandita | Twitter, Instagram | Linktree',
  'url': 'https://linktr.ee/IshaanPandita'},
 {'content_snippet': '102K Followers, 267 Following, 126 Posts - See Instagram '
                     'photos and videos from Ishan Pandita (@_ishanpandita_)',
  'name': 'Ishan Pandita (@_ishanpandita_) • Instagram photos and videos',
  'url': 'https://www.instagram.com/_ishanpandita_/'},
 {'content_snippet': 'Ishaan Sunita Pandita | Strengths Presentation '
                     'Communication is my forte, especially when it comes to '
                     'conveying information to an audience. I have proven my '
                     'presentation skills while serving my tenure in '
                     'communities like GDSC as the Student Lead and by hosting '
                     'a multitude of events at my University.',
  'name': 'Ishaan Sunita Pandita - GitHub Pages',
  'url': 'https://emperorarthurix.github.io/The-ISP/'},
 {'content_snippet': 'Ishaan Sunita Pandita EmperorArthurIX. Follow. Living '
                     'life and becoming better than who I was yesterday. Oh, '
                     'and also learning magic so I can turn data into money. '
                     '10 followers · 8 following. Pune. '
                     'https://emperorarthurix.github.io/The-ISP/. '
                     '@PanditaIshaan. in/ishaan-sunita-pandita.',
  'name': 'EmperorArthurIX (Ishaan Sunita Pandita) · GitHub',
  'url': 'https://github.com/EmperorArthurIX/'},
 {'content_snippet': 'Hello #connections! We had yet another great and '
                     'indulging session with Jetpack Compose for Android '
                     'Development at Google Developer Student Clubs - Amity…',
  'name': 'Ishaan Pandita on LinkedIn: About GDSC | Google Developer Student '
          'Clubs',
  'url': 'https://www.linkedin.com/posts/ishaan-sunita-pandita_about-gdsc-google-developer-student-clubs-activity-6978713682356649984-PzBc'},
 {'content_snippet': 'Ishaan Pandita Expand search. Jobs People Learning '
                     'Dismiss Dismiss. Dismiss. Dismiss. Dismiss. Join now '
                     'Sign in Ishaan Pandita’s Post Ishaan Pandita Using words '
                     "to make art | GDSC Lead '22 | Beta MLSA '22 3mo Edited "
                     'Report this post A journey of a thousand miles begins '
                     'with a single step! I express my heartfelt gratitude to '
                     '...',
  'name': 'Ishaan Pandita on LinkedIn: #gratitude #community #growth #learning '
          '# ...',
  'url': 'https://in.linkedin.com/posts/ishaan-sunita-pandita_a-journey-of-a-thousand-miles-begins-with-activity-6961699451937677312-qD3A'}]
    st.dataframe(response)
    st.selectbox(label="Selected Sources", options=response)
