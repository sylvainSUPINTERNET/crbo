import websockets
import _thread
import time
import json
import asyncio

from services.ws import add_coin_listener


ws_client = "";

async def echo(websocket, path):
    async for message in websocket:
        print("MESSAGE")
        await add_coin_listener(json.loads(message), websocket, ws_client=ws_client)
        # await websocket.send(message)

async def main():
    print("main")
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

async def client():
    async with websockets.connect("wss://ws-feed.pro.coinbase.com") as websocket:
        await websocket.send('{"type":"subscribe","channels":[{"name":"ticker","product_ids":["BTC-EUR"]}]}')
        ws_client = websocket
        data = await websocket.recv()
        print(data)

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