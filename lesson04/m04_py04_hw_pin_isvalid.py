def is_valid_pin_codes(pin_codes):
    answer = 0

    if pin_codes and len(pin_codes) == len(set(pin_codes)):

        for pin_code in pin_codes:

            if pin_code.isdigit() and len(pin_code) == 4:
                answer += 1
    
    else:
        return False

    return answer == len(set(pin_codes))


if __name__ == "__main__":
    print(f"True : {is_valid_pin_codes(['1101', '9034', '0010', '0011', '1110'])}")
    print(f"False : {is_valid_pin_codes(['1101', '0010', '0010'])}")
    print(f"False : {is_valid_pin_codes(['1101', '0010', '001a'])}")
    print(f"False : {is_valid_pin_codes(['1101', '0010', '00103'])}")
    print(f"False : {is_valid_pin_codes(['111', '9034', '0010'])}")
    print(f"False : {is_valid_pin_codes(['1101', '0a10', '0010'])}")
    print(f"False : {is_valid_pin_codes(['11a1', '0010', '001a'])}")
    print(f"False : {is_valid_pin_codes([])}")
    print(f"{'001a'.isdigit()}")

