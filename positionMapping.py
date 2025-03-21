from pymodbus.client import ModbusTcpClient
from address_enum import READ_ADDRESSES
import atexit
import struct
import requests

def shift_bits(number, shift_bit_amount):
        number = number & 0xffff
        result = number >> shift_bit_amount
        return result



SERVER_URL = "http://127.0.0.1:5001/"
SERVER_IP_LEFT="192.168.0.211"
SERVER_IP_RIGHT="192.168.0.212"
SERVER_PORT=502
client_leFt = ModbusTcpClient(host=SERVER_IP_LEFT, port=SERVER_PORT)
client_right = ModbusTcpClient(host=SERVER_IP_RIGHT, port=SERVER_PORT)

client_right.connect()
client_leFt.connect()

def main():
    
    print("Connected to both motors")
    try:
        while(True):
            user_input = input("Press 'r' to read motor position values or 'x' to exit: \n Press 'l' to move left motor, Press 'r' to move right motor").lower()
            if (user_input == 'x'):
                break
            if (user_input == 'y'):
                client_leFt.write_register(address=4001, value=1)
                client_right.write_register(address=4001, value=1)
            if user_input == 'k':
                response_left = client_leFt.read_holding_registers(address=31, count=1)
                response_right = client_right.read_holding_registers(address=31, count=1)
            if user_input == 'p':
                response_left = client_leFt.read_holding_registers(address=7101, count=1)
                response_right = client_right.read_holding_registers(address=7101, count=1) 

                response_left = client_leFt.read_holding_registers(address=5107, count=1)
                response_right = client_right.read_holding_registers(address=5107, count=1)

                response_left = client_leFt.read_holding_registers(address=5106, count=1)
                response_right = client_right.read_holding_registers(address=5106, count=1) # defaul modet

                response_left = client_leFt.read_holding_registers(address=4303, count=1) # IEG MOTION
                response_right = client_right.read_holding_registers(address=4303, count=1)

                response_left = client_leFt.read_holding_registers(address=7102, count=2) #ANALOG POS MIN
                response_right = client_right.read_holding_registers(address=7102, count=2) 

                response_left = client_leFt.read_holding_registers(address=7104, count=2)# ANALOG POS MAX
                response_right = client_right.read_holding_registers(address=7104, count=2)

                response_left = client_leFt.read_holding_registers(address=7106, count=2) # VELOCITY 213 - 256
                response_right = client_right.read_holding_registers(address=7106, count=2)
                
                response_left = client_leFt.read_holding_registers(address=7108, count=2) # ACCEL
                response_right = client_right.read_holding_registers(address=7108, count=2)

                response_left = client_leFt.read_holding_registers(address=7188, count=1) # MODBUSCNTRL
                response_right = client_right.read_holding_registers(address=7188, count=1)

                client_leFt.write_register(address=7188, value=3000)

                response_left = client_leFt.read_holding_registers(address=4316, count=1) # mODBUSCNTRL
                response_right = client_right.read_holding_registers(address=4316, count=1)

                response_right = client_right.read_holding_registers(address=104, count=1)
                response_left = client_right.read_holding_registers(address=104, count=1)

                response_left = client_right.read_holding_registers(address=6002, count=2)
                response_right = client_right.read_holding_registers(address=6002, count=2)

                response_left = client_right.read_holding_registers(address=6002, count=2)
                response_right = client_right.read_holding_registers(address=54, count=2)

                response_left = client_right.read_holding_registers(address=5107, count=1)
                response_right = client_right.read_holding_registers(address=5107, count=1)

                response_left = client_leFt.read_holding_registers(address=5108, count=1) # IPEAK
                response_right = client_right.read_holding_registers(address=5108, count=1)

            
            if (user_input == "s"):
                requests.get(SERVER_URL+"stop")

            if (user_input == "l"):
                requests.get(SERVER_URL+"write", {"direction": "l"})
            if (user_input == "r"):
                requests.get(SERVER_URL+"write", {"direction": "r"})
    except Exception as e:
        print(e)

if __name__ == "__main__":
     main()