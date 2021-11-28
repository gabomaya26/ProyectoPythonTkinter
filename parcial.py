from tkinter import *
from tkinter import messagebox 
import json

class Juego:
	def __init__(self):
		self.preguntas_no=0
		self.ventana_titulo()
		self.ventana_pregunta()
		self.opcion_seleccionada=IntVar()
		self.opts=self.radio_botones()
		self.ventana_opciones()
		self.botones()
		self.total_preguntas=len(pregunta)
		self.correctas=0
        
	def ventana_resultado(self):
		contador_incorrectas = self.total_preguntas - self.correctas
		correctas = f"correctas: {self.correctas}"
		incorrectas = f"incorrectas: {contador_incorrectas}"
		puntaje = int(self.correctas / self.total_preguntas * 100)
		resultado = f"puntaje: {puntaje}%"
		messagebox.showinfo("resultado", f"{resultado}\n{correctas}\n{incorrectas}")

	def verificar_respuesta(self, preguntas_no):
		if self.opcion_seleccionada.get() == respuesta[preguntas_no]:
			return True
	#pregunta1 , respuesta1[1], opciones1[1,2,3,4]
	def siguiente_boton(self):
		if self.verificar_respuesta(self.preguntas_no):
			self.correctas += 1
		self.preguntas_no += 1
		if self.preguntas_no==self.total_preguntas:
			self.ventana_resultado()
			ventana.destroy()
		else:
			self.ventana_pregunta()
			self.ventana_opciones()

	def botones(self):
		siguiente_btn = Button(ventana,text="Siguiente",command=self.siguiente_boton,width=10,bg="skyblue",fg="black",font=("arial",14,"bold")            )
		siguiente_btn.place(x=350,y=380)
		salir_btn = Button(ventana, text="Salir", command=ventana.destroy,width=5,bg="red", fg="black",font=("arial",14," bold"))
		salir_btn.place(x=700,y=50)

	def ventana_opciones(self):
		val=0
		self.opcion_seleccionada.set(0)
		for x in opciones[self.preguntas_no]: 
			self.opts[val]['text']=x
			val+=1

	def ventana_pregunta(self):
		preguntas_no = Label(ventana, text=pregunta[self.preguntas_no], width=50,font=( 'arial' ,14, 'bold' ), bg="skyblue",anchor= 'w',wraplength=700,justify='center')
		preguntas_no.place(x=70, y=100)

	def ventana_titulo(self):
		title = Label(ventana, text="CUANTO SABES DE LA UTS",width=50, bg="green",fg="black", font=("arial", 20, "bold"))
		title.place(x=0, y=2)
		title = Label(ventana, text="Edgar Hernandez Maya",width=80, bg="green",fg="black", font=("arial", 12, "bold"))
		title.place(x=0, y=475)

	def radio_botones(self):
		pregunta_lista = []
		y_pos = 150
		while len(pregunta_lista) < 4:
			radio_btn = Radiobutton(ventana,text="",variable=self.opcion_seleccionada,value = len(pregunta_lista)+1,bg="skyblue",font = ("arial",14))
			pregunta_lista.append(radio_btn)
			radio_btn.place(x = 100, y = y_pos)
			y_pos += 40
		return pregunta_lista

ventana = Tk()
ventana.geometry("800x500")
ventana.title("Parcial Numero 3")
imagen = PhotoImage(file= "1.png")
background = Label(image = imagen, text="Fondo")
background.place(x=1, y=1, relwidth=1, relheight=1)
with open(('data.json')) as f:
	data = json.load(f)
pregunta = (data['pregunta'])
opciones = (data['opciones'])
respuesta = (data[ 'respuesta'])

juego = Juego()

ventana.mainloop()