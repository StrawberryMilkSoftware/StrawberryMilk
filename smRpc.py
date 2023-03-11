
from pypresence import Presence
import time


client_id = "1082120410373562438"
try:
    RPC = Presence(client_id)
except:
    print("")

def enable():
    RPC.connect()

    RPC.update(
        state="In the SMILK shell (enablerpc)",
        large_image="icon"
    )