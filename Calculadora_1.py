from tkinter import *

# Creacion de la Ventana y sus parametros:
ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("325x280")     #El .geometry es para dar valores al tamaño de tu ventana
ventana.iconbitmap(r"D:\Misael\Descargas\Programacion-Python\Calculadora V0.1(Misael)\Calculadora-Icono.ico")  #Opcional solo fue para meterle otro icono y darle mas estilo en caso de error copia aca la direccion de este icono en tu computadora

i= 0            #i es la variable de referencia para borrar y recorrer la entrada de texto

#Creacion de la Entrada de texto:
entrada_1 = Entry(ventana, font=("Calibri 20"))
entrada_1.grid(row=0, column=0, columnspan=4, padx=20, pady=5)

#Definimos la funcion para el valor a cada boton:
def click_boton(valor):             #Esta funcion es la encargada de insertar los valores a los botones
    global i                        #Globalizamos para evitar errores
    entrada_1.insert(i, valor)      #Nos permite insertar los valores en la entrada de texto
    i += 1                          #i+=1 es para que al borrar se corra hacia la derecha y no a la izquierda

def borrar():                       #Esta funcion es la encargada de borrar o reiniciar la calculadora con AC
    entrada_1.delete(0,END)         #delete es el comando para eliminar y (0,END) para que borre todos los datos de la entrada

def operaciones():                  #Esta funcion es la encargada de realizar las operaciones en la calculadora
    ecuacion = entrada_1.get()      #.get te permite tomar el valor que ingresaste a la calculadora
    resultado = eval(ecuacion)      #La funcion eval es una funcion de python que te evalua la operacion independientemente de cual sea
    entrada_1.delete(0, END)        #En esta parte el .delete hace que al lanzar el resultado borre lo que habia anteriormente
    entrada_1.insert(0,resultado)   #Y por ultimo .insert(0,resultado) hace que lance el resultado en la entrada de texto
    i = 0 

#Creacion de los Botones numericos:
boton_1 = Button(ventana, text="1", width=5, height=2, command=lambda:click_boton(1))   #se utiliza lambda debido a que es
boton_2 = Button(ventana, text="2", width=5, height=2, command=lambda:click_boton(2))   #la funcion que permite una entrada
boton_3 = Button(ventana, text="3", width=5, height=2, command=lambda:click_boton(3))   #con parentesis click_boton()
boton_4 = Button(ventana, text="4", width=5, height=2, command=lambda:click_boton(4))
boton_5 = Button(ventana, text="5", width=5, height=2, command=lambda:click_boton(5))
boton_6 = Button(ventana, text="6", width=5, height=2, command=lambda:click_boton(6))
boton_7 = Button(ventana, text="7", width=5, height=2, command=lambda:click_boton(7))
boton_8 = Button(ventana, text="8", width=5, height=2, command=lambda:click_boton(8))
boton_9 = Button(ventana, text="9", width=5, height=2, command=lambda:click_boton(9))
boton_0 = Button(ventana, text="0", width=17, height=2, command=lambda:click_boton(0))

#Creacion de los botones de simbolos y borrar:
boton_delete = Button(ventana, text="AC", width=5, height=2, command=lambda: borrar())
boton_parentesis1 = Button(ventana, text="(", width=5, height=2, command=lambda:click_boton("("))
boton_parentesis2 = Button(ventana, text=")", width=5, height=2, command=lambda:click_boton(")"))
boton_punto = Button(ventana, text=".", width=5, height=2, command=lambda:click_boton("."))

#Creacion de los botones para las operaciones aritmeticas:
boton_sumar = Button(ventana, text="+", width=5, height=2, command=lambda:click_boton("+"))
boton_restar = Button(ventana, text="-", width=5, height=2, command=lambda:click_boton("-"))
boton_multiplicar = Button(ventana, text="x", width=5, height=2, command=lambda:click_boton("*"))
boton_dividir = Button(ventana, text="/", width=5, height=2, command=lambda:click_boton("/"))
boton_igual = Button(ventana, text="=", width=5, height=2, command=lambda: operaciones())

#Agregamos los botones creados a la pantalla o interfaz tkinter: el comando.grid nos permite manejar las posiciones de estos
boton_delete.grid(row="1",column="0", padx="5", pady="2")
boton_parentesis1.grid(row="1",column="1", padx="5", pady="2")
boton_parentesis2.grid(row="1",column="2", padx="5", pady="2")
boton_dividir.grid(row="1",column="3", padx="5", pady="2")

boton_7.grid(row=2,column=0, padx=5, pady=2)
boton_8.grid(row=2,column=1, padx=5, pady=2)
boton_9.grid(row=2,column=2, padx=5, pady=2)
boton_multiplicar.grid(row=2,column=3, padx=5, pady=2)

boton_4.grid(row=3,column=0, padx=5, pady=2)
boton_5.grid(row=3,column=1, padx=5, pady=2)
boton_6.grid(row=3,column=2, padx=5, pady=2)
boton_sumar.grid(row=3,column=3, padx=5, pady=2)

boton_1.grid(row=4,column=0, padx=5, pady=2)
boton_2.grid(row=4,column=1, padx=5, pady=2)
boton_3.grid(row=4,column=2, padx=5, pady=2)
boton_restar.grid(row=4,column=3, padx=5, pady=2)

boton_0.grid(row=5, column=0,columnspan=2, padx=5, pady=2)
boton_punto.grid(row=5, column=2, padx=5, pady=2)
boton_igual.grid(row=5, column=3, padx=5, pady=2)

ventana.mainloop()    #el .mainloop nos indica el final de nuestra ventana es por ello que todo debe ir antes