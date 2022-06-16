print("Program queue kelompok 5")

jalan = True

# fungsi untuk method method dalam queu

def create_queu():
    queu = []
    return queu

def empty_queu(queu):
    if len(queu) == 0:
        print("data is empty")
        return False
    else:
        print("data is not empty")

def add_value(queu,item):
    queu.append(item)
    print("add value "+ str(item) +" in queu")

def show_queu(queu):
    print(queu)

def remove_queu(queu):
    if (empty_queu(queu) == False):
        return "data is empty"
    else:
        queu.pop(0)
        print("first data is removed")

def size(queu):
    print("panjang queu adalah = "+ str(len(queu)))


queu = create_queu()

while jalan:
    print(" ")
    print(" ")
    print("Menu dalam program queu python sederhana")
    print("1. Empty queue")
    print("2. Add queue value")
    print("3. Show queue value")
    print("4. remove a data in queue")
    print("5. size queue")
    print("6. stop program")

    print(" ")
    data = int(input("Masukan fungsi yang dipilih = "))

    if data == 1:
        empty_queu(queu)
    elif data == 2:
        value = int(input("Masukkan nilai = "))
        add_value(queu,value)
    elif data == 3:
        show_queu(queu)
    elif data == 4:
        remove_queu(queu)
    elif data == 5:
        size(queu)
    elif data == 6:
         jalan = False
