
import re

def parse_range(text):
    m = re.search(r"(\d+)-(\d+)", text)
    if m:
        return int(m.group(1)), int(m.group(2))
    return None
