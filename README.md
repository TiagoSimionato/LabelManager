# LabelManager

 Software for extracting zpl labels from all .zip files in a specific folder and turning them into pdf

# Project Setup

1. Create Virtual environment
   ```bash
   $ python -m venv venv
   $ source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

2. Install Dependencies
   ```bash
   $ pip install -r requirements.txt
   ```

## Dependencies

`pip install labelary-mwisslead pyinstaller`

## Run

Run `labelManager.py` to start the GUI and begin interacting with the program

## Compile into exe

`pyinstaller --onedir --icon=favicon/favicon.ico --distpath build/dist --workpath build/build labelManager.pyw`
