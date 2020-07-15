#!/usr/bin/env python
#_*_ coding: utf8 _*_
from tkinter import ttk
from tkinter import *

def inicializar_variables():
	global mp,mpi,mod,moi,ocifs_acum,gastos_administrativos,gadmin_acum,impuestos,ventas,iipt,ifpt,iipp,ifpp,iimp,ifmp,iimi,ifmi,cif,cprimo,conversion,mpc,mic,cfab,cprod,cventas,d_basicos,d_basicos2,datos_mostrar, utilidad_bruta, otros_gastos, on_of_inventarios, color
	mp = 0
	mpi = 0
	mod = 0
	moi = 0

	color = "#73947D"

	ocifs_acum = []
	gastos_administrativos = 0
	gadmin_acum = []
	impuestos = 0.30
	ventas = 0
	otros_gastos = 0

	iipt = 0
	ifpt = 0
	iipp = 0
	ifpp = 0
	iimp = 0
	ifmp = 0
	iimi = 0
	ifmi = 0

	cif = 0
	cprimo = 0
	conversion = 0
	mpc = 0
	mic = 0
	cfab = 0
	cprod = 0
	cventas = 0

	d_basicos = {}
	d_basicos2 = {}
	datos_mostrar = {}

	utilidad_bruta = 0

	on_of_inventarios = False

inicializar_variables()
#FUNCION DE AYUDA
def validar(dato):
	try:
		n = float(dato)
		if dato != "":
			return True
		else:
			return False
	except:
		return False

#*************************************FUNCIONES PARA INICIALIZAR LOS DATOS RECIBIDOS
def agregar_mp():
	global mp
	if validar(var_mp.get()):
		mp = float(var_mp.get())
		datos_mostrar["mp"] = mp
		mostrar_datos()
def agregar_mpi():
	global mpi
	if validar(var_mpi.get()):
		mpi = float(var_mpi.get())
		datos_mostrar["mpi"] = mpi
		cifs()
		mostrar_datos()
	
def agregar_mod():
	global mod
	if validar(var_mod.get()):
		mod = float(var_mod.get())
		datos_mostrar["mod"] = mod
		mostrar_datos()
def agregar_moi():
	global moi
	if validar(var_moi.get()):
		moi = float(var_moi.get())
		datos_mostrar["moi"] = moi
		cifs()
		mostrar_datos()

def set_datos_basicos():
	agregar_mp()
	agregar_mpi()
	agregar_mod()
	agregar_moi()

def agregar_iipt():
	global iipt
	if validar(var_iipt.get()):
		iipt = float(var_iipt.get())
		datos_mostrar["IIPT"] = iipt
	mostrar_datos()
def agregar_ifpt():
	global ifpt
	if validar(var_ifpt.get()):
		ifpt = float(var_ifpt.get())
		datos_mostrar["IFPT"] = ifpt
	mostrar_datos()

def agregar_iipp():
	global iipp
	if validar(var_iipp.get()):
		iipp = float(var_iipp.get())
		datos_mostrar["IIPP"] = iipp
	mostrar_datos()
def agregar_ifpp():
	global ifpp
	if validar(var_ifpp.get()):
		ifpp = float(var_ifpp.get())
		datos_mostrar["IFPP"] = ifpp
	mostrar_datos()

def agregar_iimp():
	global iimp
	if validar(var_iimp.get()):
		iimp = float(var_iimp.get())
		datos_mostrar["IIMP"] = iimp
	mostrar_datos()
def agregar_ifmp():
	global ifmp
	if validar(var_ifmp.get()):
		ifmp = float(var_ifmp.get())
		datos_mostrar["IFMP"] = ifmp
	mostrar_datos()

def agregar_iimi():
	global iimi
	if validar(var_iimi.get()):
		iimi = float(var_iimi.get())
		datos_mostrar["IIMI"] = iimi
	cifs()
	mostrar_datos()
def agregar_ifmi():
	global ifmi
	if validar(var_ifmi.get()):
		ifmi = float(var_ifmi.get())
		datos_mostrar["IFMI"] = ifmi
	cifs()
	mostrar_datos()

def set_inventarios():
	agregar_iipt()
	agregar_ifpt()
	agregar_iipp()
	agregar_ifpp()
	agregar_iimp()
	agregar_ifmp()
	agregar_iimi()
	agregar_ifmi()

def agregar_impuestos():
	global impuestos
	if validar(var_impuestos.get()):
		impuestos = float(var_impuestos.get())/100
		datos_mostrar["impuesto"] = impuestos
	datos_mostrar["impuesto"] = impuestos
	mostrar_datos()

def agregar_ventas():
	global ventas
	if validar(var_ventas.get()):
		ventas = float(var_ventas.get())
		datos_mostrar["ventas"] = ventas
	mostrar_datos()

def agregar_gadmin():
	global gadmin_acum
	try: 
		gadmin = float(var_gadmin.get())
		if gadmin != "":
			if len(gadmin_acum) == 0:
				gadmin_acum.append(gadmin)
				var_gadmin.set("")
			elif gadmin_acum[len(gadmin_acum)-1] != gadmin:
				gadmin_acum.append(gadmin)
				var_gadmin.set("")
		mostrar_gadmin()
		cal_gastos_adm()
		mostrar_datos()
	except:
		return

def agregar_otros_cifs():
	global ocifs_acum
	try:
		ocifs = float(var_ocifs.get())
		if ocifs!="":
			if  len(ocifs_acum) == 0:
				ocifs_acum.append(ocifs)
				var_ocifs.set("")
			elif ocifs_acum[len(ocifs_acum)-1] != ocifs:
				ocifs_acum.append(ocifs)
				var_ocifs.set("")
		mostrar_cifs()
		cifs()
		mostrar_datos()
		
	except:
		return

def agregar_otros_gastos():
	global otros_gastos
	if validar(var_otros_gastos.get()):
		otros_gastos = float(var_otros_gastos.get())
		datos_mostrar["otros gastos"] = otros_gastos
	mostrar_datos()

def activar_inventarios():
	global on_of_inventarios
	if on_of_inventarios == False:
		on_of_inventarios = True
		txt_inventario.set("> of <")
		onb.config(bg="green")
		entry_inventarios()
	else:
		on_of_inventarios = False
		txt_inventario.set("> on <")
		onb.config(bg="red")
		entry_inventarios()

def entry_inventarios():
	if on_of_inventarios == False:
		iipte.config(state="readonly")
		ifpte.config(state="readonly")
		iippe.config(state="readonly")
		ifppe.config(state="readonly")
		iimpe.config(state="readonly")
		ifmpe.config(state="readonly")
		iimie.config(state="readonly")
		ifmie.config(state="readonly")
		reset_inventarios()
	else:
		iipte.config(state="normal")
		ifpte.config(state="normal")
		iippe.config(state="normal")
		ifppe.config(state="normal")
		iimpe.config(state="normal")
		ifmpe.config(state="normal")
		iimie.config(state="normal")
		ifmie.config(state="normal")
def reset_inventarios():
	global iipt,ifpt,iipp,ifpp,iimp,ifmp,iimi,ifmi, datos_mostrar
	iipt = 0
	ifpt = 0
	iipp = 0
	ifpp = 0
	iimp = 0
	ifmp = 0
	iimi = 0
	ifmi = 0

	datos_mostrar["IIPT"] = iipt
	datos_mostrar["IFPT"] = ifpt
	datos_mostrar["IIPP"] = iipp
	datos_mostrar["IFPP"] = ifpp
	datos_mostrar["IIMP"] = iimp
	datos_mostrar["IFMP"] = ifmp
	datos_mostrar["IIMI"] = iimi
	datos_mostrar["IFMI"] = ifmi

	del(datos_mostrar["IIPT"])
	del(datos_mostrar["IFPT"])
	del(datos_mostrar["IIPP"])
	del(datos_mostrar["IFPP"])
	del(datos_mostrar["IIMP"])
	del(datos_mostrar["IFMP"])
	del(datos_mostrar["IIMI"])
	del(datos_mostrar["IFMI"])

	var_iipt.set("") 
	var_ifpt.set("") 
	var_iipp.set("") 
	var_ifpp.set("") 
	var_iimp.set("") 
	var_ifmp.set("") 
	var_iimi.set("") 
	var_ifmi.set("") 
	cifs()
	mostrar_datos()

#*********************************FUNCIONES PARA MOSTRAR Y BORRAR EN PANTALLA
def mostrar_datos():
	#Limpiando la tablita
	records = tabla6.get_children()
	for elemento in records:
		tabla6.delete(elemento)

	for datos in datos_mostrar:
		text = "{} = {}".format(datos, datos_mostrar[datos])
		tabla6.insert("",END, text=text)

def mostrar_cifs():
	#Limpiando la tablita
	records = tabla.get_children()
	for elemento in records:
		tabla.delete(elemento)

	for cifs in ocifs_acum:
		tabla.insert("",END, text=cifs)

def borrar_cifs():
	global ocifs_acum
	try:
		dato = tabla.item(tabla.selection())['text']
		ocifs_acum.remove(dato)
		mostrar_cifs()
		cifs()
		mostrar_datos()
	except:
		return
	
def mostrar_gadmin():
	#Limpiando la tablita
	records = tabla2.get_children()
	for elemento in records:
		tabla2.delete(elemento)

	for admin in gadmin_acum:
		tabla2.insert("",END, text=admin)

def borrar_gadmin():
	global tabla2, gadmin_acum
	try:
		dato = tabla2.item(tabla2.selection())['text']
		gadmin_acum.remove(dato)
		mostrar_gadmin()
		cal_gastos_adm()
		mostrar_datos()
	except:
		return

def mostar_resultados_en_tablas(tabl, arreglo):
	#Limpiando la tablita
	records = tabl.get_children()
	for elemento in records:
		tabl.delete(elemento)

	for datos in arreglo:
		tabl.insert("",END, text=datos, values = arreglo[datos])

def mostrar_resultados():
	mostar_resultados_en_tablas(tabla3, d_basicos)
	mostar_resultados_en_tablas(tabla5, d_basicos2)

def reset_todo():
	var_iipt.set("") 
	var_ifpt.set("") 
	var_iipp.set("") 
	var_ifpp.set("") 
	var_iimp.set("") 
	var_ifmp.set("") 
	var_iimi.set("") 
	var_ifmi.set("") 

	var_mp.set("") 
	var_mpi.set("") 
	var_mod.set("") 
	var_moi.set("") 

	var_ocifs.set("") 
	var_gadmin.set("") 
	var_impuestos.set("") 
	var_ventas.set("")
	var_otros_gastos.set("")

	inicializar_variables()
	mostrar_cifs()
	mostrar_gadmin()
	mostrar_datos()
	
	mostrar_resultados()


#**********************************FUNCIONES PARA REALIZAR LOS CALCULOS
def materia_prim_consumida():
	global mpc
	mpc = iimp + mp - ifmp
	d_basicos["Materiales Prima Consumida(MPC)"] = mpc

def materia_indi_cosumida():
	global mic
	mic = iimi + mpi - ifmi
	d_basicos["Materiales Indirectos Consumidos (MIC)"] = mic

def cifs():
	materia_indi_cosumida()
	otros_cifs = sum(ocifs_acum)
	global cif
	cif = moi + mic + otros_cifs
	datos_mostrar["cif"] = cif
	d_basicos["CIF"] = cif

def cal_gastos_adm():
	global gastos_administrativos
	gastos_administrativos = sum(gadmin_acum)
	datos_mostrar['Gast.Administrativos'] = gastos_administrativos

def costo_primo():
	materia_prim_consumida()
	global cprimo
	cprimo = mpc + mod
	d_basicos["Costo Primo"] = cprimo

def costo_conversion():
	global conversion
	conversion = mod + cif
	d_basicos["Costo de Conversion"] = conversion

def cfabr():
	materia_prim_consumida()
	global cfab
	cfab = mpc + mod + cif
	d_basicos2["Costo de Fabricacion"] = cfab
	
def cprodr():
	global cprod
	cprod = iipp + cfab - ifpp
	d_basicos2["Costo de Produccion"] = cprod

def cvtansr():
 	global cventas
 	cventas = iipt + cprod - ifpt
 	d_basicos2["Costo de Ventas"] = cventas

def utilidad_operativa():
	global utilidad_bruta
	if on_of_inventarios:
		utilidad_bruta = ventas - cventas 
		utilidad_de_operacion = utilidad_bruta - gastos_administrativos - otros_gastos
		d_basicos2["Utilidad Bruta"] = utilidad_bruta
		d_basicos2["Utilidad Operativa"] = utilidad_de_operacion
		d_basicos2["Utilidad despues de Imp."] = utilidad_de_operacion - (utilidad_de_operacion*impuestos)
	else:
		utilidad_bruta = ventas - cfab
		utilidad_de_operacion = utilidad_bruta - gastos_administrativos - otros_gastos
		d_basicos2["Utilidad Bruta"] = utilidad_bruta
		d_basicos2["Utilidad Operativa"] = utilidad_de_operacion
		d_basicos2["Utilidad despues de Imp."] = utilidad_de_operacion - (utilidad_de_operacion*impuestos)
	
def realizar_calculo():
	cifs()
	costo_primo()
	costo_conversion()
	cfabr()
	cprodr()
	cvtansr()
	utilidad_operativa()
	mostrar_resultados()

#FUNCIONES PARA INTERFAZ BASICA
def crear_label(raiz, r, c, text=None,columnspan=1,x=0, y=0, st="e", tam=None, fg="white", bg="#73947D"):
	l = Label(raiz, text=text)
	l.grid(row=r, column=c, columnspan=columnspan, padx=x, pady=y, sticky=st)
	l.config(bg=bg, font=("Consolas",14), fg=fg, width=tam)
	return l

def crear_canvas(raiz, r, c):
	c = Canvas(raiz)
	c.grid(row=r, column=c)
	return c

def crear_entry(raiz, textvariable, r, c, x=5, y=6):
	e = Entry(raiz, textvariable=textvariable, justify="center")
	e.grid(row=r, column=c, padx=x, pady=y)
	return e
def crear_entry2(raiz, textvariable, r, c, x=5, y=6):
	e = Entry(raiz, textvariable=textvariable, justify="center", state="readonly")
	e.grid(row=r, column=c, padx=x, pady=y)
	return e

def crear_button(raiz, text, r, c,command=None, x=5, y=1, col=1,w=None, h=None, bg=None):
	b = Button(raiz, text=text, command=command)
	b.grid(row=r, column=c, columnspan=col, padx=x, pady=y)
	b.config(font=("Consolas",10), width=w, height=h, bg=bg)
	return b

def crear_button2(raiz, textvariable, r, c,command=None, x=5, y=1, col=1,w=None, h=None, bg=None):
	b = Button(raiz, textvariable=textvariable, command=command)
	b.grid(row=r, column=c, columnspan=col, padx=x, pady=y)
	b.config(font=("Consolas",10), width=w, height=h, bg=bg)
	return b

def crear_frame(raiz, r, c, col=1, colr=1, st=None, bg=None):
	f = Frame(raiz)
	f.grid(row=r, column=c, columnspan=col, rowspan=colr, sticky=st)
	f.config(bg=bg)
	return f

#Funcion de busqueda 
import os
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#************+INTERFAZ+*************

ventana = Tk()
ventana.title("Costos Basico")
icono = resource_path("pato.ico")
ventana.iconbitmap(icono)
ventana.geometry()
ventana.config(bg=color)
ventana.resizable(False,False)


espacio = crear_frame(ventana, r=0, c=0, st="nsew", bg=color)

#Labels
datos_basicos = crear_label(espacio, text="Datos Basicos", r=0, c=1, st="ew")
#datos_basicos.config(bg='black')

mpl = crear_label(espacio, text="MP:", r=1, c=0)

mpil = crear_label(espacio, text="MPI:",r=2, c=0)

modl = crear_label(espacio, text="MOD:", r=3, c=0)

moil = crear_label(espacio, text="MOI:", r=4, c=0)

otros_cifsl = crear_label(espacio, text="Otros CIFs:", r=6, c=0)

gastos_adml = crear_label(espacio, text="Gastos Adm:", r=7, c=0)

impuestol = crear_label(espacio, text="Impuesto:", r=8, c=0)

ventasl = crear_label(espacio, text="Ventas:", r=9, c=0)

otros_gastosl = crear_label(espacio, text="Otros Gastos:", r=10, c=0)

#-----------Inventarios
inventariosl = crear_label(espacio, text="Inventarios", r=0, c=4, st="ew")

iiptl = crear_label(espacio, text="IIPT:", r=1, c=3)

ifptl = crear_label(espacio, text="IFPT:",r=2, c=3)

iippl = crear_label(espacio, text="IIPP:", r=3, c=3)

ifppl = crear_label(espacio, text="IFPP:", r=4, c=3)

iimpl = crear_label(espacio, text="IIMP:",r=5, c=3)

ifmpl = crear_label(espacio, text="IFMP:", r=6, c=3)

iimil = crear_label(espacio, text="IIMI:", r=7, c=3)

ifmil = crear_label(espacio, text="IFMI:", r=8, c=3)

#Entryes
var_mp = StringVar()
var_mpi = StringVar()
var_mod = StringVar()
var_moi = StringVar()

var_ocifs = StringVar()
var_gadmin = StringVar()
var_impuestos = StringVar()
var_ventas = StringVar()
var_otros_gastos = StringVar()

mpe = crear_entry(espacio, textvariable=var_mp, r=1, c=1)

mpie = crear_entry(espacio, textvariable=var_mpi, r=2, c=1)

mode = crear_entry(espacio, textvariable=var_mod, r=3, c=1)

moie = crear_entry(espacio, textvariable=var_moi, r=4, c=1)

otros_cifse = crear_entry(espacio, textvariable=var_ocifs, r=6, c=1)

gastos_adme = crear_entry(espacio, textvariable=var_gadmin, r=7, c=1)

impuestoe = crear_entry(espacio, textvariable=var_impuestos, r=8, c=1)

ventase = crear_entry(espacio, textvariable=var_ventas, r=9, c=1)

otros_gastose = crear_entry(espacio, textvariable=var_otros_gastos, r=10, c=1)

#---------Inventarios
var_iipt = StringVar()
var_ifpt = StringVar()
var_iipp = StringVar()
var_ifpp = StringVar()
var_iimp = StringVar()
var_ifmp = StringVar()
var_iimi = StringVar()
var_ifmi = StringVar()

iipte = crear_entry2(espacio, textvariable=var_iipt, r=1, c=4)

ifpte = crear_entry2(espacio, textvariable=var_ifpt, r=2, c=4)

iippe = crear_entry2(espacio, textvariable=var_iipp, r=3, c=4)

ifppe = crear_entry2(espacio, textvariable=var_ifpp, r=4, c=4)

iimpe = crear_entry2(espacio, textvariable=var_iimp, r=5, c=4)

ifmpe = crear_entry2(espacio, textvariable=var_ifmp, r=6, c=4)

iimie = crear_entry2(espacio, textvariable=var_iimi, r=7, c=4)

ifmie = crear_entry2(espacio, textvariable=var_ifmi, r=8, c=4)

#Buttons
mpb = crear_button(espacio, text="Agregar",command=agregar_mp, r=1, c=2)

mpib = crear_button(espacio, text="Agregar", command=agregar_mpi, r=2, c=2)

modb = crear_button(espacio, text="Agregar", command=agregar_mod, r=3, c=2)

moib = crear_button(espacio, text="Agregar", command=agregar_moi, r=4, c=2)

add_todo = crear_button(espacio, text="Agregar Todo", command=set_datos_basicos, r=5, c=1, bg="pink")

otros_cifsb = crear_button(espacio, text="Agregar", command=agregar_otros_cifs, r=6, c=2)

gastos_adme = crear_button(espacio, text="Agregar", command=agregar_gadmin, r=7, c=2)

impuestob = crear_button(espacio, text="Agregar", command=agregar_impuestos, r=8, c=2)

ventasb = crear_button(espacio, text="Agregar", command=agregar_ventas, r=9, c=2)

otros_gastosb = crear_button(espacio, text="Agregar", command=agregar_otros_gastos, r=10, c=2)

#---------Inventarios
iiptb = crear_button(espacio, text="Agregar", command=agregar_iipt, r=1, c=5)

ifptb = crear_button(espacio, text="Agregar", command=agregar_ifpt, r=2, c=5)

iippb = crear_button(espacio, text="Agregar", command=agregar_iipp, r=3, c=5)

ifppb = crear_button(espacio, text="Agregar", command=agregar_ifpp, r=4, c=5)

iimpb = crear_button(espacio, text="Agregar", command=agregar_iimp, r=5, c=5)

ifmpb = crear_button(espacio, text="Agregar", command=agregar_ifmp, r=6, c=5)

iimib = crear_button(espacio, text="Agregar", command=agregar_iimi, r=7, c=5)

ifmib = crear_button(espacio, text="Agregar", command=agregar_ifmi, r=8, c=5)

txt_inventario = StringVar()
txt_inventario.set("> on <")

onb = crear_button2(espacio, textvariable=txt_inventario, r=9, c=4, command=activar_inventarios, bg="red")


add_todo2 = crear_button(espacio, text="Agregar Todo", command=set_inventarios, r=10, c=4, bg="pink")

#Espacio 2
espacio2 = crear_frame(ventana, r=0, c=1, bg=color)


tabla = ttk.Treeview(espacio2, height=7)
tabla.grid(row=0, column=0, sticky="nsew")
tabla.heading("#0", text="Lista de Otros CIFs que agregaste:", anchor=CENTER)

tabla2 = ttk.Treeview(espacio2, height=7)
tabla2.grid(row=2, column=0, sticky="nsew")
tabla2.heading("#0", text="Gastos Administrativos:", anchor=CENTER)

#----Button espacio 2
borrar = crear_button(espacio2, text="Borrar", command=borrar_cifs, r=1, c=0)
borrar2 = crear_button(espacio2, text="Borrar", command=borrar_gadmin, r=3, c=0)


#ESPACIO 3
espacio3 = crear_frame(ventana, r=1, c=0, col=2, st="nsew", bg=color)

titulo = crear_label(espacio3, text="\U0001f440 RESULTADOS \U0001f440", r=0, c=0, x=3, st="ew", columnspan=3, bg=color, fg="black")


#-------tablas
tabla3 = ttk.Treeview(espacio3, column=2, height=6)
tabla3.grid(row=1, column=0, padx=3)
tabla3.heading("#0", text="Datos", anchor=CENTER)
tabla3.heading("#1", text="Respuesta", anchor=CENTER)

tabla5 = ttk.Treeview(espacio3, column=2, height=6)
tabla5.grid(row=1, column=2, padx=3)
tabla5.heading("#0", text="Datos", anchor=CENTER)
tabla5.heading("#1", text="Respuesta", anchor=CENTER)

#ESPACIO4 
espacio4 = crear_frame(ventana, r=0, c=2, colr=2, st="nsew", bg=color)

tabla6 = ttk.Treeview(espacio4, height=23)
tabla6.grid(row=0, column=0, sticky="nsew")
tabla6.heading("#0", text="Datos para la operacion", anchor=CENTER)

#--boton calcular todo
calc = crear_button(espacio4, text="Realizar calculo", command=realizar_calculo, r=1, c=0, h=2,y=3, bg="pink")

calc2 = crear_button(espacio4, text="Resetear Todo", command=reset_todo, r=2, c=0, w=16)

#Frame del Pie de la Interfaz
pie = crear_frame(ventana, r=2, c=0, col=3, st="nsew",bg=color)

mensaje = StringVar()
mensaje.set("version 1.5 \U0001f951 "*5)

monitor = Label(pie, textvar=mensaje)
monitor.pack(expand=True, fill="x")
monitor.config(bg="#FFD700",font=("Consolas",14))


ventana.mainloop()