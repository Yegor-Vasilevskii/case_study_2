#Developers:
#Mahanov S (%), Pestretsova M (%), Pokareva C (20%), Vasilevskiy Y (%)
#Let's say hello to our guests!
print('Добро пожаловать!')
income_month = int(input('Введите ваш месячный доход:'))
jan = income_month
Feb = income_month
Mar = income_month
Apr = income_month
May = income_month
Jun = income_month
Jul = income_month
Aug = income_month
Sep = income_month
Oct = income_month
Nov = income_month
Dec = income_month
month = [jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec]
income = 0
for element in month:
    income += element
print('Введите ваше семейное положение: 1 - Холост(а); 2 - Женат(а); 3 - отец/мать одиночка')
number_type = input()
def tax_for_lonely(b):
    if b > 0 and b <= 9075:
        return 0.1 * b
    elif b > 9075 and b <= 36900:
        return 0.1 * 9075 + (b - 9075) * 0.15
    elif b > 36900 and b <= 89350:
        return 0.1 * 9075 + (36900 - 9075) * 0.15 + (b - 36900) * 0.25
    elif b > 89350 and b <= 186350:
        return 0.1 * 9075 + (36900 - 9075) * 0.15 + (89350 - 36900) * 0.25 + (b - 89350) * 0.28
    elif b > 186350 and b <= 405100:
        return 0.1 * 9075 + (36900 - 9075) * 0.15 + (89350 - 36900) * 0.25 + (186350 - 89350) * 0.28 + (b - 186350) * 0.33
    elif b > 405100 and b <= 406750:
        return 0.1 * 9075 + (36900 - 9075) * 0.15 + (89350 - 36900) * 0.25 + (186350 - 89350) * 0.28 + (405100 - 186350) * 0.33 + (b - 405100) * 0.35
    else:
        return 0.1 * 9075 + (36900 - 9075) * 0.15 + (89350 - 36900) * 0.25 + (186350 - 89350) * 0.28 + (405100 - 186350) * 0.33 + (406750 - 405100) * 0.35 + (b - 406750) * 0.396
   

#Pestretsova:    
    
#Pokareva: I'll write about lonely parent, if type_number == 3
    
def  tax_for_lonely_parents(b):
    if b > 0 and b <= 12950:
        return 0.1 * b
    elif b > 12950 and b <= 49400:
        return 0.1 * 12950 + (b - 12951) * 0.15
    elif b > 49400 and b <= 127550:
        return 0.1 * 12950 + (49400 - 12951) * 0.15 + (b - 49401) * 0.25
    elif b > 127550 and b <= 206600:
        return 0.1 * 12950 + (49400 - 12951) * 0.15 + (127550 - 49401) * 0.25 + (b - 127551) * 0.28
    elif b > 206600 and b <= 405100:
        return 0.1 * 12950 + (49400 - 12951) * 0.15 + (127550 - 49401) * 0.25 + (186350 - 127551) * 0.28 + (b - 206601) * 0.33
    elif b > 405100 and b <= 432200:
        return 0.1 * 12950 + (49400 - 12951) * 0.15 + (127550 - 49401) * 0.25 + (186350 - 127551) * 0.28 + (405100 - 206601) * 0.33 + (b - 405101) * 0.35
    else:
        return 0.1 * 12950 + (49400 - 12951) * 0.15 + (127550 - 49401) * 0.25 + (186350 - 127551) * 0.28 + (405100 - 206601) * 0.33 + (432200 - 405101) * 0.35 + (b - 432201) * 0.396
    
