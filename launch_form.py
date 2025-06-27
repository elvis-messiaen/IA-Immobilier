import webbrowser
import os

file_path = os.path.abspath("api/app/frontend/predict_lille_form.html")
webbrowser.open_new_tab(f"file://{file_path}")
