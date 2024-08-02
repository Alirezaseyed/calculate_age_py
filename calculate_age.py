import datetime

def calculate_age(birth_year):
    current_year = datetime.datetime.now().year
    if birth_year > current_year:
        raise ValueError("سال تولد نمی‌تواند در آینده باشد!")
    if birth_year <= 0:
        raise ValueError("سال تولد باید یک عدد مثبت باشد!")
    return current_year - birth_year

def age_calculator():
    while True:
        user_input = input("لطفا سال تولد خود را وارد کنید (یا 'exit' برای خروج): ")
        if user_input.lower() == 'exit':
            print("خروج از برنامه.")
            
            break
        try:
            birth_year = int(user_input)
            age = calculate_age(birth_year)
            print(f"سن شما {age} سال است.")
        except ValueError as ve:
            print(f"خطا: {ve}")
        except Exception as e:
            print("خطای نامشخص رخ داده است. لطفا یک عدد معتبر وارد کنید.")

if __name__ == "__main__":
    age_calculator()
