import time
import requests
import random
import validation

print("*******************************")
print("|                             |")
print("|     Auto Sender Discord     |")
print("|                             |")
print("*******************************")
print("\nPress CTRL + C to stop program")

while True:
    print("\n1.Enter number for delay (You can enter more than 1 delay, separate them with a space.): ")
    inputdelay = input()
    delay = validation.validasi_delay(inputdelay)

    if delay is not None:
        break
print(f"Your delay is {delay} seconds")

print("\n2.Enter your content")
inputpayload = input()
payload = {"content": inputpayload}

proxy = None
print("Input proxy (Optional) Y/N")
question = input().strip().upper()

while True:

    if question == "Y":
        print("Enter your proxy ex(http://user:pass@ip:port or http://ip:port)")
        print("(Type exit to skip proxy)")
        inputproxy = input()
        

        valid_proxy = validation.validasi_proxy(inputproxy)

        if inputproxy.lower() == "exit":
            break

        if valid_proxy is not None:
            proxy = {"http": valid_proxy,
             "https": valid_proxy}
            break
        
        else:
            continue

    elif question == "N":
        break

    else:
        print("Type Y/N")
        question = input().strip().upper()

while True:
    print("\n3.Enter your authorization")
    inputheader = input()
    valid_header = validation.validasi_header(inputheader)
    
    if valid_header is not None:
        header = {"authorization": valid_header}
        break

while True:
    print("\n4.Enter link api")
    channel = validation.validasi_link(input())
    if channel is not None:
        break

try:
    while True:

        randomizer = random.choice(delay)

        req = requests.post(channel, json=payload,
                            headers=header, proxies=proxy)
        status = req.status_code
        if status == 200:
            print(f"{time.strftime('(%H:%M:%S)')}Message sent")
        else:
            print(
                f"{time.strftime('(%H:%M:%S)')}Message failed to send (code{status})")

        print(f"Next message in {randomizer} seconds")
        time.sleep(randomizer)

except requests.exceptions.Timeout:
    print("Request timeout")

except requests.exceptions.ConnectionError:
    print("Connection eror")

except (KeyboardInterrupt):
    print("Bot mati")
