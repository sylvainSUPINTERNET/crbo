import json

async def add_coin_listener(msg, ws, ws_client):
    if msg["topic"] == "add_coin_listener":
        print("ok")
        await ws_client.send(json.dumps({
                "type": "subscribe",
                "channels": [
                    {
                        "name": "ticker",
                        "product_ids": [
                            msg["COIN_PAIR"]
                        ]
                    }
                ]
            }))