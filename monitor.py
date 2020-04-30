import requests # Модуль для обработки URL
from bs4 import BeautifulSoup # Модуль для работы с HTML
import time # Модуль для остановки программы



# Основной класс
class Currency:
    # Ссылка на нужную страницу
    DOLLAR_RUB = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
    EURO_RUB = 'https://www.google.com/search?sxsrf=ALeKk01lKl5d6ZDYq6S4tiIYFTV_OosApw%3A1584863004411&ei=HBd3XvzdGMGImwW_065I&q=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=tdhj+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_l=psy-ab.1.0.0i67j0i10l9.7586.10360..12011...0.3..0.90.738.10......0....1..gws-wiz.......0i71j35i305i39j0i7i30j0i324j0i7i10i30j0i7i10i30i42j0i7i5i10i30j0i13.E8aVe5eyXmA'
    BRENT = 'https://yandex.ru/'
    # Заголовки для передачи вместе с URL
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    current_converted_price_USD = 0
    current_converted_price_EU = 0
    current_converted_price_BRENT = 0
    difference = 5 # Разница после которой будет отправлено сообщение

    def __init__(self):
        # Установка курса при создании объекта
        Get = self.get_currency_price()
        self.current_converted_price_USD = float(Get[0].replace(",", "."))
        self.current_converted_price_EU = float(Get[1].replace(",", "."))
        self.current_converted_price_BRENT = float(Get[2].replace(",", "."))
    # Метод для получения курса
    def get_currency_price(self):
        # Парсим всю страницу
        full_page_USD = requests.get(self.DOLLAR_RUB, headers=self.headers)
        full_page_EU = requests.get(self.EURO_RUB, headers=self.headers)
        full_page_BRENT = requests.get(self.BRENT, headers=self.headers)
        # Разбираем через BeautifulSoup
        soup = BeautifulSoup(full_page_USD.content, 'html.parser')
        soup1 = BeautifulSoup(full_page_EU.content, 'html.parser')
        soup2 = BeautifulSoup(full_page_BRENT.content, 'html.parser')
        # Получаем нужное для нас значение и возвращаем его
        convert = soup.findAll("span", { "class": "SwHCTb", "data-precision": 2})
        convert1 = soup1.findAll("span", { "class": "SwHCTb", "data-precision": 2})
        convert2 = soup2.findAll("span", { "class": "inline-stocks__value_inner"})
        return convert[0].text, convert1[0].text, convert2[2].text

    # Проверка изменения валюты
    def check_currency(self):
        currency = float(self.get_currency_price()[0].replace(",", "."))
        currency1 = float(self.get_currency_price()[1].replace(",", "."))
        currency2 = float(self.get_currency_price()[2].replace(",", "."))
        if currency >= self.current_converted_price_USD + self.difference:
            print("Курс сильно вырос, может пора что-то делать?")
        elif currency <= self.current_converted_price_USD - self.difference:
            print("Курс сильно упал, может пора что-то делать?")

        print("Сейчас курс:" + "\n" + "1 доллар = " + str(currency) + "\n" + "1 евро = " + str(currency1) + "\n" + "нефть Brent = " + str(currency2))
        # time.sleep(3) # Засыпание программы на 3 секунды
        # self.check_currency()

    def return_currency(self):
        return "Сейчас курс:" + "\n" + "1 доллар = " + str(self.current_converted_price_USD) + "\n" + "1 евро = " + str(self.current_converted_price_EU) + "\n" + "нефть Brent = " + str( self.current_converted_price_BRENT)

def main():

    #  currency = Currency()
    #  p = currency.return_currency()
    #  print(p)
    return
   

if __name__ == "__main__":
    main()