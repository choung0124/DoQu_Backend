# DoQu_Backend

### Must have CUDA capable GPU and CUDA Toolkit installed -> Tested on CUDA 12.1 and python 3.11.3

### Installing packages:
pip install -r requirements.txt

### Running the Server
python3 -m uvicorn server:app --reload

netsh interface portproxy add v4tov4 listenport=8000 listenaddress=0.0.0.0 connectport=8000 connectaddress=127.0.0.1
