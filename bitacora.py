#integrantes:
# FIGUEROA MARTINEZ ARMANDO
# MARTINEZ VALENCIA LUIS EDUARDO
# HERNANDEZ TOVAR ANDRES
# GARCIA GARCAIA SALVADOR 
class dia:
     def dia(self,a):
          b=int(input("\n\t dame la hora del 0 al 12"))
          if(a==0):
               print("el lunes")
               self.hora(b)
          if(a==1):
               print("el martes")
               self.hora(b)
          if(a==2):
               print("el miercoles")
               self.hora(b)
          if(a==3):
               print("el jueves")
               self.hora(b)
          if(a==4):
               print("el viernes")
               self.hora(b)
          if(a==5):
               print("el sabado")
               self.hora(b)
          if(a==6):
               print("el domingo")
               self.hora(b)



          
class hora:
   def __init__(self):
         pass
   def hora(self,a):
          if(a==0):
               print(" estudiaste dinamica")
               rutina1.encendido()
          if(a==1):
               print("tuviste entrenamiento")
               rutina1.encendido()
          if(a==2):
               print(" terminaste  tu tarea ")
               rutina1.encendido()
          if(a==3):
               print("repasaste ingles")
               rutina1.encendido()
          if(a==4):
               print(" tomaste un baño")
               rutina1.encendido()
          if(a==5):
               print("desaynaste con tus padres ")
               rutina1.encendido()
          if(a==6):
               print(" viste un partido")
               rutina1.encendido()
          if(a==7):
               print(" estudiaste mecanica de materiales")
               rutina1.encendido()
          if(a==8):
               print("comenzaste a  a dormir")
               rutina1.encendido()
          if(a==9):
               print(" tuviste examen ")
               rutina1.encendido()
          if(a==10):
               print("saliste a pasear")
               rutina1.encendido()
          if(a==11):
               print(" tomaste clases de calculo")
               rutina1.encendido()
          if(a==12):
               print("tomaste clases ")
               rutina1.encendido()
          if(a==13):
               print("jugaste videojuegos")
               rutina1.encendido()


class rutina(dia,hora):
     def encendido(self):
          print("\n\t hola bienvenido a tu bitacora deseas saber \n\t que hiciste un dia dame el numero de dia \n\t lunes=0 y asi sucesivamente")
          a=int(input("\n\t dame el dia"))         
          self.dia(a)


rutina1=rutina()
rutina1.encendido()

