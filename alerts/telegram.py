import requests

def send_trade_alert(msg, token, chat_id):
    requests.post(f'https://api.telegram.org/bot{token}/sendMessage', data={'chat_id': chat_id, 'text': msg})