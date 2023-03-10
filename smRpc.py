
from pypresence import Presence
import time


client_id = "1082120410373562438"
RPC = Presence(client_id)

def enable():
    RPC.connect()

    RPC.update(
        state="In the SMILK shell (enablerpc)",
        large_image="icon"
    )