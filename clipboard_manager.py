import sys
import clipboard
import json

'''
in case you are using a system with no copy paste mechanism, please install one.
Here is a one for Linux: 
sudo apt-get install xclip
'''

SAVED_DATA = "clipboard.json"

def save_items(filepath,data):
    with open(filepath,"w") as f:
        json.dump(data,f)

def load_items(filepath):
    #we try to ge the file if it exists
    try:
        with open(filepath,"r") as f:
            data = json.load(f)
            print(data)
            return data
    #we return an empty object
    except:
        return {}

#  selects the arguments after 'python clipboard_manager.py'.
print(sys.argv[1:])

save_items("test.json",{"hell": "cute"})


if len(sys.argv) ==2:
    command = sys.argv[1] # we get the 
    # print(command)
    data = load_items(SAVED_DATA) # we load the JSON file before checking for command.
    if command == "save":
        #get the input as key to ref the data being pasted
        key = input("enter a key label for the data: ").strip()
        if key == "":
            print("please enter a key without spaces")
        elif " " in key:
            print("please do not include spaces in commands")
        else:     
            #as soon as we enter the key this will get the latest content from sys clipboard
            data[key] = clipboard.paste()
            #save the data to the loaded file
            save_items(SAVED_DATA,data)
    elif command == "load":
        pass
    elif command == "list":
        pass
    else:
        print("unknown command")
else:
    print("please pass 1 arguement only")