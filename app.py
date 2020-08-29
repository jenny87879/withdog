import pprint

# import requests
# from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request
from pip._vendor import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/place_save')
def move_page():
    return render_template('place save.html', title='장소 저장')


# client = MongoClient(sss'localhost', 27017)
# db = client.withdog_cafe

# 네이버 검색 API 신청을 통해 발급받은 아이디와 시크릿 키를 입력합니다.
client_id = "1Xsii9AuUSgWE7d_7Fuh"
client_secret = "It9yaARp4U"


@app.route('/api/search', methods=['GET'])
def get_place():
    place = request.args.get("searchWord")
    print(place)

    # 네이버 검색 API 신청을 통해 발급받은 아이디와 시크릿 키를 입력합니다.
    client_id = "1Xsii9AuUSgWE7d_7Fuh"
    client_secret = "It9yaARp4U"
    keyword = place
    api_url = "https://openapi.naver.com/v1/search/local.json?query=" + keyword + "&display=500&start=1&sort=comment"
    # 아이디와 시크릿 키를 부가 정보로 같이 보냅니다.
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}
    # 검색 결과를 data에 저장합니다.
    resp = requests.get(api_url, headers=headers)
    # 받아온 JSON 결과를 딕셔너리로 변환합니다.
    data = resp.json()
    # 검색 결과 중 items를 꺼내어 반환합니다.
    pprint.pprint(data)

    return jsonify({'result': 'success', 'msg': 'GET요청 성공', 'items_list': data})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
