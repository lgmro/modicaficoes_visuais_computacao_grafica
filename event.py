subscribers = dict()

def subscribe(event_type: str, fn):
    if not event_type in subscribers:
        subscribers[event_type] = []
    subscribers[event_type].append(fn)

def post_event(event_type: str, data=None):
    if not event_type in subscribers:
        return
    
    if data is not None:
        for fn in subscribers[event_type]:
            fn(data)
    else:        
        for fn in subscribers[event_type]:
            fn()
            
async def post_event_async(event_type: str, data=None):
    if not event_type in subscribers:
        return

    if data is not None:
        for fn in subscribers[event_type]:
            await fn(data)
    else:        
        for fn in subscribers[event_type]:
            await fn()
            