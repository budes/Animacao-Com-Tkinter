from tkinter import *
#import pdb

class Mario():
	print('Hello world 6')

	def __init__(self):

		# Instancia Tk
		self.inst = Tk()

		self.imgs = [PhotoImage(file='mario/mario_%s.ppm' %str(i+1)) for i in range(4)]
		print(self.imgs)
		self.imgsI = [PhotoImage(file='mario/mario_l%s.ppm' %str(i+1)) for i in range(4)]
		print(self.imgsI)

		# Os widgets
		self.canvas = Canvas(self.inst, bg='black', height=100, width=300)
		self.but = Button(self.inst, text='Jogar', command=self.iniciarjogo, bg='yellow', fg='black')

		# -----------------------------------------------------------
		
		# O sistema de movimentação

		self.canvas.bind('<Left>', self.esquerda)
		self.canvas.bind('<Right>', self.direita)

		self.i = 2
		self.mov = 0

		# -----------------------------------------------------------

		# O empacotamento dos widgets
		self.canvas.pack()
		self.but.pack()

		self.update()

		# O mainloop 
		self.inst.mainloop()

	def iniciarjogo(self):
		# Passa o foco pro canvas, pra que o sistema de movimentação comece a funcionar
		self.canvas.focus_force()

		# O personagem
		self.canvas.create_image((150, 75), image=self.imgs[1], tag='mario')

	def direita(self, event):
		# Move pra direita
		self.mov = 1
		self.canvas.move('mario', 5, 0)

	def esquerda(self, event):
		# Move pra esquerda
		self.mov = -1
		self.canvas.move('mario', -5, 0)

		
	def update(self):
        # Atualiza o frame do personagem

		if self.mov != 0: # Se tiver movimento
			
			self.i += 1
			if self.i > len(self.imgs)-1:
				self.i = 0

			if self.mov == 1:
				self.canvas.itemconfig('mario', image=self.imgs[self.i])
			elif self.mov == -1:
				self.canvas.itemconfig('mario', image=self.imgsI[self.i])

			self.mov = 0

		else: # Se não tiver movimento
			self.i = 2

		# Atualiza a cada 70 milissegundos.
		self.inst.after(70, self.update)

if __name__ == '__main__':
	Mario()
