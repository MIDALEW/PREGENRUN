import time
from mcrcon import MCRcon
PORT = 25575
PASSWORD = ''
PREGEN_RADIUS = 1000

def main():
    with MCRcon("127.0.0.1",password=PASSWORD ,port=PORT) as con:
        enabled = False
        while True:
            time.sleep(4)
            try:
                resp = con.connect("list");
                resp = resp[11:]
                players = 0
                for i in resp:
                    if i.isdigit():
                        players == players*10 + int(i);
                    if i == "/":
                        break;
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
    main()