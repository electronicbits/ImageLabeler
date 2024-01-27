# ImageLabeler

`ImageLabeler.py` is a Python script designed to simplify the process of labeling images for various applications, such as training machine learning models for image classification. It features a graphical user interface (GUI) for easy navigation and quick labeling of images by pressing designated keys.

## Use Cases

- Preparing datasets for machine learning image classifiers.
- Organizing large photo libraries according to specific categories.
- Data preprocessing for computer vision projects.

## Features

- Easy-to-use GUI for image browsing.
- Fast labeling with keyboard shortcuts.
- Progress tracking through sequential image loading.

## Setup

### Using Miniconda

If you prefer using Miniconda (a minimal installer for conda), you can set up your environment using the `environment.yml` file provided in this repository.

1. **Install Miniconda**: Download and install Miniconda from the [official site](https://docs.conda.io/en/latest/miniconda.html) if you haven't already.

2. **Create the Conda Environment**: Navigate to the cloned repository's directory and run the following command to create a conda environment from the `environment.yml` file:

   ```sh
   conda env create -f environment.yml
   ```

3. **Activate the Environment**: Once the environment is created, activate it with:

   ```sh
   conda activate image_labeler_env
   ```

4. **Run the Script**: With the environment activated, you can run the script as follows:

   ```sh
   python ImageLabeler.py
   ```

### Using pip

If you prefer using pip, you can set up your environment using the `requirements.txt` file.

1. **Create a Virtual Environment** (optional but recommended):

   ```sh
   python -m venv image_labeler_venv
   ```

   Activate the virtual environment:

   - On Windows:
     ```sh
     image_labeler_venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```sh
     source image_labeler_venv/bin/activate
     ```

2. **Install Dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Script**:

   ```sh
   python ImageLabeler.py
   ```

## Customization

Modify the `output_folders` dictionary in the script to suit your labeling needs, where each key represents a keyboard shortcut and each value represents a corresponding label/folder name.

## Contributing

Contributions are welcome! Feel free to fork the repo, make changes, and submit pull requests.

## License

This project is open-sourced under the MIT License.

## Acknowledgments

- This tool is designed to assist in the machine learning data preprocessing workflow.
