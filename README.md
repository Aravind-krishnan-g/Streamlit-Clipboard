# Streamlit-Clipboard

About the solution: 
- A simple clipping function to copy data from the streamlit server to your system clipboard while running a streamlit app. 
- Uses components API of streamlit to manipulate the frontend code.
- Inspired from this [youtube video](https://www.youtube.com/watch?v=SLyS0v8br20) 

How to use it:
- make sure streamlit library is installed
- import the Clipper python file provided in the repo
    ```
    import Clipper
    ```
- use the clip function from Clipper with string as argument
    ```
    Clipper.clip(<YOUR TEXT>)