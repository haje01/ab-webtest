import asyncio
import random

from faker import Faker 
from playwright.async_api import async_playwright

USER_CNT = 50

fake = Faker()

users = []
for i in range(USER_CNT):
    game_id = fake.unique.random_int(min=111111, max=999999)
    plat_id = fake.unique.random_int(min=111111, max=999999)
    email = fake.email()
    users.append([game_id, plat_id, email])


def handle_console_msg(msg):
    print(f"{msg.type}: {msg.text}")


async def visit(game_id, plat_id, email):
    print(f"visit {game_id} {plat_id}")
    sleep = random.randint(0, 50)
    await asyncio.sleep(sleep)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        page.on('console', handle_console_msg)

        await page.goto(f"http://server?game_id={game_id}&plat_id={plat_id}&email={email}")
        # wait for send
        await asyncio.sleep(5)
        await browser.close()


async def main():
    tasks = []
    for user in users:
        task = asyncio.ensure_future(visit(*user))
        tasks.append(task)

    ress = await asyncio.gather(*tasks)
    for res in ress:
        print(res)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
