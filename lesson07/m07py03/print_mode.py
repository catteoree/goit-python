def print_mode(num1, num2, sign, answer):
    if answer != "Error":
        return f"{num1} {sign} {num2} = {answer}"
    else:
        return answer


if __name__ == "__main__":
    print_mode(3, 2, "+", 5)