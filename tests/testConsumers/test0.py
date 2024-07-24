import asyncio
import json

import websockets


async def test_chat_consumer():
    uri = "ws://localhost:8000"  # Update this URI if your server is running on a different address or path

    async with websockets.connect(uri) as websocket:
        # Receive the welcome message
        welcome_message = await websocket.recv()
        print("Received:", welcome_message)

        # Send a chat message
        chat_message = {
            "type": "chat_message",
            "name": "TestUser",
            "message": "Hello, this is a test message.",
        }
        await websocket.send(json.dumps(chat_message))
        print("Sent:", chat_message)

        # Receive the echoed chat message
        echoed_message = await websocket.recv()
        print("Received:", echoed_message)


# Run the test
asyncio.get_event_loop().run_until_complete(test_chat_consumer())
