import requests
import json 
import time
import csv

page = 1
url = "https://api.etherscan.io/api?module=account&"\
    "action=txlist&"\
    "address=0x7Be8076f4EA4A4AD08075C2508e481d6C946D12b&"\
    "startblock=13333161&"\
    "endblock=13431081&"\
    "page=PAGENO&"\
    "offset=10&"\
    "sort=asc&"\
    "apikey=RY1QF8U67EGBIFGPJDKDIMQZ3ZJDJHGYSB"
transaction_list = []

for i in range(1,10):
    print('page %d' %(i))
    new_url = url.replace('PAGENO',str(i))
    time.sleep(0.2)
    resp = json.loads(requests.get(url).text)
    
    if resp['status'] == '1':
        for i in resp['result']:
            del i['input']
            transaction_list.append(i)
        # transaction_list.extend(resp['result'])


print(len(transaction_list))

# print(transaction_list)
# with open('./data/transaction_list_opensea.json', 'w') as f:
#     json.dump(transaction_list, f)

# now we will open a file for writing
data_file = open('./data/transaction_list_opensea.csv', 'w')
 
# create the csv writer object
csv_writer = csv.writer(data_file)
 
# Counter variable used for writing
# headers to the CSV file
count = 0
 
for txn in transaction_list:
    if count == 0:
 
        # Writing headers of CSV file
        header = txn.keys()
        csv_writer.writerow(header)
        count += 1
 
    # Writing data of CSV file
    csv_writer.writerow(txn.values())
 
data_file.close()






