from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio
import redis

app = FastAPI()

redis_conn = None

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    global redis_conn
    if redis_conn is None:
        redis_conn = redis.Redis(host='localhost', port=6379)

    pubsub = redis_conn.pubsub()
    pubsub.subscribe("chat")

    try:
        while True:
            message = pubsub.get_message()
            if message and message['type'] == 'message':
                await websocket.send_text(message['data'].decode("utf-8"))
    except WebSocketDisconnect:
        pass
    finally:
        pubsub.unsubscribe("chat")
