priority_queue = []
elements = [2, 5, 3, 7, 1]


def prior_queue_append(values, queue):
    for i in values:
        queue.append(i)
        queue.sort()
    return queue


def prior_queue_delete(queue):
    delete = int(
        input('Di que numero quieres eliminar de la cola de prioridad'))
    if delete in queue:
        queue.remove(delete)
    return queue


print(prior_queue_append(elements, priority_queue))
print(prior_queue_delete(priority_queue))
