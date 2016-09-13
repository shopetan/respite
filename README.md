# Respuit
馬鹿野郎お前俺はreqruitのAPI使うぞお前

# Use Teck
- python(3.5)
- Flask(0.10.1)
- Flask-Cors(2.1.2)
- Flask_RESYful(0.3.5)

# usage

- query

```
$ curl -X GET "http://127.0.0.1:5000/hot_pepper?lat=34.65&lng=135.52&range=1"
```

- response

```
{
  "results": {
    "api_version": "1.26",
    "results_available": 7,
    "results_returned": "7",
    "results_start": 1,
    "shop": [
      {
        "access": "寺田町駅より西へ徒歩5分",
        "address": "大阪府大阪市天王寺区大道３-1-26ヌーベルハイツ1F",
        "band": "不可",
        "barrier_free": "なし",
        "budget": {
          "average": "700円",
          "code": "B001",
          "name": "～2000円"
        },
        "budget_memo": "",
        "capacity": "10",
        "card": "利用不可",
        "catch": "だしが決め手！ こだわりの卵",
        "charter": "貸切不可",
        "child": "お子様連れ歓迎",
        "close": "祝前日",
        "coupon_urls": {
          "mobile": "http://hpr.jp/S/S511.jsp?SP=J001127651&uid=NULLGWDOCOMO&vos=hpp336",
          "pc": "https://www.hotpepper.jp/strJ001127651/map/?vos=nhppalsa000016",
          "qr": "http://webservice.recruit.co.jp/common/qr?url=http%3A%2F%2Fhpr.jp%2FS%2FS511.jsp%3FSP%3DJ001127651%26uid%3DNULLGWDOCOMO%26vos%3Dhpp337",
          "sp": "https://www.hotpepper.jp/strJ001127651/scoupon/?vos=nhppalsa000016"
        },
        "course": "なし",
        "english": "なし",
        "equipment": "なし",
        "food": {
          "code": "R012",
          "name": "そば・うどん"
        },
        "free_drink": "なし",
        "free_food": "なし",
        "genre": {
          "catch": "本格肉うどん",
          "code": "G004",
          "name": "和食"
        },
        "horigotatsu": "なし",
        "id": "J001127651",
        "karaoke": "なし",
        "ktai": "つながる ：ＮＴＴドコモ／au／ソフトバンク",
        "ktai_coupon": "1",
        "large_area": {
          "code": "Z023",
          "name": "大阪"
        },
        "large_service_area": {
          "code": "SS20",
          "name": "関西"
        },
        "lat": "34.6505860815",
        "lng": "135.5209216035",
        "logo_image": "https://imgfp.hotp.jp/IMGH/77/82/P022607782/P022607782_69.jpg",
        "lunch": "なし",
        "middle_area": {
          "code": "Y325",
          "name": "天王寺"
        },
        "midnight": "営業していない",
        "mobile_access": "寺田町駅",
        "name": "本格肉うどん 牛若",
        "name_kana": "ほんかくにくうどん　うしわか",
        "non_smoking": "全面禁煙",
        "open": "月～金: 11:00～14:30 （料理L.O. 14:30 ドリンクL.O. 14:30）17:30～21:30 （料理L.O. 21:30 ドリンクL.O. 21:30）土、日、祝日: 11:00～21:30 （料理L.O. 21:30 ドリンクL.O. 21:30）",
        "open_air": "なし",
        "other_memo": "",
        "parking": "あり ：近隣にコインパーキングあり",
        "party_capacity": "10",
        "pet": "不可",
        "photo": {
          "mobile": {
            "l": "https://imgfp.hotp.jp/IMGH/31/11/P022623111/P022623111_168.jpg",
            "s": "https://imgfp.hotp.jp/IMGH/31/11/P022623111/P022623111_100.jpg"
          },
          "pc": {
            "l": "https://imgfp.hotp.jp/IMGH/31/11/P022623111/P022623111_238.jpg",
            "m": "https://imgfp.hotp.jp/IMGH/31/11/P022623111/P022623111_168.jpg",
            "s": "https://imgfp.hotp.jp/IMGH/31/11/P022623111/P022623111_58_s.jpg"
          }
        },
        "private_room": "なし",
        "service_area": {
          "code": "SA23",
          "name": "大阪"
        },
        "shop_detail_memo": "",
        "show": "なし",
        "small_area": {
          "code": "XEIX",
          "name": "寺田町"
        },
        "sommelier": "いない",
        "station_name": "寺田町",
        "tatami": "なし",
        "tv": "なし",
        "urls": {
          "mobile": "http://hpr.jp/strJ001127651/?uid=NULLGWDOCOMO&vos=hpp336",
          "pc": "https://www.hotpepper.jp/strJ001127651/?vos=nhppalsa000016",
          "qr": "http://webservice.recruit.co.jp/common/qr?url=http%3A%2F%2Fhpr.jp%2FstrJ001127651%2F%3Fuid%3DNULLGWDOCOMO%26vos%3Dhpp337"
        },
        "wedding": "",
        "wifi": "なし"
      }, ...
								        },
```

- また今度!
