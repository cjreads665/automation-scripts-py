import sys
import clipboard
import json

def save_items(filepath,data):
    with open(filepath,"w") as f:
        json.dump(data,f)

print(sys.argv[1:])

save_items("test.json",{"hell": "cute"})

if len(sys.argv) ==2:
    command = sys.argv[1]
    print(command)

    if command == "save":
        pass
    elif command == "load":
        pass
    elif command == "list":
        pass
    else:
        print("unknown command")
else:
    print("please pass 1 arguement only")