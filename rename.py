from pathlib import Path
import re

REX_LINK = re.compile(r'https?\://[^\s\)\>]+')
REX_BAD_TITLE = re.compile(r'title\: [0-9]+')


def get_links(text: str) -> list[str]:
    return REX_LINK.findall(text)


def detect_title(text: str) -> str | None:
    links = get_links(text)
    if not links:
        return None
    link = links[0]
    if not link.startswith('https://github.com/'):
        return None
    return link.rstrip('/').split('/')[-1]


for path in sorted(Path('posts').iterdir()):
    text = path.read_text()
    if not REX_BAD_TITLE.findall(text):
        print(f'skipping {path.name}, already has a title')
        continue
    new_title = detect_title(text)
    if not new_title:
        print(f'skipping {path.name}, cannot detect title')
        continue
    text = REX_BAD_TITLE.sub(f'title: {new_title}', text, count=1)
    path.write_text(text)
