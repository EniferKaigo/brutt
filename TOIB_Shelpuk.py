import hashlib
import itertools
import string

def brute_force_password(target_hash, characters, max_length):
    attempt_count = 0  

    for length in range(1, max_length + 1):  
        for password_combination in itertools.product(characters, repeat=length):
            candidate_password = ''.join(password_combination)
            candidate_hash = hashlib.sha256(candidate_password.encode()).hexdigest()
            
            attempt_count += 1  

            if attempt_count % 10000 == 0:
                print(f"Проверено паролей: {attempt_count}")

            if candidate_hash == target_hash:
                return candidate_password, attempt_count

    return None, attempt_count

if name == "main":
    input("Программа готова. Нажмите Enter для продолжения...")

    target_password = input("Введите пароль для подбора (до 8 символов): ")
    
    if len(target_password) > 8:
        print("Ошибка: длина пароля не должна превышать 8 символов.")
    else:
        target_password_hash = hashlib.sha256(target_password.encode()).hexdigest()
        print(f"Хеш целевого пароля: {target_password_hash}")

        characters = string.ascii_letters + string.digits  # Строчные/заглавные буквы и цифры
        max_length = 8

        input("Нажмите Enter, чтобы начать подбор пароля")

        found_password, attempts = brute_force_password(target_password_hash, characters, max_length)

        if found_password:
            print(f"Пароль успешно подобран: {found_password}")
        else:
            print("Пароль не найден в пределах заданного диапазона.")
        
        print(f"Всего проверено паролей: {attempts}")
