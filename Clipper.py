import streamlit as st
import streamlit.components.v1 as components

def clip(text):
    html_string = "<script> window.parent.navigator.clipboard.writeText(\""+text+"\").then(() =>{}); </script> "
    components.html(html_string,
                    height=0,
                    width=0)
    