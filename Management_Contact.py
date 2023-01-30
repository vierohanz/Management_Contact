import os

nama = ['Rais Hannan Rizanto', 'widayatii']
nim = ['4.33.22.1.21', '4.33.22.1.40']
email = ['rizantohannan@gmail.com', 'widayati@gmail.com']


def data_display():  # fungsi untuk menampilkan data yang tersimpan di list
    print('DISPLAY DATA:')
    for i in range(len(nama)):
        print(f'Nama\t: {nama[i]}')
        print(f'NIM \t: {nim[i]}')
        print(f'Email \t: {email[i]}')
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
        

def add_data():  # fungsi untuk menambahkan data
    print("ADD DATA:")
    nama.append(input('Nama\t: '))
    nim.append(input('NIM\t: '))
    email.append(input('Email\t: '))
    print('Successfully Update')

def search_data(): # Fungsi untuk mencari data 
    print("SEARCH DATA:")
    inputSearch = input("NIM : ")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
    for a in range(len(nim)):

        if nim[a].lower().find(inputSearch) != -1:
            indeks = a
            print(f"Nama\t: {nama[indeks]}")
            print(f"NIM\t: {nim[indeks]}")
            print(f"Email\t: {email[indeks]}")

def change_data(): # fungsi untuk mengubah data
    print("CHANGE DATA")
    userInput = input("Input Name : ")
    
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
    chgnama = input("New Name\t: ")
    chgnim = input("New NIM\t\t: ")
    chgemail = input("New Email\t: ")
    for a in range(len(nama)):
        data = nama[a]
        if userInput == (data):
            nama[a] = chgnama
            nim[a] = chgnim
            email[a] = chgemail


def delete_data(): # fungsi untuk menghapus data
    inputdata = input("Masukkan Nama : ")
    index = -1
    for i in range(0, len(nama)):
        
        if inputdata == nama[i]:
            index = i
            break

    if index == i:
        del nama[index] 
        print("Successfully Deleted")
    else:
        print("Data Not Found")
        


while True:
    print('_________________________________')
    print("Nama \t: RAIS HANNAN RIZANTO")
    print("NIM \t: 4.33.22.1.21")
    print("Kelas \t: TI-1B")
    print('_________________________________')
    print("===============MENU==============")
    print("1. Add Data")
    print("2. Search Data")
    print("3. Data Display")
    print("4. Delete Data")
    print("5. Change Data")
    print("0. Out")
    userInput = input("\nPilih Menu : ")
    os.system("cls")

    if userInput == '0':
        break
    
    elif userInput == '1':
        add_data()

    elif userInput == '2':
        search_data()

    elif userInput == '3':
        data_display()

    elif userInput == '4':
        delete_data()

    elif userInput == '5':
        change_data()
