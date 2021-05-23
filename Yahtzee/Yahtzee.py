from tkinter import *
from tkinter import font
import tkinter.messagebox
import random


class Dice:
	def rollDice(self):
		self.roll = random.randint(1,6)
	def getRoll(self):
		return self.roll


class Player:
	UPPER = 6 # upper category 6H
	LOWER = 7 # lower category 77H
	def __init__(self,name):
		self.name = name
		self.scores=[0 for i in range(self.UPPER+self.LOWER)] #137H category #13개 category 사용여부
		self.used=[False for i in range(self.UPPER+self.LOWER)]

	def setScore(self, score, index):
		self.scores[index] = score

	def setAtUsed(self, index):
		self.used[index] = True

	def getUpperScore(self):
		sum = 0
		for i in range(self.UPPER):
			sum += self.scores[i]
		self.upperScore = sum
		return sum

	def getLowerScore(self):
		sum = 0
		for i in range(self.UPPER,self.UPPER+self.LOWER ):
			sum += self.scores[i]
		return sum

	def getUsed(self):
		return used

	def getTotalScore(self): 
		sum = 0
		for i in range(0,self.UPPER+self.LOWER ):
			sum += self.scores[i]
		return sum

	def toString(self):
		return self.name

	def allLowerUsed(self): #lower category 77W 2 W
		for i in range(self.UPPER,self.UPPER+self.LOWER): 
			if (self.used[ i ] == False):
				return False 
		return True

	def allUpperUsed(self): #upper category 61
		#Upper Scores, Upper Bonus
		for i in range(self.UPPER): 
			if (self.used[ i ] == False):
				return False 
		return True

	def clear(self):
		self.scores = [0 for i in range(self.UPPER+self.LOWER)]
		self.used = [False for i in range(self.UPPER+self.LOWER)]

class Configuration:
	configs = ["Category", "Ones", "Twos", "Threes", "Fours", "Fives", "Sixes",
	"Upper Scores", "Upper Bonus (35)", "Three of a kind", "Four of a kind", "Full House(25)", "Small Straight (30)", "Large Straight (40)", "Yahtzee(50)", "Chance","Lower Scores", "Total"]
	def getConfigs(): # 정적 메소드: 객체생성 없이 사용 가능
		return Configuration.configs
	def score(row, d): # 정적 메소드: 객체생성 없이 사용 가능
		#row에 따라 주사위 점수를 계산 반환, 예를 들어, row가 0이면 "Ones"가 채점되어야 함을
		## 의미합니다. row가 2이면, "Threes"가 득점되어야 함을 의미합니다. row가 득점 (scored)하지 
		## 않아야 하는 버튼 (즉, Upper Score, UpperBonus, Lower Score, Total 등)을 나타내는 경우 
		## -1을 반환합니다.
		if (row>=0 and row<=6):
			return Configuration.scoreUpper (d, row+1) 
		elif (row==8):
			return Configuration.scoreThreeOfAKind(d)
		elif row==9:
			return Configuration.scoreFourOfAKind(d)
		elif row==10:
			return Configuration.scoreFullHouse(d)
		elif row==11:
			return Configuration.scoreSmallStraight(d)
		elif row==12:
			return Configuration.scoreLargeStraitght(d)
		elif row==13:
			return Configuration.scoreYahtzee(d)
		elif row==14:
			return Configuration.sumDie(d)
		return -1

	def scoreUpper(d, r):
		#Upper Section 구성에 대해 주사위 점수를 매깁니다.
		#num 1이면 ones 구성의 점수를 반환합니다.
		cnt = 0
		for i in d:
			if i.getRoll() == r: cnt += r
		return cnt

	def scoreThreeOfAKind(d):
		cnt = [0 for i in range(6)]
		sum = [0 for i in range(6)]
		for i in d:
			i = i.getRoll()-1
			cnt[i] += 1
			sum[i] += i
			if cnt[i] == 3:
				return Configuration.sumDie(d)
		return 0

	def scoreFourOfAKind(d):
		cnt = [0 for i in range(6)]
		sum = [0 for i in range(6)]
		for i in d:
			i = i.getRoll()-1
			cnt[i] += 1
			sum[i] += i
			if cnt[i] == 4:
				return Configuration.sumDie(d)
		return 0

	def scoreFullHouse(d):
		cnt = [0 for i in range(6)]
		for i in d:
			cnt[i.getRoll()-1] += 1
		
		if cnt.index(2) != 0 and cnt.index(3) != 0:
			return 25

		return 0

	def scoreSmallStraight(d):
		t = [i.getRoll() for i in d]
		t = list(set(t))
		t.sort()
		idx = t[0]
		cnt = 0
		for i in t:
			if i == idx:
				cnt += 1
				if cnt == 4:
					return 30
			else:
				cnt = 1
			idx = i+1
		return 0

	def scoreLargeStraitght(d):
		t = [i.getRoll() for i in d]
		t = list(set(t))
		t.sort()
		idx = t[0]
		cnt = 0
		for i in t:
			if i == idx:
				cnt += 1
				idx = i+1
				if cnt == 5:
					return 40
			else:
				cnt = 1
				idx = i
		return 0

	def scoreYahtzee(d):
		cnt = [0 for i in range(6)]
		for i in d:
			i = i.getRoll()-1
			cnt[i] += 1
		if 5 in cnt:
			return 50
		return 0

	def sumDie(d):
		t = [i.getRoll() for i in d]
		return sum(t)



class YahtzeeBoard:
	UPPERTOTAL = 6
	UPPERBONUS = 7
	LOWERTOTAL = 15
	TOTAL = 16
	dice = []
	diceButtons = []
	fields = [] #각 플레이어 점수판 2차원 리스트
				#열 플레이어, 0열=플레이어1, 1열 플레이어2,...
				#17행 점수 = 카테고리 13행 + upperScore + ..

	players = []
	numPlayers = 0
	player = 0
	round = 0 #13 라운드
	roll = 0 # 각라운드마다 3번굴리기

	def __init__(self):
 		self.initPlayers()

	def initPlayers(self): #player window $617 CH 109 / 2100
		self.pwindow = Tk()
		self.TempFont = font.Font (size=16, weight='bold', family='Consolas')
		self.label = [] 
		self.entry = []
		self.label.append(Label (self.pwindow, text="플레이어 명수", font=self.TempFont))
		self.label[0].grid(row=0, column=0)

		for i in range(1,11):
			self. label.append(Label (self.pwindow, text="플레이어"+str(i)+" 이름",font=self.TempFont))
			self. label [i].grid(row=i,column=0)
		for i in range(11):
			self.entry.append(Entry(self.pwindow, font=self. TempFont))
			self.entry[i].grid(row=i,column=1)
		Button(self.pwindow, text="Yahtzee 플레이어 설정 완료",
		 font=self.TempFont, command=self.playerNames).grid(row=11,column=0)
		self.pwindow.mainloop()

	def playerNames(self): ## 2010/ 25 HE422 4 E
		self.numPlayers = int(self.entry[0].get())
		for i in range(1, self.numPlayers+1):
			self.players.append(Player (str(self.entry[i].get())))
		self.pwindow.destroy() 
		self.initInterface() #Yahtzee SE 30/04 94 213

	def initInterface(self):
		self.window = Tk("Yahtzee Board")
		self.window.geometry("1600x800")
		self.TempFont = font.Font(size=16,weight = 'bold', family='Consolas')

		for i in range(5):
			self.dice.append(Dice())

		self.rollDice = Button(self.window, text="Roll Dice", font=self.TempFont, command=self.rollDiceListener)
		self.rollDice.grid(row=0,column = 0)

		for i in range(5):
			self.diceButtons.append(Button(self.window, text="?", font=self.TempFont, width=8, command=lambda row=i: self.diceListener(row))) # 각각의 dice 버튼에 대한 이벤트 처리 diceListenser 연결
			#람다함수를 이요해서 diceListener 매개변수 설정하면 하나의 Listener로 
			self.diceButtons[i].grid(row=i+1, column = 0)

		for i in range(self. TOTAL + 2): # i행 점수
			Label (self.window, text=Configuration.configs[i], font=self. TempFont).grid(row=i, column=1) 
			for j in range(self.numPlayers): # j열 : 플레이어
				if (i == 0): # 플레이어 이름 표시
					Label (self.window, text=self.players[j].toString(), font=self. TempFont).grid(row=i, column=2 + j) 
				else:
					if (j==0): # 각 행마다 한번씩 리스트 추가, 다중 플레이어 지원
						self.fields.append(list())
						# i-1행에 플레이어 개수 만큼 버튼 추가하고 이벤트 Listener 설정, 매개변수 설정
					self.fields [i-1].append(Button(self.window, text="", font=self. TempFont, width=8, command=lambda row=i-1: self.categoryListener (row)))
					self.fields[i-1][j].grid(row=i,column=2 + j) # +AE HEE disable 1/2
					# 누를 필요없는 버튼은 disable 시킴
					if (j != self.player or (i-1) == self. UPPERTOTAL or (i-1) == self. UPPERBONUS
						or (i-1) == self.LOWERTOTAL or (i-1) == self. TOTAL):
						self.fields [i-1][j]['state'] = 'disabled'
						self.fields[i-1][j]['bg'] = 'light gray' #상태 메시지 출력 
		self.bottomLabel=Label(self.window, text=self.players[self.player].toString()+
		"차례 : Roll Dice 버튼을 누르세요", width=35, font=self. TempFont)
		self.bottomLabel.grid(row=self. TOTAL + 2, column=0)
		self.window.mainloop()


	def rollDiceListener(self):
		for i in range(5):
			if(self.diceButtons[i]['state']!='disabled'):
				self.dice[i].rollDice() 
				self.diceButtons[i].configure(text=str(self.dice[i].getRoll()))
		if (self.roll == 0 or self.roll == 1):
			self.roll += 1 
			self.rollDice.configure(text="Roll Again")
			self.bottomLabel.configure(text="보관할 주사위 선택 후 Roll Again")
		elif (self.roll==2):
			self.bottomLabel.configure(text="카테고리를 선택하세요") 
			self.rollDice['state'] = 'disabled'
			self.rollDice[ 'bg'] = 'light gray'

		if self.round == 13:
			for i in self.fields:
				for j in i:
					j['text'] = ''
					if i == self.UPPERBONUS or i == self.UPPERTOTAL or i == self.TOTAL or i == self.LOWERTOTAL:
						continue
					j['state'] = 'active'
					j['bg'] = 'white'
			for i in self.players:
				i.clear()
			self.round = 0
			self.rollDice['text'] = 'Roll'


	def diceListener(self, row): #Dicelistener
		self.diceButtons[row]['state'] = 'disabled'
		self.diceButtons[row]['bg'] = 'light gray'

	# category부터 1열로 침
	def categoryListener (self, row): #categoryListener
		#점수 계산
		score = Configuration.score(row, self.dice) 
		index = row 
		if (row>7):
			index = row-2
		#XEL 3151 221 7 di sable 1/2 
		self.players[self.player].setScore(score, index) 
		self.players[self.player].setAtUsed( index) 
		self.fields [row][self.player].configure(text=str(score)) 
		self.fields [row][self.player]['state'] = 'disabled'
		self.fields [row][self.player]['bg'] = 'light gray'

		# UPPER category 1 W& Og Upper Score, Upper Bonus 보너스점수기록
		if (self.players[self.player ]. allUpperUsed()):
			self.fields [self. UPPERTOTAL] [self.player ]. configure(text =
				str(self.players[self.player ].getUpperScore())) 
			if (self.players[self.player].getUpperScore() > 63):
				self.fields[self. UPPERBONUS ] [self.player]. configure(text="35") #UPPERBONUS=7
				score += 35
				self.players[self.player].setScore(score, index) 
			else:
				self.fields[self. UPPERBONUS] [self.player].configure(text="0") #UPPERBONUS=7

		# LOWER category 전부 사용되었으면 LowerScore 계산
		if self.players[self.player].allLowerUsed():
			self.fields[self.LOWERTOTAL][self.player].configure(text=str(self.players[self.player].getLowerScore()))

		# UPPER category 와 LOWER category가 전부 사용되었으면 TOTAL 계산
		if self.players[self.player].allUpperUsed() and self.players[self.player].allLowerUsed():
			self.fields[self.TOTAL][self.player].configure(text=str(self.players[self.player].getTotalScore()))

		#다음 플레이어로 넘어가고 선택할 수 없는 카테고리들은 disable 시킴
		self.player = (self.player +1)%self.numPlayers
		for i in range(self.TOTAL+1):
			if i == self.UPPERBONUS or i == self.UPPERTOTAL or i == self.TOTAL or i == self.LOWERTOTAL:
				continue

			for j in range(self.numPlayers):
				if j != self.player:
					self.fields [i][j]['state'] = 'disabled'
					self.fields [i][j]['bg'] = 'light gray'
				else:
					if self.fields [i][j]['text'] != '':
						self.fields [i][j]['state'] = 'disabled'
						self.fields [i][j]['bg'] = 'light gray'
					else:
						self.fields [i][j]['state'] = 'active'
						self.fields [i][j]['bg'] = 'white'

		self.rollDice['state'] = 'active'
		self.rollDice[ 'bg'] = 'white'
		self.rollDice['text'] = 'Roll Dice'
		self.roll = 0

		print("hi",self.round)

		for i in self.diceButtons:
			i['state'] = 'active'
			i['bg'] = 'white'
			i['text'] = '?'

		if(self.player == 0):
			self.round += 1
			self.bottomLabel.configure(text=self.players[self.player].toString()+"차례"+str(self.round)+" : Roll Dice 버튼을 누르세요")
		if(self.round == 13): # 모든 버튼 초기화
			self.rollDice['text'] = 'RESET'
			self.bottomLabel.configure(text=self.players[self.player].toString()+"가 승리했습니다!")

		

YahtzeeBoard()