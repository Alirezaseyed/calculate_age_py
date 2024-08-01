import datetime

def calculate_age(birth_year):
    """
    محاسبه سن بر اساس سال تولد.

    Args:
        birth_year (int): سال تولد.

    Returns:
        int: سن فعلی.

    Raises:
        ValueError: اگر سال تولد در آینده باشد.
    """
    current_year = datetime.datetime.now().year
    if birth_year > current_year:
        raise ValueError("سال تولد نمی‌تواند در آینده باشد!")
    if birth_year <= 0:
        raise ValueError("سال تولد باید یک عدد مثبت باشد!")
    return current_year - birth_year

def age_calculator():
    """
    درخواست سال تولد از کاربر و محاسبه سن.

    این تابع به صورت مداوم از کاربر درخواست می‌کند تا سال تولد خود را وارد کند و سن را محاسبه می‌کند.
    کاربر می‌تواند با وارد کردن 'exit' از برنامه خارج شود.
    """
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

# اجرای برنامه
if __name__ == "__main__":
    age_calculator()