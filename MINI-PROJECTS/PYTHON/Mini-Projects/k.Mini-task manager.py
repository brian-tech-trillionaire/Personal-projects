tasks = []
done = []


def add_tasks(task):
    tasks.append(task)


def complete_tasks():
    if tasks:
        done.append(tasks.pop(0))


add_tasks("Finish homework")
add_tasks("Cook food")
add_tasks("Read book")
add_tasks("Exercise")
add_tasks("Read bible")

complete_tasks()

print(f"Pending: {tasks}")
print(f"Done: {done}")
