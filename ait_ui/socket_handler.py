socket = None # set by app.py
send_queue = []


def sample_client_handler(id, value, event_name):
    print("sample_client_handler", id, value, event_name)
clientHandler = sample_client_handler


def set_client_handler(handler):
    global clientHandler
    clientHandler = handler
    print("client handler set to", handler)


def send(id, value, event_name):
    global socket
    socket.emit("from_server", {'id': id, 'value': value, 'event_name': event_name})

def queue_for_send(id, value, event_name):
    global send_queue
    print("queueing for send", id, value, event_name)
    send_queue.append({'id': id, 'value': value, 'event_name': event_name})

def flush_send_queue():
    global send_queue
    for item in send_queue:
        print("sending", item)
        send(item['id'], item['value'], item['event_name'])
    send_queue = []