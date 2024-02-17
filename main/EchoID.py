def caller(*user):
    try:
        number = int(input("Enter the number: "))
        for in_dict in user:
            if number in in_dict:
                print("The number you entered corresponds to:", in_dict[number])
                break
        else:
            print("User not found")
    except ValueError:
        print("Please enter a valid number.")

# Your dictionaries A, B, C remain the same

caller(A, B, C)

# Format for User Contact book
# var = {"Number": "name"}


A = {
    9009009001: "Abhinav",
    8008008001: "Divya",
    7007007001: "Shashank",
    5005005001: "Jaitely"
}

B = {
    2323232323: "JOJO",
    1212121212: "KOKO",
    3434343434: "Momo",
    5005005001: "Jaitely-airtel"
}

C = {
    5555555555: "Ram",
    6666666666: "Shyam",
    7777777777: "Pooja",
    8888888888: "Aarti"
}

caller(A, B, C)

#  all code files are moved to the server folder !!
