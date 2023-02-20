import gradio as gr
import upscaler
import os
from PIL import Image

def upscale_image(prompt, rows=3,seed=0, image=None,xformers_input=False,cpu_offload_input=False,attention_slicing_input=False):
    cols = rows
    output_image = upscaler.upscale_image(image, int(rows), int(cols),int(seed), prompt,xformers_input,cpu_offload_input,attention_slicing_input)
    output_image_path = "result.png"
    output_image.save(output_image_path)

    return output_image_path


image_input = gr.inputs.Image(label="Input Image")
prompt_input = gr.inputs.Textbox(default="8k, photography, cgi, unreal engine, octane render, best quality",label="Prompt")
seed_input = gr.inputs.Number(default=-1, label="Seed")
row_input = gr.inputs.Number(default=3, label="Tile grid dimension amount (number of rows and columns) - v x v")
xformers_input = gr.inputs.Checkbox(default=False,label="Enable Xformers memory efficient attention")
cpu_offload_input = gr.inputs.Checkbox(default=False,label="Enable sequential CPU offload")
attention_slicing_input = gr.inputs.Checkbox(default=False,label="Enable attention slicing")
output_image = gr.outputs.Image(label="Output Image",type='pil')


#save_png_button, save_png_halfsize_button ; I don't know how to implement them
save_png_button = gr.Button(label="Save as a PNG image") # Added this button with the save_png function
save_png_halfsize_button = gr.Button(label="Save as a PNG image (half size)") # Added this button with the save_png_halfsize function

gr.Interface(fn=upscale_image,
             inputs=[prompt_input,row_input,
                     seed_input,image_input,
                     xformers_input,
                     cpu_offload_input,
                     attention_slicing_input],
             outputs=[output_image],
             title="Stable Diffusion x4 Upscaler - Web GUI",
             allow_flagging=False).launch()