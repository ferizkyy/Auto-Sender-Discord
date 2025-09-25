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

while True:
    print("\n3.Enter your authorization")
    inputheader = input()
    valid_header = validation.validasi_header(inputheader)
    header = {"authorization": valid_header}
    if valid_header is not None:
        break

while True:
    print("\n4.Enter link api")
    channel = validation.validasi_link(input())
    if channel is not None:
        break

try:
    while True:

        randomizer = random.choice(delay)

        req = requests.post(channel, json=payload, headers=header)
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
