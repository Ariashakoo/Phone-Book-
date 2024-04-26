import os
# choose desired Path
Path = ""
def IsValid():
    if not os.path.exists(Path):
        f = open(Path, "w+")
        f.write("")


def add(name , number):
    IsValid()
    f = open(Path, "a+")
    Phone = name + "_" + number + "\n"
    f.write(Phone)
    f.close()


def Search(name):
    IsValid()
    f = open(Path , "r")
    for Line in f.readlines():
        if name == Line.split("_")[0]:
            print(name + " : " + Line.split("_")[1])
    f.close()


def Delete(name):
    IsValid()
    f = open(Path , "r")
    Save = ""
    for Line in f.readlines():
        if not name == Line.split("_")[0]:
            Save += Line
    f.close()

    f = open(Path  , "w")
    f.write(Save)
    f.close()


def Show_Info():
    IsValid()
    f = open(Path , "r")
    DataBase = ""
    DataBase = f.read()
    f.close()
    print(DataBase)



choice = 1
while choice != 0 :
    print("Choose your desired choice\n 1.Add User\n 2.Search Phone \n 3.Delete Phone\n 4.Show numbers\n 0.Exit\n")
    choice = int(input())
    os.system('cls')

    if choice == 1:
        Name = input("Enter The Name :")
        Number = input("Enter The Number :")
        add(Name , Number)
    
    elif choice == 2:
        Name = input("Enter The Name :")
        Search(Name)
    
    elif choice == 3:
        Name = input("Enter The Name :")
        Delete(Name)
    
    elif choice == 4:
        Show_Info()