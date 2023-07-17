

from pathlib import Path


EMOJI = {
    '🐚': 'shell',
    '📄': 'article',
    '🔧': 'tool',
    '🎥': 'video',

    '🐍': 'python',
    '🏃': 'golang',
    '🦀': 'rust',
}


def get_hashtags(text: str) -> set[str]:
    text = text.strip()
    text = text.splitlines()[-1]
    if not text.startswith('#'):
        return set()
    text = text.replace('#', '')
    return set(text.lower().split())


def get_emoji_tags(text: str) -> set[str]:
    result = set()
    for emoji, tag in EMOJI.items():
        if emoji in text:
            result.add(tag)
    return result


for dir_path in sorted(Path('content', 'posts').iterdir()):
    for path in dir_path.iterdir():
        text = path.read_text()
        if 'tags: []' not in text:
            print(f'skipping {path.name}, already has tags')
            continue
        tags = sorted(get_hashtags(text) | get_emoji_tags(text))
        if not tags:
            print(f'skipping {path.name}, cannot detect tags')
            continue
        text = text.replace('tags: []', f'tags: [{", ".join(tags)}]')
        path.write_text(text)
