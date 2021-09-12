import json

async def add_coin_listener(msg, ws, ws_client):
    print(msg)
    if msg["topic"] == "add_coin_listener":
        await ws_client.send(json.dumps({
                "type": "subscribe",
                "channels": [
                    {
                        "name": "ticker",
                        "product_ids": [
                            msg["coin_pair"]
                        ]
                    }
                ]
            }))
    if msg["topic"] == "remove_coin_listener":
        await ws_client.send(json.dumps({
                "type": "unsubscribe",
                "channels": [
                    {
                        "name": "ticker",
                        "product_ids": [
                            msg["coin_pair"]
                        ]
                    }
                ]
            }))
