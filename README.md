# Streamlit-Clipboard

## About the solution: 
- A simple clipping function to copy data from the streamlit server to your system clipboard while running a streamlit app. 
- Uses components API of streamlit to manipulate the frontend code.
- Inspired from this [youtube video](https://www.youtube.com/watch?v=SLyS0v8br20) 
<br>
<br>
## Files in the repo:
- requirements.txt - If streamlit is not installed, you can install it using <code>pip install streamlit</code> or <code>pip install -f requirements.txt</code>
- clipper.py - clipping function wrapped in a python file
- demo.py - a working demo of the clipper package 
<br>
<br>
## How to use it:
- make sure streamlit library is installed
- import the clipper python file
    ```
    import clipper
    ```
- use the clip function from the cliiper file with string as argument
    ```
    clipper.clip(<YOUR TEXT>)
    ```
- check a demo of the working usind the demo.py file
    ```
    streamlit run demo.py
    ```
