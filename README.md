# collimg
### A simple Gradio app to collect image data

## Installation
```bash
git clone https://github.com/pranftw/collimg.git
cp config.py.example config.py
# edit config.py
# create a virtual environment and activate it
pip install -r requirements.txt
gradio app.py
```

## Editing `config.py`
`CATEGORIES` should be a dictionary with keys as category names and values as category indices. Ex. {'truck':0, 'ship':1}<br>
`DATASET_PATH` should contain the absolute path to the directory where the data should be stored as a string. Ex. '/home/foo/Documents/test_dataset'

## Image saving
All images are saved in PNG format<br>
Images are saved in sub directories that are created within `DATASET_PATH` with the format `<category>_<category_path>`<br>
Their filenames will be of the format `<random 16 hex chars>.png`