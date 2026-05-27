from project import verify_signature, parse_input, generate_nonce
import pytest

def test_verify_signature():
    assert verify_signature([1.0, 2.0], [1.0, 2.0])==True
    assert verify_signature([1.0, 2.0], [9.0, 9.0])==False
    assert verify_signature([1.0, 2.0], [1.0])==False

def test_parse_input():
    assert parse_input("1.1, 2.2, 3.3") == [1.1, 2.2, 3.3]
    assert parse_input(" 1.1 , 2.2 ") == [1.1, 2.2]
    assert parse_input("cat, dog") == None

def test_generate_nonce():
    assert isinstance(generate_nonce(), str)
    assert generate_nonce() != generate_nonce()