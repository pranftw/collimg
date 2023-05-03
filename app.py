from config import CATEGORIES, IP
import gradio as gr


def on_submit(img, category):
  if img is None:
    raise gr.Error('Image is required')
  if category=='':
    raise gr.Error("Category shouldn't be empty")
  return None, ''


img = gr.Image(type='pil', image_mode='RGBA', label='Image')
category = gr.Dropdown(choices=CATEGORIES.keys(), label='Category', multiselect=False)
collimg = gr.Interface(fn=on_submit, inputs=[img, category], outputs=[img, category], allow_flagging='never')


collimg.launch(server_name=IP)