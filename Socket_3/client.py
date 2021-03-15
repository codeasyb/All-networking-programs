
import socket as soc


try:
	s = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
	print("[C]: client socket created.")
except soc.error as err:
	print('{} \n'.format(f"socket open error {err}"))


s.connect((soc.gethostname(), 1234))
msg = s.recv(100)

getMsg = msg.decode('utf-8')
print(f"[C]: Data received from server: {getMsg}")

s.close;
exit()

