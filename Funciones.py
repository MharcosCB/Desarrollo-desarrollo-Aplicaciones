from Usuarios import Usuarios
from Clientes import Clientes
from Productos import Productos
from Tipo import Tipo
from DAO import DAO
from os import system 
from beautifultable import BeautifulTable
import os
import getpass


class Funciones:

    d = DAO()
    tipo = Tipo()
    sesion = Usuarios()
    cliente = Clientes()

    def __init__(self):
        pass
    
    def __validarTexto(self, cantidad, texto):
        t = ""
        while True:
            try:
                t = input("Ingrese " + str(texto) +" : ")
                assert len(t) >= 1 and len(t) <= cantidad
            except AssertionError:
                print("Error en la cantidad de caracteres")
                system("pause")
            except:
                print("Error!") 
                system("pause")
            else:
                break
        return t
    
    def __validarNumeros(self, min, max, texto):
        num = 0
        while True:
            try:
                num = int(input("Ingrese " + str(texto) + ":"))
                assert num >= min and num <= max
            except AssertionError:      
                    print("El numero esta fuera del rango valido!")   
            except:
                print("Error!")
            else:
                break
        return num
#--------------------------------------------------------------------
#MENU INICIAL
#--------------------------------------------------------------------
    def menuInicial(self):
        while True:
            try:
                system("cls")               
                print("--- MENU INICIAL ---")
                print("1.Iniciar Sesion")
                print("2.Salir")

                op = self.__validarNumeros(1,3,'opcion de menu')
                if  op == 1:
                    self.__login()
                elif op == 2:
                    self.__salir()
                    os._exit(1)
                else:
                    print("\n--- Error De Opcion !! ---\n", end="\n\n")
                    system("pause")
            except:
                print("\n--- Error Al Digitar Opcion (Menu Inicial)!! ---\n")
                system("pause")
#--------------------------------------------------------------------
# LOGIN
#--------------------------------------------------------------------

    def __login(self):
        while True:
            try:
                system("cls")               
                print("--- LOGIN ---")
                nom = input("Digite El Nombre de Usuario : ")
                if len(nom)<1 or len(nom)>50:
                    print("\n--- Debe Tener Entre 1 y 50 Caracteres!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error Al Ingresar Nombre De Usuario (LOGIN)!! ---")
                system("pause")

        while True:
            try:
                system("cls")               
                print("--- LOGIN ---")
                pas = getpass.getpass("Digite La Contraseña Del Usuario ("+nom.upper()+") : ") #getpass permite ocultar la contraseña
                if len(pas)<1 or len(pas)>50:
                    print("\n--- Debe Tener Entre 1 y 50 Caracteres!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error Al Ingresar Contraseña (Login)!! ---")
                system("pause")
                    
    
        system("cls")
        
        r = self.d.iniciarSesion(nom,pas)  #clase DAO, se les mandan los datos para ver si son correctos
        if r is None:
            print("\n--- Error de usuario y/o contraseña!! ---", end="\n\n")
            system("pause")
            self.menuInicial()
        else:
            self.sesion.setId_usu(r[0][0])
            self.sesion.setNom_usu(r[0][1])
            self.sesion.setCon_usu(r[0][2])
            self.sesion.setId_tip(r[0][3])
            print("\n--- Bienvenido Usuario " + self.sesion.getNom_usu().upper()+"!! ----", end= "\n\n")
            system("pause")

            if self.sesion.getId_tip() == 3:
                self.menuInicialAdmin()
            elif self.sesion.getId_tip() == 2:
                self.menuInicialJefeventas()
            elif self.sesion.getId_tip() == 1:
                self.menuInicialVendedor()
            else:
                print("\n--- Error: Tipo de usuario desconocido ---\n")
                system("pause")
                self.menuInicial()
 #--------------------------------------------------------------------
 # - MENU ADMINISTRADOR
 #--------------------------------------------------------------------        

    def menuInicialAdmin(self):
        while True:
            try:
                system("cls")               
                print("--- MENU INICIAL ---")
                print("1.Crear Cuenta")
                print("2.Regresar al menu principal")
                op = self.__validarNumeros (1,2,'opcion de menu')
                if op == 1:
                    self.__crearCuenta()
                elif op == 2:
                    print("\n-----------------------------\n")
                    print("Volviendo al menu principal!")
                    print("\n-----------------------------\n")
                    system("pause")
                    self.menuInicial()
                else:
                    print("\n--- Error De Opcion!! ---", end="\n\n")
                    system("pause")
            except:
                print("\n--- Error Al Digitar Opcion (Menu Inicial)!! ---\n")
                system("pause")
#--------------------------------------------------------------------
#-MENU VENDEDOR
#--------------------------------------------------------------------                
    def menuInicialVendedor(self):
        while True:
            try:
                system("cls")               
                print("--- MENU VENDEDOR ---")
                print("1.Realizar venta")
                print("2.Regresar al menu principal")
                op = self.__validarNumeros (1,2,'opcion de menu')
                if op == 1:
                    self.__login()
                elif op == 2:
                    print("\n-----------------------------")
                    print("Volviendo al menu principal!")
                    system("pause")
                    self.menuInicial()
                else:
                    print("\n--- Error De Opcion!! ---", end="\n\n")
                    system("pause")
            except:
                print("\n--- Error Al Digitar Opcion (Menu Inicial)!! ---\n")
                system("pause")
#--------------------------------------------------------------------
#- MENU JEFE DE VENTAS
#--------------------------------------------------------------------

    def menuJefe(self):
        try:
            system("cls")               
            print("--- MENU DE JEFE DE VENTAS:"+ str(self.sesion.getNom_usu().upper())+"---")
            print("1. GESTIONAR PRODUCTOS")
            print("2. OBTENER VENTAS")
            print("3. OPCION CAJA")
            print("4. CERRAR SESION")
            op = int(input("Digite Una Opcion : "))
            if op== 1:
                self.menuProductos()
            elif op== 2:
                self.menuJefeVentas()
            elif op== 3:
                self.menuJefeCaja()
            elif op== 4:    
                self.menuInicial()
            else:
                print("\n--- Error De Opcion!! ---", end="\n\n")
                system("pause")
        except:
            print("\n--- Error De Opcion Del Menu (try)!! ---")
            system("pause")
            self.menu()
#--------------------------------------------------------------------
#- MENU JEFE DE VENTAS OPCION CAJA "3"
#--------------------------------------------------------------------
    def menuJefeCaja(self):
        try:
            system("cls")               
            print("--- MENU DE JEFE DE VENTAS:"+ str(self.sesion.getNom_usu().upper())+"---")
            print("1. APERTURA CAJA")
            print("2. CERRAR CAJA")
            print("4. REGRESAR A MENU ANTERIOR")
            op = int(input("Digite Una Opcion : "))
            if op== 1:
                self.menuJefeAbierta()
            elif op== 2:
                self.menuJefeCerrada()
            elif op== 3:
                self.menuJefe()
            else:
                self.menuJefeCaja()
                print("\n--- Error De Opcion!! ---", end="\n\n")
                system("pause")
        except:
            print("\n--- Error De Opcion Del Menu (try)!! ---")
            system("pause")
            self.menuJefeCaja()
#--------------------------------------------------------------------
#- CREAR CUENTA
#--------------------------------------------------------------------
    def __crearCuenta(self):
        while True:
            try:
                system("cls")
                nom = input("Digite El Nombre del Usuario a Registrar : ")
                if len(nom.strip())<1 or len(nom.strip())>20:
                    print("\n--- El Nombre Debe Tener Entre 1 y 20 Caracteres!! ---")
                    system("pause")
                else:
                    r = self.d.comprobarNombreUsuario(nom)
                    if r is not None:
                        print("\n--- El Nombre de Usuario (",nom,") Ya Existe!! ---\n")
                        system("pause")
                    else:
                        break
            except:
                print("\n--- Error Al Intentar Almacenar El Nombre De Usuario!! ---")
                system("pause")
#--------------------------------------------------------------------
#- PATERNO
#--------------------------------------------------------------------
        while True:
            try:
                system("cls")
                pat = input("Digite El apellido del Usuario a Registrar : ")
                if len(pat.strip())<1 or len(pat.strip())>20:
                    print("\n--- El apellido Debe Tener Entre 1 y 20 Caracteres!! ---")
                    system("pause")
                else:                        
                    break
            except:
                print("\n--- Error Al Intentar Almacenar El Apellido!! ---")
                system("pause")
#--------------------------------------------------------------------
#- MATERNO
#--------------------------------------------------------------------
        while True:
            try:
                system("cls")
                mat = input("Digite El apellido del Usuario a Registrar : ")
                if len(mat.strip())<1 or len(mat.strip())>20:
                    print("\n--- El apellido Debe Tener Entre 1 y 20 Caracteres!! ---")
                    system("pause")
                else:                        
                    break
            except:
                print("\n--- Error Al Intentar Almacenar El Apellido!! ---")
                system("pause")   
#--------------------------------------------------------------------
#- RUT
#-------------------------------------------------------------------- 
        while True:
            try:
                system("cls")
                rut = input("Digite el rut Del Usuario ("+str(nom.upper())+") (ejemplo : XXXXXXXX-X): ")
                if len(rut.strip())<1 or len(rut.strip())>10:
                    print("\n--- Debe Tener Entre 1 y 10 Caracteres!! ---\n")
                    system("pause")
                else:
                    pas = rut.split('-')[0]
                    print ("su contraseña es: "+ pas)
                    print("ASEGURESE DE GUARDAR LA CONTRASEÑA!!")
                    system("pause")
                    break
            except:
                print("\n--- Error Al Intentar Almacenar El Rut!! ---")
                system("pause")
#--------------------------------------------------------------------
#- ID CARGO
#--------------------------------------------------------------------  
        while True:
            try:
                system("cls")
                car = int(input("Digite el cargo del usuario a crear (1. VENDEDOR, 2. JEFE DE VENTAS) del usuario "+str(nom.upper())+") : "))
                if car.strip()==1 or car.strip()==2: # strip eliminar espacios en blanco 
                    if car == 1:
                        car2 = "VENDEDOR"
                        print("Usted le asigno al usuario:"+str(nom.upper())+"el cargo : "+ car2)
                        break
                    elif car == 2:
                        car2 = "JEFE DE VENTAS"
                        print("Usted le asigno al usuario:"+str(nom.upper())+"el cargo : "+ car2)
                        break
                else:
                    print("\n--- Debe Ser opcion 1 u opcion 2 !! ---\n")
                    system("pause")

            except:
                print("\n--- Error Al Intentar asignar el cargo!! ---")
                system("pause")
        
        
        t = Tipo()
        t.setNom_tip(nom.upper())
        t.setPat_tip(pat.upper())
        t.setMat_tip(mat.upper())
        t.setRut_tip(rut)
        t.setId_car(car)
        t.setnom_car(car2)
        self.d.agregarUsuario(t)
        u = Usuarios()
        u.setNom_usu(nom.upper())
        u.setCon_usu(pas)
        
        self.d.agregarContraseña(u)
        system("cls")
        print("\n ----usuario(",nom.upper()," creado correctamente -----", end = "\n\n")
        system("pause")
        self.menuInicialAdmin()

#--------------------------------------------------------------------
#- MENU PRODUCTOS
#--------------------------------------------------------------------            
    def menuProductos(self):
        system('cls')
        print("----Menu----")
        print('1.-Registrar-')
        print('2.-Modificar-')
        print('3.-Eliminar-')
        print('4.-Listar-')
        print('5.-Salir-')
        
        op = self.__validarNumeros(1,5,'La opcion')
        
        if op == 1:
            self.__registrarProductos() #listo
        elif op == 2:
            self.__modificarProductos()
        elif op == 3:
            self.__eliminarProductos()
        elif op == 4:
            self.__listarProductos()
        else:
            self.__salir()
    
#-----------------------------------------------------------------------
#-REGISTRAR UN PRODUCTO
#--------------------------------------------------------------------
    def __registrarProductos(self):
        system('cls')
        nom = self.__validarTexto(40,'el nombre')
        pre = self.__validarNumeros(1,100000,'el precio')
        
        m=Productos()
        m.setNombre(nom)
        m.setPrecio(pre)
        self.d.insertarProductos(m)
        system('pause')
        self.menuProductos()
#--------------------------------------------------------------------
#--MODIFICAR UN PRODUCTO
#--------------------------------------------------------------------
    def __modificarProductos(self):
        system('cls')
        id = self.__validarNumeros(1,99999,'el id')
        validacion = self.d.buscarProductos(id)
        if validacion == True:
            nom = self.__validarTexto(40,'el nombre')
            pre = self.__validarNumeros(1,1000000,'precio')
            
            m = Productos()
            m.setId(id)
            m.setNombre(nom)
            m.setPrecio(pre)
            
            self.d.modificarProductos(m)
        else:
            print('el id ingresado no esta registrado!')
        
        system ('pause')
        self.menuProductos()
#--------------------------------------------------------------------------
# ELIMINAR UN PRODUCTO
#--------------------------------------------------------------------------
    def __eliminarProductos(self):
        system('cls')
        id = self.__validarNumeros(1,9999,'el id')
        validacion = self.d.buscarProductos(id)
        if validacion == True:
            self.d.eliminarProductos(id)
        else:
            print('el id ingresado no esta registrado!')
        
        system ('pause')
        self.menu2()
#--------------------------------------------------------------------------
# LISTAR PRODUCTOS
#--------------------------------------------------------------------------        
    def __listarProductos(self):
        system('cls')
        rs = self.d.listar_productos3() #resultado
        print('------LISTADO DE Productos-----')
        
        for x in rs:
            print('ID:',x[0])
            print('NOMBRE:',x[1])
            print('PRECIO:',x[2])
            print('------------------------')
            
        system ('pause')
        self.menu2()
        
    def __salir(self):

        print("saliendo del sistema!!!")
        print("Adios!!!")
#--------------------------------------------------------------------
#- AGREGAR UN PRODUCTO
#-------------------------------------------------------------------
    def __agregarProductos(self):
        while True:
            try:
                system("cls")
                nom = input("Ingrese el nombre del producto:")
                if(len(nom) < 1):
                     print("Este campo no puede quedar vacio")
                else:
                     break
            except:
                    print("\n--- Error de ingresar nombre !! ---")
                    print("\n-- Intentelo nuevamente--")
                    system("pause")
                    self.__agregarProductos()
        while True:
            try:
                pre = int(input("ingrese el precio del producto:"))
                if(len(pre) == 0):
                        print("Este campo no puede quedar vacio")
                else:
                     break
            except ValueError:
                    print("\n--- Error de ingresar el precio !! ---")
                    print("\n-- Intentelo nuevamente--")
                    system("pause")
                    self.__agregarProductos()
#--------------------------------------------------------------------        
#- MENU JEFE DE VENTAS  
#--------------------------------------------------------------------

    def menuJefeVentas(self):
        try:
            system("cls")
            print("--- INICIASTE CON JEFE DE VENTAS:" + str(self.sesion.getNomUsuario().upper())+"---")               
            print("--- MENU DE OBTENER VENTAS ---")
            print("1. VER VENTAS CON FACTURA")
            print("2. VER VENTAS CON BOLETA")
            print("3. INFORME DE VENTAS")
            print("4. VOLVER A MENU")

            op = int(input("Digite Una Opcion : "))
            if op == 5:
                self.menuInicial()
        except:
            print("\n--- Error De Opcion Del Menu (try)!! ---")
            system("pause")
            self.menuJefeVentas()
#--------------------------------------------------------------------
#- MENU FACTURAS
#--------------------------------------------------------------------

    def menuJefeFactura(self):
        try:
            system("cls")               
            print("--- INICIASTE CON JEFE DE VENTAS:" + str(self.sesion.getNomUsuario().upper())+"---") 
            print("--- MENU DE VENTAS CON FACTURA ---")
            print("1. BUSCAR VENTAS POR VENDEDOR")
            print("2. LISTAR")
            print("3. MOSTRAR HISTORIAL")
            print("4. VOLVER A MENU")

            op = int(input("Digite Una Opcion : "))
            if op == 5:
                self.menuInicial()
        except:
            print("\n--- Error De Opcion Del Menu (try)!! ---")
            system("pause")
            self.menuJefeFactura()

#--------------------------------------------------------------------
#- APERTURA DE CAJA                      
#--------------------------------------------------------------------
    def menuJefeAbierta(self):
        try:
            system("cls")
            Caja = input("¿Estas seguro de querer abrir caja? (Y/N)")
            ejecutar = False
            if Caja == "Y":
                print("La caja esta disponible para ventas")
                ejecutar = True
            elif Caja == "N":
                print("La caja permanecera cerrada")
            else:
                print("error de tipeo, debe ingresar Y/N")
                self.menuJefeAbierta()
                
                            
        except:
            print("\n--- Error Al abrir caja!! ---")
            system("pause")
            self.menuJefe()

    def __digitarDatosProductos(self):
        pass

#--------------------------------------------------------------------
#- CIERRE DE CAJA                      
#--------------------------------------------------------------------
    def menuJefeCerrada(self):
            try:
                system("cls")
                Caja = input("¿Estas seguro de querer abrir caja? (Y/N)")
                ejecutar = True
                if Caja == "Y":
                    print("La caja ya no esta disponible para ventas")
                    ejecutar = False
                elif Caja == "N":
                    print("La caja permanecera abierta")
                else:
                    print("error de tipeo, debe ingresar Y/N")
                    self.menuJefeCerrada()                  
            except:
                print("\n--- Error Al abrir caja!! ---")
                system("pause")
                self.menuJefe()
#--------------------------------------------------------------------

    def __listarProductos(self):
        pass

#--------------------------------------------------------------------

    def __eliminarProductos(self):
        try:
            pass
        except:
            print("\n--- Error Al Buscar Ejercicio!! ---")
            system("pause")
            self.menuInicial()

#--------------------------------------------------------------------

    def __estadistica(self):
        pass

#--------------------------------------------------------------------

    def __salir(self):
        system("cls")
        print("-------------------")
        print("--- OK. Adios!! ---")
        print("-------------------")
        system("pause")

#--------------------------------------------------------------------

    def __errorOpcion(self):
        system("cls")
        print("-------------------------")
        print("--- Error De Opcion!! ---")
        print("-------------------------")
        system("pause")
        self.menuInicial()