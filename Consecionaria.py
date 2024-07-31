class Auto:
         def __init__(self):
                  self.modelos=["Ford", "Fiat", "Renault", "Peugeot", "Citroen"]
                  self.a=3
                  self.precios=[100000, 200000, 300000, 400000, 500000]
         def getmodelo(self):
                  return self.modelos
         def getprecio(self):
                  return self.precios
         def getcantford(self):
                  return self.cantford
class Cliente:
    def __init__(self):
        self.nombre=""
        
    def nombrecomprador(self):
                  print(" ________________________________")
                  print("|_________NOMBRE  CLIENTE________|")
                  self.nombre=input("        ")
         
    def getnombrecomprador(self):
                  return self.nombre
class Concesionaria:
    def __init__(self):
        self.f=""
        self.recaudacion=0
        
    def nombreC(self):
                  print(" ________________________________")
                  print("|______NOMBRE CONSECIONARIA______|")
                  self.f=input("        ")
                  
    def getConcesionaria(self):
                  return self.f
                
    def reaudacion(self):
                  self.recaudacion=0
class Vendedor:
    def __init__(self):
        self.vendedor=""
    def ventas(self):
        print(" ________________________________")
        print("|          SELECCIONA AL         |")
        print("|            VENDEDOR            |")
        print(" --------------------------------")
        print("|           1-VENDEDOR 1         |")
        print("|           2-VENDEDOR 2         |")
        print("|           3-VENDEDOR 3         |")
        print("|________________________________|")
        self.vendedor= int(input("               "))
        while self.vendedor>=4:
            print ('\n'*45)#Simulamos limpieza de pantalla
            print("         OPCION INVALIDA")
            print(" ________________________________")
            print("|          SELECCIONA AL         |")
            print("|            VENDEDOR            |")
            print(" --------------------------------")
            print("|           1-VENDEDOR 1         |")
            print("|           2-VENDEDOR 2         |")
            print("|           3-VENDEDOR 3         |")
            print("|________________________________|")
            self.vendedor= int(input("               "))

    def getvendedor(self):
        return self.vendedor
    
class Menu:
         def __init__(self):
             
                  self.autos=""
                  self.precios=0
                  self.fg=""
                  self.gf=""
                  self.cantidadford=3
                  self.cantidadfiat=3
                  self.cantidadrenault=3
                  self.cantidadpeug=3
                  self.cantidadcitr=3
                  self.recaudacion=0
                  self.ventasford=0
                  self.ventasfiat=0
                  self.ventasrenault=0
                  self.ventaspeugeot=0
                  self.ventascitroen=0
                  self.ventas1=0
                  self.ventas2=0
                  self.ventas3=0
                  self.comision1=0
                  self.comision2=0
                  self.comision3=0
         def menu1(self):
                  self.autos=auto.getmodelo()
                  self.precios=auto.getprecio()
                  #self.fg=Concesionaria.getnombreconseccionaria()
                  #self.gf=cliente.getnombrecomprador()
                  
                  print(" ________________________________")
                  print("|         MENU PRINCIPAL         |")
                  print("|________________________________|")
                  print("|                                |")
                  print("|   1- Ingresar nueva compra     |")
                  print("|________________________________|")
                  print("|                                |")
                  print("|  2- Mostrar resumen/fin jorn.  |")
                  print("|________________________________|")
                  op=int(input(""))

                  while op!=1:
                      if op==2:
                           print ('\n'*45)#Simulamos limpieza de pantalla
                           return menu.resumen()
                      print("OPCION INVALIDA")
                      op=int(input(""))
                  if   op==1:
                            print ('\n'*45)#Simulamos limpieza de pantalla
                            menu.menu2()
                  elif op==2:
                           print ('\n'*45)#Simulamos limpieza de pantalla
                           return menu.resumen()
                  
         def menu2(self):
                   print(" ________________________________")
                   print("|        INGRESE EL MODELO       |")
                   print("|                                |")
                   print("|   MODELO       PRECIO    STOCK |")
                   print("|________________________________|")
                   print("|                                |")
                   print("| 1- FORD      $ 100.000    X",self.cantidadford ," |")
                   print("| 2- FIAT      $ 200.000    X",self.cantidadfiat ," |")
                   print("| 3- RENAULT   $ 300.000    X",self.cantidadrenault ," |")
                   print("| 4- PEUGEOT   $ 400.000    X",self.cantidadpeug ," |")
                   print("| 5- CITROEN   $ 500.000    X",self.cantidadcitr ," |")
                   print("|________________________________|")
                   self.op=int(input(""))
                   while self.op>5:
                       print("OPCION INVALIDA (Ingrese un modelo valido)")
                       self.op=int(input(""))
                   if self.op==1:
                            print(self.autos[0])
                   elif self.op==2:
                            print(self.autos[1])
                   elif self.op==3:
                            print(self.autos[2])
                   elif self.op==4:
                            print(self.autos[3])
                   elif self.op==5:
                            print(self.autos[4])
                            
                   concesionaria.nombreC()
                   cliente.nombrecomprador()
                   vendedor.ventas()
                   print ('\n'*45)#Simulamos limpieza de pantalla
                   menu.menu3()
                   
         def menu3(self):
                  print(" ________________________________")
                  print("|        CONFIRME LOS DATOS      |")
                  print("|________________________________|")
                  print("| NOMBRE CONCESIONARIA:",concesionaria.getConcesionaria())
                  print("|________________________________|")
                  print("|                                |")
                  print("| APELLIDO Y NOMBRE: ",cliente.getnombrecomprador())
                  print("|                                |")
                  print("| MODELO: ",self.autos[self.op-1])
                  print("| PRECIO: $" ,self.precios[self.op-1])
                  print("|________________________________|")
                  print("|VENDEDOR: VENDEDOR",vendedor.getvendedor(),"           |")
                  print("|________________________________|")
                  print("|                                |")
                  print("|          CONFIRMAR COMPRA      |")
                  print("|             1 -SI              |")
                  print("|             2 -NO              |")
                  print("|________________________________|")
                  opc=int(input(""))
                  while opc>2:
                      print ('\n'*45)#Simulamos limpieza de pantalla
                      print("OPCION INVALIDA. INGRESE NUEVAMENTE")
                      menu.menu3()
                      opc=int(input(""))
                  if opc==1:
                           if self.op==1:
                                    print ('\n'*45)#Simulamos limpieza de pantalla
                                    while self.cantidadford<1:
                                       print("NO HAY STOCK DEL AUTO FORD, ESCOJA OTRO MODELO...")
                                       menu.menu2()
                                    self.cantidadford=self.cantidadford-1
                                    self.recaudacion=self.recaudacion+self.precios[self.op-1]
                                    self.ventasford=self.ventasford+1
                                    if vendedor.getvendedor()==1:
                                         self.ventas1=self.ventas1+1
                                         self.comision1=self.comision1+self.precios[self.op-1]*15/100
                                    elif vendedor.getvendedor()==2:
                                        self.ventas2=self.ventas2+1
                                        self.comision2=self.comision2+self.precios[self.op-1]*15/100
                                    elif vendedor.getvendedor()==3:
                                        self.ventas3=self.ventas3+1
                                        self.comision3=self.comision3+self.precios[self.op-1]*15/100
                                    menu.ticket()
                                    
                
                           if self.op==2:
                                    print ('\n'*45)#Simulamos limpieza de pantalla
                                    while self.cantidadfiat<1:
                                       print("NO HAY STOCK DEL AUTO FIAT, ESCOJA OTRO MODELO...")
                                       menu.menu2()
                                    self.cantidadfiat=self.cantidadfiat-1
                                    self.recaudacion=self.recaudacion+self.precios[self.op-1]
                                    self.ventasfiat=self.ventasfiat+1
                                    if vendedor.getvendedor()==1:
                                         self.ventas1=self.ventas1+1
                                         self.comision1=self.comision1+self.precios[self.op-1]*15/100
                                    elif vendedor.getvendedor()==2:
                                        self.ventas2=self.ventas2+1
                                        self.comision2=self.comision2+self.precios[self.op-1]*15/100
                                    elif vendedor.getvendedor()==3:
                                        self.ventas3=self.ventas3+1
                                        self.comision3=self.comision3+self.precios[self.op-1]*15/100
                                    menu.ticket()
                                    
                           if self.op==3:
                                    print ('\n'*45)#Simulamos limpieza de pantalla
                                    while self.cantidadrenault<1:
                                       print("NO HAY STOCK DEL AUTO RENAULT, ESCOJA OTRO MODELO...")
                                       menu.menu2()
                                    self.cantidadrenault=self.cantidadrenault-1
                                    self.recaudacion=self.recaudacion+self.precios[self.op-1]
                                    self.ventasrenault=self.ventasrenault+1
                                    if vendedor.getvendedor()==1:
                                         self.ventas1=self.ventas1+1
                                         self.comision1=self.comision1+self.precios[self.op-1]*15/100
                                    elif vendedor.getvendedor()==2:
                                        self.ventas2=self.ventas2+1
                                        self.comision2=self.comision2+self.precios[self.op-1]*15/100
                                    elif vendedor.getvendedor()==3:
                                        self.ventas3=self.ventas3+1
                                        self.comision3=self.comision3+self.precios[self.op-1]*15/100
                                    menu.ticket()
                                    
                           if self.op==4:
                                    print ('\n'*45)#Simulamos limpieza de pantalla
                                    while self.cantidadpeug<1:
                                       print("NO HAY STOCK DEL AUTO PEUGEOT, ESCOJA OTRO MODELO...")
                                       menu.menu2()
                                    self.cantidadpeug=self.cantidadpeug-1
                                    self.recaudacion=self.recaudacion+self.precios[self.op-1]
                                    self.ventaspeugeot=self.ventaspeugeot+1
                                    if vendedor.getvendedor()==1:
                                         self.ventas1=self.ventas1+1
                                         self.comision1=self.comision1+self.precios[self.op-1]*15/100
                                    elif vendedor.getvendedor()==2:
                                        self.ventas2=self.ventas2+1
                                        self.comision2=self.comision2+self.precios[self.op-1]*15/100
                                    elif vendedor.getvendedor()==3:
                                        self.ventas3=self.ventas3+1
                                        self.comision3=self.comision3+self.precios[self.op-1]*15/100
                                    menu.ticket()
                                    
                           if self.op==5:
                                    print ('\n'*45)#Simulamos limpieza de pantalla
                                    while self.cantidadcitr<1:
                                       print("NO HAY STOCK DEL AUTO CITROEN, ESCOJA OTRO MODELO...")
                                       menu.menu2()
                                    self.cantidadcitr=self.cantidadcitr-1
                                    self.recaudacion=self.recaudacion+self.precios[self.op-1]
                                    self.ventascitroen=self.ventascitroen+1
                                    if vendedor.getvendedor()==1:
                                         self.ventas1=self.ventas1+1
                                         self.comision1=self.comision1+self.precios[self.op-1]*15/100
                                    elif vendedor.getvendedor()==2:
                                        self.ventas2=self.ventas2+1
                                        self.comision2=self.comision2+self.precios[self.op-1]*15/100
                                    elif vendedor.getvendedor()==3:
                                        self.ventas3=self.ventas3+1
                                        self.comision3=self.comision3+self.precios[self.op-1]*15/100
                                    menu.ticket()
                  if opc==2:
                      print ('\n'*45)#Simulamos limpieza de pantalla
                      menu.menu1()
         def ticket(self):
                  print(" ________________________________")
                  print("|*      *|     TICKET     |*    *|")
                  print("|*______*|________________|*____*|")
                  print("|CONCESIONARIA ",concesionaria.getConcesionaria())
                  print("|                                |")
                  print("|APELLIDO Y NOMBRE: ",cliente.getnombrecomprador())
                  print("|--------------------------------|")
                  print("|MODELO: ",self.autos[self.op-1])
                  print("|                                |")
                  print("|PRECIO: $" ,self.precios[self.op-1])
                  print("|                                |")
                  print("|--------------------------------|")
                  print("|      VENDEDOR: VENDEDOR",vendedor.getvendedor(),"     |")
                  print("|                                |")
                  print("|                                |")
                  print("|* MUCHAS GRACIAS POR SU COMPRA *|")
                  print("|________________________________|")
                  print("|                                |")
                  print("|ENTER PARA VOLVER MENU PRINCIPAL|")
                  print("|________________________________|")
                  input("                ")
                  
                  print ('\n'*45)#Simulamos limpieza de pantalla
                  menu.menu1()
                  
                  
                  
                  
         def resumen(self):
                  print(" ________________________________")
                  print("|          CONCESIONARIA         |")
                  print("|________________________________|")
                  print("|                                |")
                  print("|  Vehiculos vendidos:",self.ventasford+self.ventasfiat+self.ventasrenault+self.ventaspeugeot+self.ventascitroen)
                  print("|  Ford:",self.ventasford,"                      |")
                  print("|  Fiat:",self.ventasfiat,"                      |")
                  print("|  Renault",self.ventasrenault,"                    |")
                  print("|  Peugeot",self.ventaspeugeot,"                    |")
                  print("|  Citroen",self.ventascitroen,"                    |")
                  print("|                                |")
                  print("|  TOTAL RECAUDADO: $$",self.recaudacion)
                  print("|________________________________|")
                  print("|       SALARIOS EMPLEADOS       |")
                  print("|          BASE $10.000          |")
                  print("|________________________________|")
                  print("|  Ventas Vendedor 1:",self.ventas1,"         |")
                  print("|  15% x Venta:  $",self.comision1)
                  print("|  TOTAL:  $",10000+self.comision1)
                  print("|--------------------------------|")
                  print("|  Ventas Vendedor 2:",self.ventas2,"         |")
                  print("|  15% x Venta:  $",self.comision2)
                  print("|  TOTAL:  $",10000+self.comision2)
                  print("|--------------------------------|")
                  print("|  Ventas Vendedor 3:",self.ventas3,"         |")
                  print("|  15% x Venta:  $",self.comision3)
                  print("|  TOTAL:  $",10000+self.comision3)
                  print("|________________________________|")
                  print("|         1-MENU PRINCIPAL       |")
                  print("|         2-FIN                  |")
                  print("|________________________________|")
                  a=int(input(""))
                  if a==1:
                           print ('\n'*45)#Simulamos limpieza de pantalla
                           menu.menu1()

                  

menu=Menu()
cliente=Cliente()
concesionaria=Concesionaria()
auto=Auto()
vendedor=Vendedor()
#main
print ('\n'*45)#Simulamos limpieza de pantalla
menu.menu1()

                  
         

