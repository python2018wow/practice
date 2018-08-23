from twilio.rest import Client

#Your Account SID
account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
#Your AUTH TOKEN
auth_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"

client = Client(account_sid, auth_token)

message = client.messages.create(
        to="+886xxxxxxxx",   #發送簡訊到這個號碼
        from_="xxxxxxxxxxxx", #twilio給的電話號碼
        body="測試Python自動發簡訊，別回覆")

print(message.sid)

