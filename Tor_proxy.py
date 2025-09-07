import socks
import socket
from config import Settings

def enable_tor_proxy():
    socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', Settings.TOR_SOCKS_PORT)
    socket.socket = socks.socksocket
  
