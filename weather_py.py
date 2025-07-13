import requests
import json
import win32com.client as wincom 


take = input("Enter your location: ")

url = f"https://api.weatherapi.com/v1/current.json?key=fc4ff773e24549b789171938251007&q={take}"

req =  requests.get(url)
# print(req.text)
w_dic = json.loads(req.text)
p = w_dic["current"]["temp_c"]


speak = wincom.Dispatch("SAPI.SpVoice")
text = f"The current temperaature in {take} is {p} degree celsius"
speak.Speak(text)