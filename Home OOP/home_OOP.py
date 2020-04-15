import random


class DiscountCard:

    def __init__(self, card_number, discount, card_date, summ):
        self.__card_number = card_number
        self.__discount = discount
        self.__card_date = card_date
        self.__summ = summ

    def card_info(self):
        print("Card number:", self.__card_number, ", Discount:",
              self.__discount, "%, ", "Card Date:", self.__card_date)

    def discount_info(self):
        print("Your total discount is:", int(
            (buy.summ * buy.discount)/100), "UAH")

    def amount_info(self):
        print("Your total amount is:", int(
            buy.summ - ((buy.summ * buy.discount)/100)), "UAH")

    def add_discount_info(self):
        print("If you want to get more discount, you need to purchase on this amount:",
              1000 - self.__summ % 1000, "UAH")

    @property
    def summ(self):
        return self.__summ

    @property
    def discount(self):
        return self.__discount

    @summ.setter
    def summ(self, add_summ):
        if float(add_summ) > 0:
            self.__summ += float(add_summ)
            self.__discount = 1 + self.__summ // 1000


buy = DiscountCard(random.randint(100000000, 999999999), 1, "20/02/2018", 0)

while buy.summ <= 5000:
    print("============================================================")
    buy.card_info()
    print("============================================================")
    buy.summ = float(input("Enter amount of your purchase: "))
    print("Your current discount is:", buy.discount, "%")
    buy.discount_info()
    buy.amount_info()
    buy.add_discount_info()


print("============================================================")
print("Your total amount without discount:", buy.summ)
