# whatsapp-parser
WhatsApp Export Parser -> CSV/Image Viewing

Quick script to convert a WhatsApp export `_chat.txt` file and media to a more friendly CSV format with clickable links for media files. 

Requires Regex `pip install regex`.

Simply drop the script into your directory with your `_chat.txt` file, cut and paste your media files into a folder in the same directory named `media` and run the script with `python3 wotsappenin.py`.

Have tried to account for various differences in `_chat.txt` files including embed handling (quick and dirty).
