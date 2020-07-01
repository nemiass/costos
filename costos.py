#!/usr/bin/env python
#_*_ coding: utf8 _*_
from tkinter import ttk
from tkinter import *

mp = 0
mpi = 0
mod = 0
moi = 0

ocifs_acum = []
gastos_administrativos = 0
gadmin_acum = []
impuestos = 0.30
ventas = 0

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

def validar(dato):
	try:
		n = float(dato)
		if dato != "":
			return True
		else:
			return False
	except:
		return False


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

def cal_gastos_adm():
	global gastos_administrativos
	gastos_administrativos = sum(gadmin_acum)
	datos_mostrar['Gast.Administrativos'] = gastos_administrativos

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
	mostrar_datos()
def agregar_ifmi():
	global ifmi
	if validar(var_ifmi.get()):
		ifmi = float(var_ifmi.get())
		datos_mostrar["IFMI"] = ifmi
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


#----OPERACIONES:

def materia_prim_consumida():
	global mpc
	mpc = iimp + mp - ifmp
	d_basicos["Materiales Prima Consumida(MPC)"] = mpc

def materia_indi_cosumida():
	global mic
	mic = iimi + mpi - ifmi
	d_basicos["Materiales Indirectos Consumidos (MIC)"] = mic

def cifs():
	materia_prim_consumida()
	materia_indi_cosumida()
	otros_cifs = sum(ocifs_acum)
	global cif
	cif = moi + mic + otros_cifs
	datos_mostrar["cif"] = cif
	d_basicos["CIF"] = cif

def costo_primo():
	global cprimo
	cprimo = mpc + mod
	d_basicos["Costo Primo"] = cprimo

def costo_conversion():
	global conversion
	conversion = mod + cif
	d_basicos["Costo de Conversion"] = conversion

def cfabr():
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

utilidad_bruta = 0
def utilidad_operativa():
	utilidad_bruta = ventas - cventas - cprod - cfab
	utilidad_de_operacion = utilidad_bruta - gastos_administrativos
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


def borrar():
	mp.set("")
def reset_variables():
	global mp, mpi, mod, moi, gastos_administrativos, impuestos, ventas, iipt, ifpt, iipp, ifpp, iimp, ifmp, iimi, ifmi, cif, cprimo, conversion, mpc, mic, cfab, cprod, ventas
	mp = 0
	mpi = 0
	mod = 0
	moi = 0
	gastos_administrativos = 0
	impuestos = 0.30
	ventas = 0

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

	global d_basicos, d_basicos2, datos_mostrar, ocifs_acum, gadmin_acum
	ocifs_acum = []
	gadmin_acum = []

	d_basicos = {}
	d_basicos2 = {}
	datos_mostrar = {}

	reset_variables()
	mostrar_cifs()
	mostrar_gadmin()
	mostrar_datos()
	
	mostrar_resultados()

ventana = Tk()
ventana.title("Costos Basico")
#ventana.iconbitmap("pato.ico")
ventana.geometry()
ventana.config(bg="pink")
ventana.resizable(False,False)

espacio = Frame(ventana, height="200")
espacio.grid(row=0, column=0, sticky="nsew")
espacio.config(bg="yellow")

#Labels
datos_basicos = Label(espacio, text="Datos basicos")
datos_basicos.grid(row=0, column=0, columnspan=3, pady=3, padx=3, sticky=W+E)

mpl = Label(espacio, text="MP:")
mpl.grid(row=1, column=0, padx=5)
mpl.config(width=10)

mpil = Label(espacio, text="MPI:")
mpil.grid(row=2, column=0)
mpil.config(width=10)

modl = Label(espacio, text="MOD:")
modl.grid(row=3, column=0)
modl.config(width=10)

moil = Label(espacio, text="MOI:")
moil.grid(row=4, column=0)
moil.config(width=10)

otros_cifsl = Label(espacio, text="Otros CIFs:")
otros_cifsl.grid(row=6, column=0)
otros_cifsl.config(width=10)

gastos_adml = Label(espacio, text="Gastos Adm:")
gastos_adml.grid(row=7, column=0)
gastos_adml.config(width=10)

impuestol = Label(espacio, text="Impuesto:")
impuestol.grid(row=8, column=0)
impuestol.config(width=10)

ventasl = Label(espacio, text="Ventas:")
ventasl.grid(row=9, column=0)
ventasl.config(width=10)

#-----------Inventarios
inventariosl = Label(espacio, text="Inventarios")
inventariosl.grid(row=0, column=3, columnspan=3, padx=3, sticky=W+E)

iiptl = Label(espacio, text="IIPT:")
iiptl.grid(row=1, column=3, padx=5)
iiptl.config(width=10)

ifptl = Label(espacio, text="IFPT:")
ifptl.grid(row=2, column=3)
ifptl.config(width=10)

iippl = Label(espacio, text="IIPP:")
iippl.grid(row=3, column=3)
iippl.config(width=10)

ifppl = Label(espacio, text="IFPP:")
ifppl.grid(row=4, column=3)
ifppl.config(width=10)

iimpl = Label(espacio, text="IIMP:")
iimpl.grid(row=5, column=3)
iimpl.config(width=10)

ifmpl = Label(espacio, text="IFMP:")
ifmpl.grid(row=6, column=3)
ifmpl.config(width=10)

iimil = Label(espacio, text="IIMI:")
iimil.grid(row=7, column=3)
iimil.config(width=10)

ifmil = Label(espacio, text="IFMI:")
ifmil.grid(row=8, column=3)
ifmil.config(width=10)

#Entryes
var_mp = StringVar()
var_mpi = StringVar()
var_mod = StringVar()
var_moi = StringVar()

var_ocifs = StringVar()
var_gadmin = StringVar()
var_impuestos = StringVar()
var_ventas = StringVar()

mpe = Entry(espacio, textvariable=var_mp)
mpe.grid(row=1, column=1)

mpie = Entry(espacio, textvariable=var_mpi)
mpie.grid(row=2, column=1)

mode = Entry(espacio, textvariable=var_mod)
mode.grid(row=3, column=1)

moie = Entry(espacio, textvariable=var_moi)
moie.grid(row=4, column=1)

otros_cifse = Entry(espacio, textvariable=var_ocifs)
otros_cifse.grid(row=6, column=1)

gastos_adme = Entry(espacio, textvariable=var_gadmin)
gastos_adme.grid(row=7, column=1)

impuestoe = Entry(espacio, textvariable=var_impuestos)
impuestoe.grid(row=8, column=1)

ventase = Entry(espacio, textvariable=var_ventas)
ventase.grid(row=9, column=1)

#---------Inventarios
var_iipt = StringVar()
var_ifpt = StringVar()
var_iipp = StringVar()
var_ifpp = StringVar()
var_iimp = StringVar()
var_ifmp = StringVar()
var_iimi = StringVar()
var_ifmi = StringVar()

iipte = Entry(espacio, textvariable=var_iipt)
iipte.grid(row=1, column=4)

ifpte = Entry(espacio, textvariable=var_ifpt)
ifpte.grid(row=2, column=4)

iippe = Entry(espacio, textvariable=var_iipp)
iippe.grid(row=3, column=4)

ifppe = Entry(espacio, textvariable=var_ifpp)
ifppe.grid(row=4, column=4)

iimpe = Entry(espacio, textvariable=var_iimp)
iimpe.grid(row=5, column=4)


ifmpe = Entry(espacio, textvariable=var_ifmp)
ifmpe.grid(row=6, column=4)


iimie = Entry(espacio, textvariable=var_iimi)
iimie.grid(row=7, column=4)


ifmie = Entry(espacio, textvariable=var_ifmi)
ifmie.grid(row=8, column=4)

#Buttons
mpb = Button(espacio, text="Agregar", command=agregar_mp)
mpb.grid(row=1, column=2, padx=10, pady=10)

mpib = Button(espacio, text="Agregar", command=agregar_mpi)
mpib.grid(row=2, column=2, padx=10, pady=10)

modb = Button(espacio, text="Agregar", command=agregar_mod)
modb.grid(row=3, column=2, padx=10, pady=10)

moib = Button(espacio, text="Agregar", command=agregar_moi)
moib.grid(row=4, column=2, padx=10, pady=10)

add_todo = Button(espacio, text="Agregar Todo", command=set_datos_basicos)
add_todo.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

otros_cifsb = Button(espacio, text="Agregar", command=agregar_otros_cifs)
otros_cifsb.grid(row=6, column=2, padx=10, pady=10)

gastos_adme = Button(espacio, text="Agregar", command=agregar_gadmin)
gastos_adme.grid(row=7, column=2, padx=10, pady=10)

impuestob = Button(espacio, text="Agregar", command=agregar_impuestos)
impuestob.grid(row=8, column=2, padx=10, pady=10)

ventasb = Button(espacio, text="Agregar", command=agregar_ventas)
ventasb.grid(row=9, column=2, padx=10, pady=10)

#---------Inventarios
iiptb = Button(espacio, text="Agregar", command=agregar_iipt)
iiptb.grid(row=1, column=5, padx=10, pady=10)

ifptb = Button(espacio, text="Agregar", command=agregar_ifpt)
ifptb.grid(row=2, column=5, padx=10, pady=10)

iippb = Button(espacio, text="Agregar", command=agregar_iipp)
iippb.grid(row=3, column=5, padx=10, pady=10)

ifppb = Button(espacio, text="Agregar", command=agregar_ifpp)
ifppb.grid(row=4, column=5, padx=10, pady=10)

iimpb = Button(espacio, text="Agregar", command=agregar_iimp)
iimpb.grid(row=5, column=5, padx=10, pady=10)
iimpb.config()

ifmpb = Button(espacio, text="Agregar", command=agregar_ifmp)
ifmpb.grid(row=6, column=5, padx=10, pady=10)
ifmpb.config()

iimib = Button(espacio, text="Agregar", command=agregar_iimi)
iimib.grid(row=7, column=5, padx=10, pady=10)
iimib.config()

ifmib = Button(espacio, text="Agregar", command=agregar_ifmi)
ifmib.grid(row=8, column=5, padx=10, pady=10)
ifmib.config()

add_todo2 = Button(espacio, text="Agregar Todo", command=set_inventarios)
add_todo2.grid(row=9, column=3, columnspan=3, padx=10, pady=10)

#Espacio 2
espacio2 = Frame(ventana)
espacio2.grid(row=0, column=1)
espacio2.config(bg="pink")


tabla = ttk.Treeview(espacio2, height=7)
tabla.grid(row=0, column=0, sticky="nsew")
tabla.heading("#0", text="Lista de Otros CIFs que agregaste:", anchor=CENTER)

tabla2 = ttk.Treeview(espacio2, height=7)
tabla2.grid(row=2, column=0, sticky="nsew")
tabla2.heading("#0", text="Gastos Administrativos:", anchor=CENTER)

#----Button espacio 2
borrar = Button(espacio2, text="Borrar", command=borrar_cifs).grid(row=1, column=0, pady=5)
borrar2 = Button(espacio2, text="Borrar", command=borrar_gadmin).grid(row=3, column=0, pady=5)


#ESPACIO 3
espacio3 = Frame(ventana)
espacio3.grid(row=1, column=0, columnspan=2, sticky="nsew")
espacio3.config(bg="green")

titulo = Label(espacio3, text="RESULTADOS")
titulo.grid(row=0, column=0, columnspan=3, padx=3, sticky="nsew")

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
espacio4 = Frame(ventana)
espacio4.grid(row=0, column=2, rowspan=2, sticky="nsew")
espacio4.config(bg="red")


tabla6 = ttk.Treeview(espacio4, height=23)
tabla6.grid(row=0, column=0, pady=12, sticky="nsew")
tabla6.heading("#0", text="Datos para la operacion", anchor=CENTER)

#--boton calcular todo
calc = Button(espacio4, text="Realizar calculo", height=2, command=realizar_calculo)
calc.grid(row=1, column=0, sticky="ew")

calc2 = Button(espacio4, text="Resetear Todo", command=reset_todo)
calc2.grid(row=2, column=0, pady=10, sticky="ew")
#Frame de abajo
pie = Frame(ventana)
pie.grid(row=2, column=0, columnspan=3, sticky="ew")

mensaje = StringVar()
mensaje.set("Fase Beta\U0001f951"*15)

monitor = Label(pie, textvar=mensaje)
monitor.grid(row=0, column=0, padx=20, columnspan=3, sticky="ew")

ventana.mainloop()