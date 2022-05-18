print("Program queue kelompok 5")

jalan = True

# fungsi untuk method method dalam stack

def create_stack():
    stack = []
    return stack

def empty_stack(stack):
    if len(stack) == 0:
        print("data is empty")
        return False
    else:
        print("data is not empty")

def add_value(stack,item):
    stack.append(item)
    print("add value "+ str(item) +" in stack")

def show_stack(stack):
    print(stack)

def remove_stack(stack):
    if (empty_stack(stack) == False):
        return "data is empty"
    else:
        stack.pop(0)
        print("first data is removed")

def size(stack):
    print("panjang queu adalah = "+ str(len(stack)))


stack = create_stack()

while jalan:
    print(" ")
    print(" ")
    print("Menu dalam program stack python sederhana")
    print("1. Empty queue")
    print("2. Add queue value")
    print("3. Show queue value")
    print("4. remove a data in queue")
    print("5. size queue")
    print("6. stop program")

    print(" ")
    data = int(input("Masukan fungsi yang dipilih = "))

    if data == 1:
        empty_stack(stack)
    elif data == 2:
        value = int(input("Masukkan nilai = "))
        add_value(stack,value)
    elif data == 3:
        show_stack(stack)
    elif data == 4:
        remove_stack(stack)
    elif data == 5:
        size(stack)
    elif data == 6:
         jalan = False
