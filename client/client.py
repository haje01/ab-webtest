import os
import asyncio
import random

from faker import Faker 
from playwright.async_api import async_playwright

USER_CNT = 50

fake = Faker()

users = []
# /data 에 유저 정보 파일이 없으면 생성
if not os.path.isfile('/data/users.csv'):
    print("create /data/users.csv")
    with open('/data/users.csv', 'w') as f:
        # 유저 정보 생성
        for i in range(USER_CNT):
            game_id = fake.unique.random_int(min=111111, max=999999)
            plat_id = fake.unique.random_int(min=111111, max=999999)
            email = fake.email()
            user = (game_id, plat_id, email)
            users.append(user)
            # 유저 정보 저장
            f.write(','.join(map(str, user)) + '\n')
# 있으면 읽어서 유저 정보 리스트 생성
else:
    print("load /data/users.csv")
    with open('/data/users.csv', 'r') as f:
        for line in f:
            user = line.strip().split(',')
            users.append(user)

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
