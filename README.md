# qrcode-generator
QR Code Generator based on room numbers listed in CSV file to contact support via E-Mail

### Description
This Python script generates QR codes based on room numbers listed in a CSV file. It supports both headless and graphical modes, allowing for flexibility in usage.

### Requirements
- Python 3.x
- Required Libraries: `csv`, `argparse`, `subprocess`, `tkinter`, `PIL`

You can run the installer.sh to install all dependencies.

### Usage
#### Headless Mode
In headless mode, you can specify options through command-line arguments. Here's how to use the script:

```bash
python3 qrcode-generator.py -csv /path/to/room.csv -mailto /path/to/mailto.txt -output /path/to/output -textsize 4
```

#### Options
- `-csv` : Specifies the path to the CSV file containing room numbers. (Required)
- `-mailto` : Specifies the path to the `mailto.txt` file containing the email template. (Required)
- `-output` : Specifies the folder where the generated QR code images will be saved. (Required)
- `-textsize` : Specifies the text size for annotations on the QR code images. (Optional; default is 42)

#### Example
To generate QR codes based on a CSV file located at `/path/to/room.csv`, with mail information from `/path/to/mailto.txt`, saving the output to `/path/to/output`, and with a text size of 42:

```bash
python3 qrcode-generator.py -csv /path/to/room.csv -mailto /path/to/mailto.txt -output /path/to/output -textsize 42
```

### Graphical Mode
When running the script without any arguments, it will launch in graphical mode. Follow the on-screen instructions to select the CSV and mailto files, output directory, and whether or not to include an image in the center of the QR code.
