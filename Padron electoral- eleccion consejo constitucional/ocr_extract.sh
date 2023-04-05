#!/bin/bash

## pdf to img
directory="../pdf_images" # change the path

gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER -dFirstPage=1 -dLastPage=300 -sOutputFile=output_01.pdf input.pdf
gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER -dFirstPage=301 -dLastPage=600 -sOutputFile=output_02.pdf input.pdf
gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER -dFirstPage=601 -dLastPage=900 -sOutputFile=output_03.pdf input.pdf
gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER -dFirstPage=901 -dLastPage=1200 -sOutputFile=output_04.pdf input.pdf
gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER -dFirstPage=1201 -dLastPage=1500 -sOutputFile=output_05.pdf input.pdf
gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER -dFirstPage=1501 -dLastPage=1800 -sOutputFile=output_06.pdf input.pdf
gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER -dFirstPage=1801 -dLastPage=2100 -sOutputFile=output_07.pdf input.pdf
gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER -dFirstPage=2101 -dLastPage=2400 -sOutputFile=output_08.pdf input.pdf
gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER -dFirstPage=2401 -dLastPage=2700 -sOutputFile=output_09.pdf input.pdf
gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER -dFirstPage=2701 -dLastPage=3000 -sOutputFile=output_10.pdf input.pdf



################################################# STEP 1 #################################################

for i in {3..10}; do
 if [[ $i -eq 10 ]]; then
    gs -sDEVICE=jpeg -dBATCH -dNOPAUSE -r220 -dFirstPage=1 -dLastPage=300 -sOutputFile=$directory/image_$i/output_$i-%03d.jpg output_$i.pdf
  else
    gs -sDEVICE=jpeg -dBATCH -dNOPAUSE -r220 -dFirstPage=1 -dLastPage=300 -sOutputFile=$directory/image_$i/output_0$i-%03d.jpg output_0$i.pdf
 fi
done

################################################# STEP 2 #################################################

for i in {3..10}; do
  ## OCR of characters
  if [ -d "$directory/image_$i" ]; then
    for file in $directory/image_$i/*.jpg; do
        txt_file="${file%.*}.txt"
        if [ -f "$txt_file" ]; then
            echo "TXT file already exists for $file. Skipping OCR."
        else
            tesseract "$file" "${file%.*}" -l spa > "$txt_file"
            echo "OCR completed for $file."
        fi
    done
  fi
done

################################################# STEP 3 #################################################

cd "$directory"

for i in {1..10}; do
  directory_name="image_$i"
  cd "$directory_name"
  txt_files=$(ls *.txt | sort)
  for file in $txt_files; do
    cat "$file" >> all_$i.txt
  done
  cp "all_$i.txt" "$directory"
  cd ..
done

################################################# STEP 4 #################################################
cd "$directory"
#find . -name "all_*.txt" -type f -print0 | xargs -0 sed -i 's/TEMUCO\|MAPUCHE\|\.//g'
find . -type f -name "all_*.txt" -exec sed -i 's/\b\(TEMUCO\|MAPUCHE\|TEMUGO\)\b//g' {} \;

################################################# STEP 5 #################################################
find . -name "all_*.txt" -type f -print0 | while IFS= read -r -d '' file; do mv "$file" "${file%.txt}.csv"; done
