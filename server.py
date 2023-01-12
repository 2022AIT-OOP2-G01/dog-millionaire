import socket
import threading
PORT = 50005
BUFFER_SIZE = 1024
#AF_INET=アドレスファミリーを示す関数　SOCK_STREAM=ソケットタイプを示す関数

def recv_client(sock, addr, id):
    print('Client connected', client)
    while True:
        #コネクションの相手側からsendを使用して送られた
        # オブジェクトを返す何か受け取るまでブロック
        data = sock.recv(BUFFER_SIZE).decode()
        print(data)
        if data == 'q':
            break
        sock.send(data.upper( ).encode())

         

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
    #ソケット登録   
    s.bind(('10.1.53.93', PORT))
    #ソケット接続待機
    s.listen()

    for i in range(4):
        (connection, client) = s.accept()
        # スレッドクラスのインスタンス化
        thread = threading.Thread(target=recv_client, args=(connection, client, i))
        # スレッド処理開始
        thread.start()
