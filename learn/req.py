import requests

resp = requests.get('http://127.0.0.1:8000/protected-route', headers={"Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCIIkpXVCJ9.eyJzdWIiOiIzIiwiYXVkIjpbImZhc3RhcGktdXNlcnM6YXV0aCJdLCJleHAiOjE3MDI4MzU3ODR9.NSQzdRuObBasJHkPjljJVpyl9Mlt-aD11vskeYQumuE"})
print(resp.text)