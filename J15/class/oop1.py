# مرور
class Date:
    # Constructro
    def __init__(self, y=2023 , m=1 , d=1):
        self.year = y
        self.month = m
        self.day = d
        self.name = 'None'

    def set_name(self,n):
        self.name = n
    
    def yearplus1(self):
        self.year += 1
        print('year value plus one, now')

    def update_date_by_day(self , number_of_day):
        self.day += number_of_day

        new_day = self.day % 30
        self.month = self.month + self.day // 30
        self.dey = new_day

        new_month = self.month % 12
        self.year = self.year + self.month // 12
        self.month = new_month


    def show_date(self):
        print('Name of date: ',self.name)
        print(f'{self.year}/{self.month}/{self.day}')

d1 = Date(2002 , 11 , 17)
d1.show_date()

d1.update_date_by_day(17)
d1.show_date()

d1.update_date_by_day(47)
d1.show_date()