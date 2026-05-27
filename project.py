import math
import statistics
import datetime
import secrets 
import abc
import pytest

def verify_signature(master_sign, input_sign, threshold=0.05):
    if not len(master_sign)==len(input_sign):
        return False
    total_error=0

    for m,i in zip(master_sign, input_sign):
        first_number= m-i
        squared_result=pow(first_number,2)
        total_error+=squared_result

    number_of_elements=len(master_sign)
    total_average=total_error/number_of_elements

    return total_average <= threshold

class Command:
    def __init__(self, action, signature, nonce):
        self.action=action
        self.signature=signature
        self.nonce=nonce

class Satellite:
    def __init__(self, secret_key):
        self.__secret_key= secret_key
        self.is_unlocked=False
        self.__used_nonces=[]

    def authenticate(self, command_obj):
        if command_obj.nonce in self.__used_nonces:
            string="Detected replay attack!"
            return string
        self.__used_nonces.append(command_obj.nonce)
        if verify_signature(self.__secret_key, command_obj.signature):
            self.is_unlocked=True
            string="Access granted"
            return string
        else:
            string="Access denied"
            return string