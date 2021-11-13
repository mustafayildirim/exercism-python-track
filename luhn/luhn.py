class Luhn:
    card_num = ''
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')

    def valid(self):
        if len(self.card_num) > 1:
            if not self.card_num.isdecimal():
                return False

            double_index = 0
            if len(self.card_num) % 2:
                double_index = 1

            total = 0
            for index, number in enumerate(self.card_num):
                number = int(number)
                if (index + double_index) % 2 == 0:
                    add_num = number * 2
                    if add_num > 9:
                        add_num = add_num - 9
                    total = total + add_num
                else:
                    total = total + number

            if total % 10 == 0:
                return True

        return False
