'''
import sys
import os.path
import markdown

"""
 a script markdown2html.py that takes an argument 2 strings:

First argument is the name of the Markdown file
Second argument is the output file name
"""

if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

md_file = sys.argv[1]
html_file = sys.argv[2]
"""
arguments is less than 2: print in STDERR Usage: ./markdown2html.py README.md README.html and exit 1
Markdown file doesn’t exist: print in STDER Missing <filename> and exit 1
Otherwise, print nothing and exit 0
"""
if not os.path.isfile(md_file):
    print(f"Missing {md_file}", file=sys.stderr)
    sys.exit(1)

with open(md_file, "r") as f:
    md = f.read()

html = markdown.markdown(md)

with open(html_file, "w") as f:
    f.write(html)

'''
#!/usr/bin/python3
"""
This is a script to convert a Markdown file to HTML.

Usage:
    ./markdown2html.py [input_file] [output_file]

Arguments:
    input_file: the name of the Markdown file to be converted
    output_file: the name of the output HTML file

Example:
    ./markdown2html.py README.md README.html
"""

import sys
import markdown

def main():
    """
    Main function to convert a Markdown file to HTML.
    """
    # Check if the correct number of arguments were passed in
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: ./markdown2html.py [input_file] [output_file]\n")
        sys.exit(1)

    # Get the input and output file names
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input file exists
    try:
        with open(input_file, 'r') as f:
            pass
    except FileNotFoundError:
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

    # Convert the Markdown to HTML
    with open(input_file, 'r') as f:
        html = markdown.markdown(f.read())

    # Write the HTML to the output file
    with open(output_file, 'w') as f:
        f.write(html)

    # Exit successfully
    sys.exit(0)

if __name__ == "__main__":
    main()
