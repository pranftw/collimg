from config import CATEGORIES, IP
import gradio as gr


def on_submit(img, category):
  print(category)
  return None, ''


img = gr.Image(type='pil', image_mode='RGBA', label='Image')
category = gr.Dropdown(choices=CATEGORIES.keys(), label='Category', multiselect=False, interactive=True)
collimg = gr.Interface(fn=on_submit, inputs=[img, category], outputs=[img, category], allow_flagging=False)


collimg.launch(server_name=IP)