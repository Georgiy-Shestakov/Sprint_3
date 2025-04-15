import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

# Задание 1. Напиши геттеры
    @property
    def get_name_items(self):
        return self.__name_items
    
    @property
    def get_number_items(self):
        return self.__number_items
    
# Задание 2. Добавь товар в чек
    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.get_name_items.append(name)
            self.__number_items += 1

# Задание 3. Удали товар из чека
    def delete_item_from_check(self, name):
        if name not in self.get_name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__name_items.remove(name)
            self.__number_items -= 1

# Задание 4. Посчитай общую стоимость товаров
    def check_amount(self):
        total = []
        for item in self.get_name_items:
            total.append(self.__item_price[item])
        if len(total) > 10:
            return sum(total) * 0.9
        else:
            return sum(total)
        
# Задание 5. Вычисли НДС для товаров со ставкой 20%
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for item in self.get_name_items:
            if self.__tax_rate[item] == 20:
                twenty_percent_tax.append(item)
                total.append(self.__item_price[item])
        if len(total) > 10:
            return sum(total) * 0.9 * 0.2
        else:
            return sum(total) * 0.2
        
# Задание 6. Вычисли НДС для товаров со ставкой 10%
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for item in self.get_name_items:
            if self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)
                total.append(self.__item_price[item])
        if len(total) > 10:
            return sum(total) * 0.9 * 0.1
        else:
            return sum(total) * 0.1
        
# Задание 7. Посчитай общую сумму налогов
    def total_tax(self):
        return self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()
    
# Задание 8. Верни номер телефона покупателя
    @staticmethod
    def get_telephone_number(telephone_number):
        if telephone_number % 1 != 0:
            raise ValueError('Необходимо ввести цифры')
        elif len(str(telephone_number)) < 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        else:
            return f'+7{telephone_number}'
        
# Дополнительное задание
    @staticmethod
    def get_date_and_time():
        now = datetime.datetime.now()
        date_and_time = []
        date = [['часы', (lambda x: x.hour)(now)], ['минуты', (lambda x: x.minute)(now)], ['день', (lambda x: x.day)(now)], ['месяц', (lambda x: x.month)(now)], ['год', (lambda x: x.year)(now)]]
        for mini_list in date:
            date_and_time.append(f'{mini_list[0]}: {mini_list[1]}')
        return date_and_time


# Проверки
test = OnlineSalesRegisterCollector()
# Добавление товара
test.add_item_to_cheque('кефир')
test.add_item_to_cheque('кефир')
test.add_item_to_cheque('кефир')
test.add_item_to_cheque('кефир')
test.add_item_to_cheque('кефир')
test.add_item_to_cheque('кефир')
test.add_item_to_cheque('кефир')
test.add_item_to_cheque('кефир')
test.add_item_to_cheque('кефир')
test.add_item_to_cheque('кефир')
test.add_item_to_cheque('кола')
print(f'Список товаров в корзине: {test.get_name_items}')
print(f'Кол-во товаров в корзине: {test.get_number_items}')
# # Удаление товара
# test.delete_item_from_check('кола')
# print(test.get_name_items)
# print(test.get_number_items)
# Расчёт стоимости
print(f'Сумма товаров в корзине: {test.check_amount()}')
# Расчёт НДС 20%
print(f'Включая НДС 20%: {test.twenty_percent_tax_calculation()}')
# Расчёт НДС 10%
print(f'Включая НДС 10%: {test.ten_percent_tax_calculation()}')
# Расчёт общей суммы налогов
print(f'Общая сумма налогово составляет: {test.total_tax()}')
# Проверка телефонов
print(f'Проверка телефона: {test.get_telephone_number(1234567890)}')
# Доп.задание
print(test.get_date_and_time())
