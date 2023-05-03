from config import TITLE, DESCRIPTION, IP, CATEGORIES, DATASET_PATH
import gradio as gr
import os
import secrets


def create_dirs(DATASET_PATH, CATEGORIES):
  if not os.path.exists(DATASET_PATH):
    os.mkdir(DATASET_PATH)
  for category, category_idx in CATEGORIES.items():
    category_path = os.path.join(DATASET_PATH, f'{category}_{category_idx}')
    if not os.path.exists(category_path):
      os.mkdir(category_path)


def on_submit(img, category):
  if img is None:
    raise gr.Error('Image is required!')
  if category=='':
    raise gr.Error('Category is required!')
  if category not in CATEGORIES.keys():
    raise gr.Error('Invalid category!')
  img_fname = f'{secrets.token_hex(8)}.png' # saving as png as image_mode in img is png
  category_path = os.path.join(DATASET_PATH, f'{category}_{CATEGORIES[category]}', img_fname)
  img.save(category_path)
  return None, ''


img = gr.Image(type='pil', image_mode='RGBA', label='Image')
category = gr.Dropdown(choices=CATEGORIES.keys(), label='Category', multiselect=False)
collimg = gr.Interface(fn=on_submit, inputs=[img, category], outputs=[img, category], title=TITLE, description=DESCRIPTION, allow_flagging='never')


create_dirs(DATASET_PATH, CATEGORIES)
collimg.launch(server_name=IP)