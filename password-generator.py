import string
import random

if __name__ == "__main__":

    lowerSet = string.ascii_lowercase
    upperSet = string.ascii_uppercase
    digitSet = string.digits
    punctuationSet = string.punctuation

    print("------------------------------------------------------------------")
    print("""\tInstruction : Passwords are required. A character count 
    \t\t\t of less than 6 is considered insufficient.
    \t\t\t Make sure it's between 12 and 15 characters
    \t\t\t long for a strong password.""")
    print("------------------------------------------------------------------")

    try:
        passwordLength = int(input("Enter Password Length: "))

        if passwordLength == 0:
            print("You're An Idiot!!!! 😡")

        elif passwordLength < 0:
            print("It's a Negative Number. 😒")

        elif passwordLength >= 94:
            print("Sorry!! We Can't Generate. 😴")

        else:

            def passMaker():
                password = []
                password.extend(list(lowerSet))
                password.extend(list(upperSet))
                password.extend(list(digitSet))
                password.extend(list(punctuationSet))

                return (f"Your password is :\n{''.join(random.sample(password, passwordLength))}")

            passMaker()

            if (6 <= passwordLength <= 25):
                print(passMaker())

            elif 26 <= passwordLength <= 93:
                print("The Password will be too hard to memorise. 😢")

                user_ask = input("Do you really continue ?? \n(y / n) : ").lower()

                if user_ask == "y":
                    print(passMaker())

                else:
                    print("You are smart. 😊")

            else:
                print("It's Weak, Enter At Least Greater-Than 6. 😒")

    except ValueError:
        print("Select Numbers Only. 😒")

