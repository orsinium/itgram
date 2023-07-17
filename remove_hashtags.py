from pathlib import Path


for dir_path in sorted(Path('content', 'posts').iterdir()):
    for path in dir_path.iterdir():
        text = path.read_text()
        text = text.rstrip()
        text, _, last_line = text.rpartition('\n')
        if last_line.startswith('#'):
            path.write_text(text.rstrip() + '\n')
