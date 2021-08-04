import time
from libs.openexchange import OpenExchangeClient


APP_ID = 'e07eff8a09ea4d0c9cb1b1ff996646bf'
client = OpenExchangeClient(APP_ID)

start = time.time()
usd_amount = 1000
inr_amount = client.convert(usd_amount, 'USD', 'INR')
end = time.time()

print(end-start)
print(f'USD - ${usd_amount} in INR - Rs.{inr_amount:.2f}')
