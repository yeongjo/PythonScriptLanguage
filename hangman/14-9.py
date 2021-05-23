import random
from tkinter import *

class MainGUI:
	def drawHangman(self):
		self.canvas.delete('hangman')
		self.canvas.create_arc(20,200,20+80,200+40,start=0,extent=180)
		self.canvas.create_line(20+40,200,20+40,20)
		self.canvas.create_line(20+40,20,20+40+100,20)

		if self.doneWithWrong: # 7번 틀린 경우

			self.canvas.create_text(200,250,text='정답 '+self.toString(self.hiddenWord),
							  font = 'Times 14', tags='hangman')
			if self.NofMiss > 0:
				self.canvas.create_text(200,270,text='계속하려면 ENTER',
							   font = 'Times 14', tags='hangman')
		elif self.doneWithCorrect:
			self.canvas.create_text(200,250,text='맞았습니다.'+self.toString(self.hiddenWord),
							  font = 'Times 14', tags='hangman')
			if self.NofMiss > 0:
				self.canvas.create_text(200,270,text='계속하려면 ENTER',
							   font = 'Times 14', tags='hangman')
		else:
			self.canvas.create_text(200,250,text='단어 추측'+self.toString(self.guessWord),
							  font = 'Times 14', tags='hangman')
			if self.NofMiss > 0:
				self.canvas.create_text(200,270,text='틀린 글자'+self.toString(self.missChars),
							   font = 'Times 14', tags='hangman')

		if self.NofMiss < 1:
			return
		x1 =20+40+100
		y1=20
		x2=x1
		y2=y1+20
		self.canvas.create_line(x1,y1,x2,y2,tags='hangman')

		if self.NofMiss < 2:
			return
		x3 = x2
		y3=y2+20
		self.canvas.create_oval(x3-20,y3-20,x3+20,y3+20,tags='hangman')

		if self.NofMiss < 3: #왼팔
			return
		self.canvas.create_line(x3-15,y3+15,x3-50,y3+70,tags='hangman')
		if self.NofMiss < 4: #오른팔
			return
		self.canvas.create_line(x3+15,y3+15,x3+50,y3+70,tags='hangman')
		if self.NofMiss < 5: #몸통
			return
		x4=x3
		y4=y3+100
		self.canvas.create_line(x3,y3+20,x4,y4,tags='hangman')
		if self.NofMiss < 6: #왼다리
			return
		self.canvas.create_line(x4,y4,x4-50,y4+100,tags='hangman')
		if self.NofMiss < 7: #오른다리
			return
		self.canvas.create_line(x4,y4,x4+50,y4+100,tags='hangman')

	def setWord(self):
		index = random.randint(0, len(self.words)-1)
		self.hiddenWord = self.words[index]
		self.guessWord = ['*']*len(self.hiddenWord)
		self.NofCorrectChar = 0  # 맞친 문자의 개수
		self.NofMiss = 0			# 틀린 횟수
		self.missChars = []
		self.doneWithWrong = False
		self.doneWithCorrect = False

	def KeyEvent(self, key):
		if 'a' <= key.char <= 'z':
			ch = key.char
			if ch in self.guessWord:
				print('\t',ch,'은/는 이미 포함되어 있습니다.')
			elif self.hiddenWord.find(ch) == -1: #리스트이ㅡ find 함수는  검색해서 찾으면 인덱스를 반환
				print('\t',ch,'은/는 포함되어 있지 않습니다.') #못찾으면 -1 반환
				self.NofMiss += 1
				if not key.char in self.missChars:
					self.missChars.append(ch)
				if self.NofMiss == 7:
					self.doneWithWrong = True
			else:
				k = self.hiddenWord.find(ch)
				while k >= 0:
					self.guessWord[k] = ch
					self.NofCorrectChar += 1
					k = self.hiddenWord.find(ch,k+1)
				if self.NofCorrectChar == len(self.hiddenWord):
					self.doneWithCorrect = True # 다 찾고 종료
		elif key.keycode == 13:
			if self.doneWithCorrect or self.doneWithWrong:
				self.setWord()
		self.drawHangman()

	def toString(self, guessWord):
		result =''
		for c in guessWord:
			result += c
		return result

	def __init__(self):
		fp = open('hangman.txt')
		self.words = fp.read().split()
		window = Tk()
		window.title("행맨 게임")
		self.canvas = Canvas(window,bg='white',width=400,height=300)
		self.canvas.pack()
		self.setWord()
		self.drawHangman()

		
		self.canvas.bind('<Key>',self.KeyEvent)
		self.canvas.focus_set()
		window.mainloop()




MainGUI()