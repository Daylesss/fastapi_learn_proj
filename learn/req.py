import requests

resp = requests.get('http://127.0.0.1:8000/protected-route', headers={"Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyIiwiYXVkIjpbImZhc3RhcGktdXNlcnM6YXV0aCJdLCJleHAiOjE3MDI4NTI4NDR9.fUC-dmfR9Os1t_iXTVpEEiJKyUPMxZEAU-r99XfugKU"})
print(resp.text)
