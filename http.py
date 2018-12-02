import requests
r=requests.post("link", json={"nome":"alessandro negro"})
res=r.json()
print(res)

r = requests.get("link", headers = {"x-data":"true"})
res=r.json()
data = res["data"]



r= 9 

r=requests.post("link", json = {"data":r})
print(r.json())
