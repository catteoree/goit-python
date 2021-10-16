from collections import deque


def main():
    user_inputs = deque(maxlen=5)

    while True:
        user_input = input("Enter: ")
        user_inputs.append(user_input)

        if user_input == "q":
            break

    print(f"Last 5 inputs: {user_inputs}")


if __name__ == "__main__":
    main()
