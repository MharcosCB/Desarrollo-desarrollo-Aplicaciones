from Usuarios import Usuarios
from Productos import Productos
from Tipo import Tipo
from os import system
import pymysql

class DAO:

    def __init__(self):
        pass

#----------------------------------------------------------------------

    def conectar(self):
        self.con = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "",
            db = "bd_bazar"
        )

        self.cursor = self.con.cursor()
        
#----------------------------------------------------------------------

    def desconectar(self):
        self.con.close()

#----------------------------------------------------------------------

    def iniciarSesion(self, nom, pas):
        try:
            self.conectar()
            sql = "select * from usuario where nom_usu = %s and con_usu =%s"
            val = (nom,pas)
            self.cursor.execute(sql,val)
            rs = self.cursor.fetchall() #Registro
            self.desconectar() 
            return rs
        except:
            print("\n--- Error Al Iniciar Sesion (DAO)!! ---", end="\n\n")
            system("pause")

#----------------------------------------------------------------------

    def comprobarNombreUsuario(self, nom):
        try:
            self.conectar()
            sql = "select nom_usu from usuarios where nom_usu=%s" #si no existe me sale none, la tupla con el registro encontrado
            self.cursor.execute(sql,nom)
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Comprobar Nombre Del Usuario a Registrar (DAO)!! ---", end="\n\n")
            system("pause")
#----------------------------------------------------------------------

    def comprobarCargo(self, idcar,nomcar):
        try:
            self.conectar()
            sql = "select from cargo where id_car=%s and nom_car=%s"
            val = (idcar,nomcar)
            self.cursor.execute(sql,val)
            rs = self.cursor.fetchall()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Comprobar Nombre Del Usuario a Registrar (DAO)!! ---", end="\n\n")
            system("pause")

#----------------------------------------------------------------------
    def agregarContraseña(self, u):
        try:
            self.conectar()
            sql = "insert into usuarios (nom_usu ,con_usu,id_tip) values(%s,%s,%s)"
            val = (u.getNom_usu(),u.getCon_usu(),u.getId_tip)
            self.cursor.execute(sql,val)
            self.con.commit()
            self.desconectar()
        except:
            print("\n--- Error Al Agregar Nuevo Usuario (DAO)!! ---", end="\n\n")
            system("pause")
        
    def agregarUsuario(self, t):
        try:
            self.conectar()
            sql = "insert into tipo_usuario (nom_tip,pat_tip,mat_tip,rut_tip,id_car) values(%s,%s,%s,%s,%s)"
            val = (t.getNom_tip(),t.getpat_tip(),t.getmat_tip(),t.getrut_tip(),t.getid_car())
            self.cursor.execute(sql,val)
            self.con.commit()
            self.desconectar()
        except:
            print("\n--- Error Al Agregar Nuevo Usuario (DAO)!! ---", end="\n\n")
            system("pause")


#----------------------------------------------------------------------

    def comprobarIdEjercicio(self, id):
        try:
            pass
        except:
            print("\n--- Error Al Comprobar El ID Del Ejercicio!! (DAO) ---", end="\n\n")
            system("pause")

#----------------------------------------------------------------------

    def comprobarNombreEjercicio(self, nom):
        try:
            pass
        except:
            print("\n--- Error Al Comprobar Nombre De Ejercicio (DAO)!! ---", end="\n\n")
            system("pause")

#----------------------------------------------------------------------

    def comprobarTipoFK(self, tip):
        try:
            pass
        except:
            print("\n--- Error Al Comprobar Tipo FK (DAO)!! ---", end="\n\n")
            system("pause")

#----------------------------------------------------------------------

    def agregarEjercicio(self, e):
        try:
            pass
        except:
            print("\n--- Error Al Agregar Ejercicio (DAO)!! ---", end="\n\n")
            system("pause")

#----------------------------------------------------------------------

    def obtenerEjercicios(self):
        try:
            pass
        except:
            print("\n--- Error Al Obtener Ejercicios (DAO)!! ---", end="\n\n")
            system("pause")

#----------------------------------------------------------------------

    def obtenerTipos(self):
        try:
            pass
        except:
            print("\n--- Error Al Obtener Tipos (DAO)!! ---", end="\n\n")
            system("pause")

#----------------------------------------------------------------------

    def buscarEjercicioExistente(self, id):
        try:
            pass
        except:
            print("\n--- Error Al Buscar Ejercicio Existente (DAO)!! ---", end="\n\n")
            system("pause")

#----------------------------------------------------------------------

    def eliminarEjercicioExistente(self, id):
        try:
            pass
        except:
            print("\n--- Error Al Intentar Eliminar Ejercicio (DAO)!! ---", end="\n\n")
            system("pause")

#----------------------------------------------------------------------

    def obtenerEstadistica(self, opcion):
        try:
            pass
        except:
            print("\n--- Error Al Obtener Estadistica!! (DAO) ---", end="\n\n")
            system("pause")


    
    def buscarProductos(self, id):
        try:
            sql = "select * from Productos where id_pro = %s;"
            val = (id)
            self.cursor.execute(sql, val)
            rs = self.cursor.fetchall()
            if int(rs[0][0]) == int(id):
                return True
            else:
                return False
        except Exception:
            print("Error en la busqueda!")
    
    def insertarProductos(self,m):
        try:
            sql = "insert into productos (nom_pro, pre_pro) values (%s,%s);"
            val = (m.getNombre(), m.getPrecio()) #Se genera una tupla con los datos
            self.cursor.execute(sql, val) #se ejecuta la instruccion sql con los datos
            self.con.commit() #Se almacena el registro en la BD
            print("Producto registrado correctamente!")
        except Exception:
            print("Error al insertar!")
    
    def modificarProductos(self,m):
        try:
                sql = "update Productos set nom_pro=%s, pre_pro=%s where id_pro=%s;"
                val = (m.getNombre(),m.getPrecio())
                self.cursor.execute(sql, val)
                self.con.commit()
                print("Producto actualizado correctamente!")
        except Exception:
            print("Error al actualizar!")
        
    
    def eliminarProductos(self,id):
        try:
            val = (id)
            sql = "delete from productos where id_pro=%s;"
            self.cursor.execute(sql, val)
            self.con.commit()
            print("Producto eliminado correctamente!")
        except Exception:
            print("Error al eliminar!")
    
    def listar_productos3(self):
        sql = "select * from productos;"
        try:
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            return rs     #----
        except Exception:
            print("Error en la consulta3")     
    
    def obtenerVentas(self):
        try: 
            pass   
        except Exception:
            print("Error")