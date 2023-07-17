from pathlib import Path


for dir_path in sorted(Path('content', 'posts').iterdir()):
    for path in dir_path.iterdir():
        text = path.read_text()
        try:
            post_id = int(path.stem[11:])
        except ValueError:
            continue
        text = text.replace(
            'layout: post',
            f'layout: post\ntelegram_id: {post_id}',
        )
        path.write_text(text)
