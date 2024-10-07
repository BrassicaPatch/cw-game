import sys
import socket
import selectors
import traceback
import struct

import libclient

class Connection_Manager:

    def __init__(self):
        self.sel
        self.addr
        self.sock

    async def send_message(ip, name, msg):

        def create_request(action, name, value):
            if action == "message":
                return dict(
                    type="text/json",
                    encoding="utf-8",
                    content=dict(action=action, name=name, value=value),
                )
            else:
                return dict(
                    type="binary/custom-client-binary-type",
                    encoding="binary",
                    content=bytes(action + value, encoding="utf-8"),
                )

        sel = selectors.DefaultSelector()

        request = create_request('message', name, msg)

        addr = (ip, 65432)
        print("starting connection to", addr)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        message = libclient.Message(sel, sock, addr, request)
        sel.register(sock, events, data=message)

        try:
            while True:
                events = sel.select(timeout=1)
                for key, mask in events:
                    message = key.data
                    try:
                        message.process_events(mask)
                    except Exception:
                        print(
                            "main: error: exception for",
                            f"{message.addr}:\n{traceback.format_exc()}",
                        )
                        message.close()
                # Check for a socket being monitored to continue.
                if not sel.get_map():
                    break
        except KeyboardInterrupt:
            print("caught keyboard interrupt, exiting")
        finally:
            sel.close()

    # async def open_connection(self, ip, name):

    #     def create_request(action, value):
    #         if action == "set_name":
    #             return dict(
    #                 type="text/json",
    #                 encoding="utf-8",
    #                 content=dict(action=action, value=value),
    #             )
    #         elif action == "message":
    #             return dict(
    #                 type="text/json",
    #                 encoding="utf-8",
    #                 content=dict(action=action, value=value),
    #             )
    #         else:
    #             return dict(
    #                 type="binary/custom-client-binary-type",
    #                 encoding="binary",
    #                 content=bytes(action + value, encoding="utf-8"),
    #             )

    #     self.sel = selectors.DefaultSelector()

    #     request = create_request('set_name', name)

    #     self.addr = (ip, 65432)
    #     print("starting connection to", self.addr)
    #     self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     self.sock.setblocking(False)
    #     self.sock.connect_ex(self.addr)
    #     events = selectors.EVENT_READ | selectors.EVENT_WRITE
    #     message = libclient.Message(self.sel, self.sock, self.addr, request)
    #     self.sel.register(self.sock, events, data=message)

    #     try:
    #         while True:
    #             events = self.sel.select(timeout=1)
    #             for key, mask in events:
    #                 message = key.data
    #                 try:
    #                     message.process_events(mask)
    #                 except Exception:
    #                     print(
    #                         "main: error: exception for",
    #                         f"{message.addr}:\n{traceback.format_exc()}",
    #                     )
    #                     message.close()
    #             # Check for a socket being monitored to continue.
    #             if not self.sel.get_map():
    #                 break
    #     except KeyboardInterrupt:
    #         print("caught keyboard interrupt, exiting")
    #     finally:
    #         self.sel.close()





