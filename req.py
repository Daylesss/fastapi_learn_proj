import requests

resp = requests.get('http://127.0.0.1:8082/protected-route', headers={"Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiYXVkIjpbImZhc3RhcGktdXNlcnM6YXV0aCJdLCJleHAiOjE3MDMwMjg4NzJ9.f0iSROe0PNFmPBy1Xi3_RBtLSfJAEltsSuRyJQPTawM"})
print(resp.text)
