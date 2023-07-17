from pathlib import Path
import re

REX_LINK = re.compile(r'https?\://[^\s\)\>]+')
REX_BAD_TITLE = re.compile(r'title\: [0-9]+')


def get_links(text: str) -> list[str]:
    return REX_LINK.findall(text)


def detect_title(text: str) -> str | None:
    return detect_title_from_url(text) or get_title_from_first_link_text(text)


def get_title_from_first_link_text(text: str) -> str | None:
    text = text.split('layout: post\n---')[-1]
    text = text.strip()
    if not text:
        return None
    if text[0] != '[':
        text = text[1:]
    text = text.lstrip('📊🔧🐍🏃🦀🐚📄🔧🎥')
    if text[0] != '[':
        text = text[1:]
    text = text.strip()
    if text[0] != '[':
        return None
    title = text.lstrip('[').split(']')[0]
    if title[1] == ' ':
        title = title[2:]
    return f'"{title}"'


def detect_title_from_url(text: str) -> str | None:
    links = get_links(text)
    if not links:
        return None
    link = links[0]
    if not link.startswith('https://github.com/'):
        return None
    return link.rstrip('/').split('/')[-1]


for dir_path in sorted(Path('content', 'posts').iterdir()):
    for path in dir_path.iterdir():
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
