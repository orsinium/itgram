import asyncio
from datetime import date, datetime, time, timedelta
import os
from pathlib import Path
from random import randint
from telethon import TelegramClient

# Remember to use your own values from my.telegram.org!
client = TelegramClient('bot', os.environ['API_ID'], os.environ['API_HASH'])


async def schedule_post(send_on: date, path: Path) -> None:
    send_at = datetime.combine(send_on, time(15, 0, 0))
    send_at += timedelta(minutes=randint(0, 60))
    in10m = datetime.now() + timedelta(minutes=10)
    if send_at < in10m:
        send_at = in10m

    text = path.read_text()
    text = text.lstrip('-')
    text = text.split('\n---\n', maxsplit=1)[1]

    print(f'scheduling {path.stem}')
    await client.send_message(
        'itgram_channel',
        text,
        schedule=send_at,
        link_preview=False,
    )
    print(f'  scheduled at {send_at}')


async def main():
    async with client:
        for path in Path('content').glob('*/**/*.md'):
            send_on = date.fromisoformat(path.stem[:10])
            if send_on < date.today():
                continue
            await schedule_post(send_on, path)


if __name__ == '__main__':
    asyncio.run(main())
