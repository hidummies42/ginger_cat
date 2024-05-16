# notebook
def print_nb():
    nb = open("notebook.txt", "r")
    for line in nb:
        print(line, end="")
    print("\n ***printing ended***")
    
def write_nb():
    nb = open("notebook.txt", "r")
    i = 0
    for line in nb:
        i += 1
    nb = open("notebook.txt", "a")
    while True:
        text = input("What to write down? Type \"exit()\" when finished. \n")
        if text != "exit()":
            nb.write(f"#{i+1}##  " + text + "\n")
            i += 1
        else:
            print("***text saved***")
            break
    nb.close()

def delete_range(filename, s, e):
    nb = open("notebook.txt", "r")
    i = 0
    txt_list = []
    for line in nb:
        i += 1
        two_pounds = line.index("##")
        txt_list.append(line[two_pounds+4 : -1])
        count = 0
        new_list = []
        for item in txt_list:
            count += 1
            if count in range(s,e+1):
                pass
            else:
                new_list.append(item)
        
        nb = open("notebook.txt", "w")
        j = 0
        for item in new_list:
            nb.write(f"#{j+1}##  " + item + "\n")
            j += 1
        nb.close()
 
# main
print("Hello, this is the NoteBook! \n******\n ")

while True:
    o = input("What to do now? write() or print() or delete() or exit() \n")
    if o == "write()":
        write_nb()
    elif o == "print()":
        print_nb()
    elif o == "delete()":
        oo = input("Delete all() or some()? ")
        if oo == "all()":
            nb = open("notebook.txt", "w")
            nb.close()
        elif oo == "some()":
            s = int(input("start: "))
            e = int(input("end: "))
            delete_range("notebook.txt", s,e)
        else:
            print("Input error. Try again. \n ****** \n")
        
    elif o == "exit()":
        print("******\nBye!")
        break
    else:
        print("Input error. Try again. \n ****** \n")
   


