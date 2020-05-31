from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.homework_0530                 # 'homework_0530'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])
def write_orders():
    # buyer_receive로 클라이언트가 준 buyer 가져오기
    buyer_receive = request.form['buyer_give']
    # count_receive로 클라이언트가 준 count 가져오기
    count_receive = request.form['count_give']
    # address_receive로 클라이언트가 준 address 가져오기
    address_receive = request.form['address_give']
    # phone_receive로 클라이언트가 준 phone 가져오기
    number_receive = request.form['number_give']

    # DB에 삽입할 order 만들기
    order = {
       'buyer': buyer_receive,
       'count': count_receive,
       'address': address_receive,
       'number': number_receive
    }
    # reviews에 review 저장하기
    db.orders.insert_one(order)
    # 성공 여부 & 성공 메시지 반환
    return jsonify({'result': 'success', 'msg': '주문이 성공적으로 요청되었습니다.'})
    return jsonify({'result':'success', 'msg': '이 요청은 POST!'})


@app.route('/orders', methods=['GET'])
def read_orders():
    orders = list(db.orders.find({},{'_id':0}))
    return jsonify({'result':'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)