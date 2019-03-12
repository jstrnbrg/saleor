import requests

headers = {
    'Accept': 'application/json',
    'X-AUTH-KEY': 'u3rkCp5LPQz1EkTaMpjZIvJKtAqvnG21',
}

response = requests.get('https://globee.com/payment-api/v1/ping', headers=headers)

print response.json();
