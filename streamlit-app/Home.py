import streamlit as st
import pandas as pd
import numpy
from elasticsearch import Elasticsearch
import json
 
 
# Set up the application

st.set_page_config(
    page_title="DKP Big Data Demo",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Set up our es instance:
es = Elasticsearch(["https://a966740a868a2412eba54023109ab905-1124658745.us-west-2.elb.amazonaws.com:443/elastic"], basic_auth=('elastic', '717q73YzUpuwA6WH20H4Jqq7'), verify_certs=False)

def count_records():
    try:
        count = "{:,}".format(es.count(index="tech")['count'])
    except:
        count = 0
    return count

def aggregate_countries():
    query = {"size":0,"aggs":{"countries":{"terms":{"field":"sourcecountry.keyword","size":25}}}}
    aggregate = es.search(body=query, index="tech")['aggregations']['countries']['buckets']
    df = pd.DataFrame.from_dict(aggregate)
    df = df.rename(columns={"key": "Country", "doc_count": "Number of Articles"})
    for row in df.index:
        if len(df.loc[row, "Country"]) < 2:
            df.drop(row, inplace=True)
    return df


# Page layout
col1, col2, col3 = st.columns([1,8, 1])
with col1:
    st.text("")
    st.text("")
    st.image("../images/d2iq.png", width=95)
    
with col2:
    st.title('Tech News Data Analyser')
    st.text(f"There are currently {count_records()} articles in the search engine.")

st.markdown("""---""")    
st.bar_chart(data=aggregate_countries(), x="Country", y="Number of Articles", height=400, use_container_width=False, width=800)
st.markdown("""---""")

col1, col2 = st.columns([1, 1])

with st.sidebar:
    with st.form("search"):
        st.write("Search News Articles")
        search_term = st.text_input("Search Term")
        submitted = st.form_submit_button("Submit")