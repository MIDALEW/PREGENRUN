import time
from mcrcon import MCRcon
import os 


PORT = int(os.getenv("MINECRAFT_SERVER_PORT"))
PASSWORD = os.getenv("1234")
PREGEN_RADIUS = int(os.getenv("PREGEN_RADIUS"))
SERVER_ADRESS = os.getenv("SERVER_ADRESS")
PING_DELAY=int(os.getenv("DELAY_BEETWEEN_PINGS"))


def main():
    with MCRcon(SERVER_ADRESS,password=PASSWORD ,port=PORT) as con:
        enabled = False
        while True:
            time.sleep(PING_DELAY)
            try:
                resp = con.connect("list")
                resp = resp[11:]
                players = 0
                for i in resp:
                    if i.isdigit():
                        players == players*10 + int(i)
                    if i == "/":
                        break
                if players <= 4:
                    if not enabled:
                        con.command(f"pregen start {PREGEN_RADIUS}")
                        enabled = True
                else:
                    if enabled:
                        con.command("pregen stop")
                        enabled = False
            except Exception as e:
                print(e)


if __name__ == '__main__':
    try:
        main()
    except ConnectionRefusedError:
        print(f"Connection refused, while trying to connect:{SERVER_ADRESS} on port:{PORT}")
    except Exception as e:
        print(e)