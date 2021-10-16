from datetime import datetime


def main():
    user_input = input("Enter datetime in format dd.mm [-]: ")
    user_entered_date = datetime.strptime(user_input, '%d.%m')
    current_date = datetime.now()
    user_entered_date = user_entered_date.replace(year=current_date.year)
    if current_date > user_entered_date:
        print(f'{current_date - user_entered_date} days left.')
    else:
        user_entered_date = user_entered_date.replace(year=current_date.year+1)
        print(f'{user_entered_date - current_date} days left.')

if __name__ == "__main__":
    main()
