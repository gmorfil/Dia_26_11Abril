import pandas as pd
import xlwt
import xlrd
hoja=pd.read_excel('excel1.xls')
print(hoja)

grabar=pd.ExcelWriter('resultado.xls')
a=hoja.describe()
a.to_excel(grabar,'hoja1')

media=hoja.median()
media.to_excel(grabar,'hpoja2')

precio=hoja.eval('voltios*precio')
precio.to_excel(grabar,'hoja3')

grabar.save()