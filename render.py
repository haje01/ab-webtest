import os
import time

from jinja2 import Environment, FileSystemLoader, select_autoescape

APP_NAME=os.environ['AB_APP_NAME']
SDK_TOKEN=os.environ['AB_SDK_TOKEN']
BASE_DIR=os.path.dirname(os.path.abspath(__file__))

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape()
)

events = [
    # 상품 조회
    dict(
        category='airbridge.ecommerce.productList.viewed',
        params=dict(
            productListID='36473926',
            products=[
                dict(
                    name='Google Pixel 3',
                    price=960000,
                    currency='KRW',
                    position=1
                )
            ]
        )
    ),
    # 상품 구매 
    dict(
        category='airbridge.ecommerce.order.completed',
        params=dict(
            products=[
                dict(
                    productID='1',
                    name='MacBook Pro',
                    price=2000000,
                    currency='KRW',
                    quantity=1,
                    position=1
                ),
                dict(
                    productID='2',
                    name='MacBook Air',
                    price=1500000,
                    currency='KRW',
                    quantity=2,
                    position=2
                )
            ]
        )
    ),
]    

users = [
    dict(
        user_id="user1",
        user_email="user1@example.com",
        user_phone="123-456-7890",
        age_group="30",
        gender="Female",
        events=events
    ),
    dict(
        user_id="user2",
        user_email="user2@example.com",
        user_phone="123-456-7890",
        age_group="40",
        gender="Male",
        events=events
    )    
]

base_data = dict(
    app_name=APP_NAME,
    sdk_token=SDK_TOKEN,
)

os.makedirs('tmp', exist_ok=True)
# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
tmpl = env.get_template('user.html')
# 모든 유저 순회하며
for i, user in enumerate(users):
    # 렌더링 결과 HTML 저장
    path = f"{BASE_DIR}/tmp/{user['user_id']}.html"
    data = {**base_data, **user}
    raw_html = tmpl.render(data)
    with open(path, 'w') as f:
        f.write(raw_html)

# index.html 저장
tmpl = env.get_template('index.html')
with open('index.html', 'w') as f:
    f.write(tmpl.render(dict(users=users)))