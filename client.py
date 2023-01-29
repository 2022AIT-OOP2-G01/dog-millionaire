import socket
import json

PORT = 50000
BUFFER_SIZE = 1024
IP = "10.1.21.148"

def check_strength(top, put, revolution):
    st = [12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]
    if st[int(top[1:])-1] < st[int(put[1:])-1] and not revolution:
        return True
    elif st[int(top[1:])-1] > st[int(put[1:])-1] and revolution:
        return True
    else:
        return False

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((IP, PORT))
    server_data = s.recv(BUFFER_SIZE).decode()

    while True:
        server_data = s.recv(BUFFER_SIZE).decode()
        print(server_data)

        json_obj  = json.loads(server_data)
        my_card_list = json_obj['my_card_list']
        player_id = int(json_obj['player_id'])
        turn = int(json_obj['turn'])
        field_card = json_obj['field_card']
        revolution = json_obj['revolution']
        
        #player_idとturnが一緒なら自分の手札を表示
        if player_id == turn:
            print(my_card_list)
            #場のカードを表示
            print('場のカード',field_card)
            #自分が出すカードをインデックスで指定
            while True:
                client_data = input('あなたの番です。何を出しますか？ > ')
                if check_strength(field_card, my_card_list[int(client_data)], revolution):
                    break
                print('このカードは出せません')
            #サーバーに自分の出したカードのデータをエンコードして送信
            s.send(client_data.encode())
        