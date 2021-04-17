N = int(input())
task = []
for i in range(N):
    inpt = [x for x in input().split()]
    task.append(inpt)
arr = []
for i in range(N):
    if task[i][0] == "insert":
        arr.insert(int(task[i][1]),int(task[i][2]))
    elif task[i][0] == "print":
        print(arr)
    elif task[i][0] == "remove":
        arr.remove(int(task[i][1]))
    elif task[i][0] == "append":
        arr.append(int(task[i][1]))
    elif task[i][0] == "sort":
        arr = sorted(arr)
    elif task[i][0] == "pop":
        arr.remove(arr[-1])
    elif task[i][0] == "reverse":
        arr = arr[::-1]