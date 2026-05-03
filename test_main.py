from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

test_ips = [{"ip": "191.194.129.227", "login": "sucess"}, {"ip": "187.32.150.118", "login": "sucess"}]
test_suspects_ips = [{
    "ip": "177.127.122.97", "login": "failed"
  },
  {
    "ip": "177.127.122.97", "login": "failed"
  },
  {
    "ip": "177.127.122.97", "login": "failed"
  },
  {
    "ip": "177.127.122.97", "login": "failed"
  },
  {
    "ip": "177.127.122.97", "login": "failed"
  },
  {
    "ip": "177.127.122.97", "login": "failed"
  },]



def test_post_main_suspects():
    response = client.post("/analise", json=test_suspects_ips)
    assert response.status_code == 200
    assert response.json() == [{"Suspect IP": "177.127.122.97", "Try": 6}]

def test_post_main_positive():
    response = client.post("/analise", json=test_ips)
    assert response.status_code == 200
    assert response.json() == []



