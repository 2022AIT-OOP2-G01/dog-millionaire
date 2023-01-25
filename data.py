import json

def get_client_data(cardnum):

   #自分が出したカード
    played_card = 5
    
    return played_card
   
def get_server_data():
    server_data = {
        #プレイヤーID
        "player_id": '',
        #場に出ているカード
        "field_card": "",
        #誰のターンか
        "turn": '',
        #ゲームが終了しているか
        "gameset":True,
        #誰が買ったか
        "winer": '',
        #それぞれのプレイヤーの残り枚数
        "remaining_number_list":[],
        #自分の持っているカード
        "my_card_list":[]
    } 

    return json.dumps(server_data)