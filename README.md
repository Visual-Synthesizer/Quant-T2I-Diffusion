# Fine-Tuning Text-to-Image Diffusion Models

This repository contains tools and resources to assist in the fine-tuning of text-to-image diffusion models with Kohya-ss. It includes a Jupyter Notebook for organizing JSON files and large images, which helps track and quantify the fine-tuning process. Additionally, the repository contains a ComfyUI workflow for XY testing of fine-tuned models, and a Python script to create grids.

Fine-Tuner used:
- [kohya-ss/sd-scripts](https://github.com/kohya-ss/sd-scripts)
- [GUI fork](https://github.com/bmaltais/kohya_ss)

## Features

- Load and process Kohya SS JSON files, display/customize important settings and XY Grids.
- Create images in a grid format with folder names and prompts.
- Organize and visualize fine-tuning progress.
- ComfyUI workflow for XY testing of fine-tuned models and LoRA.
- Python script to make grids

## Requirements

Make sure to install the necessary dependencies listed in `requirements.txt`.


## Usage

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/Quant-T2I-Diffusion.git
   cd Quant-T2I-Diffusion

   ```

2. **Install the required dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Jupyter Notebook:**

   Open the Jupyter Notebook and add JSON file path to a code cell.

4. **Create Image Grid:**

   Use the provided script or ComfyUI workflow to create a grid image from your custom model. Add the image path to the notebook code.

  
## ComfyUI Workflow for XY Testing

The repository also includes a ComfyUI workflow for XY testing of the fine-tuned models. Detailed instructions for setting up and using the ComfyUI workflow can be found in the `comfyui-workflow/` directory.

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

