from flask import Flask,request
import tronapi
from tronapi import Tron


full_node = 'https://api.trongrid.io'
solidity_node = 'https://api.trongrid.io'
event_server = 'https://api.trongrid.io'

PK = "fad723ef2fbfeebda6a3e0fd0e1c3367b9568b9eb9645346d5487e8900872545"

tron = Tron(full_node=full_node,
    solidity_node=solidity_node,
    event_server=event_server)

def setTronPK(pk):
    tron.private_key = pk
    tron.default_address = tron.address.from_private_key(pk).base58

setTronPK(PK)

app = Flask(__name__)

def myfunc(add):
  txn = tron.trx.send_token(PA, 10*100000*6, "1000645");
  return "ok"
 
app.route('/')
def getHandler():
    return "ok"

@app.route('/post', methods = ['POST'])
def getHandler():
     r = request.json
     PA = r["address"]
     PS = r["amount"]
     PR = r["tokenid"]
     txn = tron.trx.send_token(PA, 1*PS, PR);
     return txn["transaction"]["txID"]
    
    
   
if __name__ == '__main__':
 app.run()
