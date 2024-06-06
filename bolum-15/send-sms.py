import vonage

client = vonage.Client(key="<key>",secret="<secret>")
sms = vonage.Sms(client)

responseData = sms.send_message({
    "from": "Deneme",
    "to": "<phone>",
    "text": "bu sms python uygulamasından gönderildi."
})

if responseData["messages"][0]["status"] == "0":
    print("mesajınız gönderildi")
else:
    print(f"hata oluştu:", {responseData['messages'][0]['error-text']})