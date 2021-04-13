import pandas as pd
import xlwt
import xlrd
hoja=pd.read_excel('excel1.xls')
print(hoja)

#creo un excel en el cual se le va tener varia hojas
grabar=pd.ExcelWriter('resultado.xls')

#calcular algunos datos estadísticos y lo agrgo en la hoja1 d eexcel
a=hoja.describe()
a.to_excel(grabar,'hoja1')

#creo una segunda hoja de excel en resultados.xls y guardo la mediana
media=hoja.median()
media.to_excel(grabar,'hpoja2')

#creo una tercer hoja de excel y guardo el producto de voltiosXprecios.
precio=hoja.eval('voltios*precio')
precio.to_excel(grabar,'hoja3')

grabar.save()

##############################################

h=pd.read_excel('parcial.xls')
print(h)

#creo un excel en el cual se le va tener varia hojas
grabar=pd.ExcelWriter('resultado_parcial.xls')

#calcular algunos datos estadísticos y lo agrgo en la hoja1 d eexcel
l=h.describe()
l.to_excel(grabar,'datos_estadistico')

#creo una segunda hoja de excel en resultados.xls y guardo la mediana
media=h.median()
media.to_excel(grabar,'hoja_media')

grabar.save()