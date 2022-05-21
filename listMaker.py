import json

def createNewList():
    fileName = input("Enter the name of the file: ")
    mainList = []
    while True:
        item = input("Enter the item: ")
        if item == "done":
            print("done")
            break
        else:
            mainList.append(item)
            print(f"added {item} to the list | {mainList}")

    with open(fileName + '.json', 'w') as f:
        f.write(json.dumps(mainList))

def editList():
    fileName = input("Enter the name of the file to edit: ")
    mainList = []
    with open(fileName + '.json', 'r') as f:
        mainList = json.loads(f.read())
    print(mainList)
    while True:
        item = input("Enter the item: ")
        if item == "done":
            print("done")
            break
        else:
            mainList.append(item)
            print(f"added {item} to the list | {mainList}")

    with open(fileName + '.json', 'w') as f:
        f.write(json.dumps(mainList))


def createNewDict():
    fileName = input("Enter the name of the dict file: ")
    mainDict = {}
    while True:
        key = input("Enter the key: ")
        if key == "done":
            print("done")
            break
        else:
            value = input("Enter the value: ")
            mainDict[key] = value
            print(f"added {key} to the dictionary | {mainDict}")

    with open(fileName + '.json', 'w') as f:
        f.write(json.dumps(mainDict))

def editDict():
    fileName = input("Enter the name of the dict file to edit: ")
    mainDict = {}
    with open(fileName + '.json', 'r') as f:
        mainDict = json.loads(f.read())
    print(mainDict)
    while True:
        key = input("Enter the key: ")
        if key == "done":
            print("done")
            break
        else:
            value = input("Enter the value: ")
            mainDict[key] = value
            print(f"added {key} to the dictionary | {mainDict}")

    with open(fileName + '.json', 'w') as f:
        f.write(json.dumps(mainDict))


def main():
    while True:
        print("""Data Store

1. List
2. Dictionary
3. Exit
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            print("""Data Store
    
1. Create a new list
2. Edit a list
3. Exit
            """)
            choice2 = input("Enter your choice: ")
            if choice2 == "1":
                createNewList()
            elif choice2 == "2":
                editList()
            elif choice2 == "3":
                break
            else:
                print("Invalid input")
        elif choice == "2":
            print("""Data Store

1. Create a new dictionary
2. Edit a dictionary
3. Exit
            """)
            choice3 = input("Enter your choice: ")
            if choice3 == "1":
                createNewDict()
            elif choice3 == "2":
                editDict()
            elif choice3 == "3":
                break
            else:
                print("Invalid input")
        elif choice == "3":
            break
        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()