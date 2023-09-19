import os
import csv
import argparse
import subprocess
from tkinter import filedialog, messagebox, Tk

# Function to read email settings from a file
def read_mail_settings(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        top_text = lines[3].strip() if len(lines) >= 4 else None
        return lines[0].strip(), lines[1].strip(), lines[2].strip(), top_text
    except Exception as e:
        print(f"Error reading mail settings: {e}")
        return None, None, None, None

# Function to run the core logic
def run_logic(InputDoc, OutputFolder, FileSize, TextSize, MailAddress, MailSubject, MailText, TopText, WantPicture, ExtraPic=None):
    with open(InputDoc, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        lns = list(reader)

    for ln in lns:
        RoomNumber = ''.join(ln)[:3]
        clipboard = f"mailto:{MailAddress}?subject={MailSubject} {RoomNumber}&body={MailText} {RoomNumber}"
        subprocess.run(f"/usr/bin/qrencode -s {FileSize} -o {OutputFolder}/{RoomNumber}.png \"{clipboard}\"", shell=True)
        
        # Add optional text at the top of the QR code
        if TopText:
            subprocess.run(f"convert {OutputFolder}/{RoomNumber}.png -gravity South -pointsize {TextSize} -annotate +0+10 '{TopText}' {OutputFolder}/{RoomNumber}.png", shell=True)

        # Add text at the bottom of the QR code
        subprocess.run(f"convert {OutputFolder}/{RoomNumber}.png -gravity North -pointsize {TextSize} -annotate +0+10 '{MailSubject} {RoomNumber}' {OutputFolder}/{RoomNumber}.png", shell=True)

# Initialize argparse
parser = argparse.ArgumentParser(description="QR-Code Room Generator")
parser.add_argument('-csv', '--csv', type=str, required=False, help="Path to the CSV file")
parser.add_argument('-mailto', '--mailto', type=str, required=False, help="Path to the mailto file")
parser.add_argument('-output', '--output', type=str, required=False, help="Path to the output folder")
parser.add_argument('-textsize', '--textsize', type=int, required=False, help="Size of the annotation text")

args = parser.parse_args()

# Variables
FileSize = 20
TextSize = 2 if args.textsize is None else args.textsize  # Default value of TextSize

# Check if any flags are present
if len(vars(args)) > 0 and any(vars(args).values()):
    InputDoc = args.csv
    OutputFolder = args.output
    MailFile = args.mailto
    MailAddress, MailSubject, MailText, TopText = read_mail_settings(MailFile)
    WantPicture = False
    ExtraPic = None
    run_logic(InputDoc, OutputFolder, FileSize, TextSize, MailAddress, MailSubject, MailText, TopText, WantPicture, ExtraPic)
else:
    root = Tk()
    root.withdraw()
    messagebox.showinfo("QR-MassCode", "Select the CSV file containing the room information...")
    InputDoc = filedialog.askopenfilename(title="WSelect the CSV file:")
    OutputFolder = filedialog.askdirectory(title="Choose the directory where the QR images should be placed:")
    MailFile = filedialog.askopenfilename(title="Select the Mailto txt file:")
    MailAddress, MailSubject, MailText, TopText = read_mail_settings(MailFile)
    WantPicture = messagebox.askyesno("QR-MassCode", "Would you like to add an image to the center of the QR code?")
    ExtraPic = None
    if WantPicture:
        ExtraPic = filedialog.askopenfilename(title="Wählen Sie die Bilddatei aus:")
    run_logic(InputDoc, OutputFolder, FileSize, TextSize, MailAddress, MailSubject, MailText, TopText, WantPicture, ExtraPic)
