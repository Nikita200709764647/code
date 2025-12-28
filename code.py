//create comment
price = float(input("Введите цену товара: "))
discount = float(input("Введите процент скидки: "))

# Вычисляем скидку в рублях
discount_amount = price * discount / 100

# Вычисляем итоговую цену
final_price = price - discount_amount

# Выводим результат
print(f"Цена со скидкой: {final_price} руб.")
