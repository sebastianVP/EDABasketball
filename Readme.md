# Exploratory Data Analysis Basketball
Veamos ahora el uso de web scrapying para recopilar data de una web y
publicar de manera efectiva el analisis y resultados con streamlit.

## Veamos el uso de la libreria **streamlit**

### ENCABEZADO
Encabezado para la pagina Web con un tipado elegante y agradable a la vista

1. st.title
2. st.markdown

Links con referencia
* [Basketball-reference.com](https://www.basketball-reference.com/).


### TITULO  CON **SIDEBAR**
3. st.sidebar.header('User Input Features')

### BOX
4. st.sidebar.selectbox('year')

###  SIDEBAR CON OPCION MULTISELECT
5. st.sidebar.multiselect('team')

Los objetos 3,4,5 se encuetran como bien se indica en el sidebar

6. st.header("Display PLayer Stats of Selected TEAM(S)")

7. st.write()

8. st.dataframe()

9. st.markdown()

10. st.button

11. st.header

12. st.pyplot objeto de ploteo

Los objetos 1,2,6,7,8,9,10,11 en la parte central derecha.

Esta pagina esta extrayendo la data de Basketball-Reference
Y te permite realizar un filtrado y correlation. Practicamente como un colab.

