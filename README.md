# DoQu_Backend

### Must have CUDA capable GPU and CUDA Toolkit installed -> Tested on CUDA 12.1 and python 3.11.3

### Installing packages:
pip install -r requirements.txt

### Running the Server
python3 -m uvicorn server:app --reload

netsh interface portproxy add v4tov4 listenport=8000 listenaddress=0.0.0.0 connectport=8000 connectaddress=127.0.0.1

(base) C:\Windows\system32> netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=8000 connectaddress=172.23.240.117 connectport=8000

(base) C:\Windows\system32> netsh interface portproxy show v4tov4

ipv4 수신 대기:             ipv4에 연결:

주소            포트        주소            포트
--------------- ----------  --------------- ----------
192.168.100.60  <SSH_PORT>  172.23.245.117  22
192.168.100.60  22          172.23.245.117  22
192.168.100.60  29500       172.23.245.117  29500
0.0.0.0         8000        172.23.240.117  8000

(base) C:\Windows\system32> netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=8000 connectaddress=172.23.245.117 connectport=8000

(base) C:\Windows\system32> netsh interface portproxy show v4tov4

ipv4 수신 대기:             ipv4에 연결:

주소            포트        주소            포트
--------------- ----------  --------------- ----------
192.168.100.60  <SSH_PORT>  172.23.245.117  22
192.168.100.60  22          172.23.245.117  22
192.168.100.60  29500       172.23.245.117  29500
0.0.0.0         8000        172.23.245.117  8000
