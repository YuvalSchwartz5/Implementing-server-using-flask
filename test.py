import requests
import json
import pytest

HOST = "http://127.0.0.1:5000"

GET_MESSAGE_BASE = "/GetMessage?"
DELETE_MESSAGE_BASE = "/DeleteMessage?"
POST_ADD_MESSAGE_BASE = "/AddMessage"


def get_request(test_request, value, expected_response):
    response = requests.get(HOST + GET_MESSAGE_BASE + test_request + value)
    assert response.status_code == 200
    assert response.json() == expected_response

def delete_request(test_request, value, expected_response):
    response = requests.get(HOST + DELETE_MESSAGE_BASE + test_request + value)
    assert response.status_code == 200
    assert response.json() == expected_response

def post_request(data, expected_response):
    response = requests.post(HOST + POST_ADD_MESSAGE_BASE, data=data.encode(), headers = {'Content-type': 'application/x-www-form-urlencoded'})
    assert response.status_code == 200
    assert response.json() == expected_response

def test_main():
    #Getting messages successfully.
    get_request("message_id=", "bbbb", [{"application_id":1, "session_id":"aaaa","message_id":"bbbb", "participants": ["avi aviv", "moshe cohen"], "content":"Hi"}])

    #trying to get message that does not exist.
    get_request("application_id=", "3", {"ERROR":"The value '3' not found at 'application_id'."})

    #trying to get message with a key that does not exist.
    get_request("lines_id=", "3", {"Error": "key not found"})

    #Adding a message successfully.
    data_to_add = """data={"application_id": 5,"session_id":"aaaa","message_id":"bafdbbb","participants":["avi aviv","moshe cohen"],"content":"Hi"}"""
    post_request(data_to_add, {"OK": "The message has been add!"})
    
    #Adding a message unsuccessfully - message id already exiits.
    data_to_add = """data={"application_id": 5,"session_id":"aaaa","message_id":"bbbb","participants":["avi aviv","moshe cohen"],"content":"Hi"}"""
    post_request(data_to_add, {"Error": "Message ID number already exists"})

    
    #Adding a message unsuccessfully - a value of a key is not valid.
    data_to_add = """data={"application_id": 6,"session_id":"aaaa","message_id":"jkl","participants":20019,"content":"Hi"}"""
    post_request(data_to_add, {"Error": "Value of key is not valid"})

    #Adding a message unsuccessfully - message id already exiits.
    data_to_add = """data={"application_id": 7,"participants":20019,"content":"Hi"}"""
    post_request(data_to_add, {"Error": "Message arguments are not valid"})

    #Deleting messages successfully.
    delete_request("session_id=", "cccc",{"OK" : "Deleted '1' messages."})

    #Deleting messages usuccessfully - key dosen't exist.
    delete_request("seion_id=", "cccc",{"Error": "key not found"})

    #Deleting messages usuccessfully - key dosen't exist.
    delete_request("message_id=", "cccc",{"ERROR":"The value 'cccc' not found at 'message_id'."})


