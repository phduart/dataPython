import time 
import random
import datetime

entradaDia = datetime.timedelta(hours=9, minutes=5)
saidaAlmoco = datetime.timedelta(hours=12, minutes=5)
voltaAlmoco = datetime.timedelta(hours=13, minutes=5)
saidaDia = datetime.timedelta(hours=16, minutes=5)

def getMinutesTimeDelta(timex):
  timex = str(timex).split(":")
  return int(timex[1])

def validateRules(entrada, saida):
  while True:
    x = random.randint(0, 10)
    minutesEntrad = getMinutesTimeDelta(entrada)
    minutesSaid = getMinutesTimeDelta(saida - datetime.timedelta(minutes=x))
    if(minutesEntrad == minutesSaid or minutesEntrad+1 == minutesSaid or minutesEntrad-1 == minutesSaid
       or minutesEntrad == minutesSaid+1 or minutesEntrad == minutesSaid-1):
      continue
    else: 
      return (saida - datetime.timedelta(minutes=x))
      
def calcEntrada(entrada):
  global entradaDia
  x = random.randint(0, 10)
  entradaDia = (entrada - datetime.timedelta(minutes=x))
  return entradaDia

def calcSaidaAlmoco(saida):
  global saidaAlmoco
  global entradaDia
  saidaAlmoco = validateRules(entradaDia, saida)
  return saidaAlmoco

def calcVoltaAlmoco(volta):
  global voltaAlmoco
  global saidaAlmoco
  voltaAlmoco = validateRules(saidaAlmoco, volta)
  return voltaAlmoco

def calcSaida(saida):
  global saidaDia
  global entradaDia
  saidaDia = validateRules(entradaDia, saida)
  return saidaDia


print( "Entrada - Saida Almoço - Volta Almoço - Saída")
for i in range(0, 10):
  print(f"{calcEntrada(entradaDia)}   {calcSaidaAlmoco(saidaAlmoco)}       {calcVoltaAlmoco(voltaAlmoco)}       {calcSaida(saidaDia)}")
  entradaDia = datetime.timedelta(hours=9, minutes=5)
  saidaAlmoco = datetime.timedelta(hours=12, minutes=5)
  voltaAlmoco = datetime.timedelta(hours=13, minutes=5)
  saidaDia = datetime.timedelta(hours=16, minutes=5)
