import tkinter
import tkinter as tk
from tkinter import*
from tkinter import messagebox, ttk
import random
import time
import logging as log
from PIL import ImageTk, Image
import sys
import webbrowser
import pandas as pd


rootLogin = tk.Tk()
rootLogin.geometry('300x130+800+300')
rootLogin.title('Login')
rootLogin.iconbitmap('Images\iconMalevo.ico')
rootLogin.resizable(0, 0)

rootLogin.rowconfigure(0, weight=1)
rootLogin.rowconfigure(1, weight=1)
rootLogin.rowconfigure(2, weight=2)
rootLogin.columnconfigure(0, weight=1)
rootLogin.columnconfigure(1, weight=3)

UsuarioLabel = tk.Label(rootLogin, text='Usuario:')
UsuarioLabel.grid(row=0, column=0, sticky='E', padx=5, pady=5, ipady=2)

UsuarioEntry = ttk.Entry(rootLogin, width=30)
UsuarioEntry.grid(row=0, column=1, sticky='W', padx=5, pady=5, ipady=2)

PasswordLabel = tk.Label(rootLogin, text='Password:')
PasswordLabel.grid(row=1, column=0, sticky='E', padx=5, pady=5, ipady=2)

PasswordEntry = ttk.Entry(rootLogin, width=30, show='*')
PasswordEntry.grid(row=1, column=1, sticky='W', padx=5, pady=5, ipady=2)

def Login():
    usuario = UsuarioEntry.get()
    password = PasswordEntry.get()
    if usuario == "Admin" and password == "Malevo":
        respuesta = messagebox.askyesno("Acceso Concedido", "Presione Si para entrar a la aplicacion\n"
                                                            "Presione No para cerrarla")
        if respuesta == 1:
            MalevoMain()
        else:
            sys.exit()
    else:
        messagebox.showerror("Error de Login", "El usuario o la contraseña son incorrectos.\n"
                                               "Vuelva a intentarlo.")

BotonLogin = ttk.Button(rootLogin, text='Login', command=Login)
BotonLogin.grid(row=2, column=1, sticky='w', ipady=8, padx=5)


def MalevoMain():
    rootLogin.withdraw()
    root = tk.Toplevel()
    root.geometry("1640x800+119+50")
    root.iconbitmap("Images\iconMalevo.ico")
    root.title("Malevo Bakery & Coffe")
    root.resizable(0, 0)

    bgMain = tk.PhotoImage(file="Images\BGPERSONALIZADO.png")
    labelBG = tk.Label(root, image=bgMain)
    labelBG.place(x=1, y=1)

    Tops = Frame(root, bg="RoyalBlue4", width=1600, height=20, relief=SUNKEN)
    Tops.pack(side=TOP)

    f1 = LabelFrame(root, bg="RoyalBlue4", text="Ordenes", fg="white", font=('aria', 12, 'bold'), width=900, height=700,
                    relief=RAISED)
    f1.pack(side=LEFT)

    f2 = LabelFrame(root, bg="RoyalBlue4", text="Calculadora", fg="white", font=('aria', 14, 'bold'), width=400,
                    height=700, relief=SUNKEN)
    f2.pack(side=RIGHT)

    # ------------------TIME----------------------

    localtime = time.asctime(time.localtime(time.time()))

    # ----------------- INFO TOP -----------------
    lblinfo = Label(Tops, font=('aria', 40, 'bold'), text="Malevo Bakery & Coffe", fg="white", bg="RoyalBlue4", bd=10,
                    anchor='w')
    lblinfo.grid(row=0, column=0, pady=5)
    lblinfo = Label(Tops, font=('aria', 20), text=localtime, bg="RoyalBlue4", fg="gray80", anchor="w")
    lblinfo.grid(row=1, column=0)

    def Ig():
        webbrowser.open("https://www.instagram.com/malevobakeryandcoffee/")

    IgPNG = tk.PhotoImage(file="Images\IgLogo.png")
    ButtonIG = tk.Button(Tops, image=IgPNG, width=19, height=19, bg="RoyalBlue4",cursor="hand2", command=Ig)
    ButtonIG.grid(row=0, column=1, sticky=E)

    # ---------------Calculator------------------

    text_Input = StringVar()
    operator = ""

    txtdisplay = Entry(f2, font=('ariel', 20, 'bold'), textvariable=text_Input, bd=5, insertwidth=7, bg="RoyalBlue4",
                       fg="white", justify='right')
    txtdisplay.grid(columnspan=4)

    def btnclick(numbers):
        global operator
        operator = operator + str(numbers)
        text_Input.set(operator)

    def clrdisplay():
        global operator
        operator = ""
        text_Input.set("")

    def eqals():
        global operator
        sumup = str(eval(operator))

        text_Input.set(sumup)
        operator = ""

    def Ref():
        if DesayunoIntegral.get() == '':
            DesayunoIntegral.set(0)
            cDI = 0
        else:
            cDI = float(DesayunoIntegral.get())

        if NotBurger.get() == '':
            NotBurger.set(0)
            cNT = 0
        else:
            cNT = float(NotBurger.get())

        if DesayunoAmericano.get() == '':
            DesayunoAmericano.set(0)
            cDA = 0
        else:
            cDA = float(DesayunoAmericano.get())

        if Cafeteria.get() == '':
            Cafeteria.set(0)
            cC = 0
        else:
            cC = float(Cafeteria.get())

        if Pasteleria.get() == '':
            Pasteleria.set(0)
            cP = 0
        else:
            cP = float(Pasteleria.get())

        if Bebidas.get() == '':
            Bebidas.set(0)
            cB = 0
        else:
            cB = float(Bebidas.get())

        CostoDelDesayunoIntegral = 1000
        CostoDelNotBurger = 1300
        CostoDelDesayunoAmericano = 1400

        costoDesayunoIntegral = cDI * CostoDelDesayunoIntegral
        costoNotBurger = cNT * CostoDelNotBurger
        costoDesayunoAmericano = cDA * CostoDelDesayunoAmericano
        costoCafeteria = cC
        costoPasteleria = cP
        costoBebidas = cB

        costoComida = "ARS.", str('%.2f' % (costoDesayunoIntegral + costoNotBurger + costoDesayunoAmericano + costoCafeteria + costoPasteleria + costoBebidas))
        costoCombos = "ARS.", str('%.2f' % (costoDesayunoIntegral + costoNotBurger + costoDesayunoAmericano))
        IVA = ((costoDesayunoIntegral + costoNotBurger + costoDesayunoAmericano + costoCafeteria + costoPasteleria + costoBebidas) * 0.21)
        CostoTotal = (costoDesayunoIntegral + costoNotBurger + costoDesayunoAmericano + costoCafeteria + costoPasteleria + costoBebidas)
        CostoServicio = ((costoDesayunoIntegral + costoNotBurger + costoDesayunoAmericano + costoCafeteria + costoPasteleria + costoBebidas) / 99)
        CostoDolar = '%.2f' % ((costoDesayunoIntegral + costoNotBurger + costoDesayunoAmericano + costoCafeteria + costoPasteleria + costoBebidas) / 296)
        Servicio = "ARS.", str('%.2f' % CostoServicio)
        OverAllCost = "ARS.", str(IVA + CostoTotal + CostoServicio)
        ImpuestosPagados = "ARS.", str('%.2f' % IVA)

        CostoDelServicio.set(Servicio)
        Costoo.set(costoComida)
        Impuestoss.set(ImpuestosPagados)
        Subtotal.set(costoComida)
        Total.set(OverAllCost)

        def agregarOrden():
            #   ------------- Alerta de impresion -------------
            respuesta = messagebox.askyesno("Detalle de Impresion", "Imprimir?\n\n"
                                                                    '--------------------------\n'
                                                                    f'{localtime}\n'
                                                                    f'N° de Mesa: {nMesa.get()}\n'
                                                                    f'Orden N° {nOrden.get()}\n'
                                                                    f'\n'
                                                                    f'Combos = {costoCombos}\n'
                                                                    f'Cafeteria = (ARS. {costoCafeteria})\n'
                                                                    f'Pasteleria = (ARS. {costoPasteleria})\n'
                                                                    f'Bebidas = (ARS. {costoBebidas})\n'
                                                                    f'TOTAL = {costoComida}\n'
                                                                    f'--------------------------\n'
                                                                    f'\n')
            if respuesta == 1:
                messagebox.showinfo("IMPRESION", "         IMPRIMIENDO ORDEN         ")

                # ----------------- Transcripcion de la orden a un archivo txt -----------------
                ruta_archivo = "ComandasMalevo"
                with open(ruta_archivo, 'a', encoding='utf8') as archivo:
                    archivo.write(f'--------------------------\n'
                                  f'{localtime}\n'
                                  f'Orden N° {nOrden.get()}\n'
                                  f'\n'
                                  f'Combos = {costoCombos}\n'
                                  f'Cafeteria = (ARS. {costoCafeteria})\n'
                                  f'Pasteleria = (ARS. {costoPasteleria})\n'
                                  f'Bebidas = (ARS. {costoBebidas})\n'
                                  f'TOTAL = {costoComida}\n'
                                  f'--------------------------\n'
                                  f'\n'
                                  )
            else:
                messagebox.showerror("IMPRESION","--------- IMPRESION CANCELADA ---------")

        if Total != "" or Total != "ARS. 0.0":
            btnImprimir = Button(f1, padx=16, pady=8, bd=10, fg="RoyalBlue1", font=('ariel', 16, 'bold'), width=10,
                                 text="IMPRIMIR", cursor="spraycan", bg="RoyalBlue4", command=agregarOrden)
            btnImprimir.grid(row=7, column=4)
        else:
            pass

    def qexit():
        root.destroy()

    def reset():
        x = random.randint(1000, 100000)
        randomRef = str(x)
        nOrden.set(randomRef)
        nMesa.set("")
        DesayunoIntegral.set("")
        NotBurger.set("")
        DesayunoAmericano.set("")
        Cafeteria.set("")
        Pasteleria.set("")
        Bebidas.set("")
        CostoDelServicio.set("")
        Impuestoss.set("")
        Costoo.set("")
        Subtotal.set("")
        Total.set("")

    btn7 = Button(f2, padx=16, pady=16, bd=4, fg="RoyalBlue3", font=('ariel', 20, 'bold'), text="7", cursor="tcross",
                  bg="midnight blue", command=lambda: btnclick(7))
    btn7.grid(row=2, column=0)

    btn8 = Button(f2, padx=16, pady=16, bd=4, fg="RoyalBlue3", font=('ariel', 20, 'bold'), text="8", cursor="tcross",
                  bg="midnight blue", command=lambda: btnclick(8))
    btn8.grid(row=2, column=1)

    btn9 = Button(f2, padx=16, pady=16, bd=4, fg="RoyalBlue3", font=('ariel', 20, 'bold'), text="9", cursor="tcross",
                  bg="midnight blue", command=lambda: btnclick(9))
    btn9.grid(row=2, column=2)

    Addition = Button(f2, padx=16, pady=16, bd=4, fg="RoyalBlue3", font=('ariel', 20, 'bold'), text="+", cursor="plus",
                      bg="RoyalBlue4", command=lambda: btnclick("+"))
    Addition.grid(row=2, column=3)

    # ---------------------------------------------------------------------------------------------

    btn4 = Button(f2, padx=16, pady=16, bd=4, fg="RoyalBlue3", font=('ariel', 20, 'bold'), text="4", cursor="tcross",
                  bg="midnight blue", command=lambda: btnclick(4))
    btn4.grid(row=3, column=0)

    btn5 = Button(f2, padx=16, pady=16, bd=4, fg="RoyalBlue3", font=('ariel', 20, 'bold'), text="5", cursor="tcross",
                  bg="midnight blue", command=lambda: btnclick(5))
    btn5.grid(row=3, column=1)

    btn6 = Button(f2, padx=16, pady=16, bd=4, fg="RoyalBlue3", font=('ariel', 20, 'bold'), text="6", cursor="tcross",
                  bg="midnight blue", command=lambda: btnclick(6))
    btn6.grid(row=3, column=2)

    Substraction = Button(f2, padx=16, pady=16, bd=4, fg="RoyalBlue3", font=('ariel', 20, 'bold'), text="-",
                          cursor="plus", bg="RoyalBlue4", command=lambda: btnclick("-"))
    Substraction.grid(row=3, column=3)

    # -----------------------------------------------------------------------------------------------

    btn1 = Button(f2, padx=16, pady=16, bd=4, fg="RoyalBlue3", font=('ariel', 20, 'bold'), text="1", cursor="tcross",
                  bg="midnight blue", command=lambda: btnclick(1))
    btn1.grid(row=4, column=0)

    btn2 = Button(f2, padx=16, pady=16, bd=4, fg="RoyalBlue3", font=('ariel', 20, 'bold'), text="2", cursor="tcross",
                  bg="midnight blue", command=lambda: btnclick(2))
    btn2.grid(row=4, column=1)

    btn3 = Button(f2, padx=16, pady=16, bd=4, fg="RoyalBlue3", font=('ariel', 20, 'bold'), text="3", cursor="tcross",
                  bg="midnight blue", command=lambda: btnclick(3))
    btn3.grid(row=4, column=2)

    multiply = Button(f2, padx=16, pady=16, bd=4, fg="RoyalBlue3", font=('ariel', 20, 'bold'), text="*", cursor="plus",
                      bg="RoyalBlue4", command=lambda: btnclick("*"))
    multiply.grid(row=4, column=3)

    # ------------------------------------------------------------------------------------------------

    btn0 = Button(f2, padx=16, pady=16, bd=4, fg="RoyalBlue3", font=('ariel', 20, 'bold'), text="0", cursor="tcross",
                  bg="midnight blue", command=lambda: btnclick(0))
    btn0.grid(row=5, column=0)

    btnc = Button(f2, padx=16, pady=16, bd=4, fg="RoyalBlue3", font=('ariel', 20, 'bold'), text="c", cursor="plus",
                  bg="RoyalBlue4", command=clrdisplay)
    btnc.grid(row=5, column=1)

    btnequal = Button(f2, padx=16, pady=16, bd=4, width=16, fg="RoyalBlue3", font=('ariel', 20, 'bold'), text="=",
                      cursor="plus", bg="RoyalBlue4", command=eqals)
    btnequal.grid(columnspan=4)

    Decimal = Button(f2, padx=16, pady=16, bd=4, fg="RoyalBlue3", font=('ariel', 20, 'bold'), text=".", cursor="plus",
                     bg="RoyalBlue4", command=lambda: btnclick("."))
    Decimal.grid(row=5, column=2)

    Division = Button(f2, padx=16, pady=16, bd=4, fg="RoyalBlue3", font=('ariel', 20, 'bold'), text="/", cursor="plus",
                      bg="RoyalBlue4", command=lambda: btnclick("/"))
    Division.grid(row=5, column=3)

    # ---------------------------------------------------------------------------------------
    x = random.randint(1000, 100000)
    randomRef = str(x)
    nOrden = StringVar()
    nOrden.set(randomRef)

    nMesa = StringVar()
    DesayunoIntegral = StringVar()
    NotBurger = StringVar()
    DesayunoAmericano = StringVar()
    Cafeteria = StringVar()
    Pasteleria = StringVar()
    Bebidas = StringVar()
    Impuestoss = StringVar()
    Costoo = StringVar()
    CostoDelServicio = StringVar()
    Subtotal = StringVar()
    Total = StringVar()

    #Orden y Mesa
    lblOrden = Label(f1, font=('aria', 16, 'bold'), text="N° de Orden", bg="RoyalBlue4", fg="white", bd=10, anchor='w')
    lblOrden.grid(row=0, column=0)
    txtOrden = Entry(f1, font=('ariel', 16, 'bold'), textvariable=nOrden, bd=6, insertwidth=4, fg="white",
                     bg="midnight blue", justify='right')
    txtOrden.grid(row=0, column=1)

    lblMesa = Label(f1, font=('aria', 16, 'bold'), text="N° de Mesa", bg="RoyalBlue4", fg="white", bd=10, anchor='w')
    lblMesa.grid(row=1, column=0)
    txtMesa = Entry(f1, font=('ariel', 16, 'bold'), textvariable=nMesa, bd=6, insertwidth=4, fg="white",
                    bg="midnight blue", justify='right')
    txtMesa.grid(row=1, column=1)

    #Combos
    ValoresComboBox = [x + 1 for x in range(-1, 10)]

    lblDesayunoIntegral = Label(f1, font=('aria', 16, 'bold'), text="Desayunos Integrales", bg="RoyalBlue4", fg="white",
                                bd=10, anchor='w')
    lblDesayunoIntegral.grid(row=2, column=0)
    txtDesayunoIntegral = ttk.Combobox(f1, font=('ariel', 16, 'bold'), textvariable=DesayunoIntegral, justify='right',
                                       width=19, height=20, values=ValoresComboBox)
    txtDesayunoIntegral.current(0)
    txtDesayunoIntegral.grid(row=2, column=1, padx=10,pady=5)


    lblNotBurger = Label(f1, font=('aria', 16, 'bold'), text="Combos Not Burger", bg="RoyalBlue4", fg="white", bd=10,
                         anchor='w')
    lblNotBurger.grid(row=3, column=0)
    txtNotBurger = ttk.Combobox(f1, font=('ariel', 16, 'bold'), textvariable=NotBurger, justify='right',
                                       width=19, height=20, values=ValoresComboBox)
    txtNotBurger.current(0)
    txtNotBurger.grid(row=3, column=1)


    lblDesayunoAmericano = Label(f1, font=('aria', 16, 'bold'), text="Desayunos Americanos", bg="RoyalBlue4",
                                 fg="white", bd=10, anchor='w')
    lblDesayunoAmericano.grid(row=4, column=0)
    txtDesayunoAmericano = ttk.Combobox(f1, font=('ariel', 16, 'bold'), textvariable=DesayunoAmericano, justify='right',
                                       width=19, height=20, values=ValoresComboBox)
    txtDesayunoAmericano.current(0)
    txtDesayunoAmericano.grid(row=4, column=1)

    #Cafeteria Pasteleria y Bebidas
    lblCafeteria = Label(f1, font=('aria', 16, 'bold'), text="Cafeteria", bg="RoyalBlue4", fg="white", bd=10,
                         anchor='w')
    lblCafeteria.grid(row=5, column=0)
    txtCafeteria = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Cafeteria, bd=6, insertwidth=4, fg="white",
                         bg="midnight blue", justify='right')
    txtCafeteria.grid(row=5, column=1)

    # --------------------------------------------------------------------------------------
    lblPasteleria = Label(f1, font=('aria', 16, 'bold'), text="Pasteleria", bg="RoyalBlue4", fg="white", bd=10,
                          anchor='w')
    lblPasteleria.grid(row=0, column=2)
    txtPasteleria = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Pasteleria, bd=6, insertwidth=4, fg="white",
                          bg="midnight blue", justify='right')
    txtPasteleria.grid(row=0, column=3)

    lblBebidas = Label(f1, font=('aria', 16, 'bold'), text="Bebidas", bg="RoyalBlue4", fg="white", bd=10, anchor='w')
    lblBebidas.grid(row=1, column=2)
    txtBebidas = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Bebidas, bd=6, insertwidth=4, fg="white",
                       bg="midnight blue", justify='right')
    txtBebidas.grid(row=1, column=3)

    lblCostoComida = Label(f1, font=('aria', 16, 'bold'), text="Costo Comida", bg="RoyalBlue4", fg="white", bd=10,
                           anchor='w')
    lblCostoComida.grid(row=2, column=2)
    txtCostoComida = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Costoo, bd=6, insertwidth=4, fg="white",
                           bg="midnight blue", justify='right')
    txtCostoComida.grid(row=2, column=3)

    lblImpuestos = Label(f1, font=('aria', 16, 'bold'), text="IVA", bg="RoyalBlue4", fg="white", bd=10, anchor='w')
    lblImpuestos.grid(row=3, column=2)
    txtImpuestos = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Impuestoss, bd=6, insertwidth=4, fg="white",
                         bg="midnight blue", justify='right')
    txtImpuestos.grid(row=3, column=3)

    lblSubTotal = Label(f1, font=('aria', 16, 'bold'), text="Subtotal", bg="RoyalBlue4", fg="white", bd=10, anchor='w')
    lblSubTotal.grid(row=4, column=2)
    txtSubTotal = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Subtotal, bd=6, insertwidth=4, fg="white",
                        bg="midnight blue", justify='right')
    txtSubTotal.grid(row=4, column=3)

    lblTotal = Label(f1, font=('aria', 16, 'bold'), text="Total", bg="RoyalBlue4", fg="white", bd=10, anchor='w')
    lblTotal.grid(row=5, column=2)
    txtTotal = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Costoo, bd=6, insertwidth=4, fg="white",
                     bg="midnight blue", justify='right')
    txtTotal.grid(row=5, column=3)

    # ----------------------------------------- Buttons ------------------------------------------

    lblTotal = Label(f1, text="---------------------", bg="RoyalBlue4", fg="RoyalBlue4")
    lblTotal.grid(row=6, columnspan=3)

    btnTotal = Button(f1, padx=16, pady=8, bd=10, fg="RoyalBlue1", font=('ariel', 16, 'bold'), width=10, text="TOTAL",
                      cursor="target", bg="RoyalBlue4", command=Ref)
    btnTotal.grid(row=7, column=1)

    btnReset = Button(f1, padx=16, pady=8, bd=10, fg="RoyalBlue1", font=('ariel', 16, 'bold'), width=10, text="RESET",
                      cursor="exchange", bg="RoyalBlue4", command=reset)
    btnReset.grid(row=7, column=2)

    btnSalir = Button(f1, padx=16, pady=8, bd=10, fg="RoyalBlue1", font=('ariel', 16, 'bold'), width=10, text="SALIR",
                      cursor="pirate", bg="RoyalBlue4", command=qexit)
    btnSalir.grid(row=7, column=3)

    def price():
        root.withdraw()
        rootPrice = tk.Toplevel()
        rootPrice.geometry("500x960+725+0")
        rootPrice.resizable(0, 0)
        rootPrice.title("Lista de Precios")
        rootPrice.iconbitmap("Images\iconMalevo.ico")
        fondo = tk.PhotoImage(file="Images\BGPERSONALIZADO.png")
        lblfondo = tk.Label(rootPrice, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)

        # ----------------------- ROW 0 ---------------------

        CostoIntegral = 1000
        CostoNotBurger = 1300
        CostoAmericano = 1400

        def Volver():
            rootPrice.withdraw()
            root.deiconify()

        ButtonVolver = tk.Button(rootPrice, text="Volver", cursor="hand2", width=4, relief="flat", bg="RoyalBlue1",
                                 fg="white", font=("arial", 10, "bold"), command=Volver)
        ButtonVolver.grid(row=0, column=4, padx=25, pady=5)

        lblinfo = Label(rootPrice, font=('aria', 15, 'bold'), text="OPCIONES", bg="indian red", fg="black", bd=5)
        lblinfo.grid(row=0, column=0)
        lblinfo = Label(rootPrice, font=('aria', 15, 'bold'), text="PRECIO", bg="SpringGreen4", fg="black", anchor=W)
        lblinfo.grid(row=0, column=3)

        # ----------------------- ROW 1 --------------------

        lblinfo = Label(rootPrice, font=('aria', 15, 'bold'), text="Desayuno Integral", bg= "RoyalBlue4", fg="white", anchor=W)
        lblinfo.grid(row=1, column=0)
        lblinfo = Label(rootPrice, font=('aria', 15, 'bold'), text=CostoIntegral, bg= "RoyalBlue4", fg="white", anchor=W)
        lblinfo.grid(row=1, column=3)

        # ----------------------- ROW 2 --------------------

        lblinfo = Label(rootPrice, font=('aria', 15, 'bold'), text="Not Burger", bg= "RoyalBlue4", fg="white", anchor=W)
        lblinfo.grid(row=2, column=0)
        lblinfo = Label(rootPrice, font=('aria', 15, 'bold'), text=CostoNotBurger, bg= "RoyalBlue4", fg="white", anchor=W)
        lblinfo.grid(row=2, column=3)

        # ----------------------- ROW 3 -------------------

        lblinfo = Label(rootPrice, font=('aria', 15, 'bold'), text="DesayunoAmericano", bg= "RoyalBlue4", fg="white", anchor=W)
        lblinfo.grid(row=3, column=0)
        lblinfo = Label(rootPrice, font=('aria', 15, 'bold'), text=CostoAmericano, bg= "RoyalBlue4", fg="white", anchor=W)
        lblinfo.grid(row=3, column=3)

        # ----------------------- ROW 4 -------------------

        lblinfo = Label(rootPrice, font=('aria', 15, 'bold'), text="x", bg= "RoyalBlue4", fg="white", anchor=W)
        lblinfo.grid(row=4, column=0)
        lblinfo = Label(rootPrice, font=('aria', 15, 'bold'), text="200", bg= "RoyalBlue4", fg="white", anchor=W)
        lblinfo.grid(row=4, column=3)

        # ----------------------- ROW 5 -------------------

        lblinfo = Label(rootPrice, font=('aria', 15, 'bold'), text="x2", bg= "RoyalBlue4", fg="white", anchor=W)
        lblinfo.grid(row=5, column=0)
        lblinfo = Label(rootPrice, font=('aria', 15, 'bold'), text="120", bg= "RoyalBlue4", fg="white", anchor=W)
        lblinfo.grid(row=5, column=3)

        # ----------------------- ROW 6 -------------------

        lblinfo = Label(rootPrice, font=('aria', 15, 'bold'), text="x3", bg= "RoyalBlue4", fg="white", anchor=W)
        lblinfo.grid(row=6, column=0)
        lblinfo = Label(rootPrice, font=('aria', 15, 'bold'), text="100", bg= "RoyalBlue4", fg="white", anchor=W)
        lblinfo.grid(row=6, column=3)

        # ----------------------- ROW 7 -------------------

        rootPrice.mainloop()

    btnPrecios = Button(f1, padx=16, pady=8, bd=10, fg="RoyalBlue1", font=('ariel', 16, 'bold'), width=10,
                        text="PRECIOS", cursor="sizing", bg="RoyalBlue4", command=price)
    btnPrecios.grid(row=7, column=0)

    #------------------ MENUS --------------------
    menu_principal = Menu(root)

    sub_menu_archivo = Menu(menu_principal, tearoff=False)
    sub_menu_archivo.add_command(label='Precios', command=price)
    sub_menu_archivo.add_separator()
    sub_menu_archivo.add_command(label='Salir', command=qexit)
    menu_principal.add_cascade(menu=sub_menu_archivo, label='Archivo')

    sub_menu_ayuda = Menu(menu_principal, tearoff=False)
    def AcercaDe():
        Mensaje = messagebox.showinfo("Acerca de...", "Aplicacion desarrollada en Python GUI Tkinter\n"
                                                      "-------------------------------------------------\n"
                                            "Realizada para la Cafeteria y Pasteleria\n"
                                            "       Malevo Bakery and Coffee\n"
                                            "\n"
                                            "Ubicado en Av.Alvarez Jonte 3260\n"
                                            "-\n"
                                            "-\n"
                                            "-\n"
                                            "-\n"
                                            "-\n"
                                            "By Felipe Intelangelo")
    sub_menu_ayuda.add_command(label='Acerca De...', command=AcercaDe)
    menu_principal.add_cascade(menu=sub_menu_ayuda, label='Ayuda')

    root.config(menu=menu_principal)

    root.mainloop()

rootLogin.mainloop()