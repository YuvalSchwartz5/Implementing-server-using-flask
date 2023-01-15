import json
from flask import Flask, jsonify, request

app = Flask(__name__)

messages = [
  {"application_id":1, "session_id":"aaaa","message_id":"bbbb", "participants": ["avi aviv", "moshe cohen"], "content":"Hi"},
  {"application_id":2, "session_id":"cccc","message_id":"dddd", "participants": ["avi aviv", "moshe cohen"], "content":"Hi"}
]

PARAMETERS_TYPE_LIST_GET = ['application_id', 'session_id', 'message_id']
PARAMETERS_TYPE_LIST_POST = ['application_id', 'session_id', 'message_id', 'participants', 'content']


@app.route('/GetMessage', methods=['GET'])
def get_messages():
    response = []
    key = list(request.args.keys())
    if len(key) == 1:
        if key[0] in PARAMETERS_TYPE_LIST_GET:
            for i in messages:
                if str(i[key[0]]) == request.args.get(key[0]):
                    response.append(i)
            if len(response) != 0:
                return jsonify(response)
            else:
                return jsonify({"ERROR":"The value '{}' not found at '{}'.".format(request.args.get(key[0]), key[0])})
        else:
            return jsonify({"Error": "key not found"})
    return jsonify({"Error": "Number of arguments is not valid"})


@app.route('/DeleteMessage', methods=['GET'])
def delete_message():
    global messages
    new_messages_list = []
    len_messages_before_delete = len(messages)
    key = list(request.args.keys())
    if len(key) == 1:
        if key[0] in PARAMETERS_TYPE_LIST_GET:
            for i in messages:
                if str(i[key[0]]) != request.args.get(key[0]):
                    new_messages_list.append(i)
            if len(new_messages_list) < len_messages_before_delete:
                messages = new_messages_list.copy()
                return jsonify({"OK" : "Deleted '{}' messages.".format(len_messages_before_delete-len(new_messages_list))}) 
            else:
                return jsonify({"ERROR":"The value '{}' not found at '{}'.".format(request.args.get(key[0]), key[0])})
        else:
            return jsonify({"Error": "key not found"})
    return jsonify({"Error": "Number of arguments is not valid"})
    

@app.route('/AddMessage', methods=['POST'])
def add_message():
    data = json.loads(request.form.get('data'))
    if len(data) != len(PARAMETERS_TYPE_LIST_POST):
      return jsonify({"Error": "Message arguments are not valid"})
    for i in data:
      if i == "application_id":
        if not isinstance(data[i], int):
          return jsonify({"Error": "Value of key is not valid"})
        continue
      elif i == 'session_id'or i == 'message_id' or i == 'content':
        if not isinstance(data[i], str):
          return jsonify({"Error": "Value of key is not valid"})
        if i == 'message_id':
          for x in messages:
            if x[i] == data[i]:
              return jsonify({"Error": "Message ID number already exists"})
        continue
      elif i == "participants":
        if not isinstance(data[i], list):
          return jsonify({"Error": "Value of key is not valid"})
        else:
          for j in data[i]:
            if not isinstance(j, str):
              return jsonify({"Error": "Value of key is not valid"})
        continue
      else:
        return jsonify({"Error": "Key is not valid"})   
    messages.append(data)
    return jsonify({"OK": "The message has been add!"})


if __name__ == "__main__":
  app.run()


