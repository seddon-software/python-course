from freesms import FreeClient

f = FreeClient(user="your_username", password="your_password")
resp = f.send_sms("Hello, this is my SMS")
print(resp.status_code)  # Should return 200 for success


