import operator
#cd C:\Users\marte\AppData\Local\Programs\Python\Python37/
#m= [input('Введите симлекс-таблицу: ')]
m=[2,-2,5,0,1,-2,1,1,-2,1,1,-1]

S=m[:4]
x1=m[4:8]
x2=m[8:12]
x3=m[::4]
x4=m[1::4]
x5=m[2::4]

def negativeElementSearch (S):
	i = 0
	while i<len(S):
		if S[i]<0:
			return(i)
			break
		i+=1
def oneStepJardanException (m,ik,rk,rj):
	# ik*=-ik/rk
	#x1 разреш. столб
	ik_=[-ik/rk for ik in ik[:]]
	# rk*=1/rk
	#разреш.эл-т
	rk_=1/rk
	# rj*=rj/rk
	#x4 разреш. стр
	rj_=[rj/rk for rj in rj[:]]
	# ij*=ij-ik*rj/rk
	i=0
	for m[i] in m[:4]:
		m[i]=m[i]-ik[i]/rk*rj[0]
		i+=1
	i=8
	for m[i] in m[8:12]:
		m[i]=m[i]-ik[i-8]/rk*rj[2]
		i+=1
	i=4
	for m[i] in ik_:
		m[i]=ik_[i-4]
		i+=1
	m[1::4]=rj_[:]	
	m[ik.index(rk)+4]=rk_  #index столб
	return m

try:
	if S[negativeElementSearch(S)]:
		print('В столбце свободных членов есть отрицательный ('+str(S[negativeElementSearch(S)])+'), указывающий на недопустимое решение: x1=x2=0, x3=' + str(int(S[0]))+', x4='+str(int(S[1]))+', x5='+str(int(S[2]))+' и F='+str(int(S[3])))		
except TypeError:
	print('В столбце свободных членов нет отрицательных')

if x1[negativeElementSearch(S)] < 0:
	print('Разрешающий столбец найден: x1. Найдем минимальное положительное отношение элемента свободных членов S к соответствующем элементу в разрешающем столбце.')
	k={'0':int(S[0]/x1[0]),'1':int(S[1]/x1[1]),'2':int(S[2]/x1[2])}
	k=sorted(k.items(),key=operator.itemgetter(1))

	#Проверка на положительность
	i=0
	k__=[]
	while i<3:
		k_=k[i]
		k_=k_[1]
		if int(k_) >0:
			k__.append(tuple(k[i]))
		i+=1
	k=list(k__)

	k=k[0]
	
	if int(k[0])==0:
		print('x3 - разрешающая строка')
	elif int(k[0])==1:
		print('x4 - разрешающая строка')
		rk=x4[int(k[0])]
		print(str(rk)+' - разрешающий элемент')
		print ('Заменим базис, поменяв местами переменные x4 и x1, используя один шаг жордановых исключений.')
		m = oneStepJardanException(m,x1,rk,x4)
		print('Получим преобразованную симплекс-таблицу: '+str(m))
	elif int(k[0])==2:
		print('x5 - разрешающая строка')
elif x2[negativeElementSearch(S)] < 0:
	print('Разрешающий столбец найден: x2.')
	# Копипаст
	print(rk)

S=m[:4]
S_=m[:3]
x4=m[4:8]
x2=m[8:12]
x3=m[::4]
x1=m[1::4]
x5=m[2::4]
F=m[3::4]

if (negativeElementSearch(S_) == None):
	if(negativeElementSearch(F) != None):
		print('Так как все элементы столбца S, кроме коэффициента целевой функции, неотрицательны, имеем опорное решение: x4=x2=0, x3='+str(int(x3[0]))+', x1='+str(int(x1[0]))+', x5='+str(int(x5[0]))+'. Целевая функция F='+str(int(F[0])))
		
if x4[negativeElementSearch(S)] > 0:
	print('Разрешающий столбец найден: x4. Найдем минимальное положительное отношение элемента свободных членов S к соответствующем элементу в разрешающем столбце.')
	k={'0':int(S[0]/x4[0]),'1':int(S[1]/x4[1]),'2':int(S[2]/x4[2])}
	k=sorted(k.items(),key=operator.itemgetter(1))
	
	#Проверка на положительность
	i=0
	k__=[]
	while i<3:
		k_=k[i]
		k_=k_[1]
		if int(k_) >0:
			k__.append(tuple(k[i]))
		i+=1
	k=list(k__)

	k=k[0]
	if int(k[0])==0:
		print('x3 - разрешающая строка')
		rk=x3[1]
		print(str(rk)+' - разрешающий элемент')
		print ('Заменим базис, поменяв местами переменные x3 и x4, используя один шаг жордановых исключений')
		m = oneStepJardanException(m,x4,rk,x3)
		print('Получим преобразованную симплекс-таблицу: '+str(m))
	elif int(k[0])==1:
		print('x1 - разрешающая строка')
	elif int(k[0])==2:
		print('x5 - разрешающая строка')
elif x2[negativeElementSearch(S)] > 0:
	print('Разрешающий столбец найден: x2.')
	# Копипаст
