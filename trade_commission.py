city = input()
volume_sales = float(input())
commission = 0
error_condition = False


if city == 'Sofia':
    if 0 <= commission <= 500:
    commission = volume_sales * 0.05
    elif 500 < commission <=  1000:
        commission = volume_sales * 0.07
    elif 1000 < commission <= 10000:
        commission = volume_sales * 0.8
    elif commission > 10000:
        commission = volume_sales * 0.12
else:
    error_condition = True

if city == "Varna":
    if 0 <= commission <= 500:
        commission = volume_sales * 0.045
    elif 500 < commission <=  1000:
        commission = volume_sales * 0.75
    elif 1000 < commission <= 10000:
        commission = volume_sales * 0.10
    elif commission > 10000:
        commission = volume_sales * 0.13
    else:
        error_condition = True
if city == "Plovdiv":
    if 0 <= commission <= 500:
        commission = volume_sales * 0.055
    elif 500 < commission <=  1000:
        commission = volume_sales * 0.08
    elif 1000 < commission <= 10000:
        commission = volume_sales * 0.12
    elif commission > 10000:
        commission = volume_sales * 0.145
    else:
        error_condition = True
else:
    pass
if not error_condition:
# ako error_condition ne e setnat na true
    print(f'{commission:.2f}')
else:
    print('error')

GRESHNA
