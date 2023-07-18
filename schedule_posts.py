import asyncio
import os
from datetime import date, datetime, time, timedelta
from pathlib import Path
from random import randint
from typing import Any
from zoneinfo import ZoneInfo

import yaml
from telethon import TelegramClient
from telethon.types import Message


# Remember to use your own values from my.telegram.org!
client = TelegramClient('bot', os.environ['API_ID'], os.environ['API_HASH'])
CHANNEL = 'itgram_channel'
TZ = ZoneInfo('Europe/Amsterdam')


async def scheduled() -> list[date]:
    result = []
    message: Message
    async for message in client.iter_messages(CHANNEL, scheduled=True):
        assert message.date
        result.append(message.date.date())
    return result


async def schedule_post(send_on: date, path: Path) -> None:
    send_at = datetime.combine(send_on, time(15, 30, 0, tzinfo=TZ))
    send_at += timedelta(minutes=randint(0, 60))
    in10m = datetime.now(TZ) + timedelta(minutes=10)
    if send_at < in10m:
        send_at = in10m

    text = path.read_text()
    text = text.lstrip('-')
    text = text.rstrip()
    meta_raw, text = text.split('\n---\n', maxsplit=1)

    meta: dict[str, Any] = yaml.safe_load(meta_raw)
    assert path.stem.startswith(meta['date'].isoformat())
    tags = meta.get('tags')
    if tags:
        text += '\n\n' + ' '.join(f'#{tag}' for tag in sorted(tags))

    print(f'scheduling {path.stem}')
    await client.send_message(
        CHANNEL,
        text,
        schedule=send_at,
        link_preview=False,
    )
    print(f'  scheduled at {send_at}')


async def main():
    async with client:
        dates = await scheduled()
        for path in Path('content').glob('*/**/*.md'):
            send_on = date.fromisoformat(path.stem[:10])
            if send_on < date.today():
                continue
            if send_on in dates:
                print(f'{path.stem} already scheduled on {send_on}')
                continue
            await schedule_post(send_on, path)


if __name__ == '__main__':
    asyncio.run(main())
