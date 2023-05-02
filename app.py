from config import CATEGORIES, IP
import gradio as gr


def on_submit(img, category):
  print(category)
  img.show()


img = gr.Image(type='pil', image_mode='RGBA', label='Image')
category = gr.Dropdown(choices=CATEGORIES.keys(), label='Category', multiselect=False, interactive=True)
collimg = gr.Interface(
  fn=on_submit, inputs=[img, category], outputs=None
)


collimg.launch(server_name=IP)