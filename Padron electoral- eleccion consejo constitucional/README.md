# PDF to Image to Text by OCR recognition bash Script

This bash script converts PDF files to JPEG images and performs OCR on the images to extract text from them.

## Requirements
- Ghostscript
- Tesseract OCR

## Usage
Clone the repository and navigate to the directory containing the script.
Modify the directory variable in the script to specify the location of the PDF files to be converted.
Execute the script in the terminal using the command ./ocr_extract.sh.

## Steps
Convert PDF files to JPEG images using Ghostscript.
Perform OCR on the JPEG images using Tesseract OCR.
Concatenate the text files generated from each image into a single file.
Replace specific words with blank spaces in the concatenated file.
Rename the concatenated text file to a CSV file.

**Step 1**: Convert PDF files to JPEG images
The script loops through the PDF files from image_3.pdf to image_10.pdf and uses Ghostscript to convert each file to a set of JPEG images. The images are saved to folders named image_3 through image_10.

**Step 2**: Perform OCR on the JPEG images
The script loops through the folders containing the JPEG images and performs OCR on each image using Tesseract OCR. The text files generated from the OCR process are saved in the same folder as the corresponding image.

**Step 3**: Concatenate text files into a single file
The script navigates to each image folder and concatenates the text files generated from OCR into a single file named all_$i.txt, where $i is the number of the image folder.

**Step 4**: Replace specific words with blank spaces
The script uses the sed command to find and replace specific words in the concatenated text files with blank spaces. The words to be replaced are TEMUCO, MAPUCHE, and TEMUGO.

**Step 5**: Rename text file to CSV file
The script renames the concatenated text files with the extension .csv using the mv command.
