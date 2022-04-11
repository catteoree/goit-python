def main():
    error = 1
    while error:
        try:
            b = int(input("Z: "))
        except ValueError:
            print("Error")
        else:
            error = 0



if __name__ == "__main__":
    main()
