import json

def make_new_entry():
    n = raw_input("name:")
    d = raw_input("date:")
    t = raw_input("new log file to enter into the logs store:")

    with open(t, "r") as f:
        logtext_to_add = f.read()

    new_log = json.dumps({'name': n, 'date' : d, 'text': logtext_to_add}, sort_keys = True)
    z = open(d + ".json", "w")
    z.write(new_log)


#    with open("logs.json", "a") as myfile:
#       myfile.write(new_log)

if __name__ == '__main__':
    make_new_entry()        
