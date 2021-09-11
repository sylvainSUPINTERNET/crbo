import websocket
import _thread
import time
import json

def on_message(ws, message):
    jsoned = json.loads(message)
    print(jsoned);
    print(jsoned["type"])

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        ws.send(json.dumps({
            "type": "subscribe",
            "product_ids": [
                "ETH-EUR"
            ],
            "channels": ["ticker"]
            # "channels": [
            #     "level2",
            #     "heartbeat",
            #     {
            #         "name": "ticker",
            #         "product_ids": [
            #             "ETH-EUR"
            #         ]
            #     }
            # ]
        }))
    _thread.start_new_thread(run, ())

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws-feed.pro.coinbase.com",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever()