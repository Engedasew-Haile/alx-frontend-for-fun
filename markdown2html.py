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
