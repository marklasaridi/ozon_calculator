

class OzonCalculator:

    def __init__(self, filament_weight, filament_price=1500, package_price=22, marketing_price=.20, ozon_cut=.35):
        self.filament_cost = filament_price / 1000
        self.filament_weight = filament_weight
        self.package_price = package_price
        self.print_cost = self.filament_weight * self.filament_cost
        self.ozon_cut = ozon_cut
        self.marketing_price = marketing_price

    def calculate_profit(self, selling_price=500):
        profit = selling_price - self.package_price - self.print_cost - (selling_price * self.ozon_cut) - (
                selling_price * self.marketing_price)

        return profit

    def calculate_selling_price(self, profit=95):
        divider = float((1 - (self.ozon_cut + self.marketing_price)).__format__(".2f"))
        selling_price = (self.package_price + self.print_cost + profit) / divider

        return selling_price

    def print_to_console(self, info="price", selling_price=600, profit=95):

        if info == "profit":
            print(f'Цена продажи: {selling_price.__format__(".1f")}')
            print(f'Цена упаковки: {self.package_price}')
            print(f'Себестоимость пластика: {self.print_cost}')
            print(f'Доля Озона: {(selling_price * self.ozon_cut).__format__(".1f")}')
            print(f'Рекламные расходы: {(selling_price * self.marketing_price).__format__(".1f")}')
            print(f'ПРИБЫЛЬ С ПРОДАЖИ: {calc.calculate_profit(selling_price=selling_price).__format__(".1f")}')

        elif info == "price":
            print(f'ЦЕНА ПРОДАЖИ: {calc.calculate_selling_price(profit=profit).__format__(".1f")}')
            print(f'Цена упаковки: {self.package_price}')
            print(f'Себестоимость пластика: {self.print_cost}')
            print(f'Доля Озона: {(calc.calculate_selling_price(profit=profit) * self.ozon_cut).__format__(".1f")}')
            print(f'Рекламные расходы: '
                  f'{(calc.calculate_selling_price(profit=profit) * self.marketing_price).__format__(".1f")}')
            print(f'Прибыль с продажи: {profit}')

        else:
            print("Выберите информацию для вывода (price / profit)")


if __name__ == '__main__':
    calc = OzonCalculator(filament_weight=45, filament_price=1500)
    calc.print_to_console(info="profit", selling_price=495)
