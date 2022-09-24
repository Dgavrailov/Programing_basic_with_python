
year_taxes_of_bascetball_training = int(input())
bascetball_shoes = year_taxes_of_bascetball_training - (year_taxes_of_bascetball_training * 0.4)
bascetball_ekip = bascetball_shoes - (bascetball_shoes * 0.2)
bascetball_ball = bascetball_ekip / 4
bascetball_prinadlejnosti = bascetball_ball / 5
razhodi = year_taxes_of_bascetball_training + bascetball_shoes + bascetball_ekip + \
          bascetball_ball + bascetball_prinadlejnosti
print(razhodi)



