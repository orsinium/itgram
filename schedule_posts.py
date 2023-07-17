import asyncio
from datetime import date, datetime, time, timedelta
import os
from pathlib import Path
from random import randint
from telethon import TelegramClient
from telethon.types import Message
from zoneinfo import ZoneInfo

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
    text = text.split('\n---\n', maxsplit=1)[1]

    print(f'scheduling {path.stem}')
    send_at
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
