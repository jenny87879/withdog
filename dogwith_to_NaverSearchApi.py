import requests
import pprint
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.withdog_cafe

# 네이버 검색 API 신청을 통해 발급받은 아이디와 시크릿 키를 입력합니다.
client_id = "1Xsii9AuUSgWE7d_7Fuh"
client_secret = "It9yaARp4U"


@app.route('/api/search', methods=['GET'])
def get_place():
    places = requests.args.get(data)
    print(places)
    return jsonify({'result': 'success', 'msg': '이 요청은 GET!', 'items_list': places})


# 네이버 검색 API 신청을 통해 발급받은 아이디와 시크릿 키를 입력합니다.
client_id = "1Xsii9AuUSgWE7d_7Fuh"
client_secret = "It9yaARp4U"

keyword = place
api_url = f"https://openapi.naver.com/v1/search/local.json?query={keyword}&display=500&start=1&sort=comment"
# 아이디와 시크릿 키를 부가 정보로 같이 보냅니다.
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}
# 검색 결과를 data에 저장합니다.
resp = requests.get(api_url, headers=headers)
# 받아온 JSON 결과를 딕셔너리로 변환합니다.
data = resp.json()
print(resp)
# 검색 결과 중 items를 꺼내어 반환합니다.
pprint.pprint(data)
