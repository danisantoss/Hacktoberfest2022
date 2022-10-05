def put(queue: list, value: any) -> None:
    """Insert in the queue"""
    queue.append(value)
    return f"'{value}' was inserted!"

def get(queue: list) -> any:
    """Get the first element of the queue"""
    if len(queue) > 0:
        return queue.pop(0)
    return "queue is empty!"

def lenght(queue: list) -> int:
    """Get the lenght of the queue"""
    return len(queue)
