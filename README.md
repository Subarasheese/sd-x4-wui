# Stable Diffusion x4 Upscaler - Web UI

![upscaler](image2.png)


This is a Gradio Web UI version of the official SD x4 Upscaler (https://huggingface.co/stabilityai/stable-diffusion-x4-upscaler).

The Stable Diffusion x4 Upscaler is a powerful tool for upscaling images with impressive results. However, it requires a high VRAM GPU to function, making it difficult for users with consumer GPUs to use.

To address this issue, I've designed a Gradio Web UI with options for memory efficiency, and the possibility to slice the image into tiles, using a grid of squared sizes, to enable users with consumer GPUs to use the upscaler. The user can select a grid size, for example, of 1 (1x1), 2 (2x2), or 3 (3x3), which results in 1, 4, or 9 tiles, respectively.

But for instance, I am an RTX 3060 (12gb) user, and I successfully managed to upscale 1600x1200 (2.1mp) images using a single (1) tile with all optimizations on, so that means, I did not have to split the image into tiles for upscaling to work, however results my vary from card to card. Please let us know what your results are! 

Please feel free to open an issue or make a pull request if you would like to help optimize the app to make lower use of VRAM or improve the Gradio GUI.



## FAQ

- CUDA is constantly running out of memory for me.

Either keep all optimizations enabled, or increase the tiling grid.

- I see tiling edge artifacts in my uspcaled images.

There is no easy solution for this as far as I know. It is currently being investigated, and if you have suggestions, feel free to talk about it on the Issues tab.

- Will this be ported to AUTOMATIC1111?

I would like to, but currently I lack the skills to do so. I don't know to to handle dependency install, for example. Please let me know how to do it, or if you can help with this endeavor, feel free to fork this and let us know.

- What is even the point of this? The Ultimate SD Upscaler script does the job!!!1111!!!!

In my humble opinion and according to my experiments, this upscaler is superior to USU. It also works "out of the box", you don't even need to set denoising strength or anything like it. It is the official implementation by Stability AI.

- It's not working on my machine nor has an AUTOMATIC1111 extension option that I can install in a few clicks, therefore this is garbage.

I realize that Stable Diffusion became a consumer product really fast, and most of its users feel entitled and everything has to be easy and benefit them. But the truth is, I am just one guy with good will and little support and I don't have the expertise most devs from the ML do in terms of coding practices, UI design etc. If this does not work for you, please simply **let me know** and I will try to do my best help you to fix it.

## Usage
### Requirements

Before running the app, you need to install the required packages by running the following commands:

```
git clone https://github.com/Subarasheese/sd-x4-wui
cd sd-x4-wui
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
### Running the App

After installing the required packages, run the app with the following command:

```
source venv/bin/activate
python gradio_gui.py
Run the local URL on the browser (probably http://127.0.0.1:7860)
```
## Image Generation

When generating images, keep in mind that the prompt will be applied to each individual tile, not the entire image. For example, if you enter "man/woman", you have to keep in mind each tile may only contain a part of the skin of the person. Focus on quality tags, such as 8k, best quality, photography, cgi, and unreal engine.


## To-Do List

Here are some items on our to-do list that we plan to address in the future:

- [ ] Add a "save image" button. Also, add another button to save a half-sized version of the image, which reduces tiling artifact while still increasing the original resolution.
- [X] ~~Fix Xformers, which is currently implemented but not working for some reason, at least on my end.~~
- [ ] Make additional optimizations that would enable users with low VRAM to upscale without aggressively increasing the number of tiles.
- [ ] Create a Colab training notebook.
- [ ] Find a way to make the tiles blend seamlessly, with no edges or artifacts.
- [X] ~~Add support for negative prompts~~
- [ ] Make a port to the AUTOMATIC1111 Stable Diffusion web UI.
- [ ] Allow batch image processing (upscale several images within a queue).

