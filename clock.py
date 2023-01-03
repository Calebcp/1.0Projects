import time
def countdown(t):
    while t > 0:
        print(t)
        t-=1
        time.sleep(1)
    print("DONE!")

print("How many seconds to count down? Enter an Integer:")
seconds = input()
while not seconds.isdigit():
    print("Not an Integer. Enter an Integer:")
    seconds = input()
seconds = int(seconds)
print("STARTED!")
countdown(seconds)