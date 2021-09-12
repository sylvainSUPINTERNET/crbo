import websockets
import _thread
import time
import json
import asyncio

from services.ws import add_coin_listener
from services.ws_conn import WsConn

# Working for only one since this app is only one ws connection for me
cl = WsConn()

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

async def client():
    async with websockets.connect("wss://ws-feed.pro.coinbase.com") as websocket:
        cl.client = websocket # set to instance the ws connection to be able to send data / send data to the coinbase ws
        while True: # run forever waiting for new data
            data = await websocket.recv()
            print(data)

async def echo(websocket, path):
    async for message in websocket:
        print(cl.client)
        await add_coin_listener(json.loads(message), websocket, ws_client=cl.client)


loop = asyncio.get_event_loop()
loop.create_task(main())
loop.create_task(client())
loop.run_forever()

# asyncio.run(main())
# ws_coinbase.run_forever()

# def on_message(ws, message):
#     jsoned = json.loads(message)

#     if  jsoned["topic"] :
#         add_coin_listener(jsoned, ws)

# def on_error(ws, error):
#     print(error)

# def on_close(ws, close_status_code, close_msg):
#     print("### closed ###")

# def on_open(ws):
#     print("open")
#     # def run(*args):
#     #     ws.send(json.dumps({
#     #         "type": "subscribe",
#     #         # "product_ids": [
#     #         #     "ETH-EUR"
#     #         # ],
#     #         "channels": [
#     #             {
#     #                 "name": "ticker",
#     #                 "product_ids": [
#     #                     "ETH-EUR",
#     #                     "BTC-EUR"
#     #                 ]
#     #             }
#     #         ]
#     #         # "channels": ["ticker"]
#     #         # "channels": [
#     #         #     "level2",
#     #         #     "heartbeat",
#     #         #     {
#     #         #         "name": "ticker",
#     #         #         "product_ids": [
#     #         #             "ETH-EUR"
#     #         #         ]
#     #         #     }
#     #         # ]
#     #     }))
#     # _thread.start_new_thread(run, ())

# if __name__ == "__main__":
#     websocket.enableTrace(True)
#     ws = websocket.WebSocketApp("wss://ws-feed.pro.coinbase.com",
#                               on_open=on_open,
#                               on_message=on_message,
#                               on_error=on_error,
#                               on_close=on_close)

#     ws.run_forever()