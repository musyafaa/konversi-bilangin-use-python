while True:
    print("==========================================")
    print("|| US DP 1 dan DP3 ||".center(40))
    print("|| Muhammad Musyafa Fadila ||".center(40))
    print("==========================================")
    print("|| pilihan bilangan yang mau kamu konversi:")
    print("|| 1. desimal")
    print("|| 2. biner")
    print("|| 3. oktal")
    print("|| 4. hexadesimal")
    print("|| 5. string to ascii")
    pilih = int(input("masukan pilihanmu (enter '21' to exit):"))

    if pilih == 21:
        break

    # desimal ke biner, oktal, dan hexadesimal
    if pilih == 1:
        desimal = int(input("masukan bilangan desimal: "))

        print("hasil konversinya:")

        biner = bin(desimal)
        print("hasil biner:", biner)

        oktal = oct(desimal)
        print("hasil oktal:", oktal)

        hexa = hex(desimal)
        print("hasil hexa:", hexa)


    # biner ke desimal, oktal, dan hexadesimal
    elif pilih == 2:
        binary_num = input("masukan bilangan biner: ")

        decimal_num = int(binary_num, 2)
        print("hasil desimal:", decimal_num)

        octal_num = oct(decimal_num)
        print("hasil oktal:", octal_num)

        hex_num = hex(decimal_num)
        print("hasil hexadesimal:", hex_num)

    # oktal ke desimal, biner, hexa
    elif pilih == 3:
        octal_number = input("masukan oktal:")

        decimal_number = int(octal_number, 8)
        print("hasil desimal:", decimal_number)

        # convert octal to binary
        binary_number = bin(int(octal_number, 8))
        print("hasil biner:", binary_number)

        # convert octal to hexadecimal
        hex_number = hex(int(octal_number, 8))
        print("hasil hexadesimal:", hex_number)

    # hexadesimal ke desimal, biner, oktal
    elif pilih == 4:
        hex_str = input("masukan hexadesimal: ")

        dec_num = int(hex_str, 16)
        print("hasil desimal:", dec_num)

        bin_num = bin(dec_num)
        print("hasil biner:", bin_num)

        oct_num = oct(dec_num)
        print("hasil oktal:", oct_num)

    elif pilih == 5:

        string_input = input("masukan string: ")

        ascii_code = [ord(char) for char in string_input]

        print("hasil string to ascii:", ascii_code)

    answer = input("mau coba konversi lain?? (nggih/mboten) ")

    if answer.lower() == "nggih":
        print(pilih)
    elif answer.lower() == "mboten":
        break
    else:
        print("koe nginpute salah. lebokna sing bener 'yes' or 'no'.")
        break