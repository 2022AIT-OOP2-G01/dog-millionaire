# dog-millionaire
犬富豪
- 進捗情報(Trello)：https://trello.com/b/bOc3UeUV/%E5%A4%A7%E5%AF%8C%E8%B1%AA
## 役割
### クライアント側
石垣・西山
### 通信
門田・須田
### サーバ側
小川・高林

## 基本ルール
- カードの強さの順(弱 3,4,5,6,7,8,9,10,11,12,1,2 強)
- 人数（４人）
- 順にカードを出す  
- カードがなくなったら勝ち  
- ３人上がるまで続ける  
- 1枚しか出せない 
- passあり（戻ってきたらpass不可）  

## 追加ルール
- 8切り
- １１バック
- ５飛ばし

## 使用するライブラリ
- Python=3.10.6
- Pyside6

## 実行方法
<pre>
$ git clone https://github.com/2022AIT-OOP2-G01/dog-millionaire.git
$ cd dog-millionaire
$ python server.py
$ python window.py
</pre>

## 通信方法
python  
ソケット通信  
手順  
1.4人が接続されるまで保持されて確認されると一斉にサーバー
からデータが送られる（ゲームの始まり）

2.送られたデータによりゲームが進み、クライアントは出したカードを返す。
  サーバーからクライアントに送るデータを取得できる関数の定義(get_server_data())
  クライアントからサーバーに送るデータを取得できる関数の定義(get_client_data())
```
ゲーム開始時：「サーバー＞クライアント」
手番時：「サーバーー＞クライアント」下記のゲーム情報
      「クライアントー＞サーバー」プレイヤーが出したカード

{
        #プレイヤーID
        "player_id": 7,
        #場に出ているカード
        "field_card": 3,
        #誰のターンか
        "turn": 1,
        #ゲームが終了しているか
        "gameset": False,
        #誰が買ったか
        "winer": [],
        #それぞれのプレイヤーの残り枚数
        "remaining_number_list":[],
        #自分の持っているカード
        "my_card_list":[]
    } 
    
    
```
3.終わるタイミング　　
・プレイヤーが3人になった場合
```
if put_card_index == -1:
   print("Pass!!")
   break
```


## クライアント側
python
- PySide6

## サーバ側
python
