import os 

from flask import Flask, render_template, request 

app = Flask(__name__)

APP_NAME = os.environ.get('ABTEST_APP')
print(f'APP_NAME: {APP_NAME}')
assert APP_NAME is not None
SDK_TOKEN = os.environ.get('ABTEST_TOKEN')
assert SDK_TOKEN is not None
print(f'SDK_TOKEN: {SDK_TOKEN}')

events = [
    # 로그인
    dict(
        category='airbridge.user.signin',
        label='',
        action='',
        params=dict(
        )
    ),
    # 튜토리얼 완료
    dict(
        category='airbridge.completeTutorial',
        label='52',
        action='fly tutorial',
        params=dict(
            ProductID=30372425,
            Description='fly tutorial'),
    ),
    # 레벨 달성
    dict(
        category='airbridge.achieveLevel',
        label='52',
        action='10',
        params=dict(
            Level=10),
    ),
    # 메인 화면 조회
    dict(
        category='airbridge.ecommerce.home.viewed',
        label='',
        action='',
        value='',
        params=dict()
    ),
    # 상품 주문 완료
    dict(
        category='airbridge.ecommerce.order.completed',
        label='first_purchase_package',
        action='dia',
        value='55000',
        params=dict(
            transaction_id=84689425,
            total_revenue=55000,
            currency="KRW",
            total_quantity=1,
            product_id=834828
        )
    ),
    # 첫 번째 메인 퀘스트 클리어
    dict(
        category='complete_quest',
        label='01',
        action='First Main Quest Clear',
        params=dict(
        )
    ),
    # 첫 필드 사냥
    dict(
        category='complete_quest',
        label='01',
        action='First Field Battle',
        params=dict(
        )
    ),
    # 장비 강화
    dict(
        category='complete_quest',
        label='01',
        action='Equipment Engancement 1 time',
        params=dict(
        )
    ),
    # 첫 번째 스킬 습득
    dict(
        category='complete_quest',
        label='01',
        action='First Skill Acquisition',
        params=dict(
        )
    ),
    # 최초 BOSS 사냥
    dict(
        category='complete_quest',
        label='01',
        action='First Boss Battle',
        params=dict(
        )
    ),
    # 첫 혜택카드 사용
    dict(
        category='complete_quest',
        label='01',
        action='Use Benefits Card',
        params=dict(
        )
    ),
    # 아이템 합성
    dict(
        category='complete_quest',
        label='01',
        action='First Compose Item',
        params=dict(
        )
    ),
    # 블러드캐슬 첫 클리어
    dict(
        category='complete_quest',
        label='01',
        action='First Quest Clear (Blood Castle)',
        params=dict(
        )
    ),
    # 레벨 10 달성
    dict(
        category='complete_event',
        label='gold',
        action='Level 10',
        params=dict(
        )
    ),
    # 레벨 20 달성
    dict(
        category='complete_event',
        label='gold',
        action='Level 50',
        params=dict(
        )
    ),
    # 레벨 30 달성
    dict(
        category='complete_event',
        label='gold',
        action='Level 30',
        params=dict(
        )
    ),
    # 유저 로그아웃
    dict(
        category='airbridge.user.signout',
        label='',
        action='',
        params=dict(
        )
    )
]   


@app.route('/')
def user():
    game_id = request.args.get('game_id')
    plat_id = request.args.get('plat_id')
    email = request.args.get('email')
    return render_template('user.html', app_name=APP_NAME, sdk_token=SDK_TOKEN,
                           game_id=game_id, plat_id=plat_id, email=email, 
                           age_group='30', gender='Male', events=events)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
