from pathlib import Path

import re
import yaml

REX_SLUG = re.compile(r'[a-zA-Z\-\.\s]{,20}')


for dir_path in sorted(Path('content', 'posts').iterdir()):
    for path in dir_path.iterdir():
        text = path.read_text()
        try:
            int(path.stem[11:])
        except ValueError:
            continue
        meta = text.split('---\n')[1]
        title = str(yaml.safe_load(meta)['title'])
        if not REX_SLUG.fullmatch(title):
            continue
        title = title.lower()
        title = title.replace('.', '-')
        title = title.replace(' ', '-')
        new_path = path.parent / f'{path.stem[:10]}-{title}.md'
        path.rename(new_path)
