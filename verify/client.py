from inspect import signature
import os
from Crypto.Hash import SHA384
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5



def get_cpuinfo():
    '''
    获取 CPU 唯一标识符
    '''
    command = "dmidecode -t 4 | grep ID |sort -u |awk -F': ' '{print $2}'"
    cpu_info = os.popen(command).read().split('\n')[0].replace(" ","")

    return cpu_info


def verifier(public_key, data, signature):
    '''
    传入公钥、CPU唯一标识符、签名过后的摘要
    '''
    id_digest = SHA384.new(data.encode("utf-8"))
    try:
        # 用公钥校验数字签名并进行解密
        PKCS1_v1_5.new(public_key).verify(id_digest, signature)
        print("Active Successful")
    except:
        print("Contact the software developer to obtain the activation code")


with open("./pub_key.pub", mode="rb") as f:
    public_key = RSA.import_key(f.read())

data = get_cpuinfo()
signature = input("Input your activation code: ")

verifier(public_key, data, signature)