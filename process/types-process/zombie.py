from os import fork

pid = fork()

if pid == 0:
    for i in range(20):
        print("I am Child")
else:
    print("I am Parent")
    while True:
        pass


