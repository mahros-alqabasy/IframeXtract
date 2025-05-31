# iframextract/cli.py

import argparse
import os
from iframextract.extractor import (
    extract_iframes_from_file,
    extract_iframes_from_directory,
)


# colorization rich package
from rich.console import Console
from rich.text import Text

console = Console()


# code
def run_cli():
    parser = argparse.ArgumentParser(
        description="Extract <iframe> elements from HTML files into standalone HTML documents.",
        epilog='Examples:\n  iframextract -i index.html -o output_dir -f "{filename}_{iframe_index}.html"',
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "-i", "--input", required=True, help="Input HTML file or directory"
    )
    parser.add_argument(
        "-o", "--output", default=None, help="Output directory for extracted iframes"
    )
    parser.add_argument(
        "-f",
        "--format",
        default="{filename}_{iframe_index}.html",
        help="Filename format for output (use: {filename}, {iframe_index}, {iframe_title})",
    )
    parser.add_argument("--version", action="version", version="IframeXtract 1.0.0")

    args = parser.parse_args()

    input_path = os.path.abspath(args.input)
    output_dir = (
        os.path.abspath(args.output) if args.output else os.path.dirname(input_path)
    )

    if os.path.isfile(input_path):
        extract_iframes_from_file(input_path, output_dir, args.format)
    elif os.path.isdir(input_path):
        extract_iframes_from_directory(input_path, output_dir, args.format)
    else:
        # print(f"Error: input path '{input_path}' is not valid.")
        console.print(
            f"[bold red]Error:[/] input path '{input_path}' is not valid.", style="red"
        )


# use those for colorized

# Replace print() calls with:
# console.print(
#     f"[bold green]Extracted iframe '{title}'[/] to [cyan]{output_file_path}[/]"
# )


# for errors
# console.print(
#     f"[bold red]Error:[/] input path '{input_path}' is not valid.", style="red"
# )
