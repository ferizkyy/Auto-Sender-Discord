def validasi_delay(input_delay):
 try:
  delays = [int(x) for x in input_delay.split()]

 except ValueError:
    print("Input invalid")
    return None

 if not delays:
      print("Delay cannot be empty")
      return None
 if any (delay <= 0 for delay in delays):
      print("Delay Cannot be less than 0 or = 0")
      return None
 return delays
 

def validasi_header(input_header):
    header = input_header.strip()

    if not header:
        print("Input your authorization")
        return None
    return header

def validasi_link(input_link):

    if not input_link.strip():
        print("Link cannot be empty")
        return None
    
    if not input_link.startswith(("https://", "http://")):
       print("Link must start with https://")
       return None
    
    return input_link