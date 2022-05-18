print("Program stack kelompok 5")

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
        stack.pop()
        print("last data is removed")


stack = create_stack()

while jalan:
    print(" ")
    print(" ")
    print("Menu dalam program stack python sederhana")
    print("1. Empty stack")
    print("2. Add stack value")
    print("3. Show stack value")
    print("4. remove a data in stack")
    print("5. stop program")

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
         jalan = False

