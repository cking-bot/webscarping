#!/Users/king/webscraping/.venv/bin/python3
"""mapit.py

Launch a map in the browser using an address from the command line or clipboard.
"""

import webbrowser
import sys
import pyperclip


if len(sys.argv) > 1:
    # Get address from command line.
    address = " ".join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open(f"https://www.google.com/maps/place/{address}")

# TODO: Get address from clipboard.