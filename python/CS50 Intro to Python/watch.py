import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(html):
    # Extract YouTube URL from iframe src attribute
    pattern = r'<iframe.*?src="((?:https?:)?//(?:www\.)?youtube\.com/embed/([^"]+))".*?>'
    match = re.search(pattern, html)
    
    # If a match is found, return the shorter youtu.be equivalent
    if match:
        video_id = match.group(2)
        return f"https://youtu.be/{video_id}"
    
    # Return None if no YouTube URL is found
    return None


if __name__ == "__main__":
    main()