from fastapi import WebSocket, APIRouter, WebSocketDisconnect

router = APIRouter()
active_connections = []


@router.websocket("/ws/table-status")
async def table_status_ws(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received: {data}")
            for connection in active_connections:
                await connection.send_text(f"Broadcast: {data}")
    except WebSocketDisconnect:
        active_connections.remove(websocket)
