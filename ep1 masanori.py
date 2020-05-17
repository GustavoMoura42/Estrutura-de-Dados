import time
import random


cont = 0
def buscab(x, v):
  global cont
  e = -1
  d = len(v)
  while e < d-1:
    m = (e + d) // 2
    cont = cont + 1
    if v[m] < x:
      e = m
    else:
      d = m
  return d

def buscaseq(v, x):
  i=0
  while i < len(v):
    if v[i] == x:
      return i
    i += 1
  ##insercao
def insercao(lista):
 for j in range(1, len(lista)):
   x = lista[j]
   i = j - 1
   while i >= 0 and lista[i] > x:
     lista[i + 1] = lista[i]
     i = i - 1
   lista[i + 1] = x
 return lista

##selecao
def selecao(v):
  resp = []
  while v:
    m = min(v)
    resp.append(m)
    v.remove(m)
  return resp

##mergesort
def merge(e, d):
    r = []
    i, j = 0, 0
    while i < len(e) and j < len(d):
        if e[i] <= d[j]:
            r.append(e[i])
            i += 1
        else:
            r.append(d[j])
            j += 1
    r += e[i:]
    r += d[j:]
    return r

def mergesort(v):
    if len(v) <= 1:
        return v
    else:
        m = len(v) // 2
        e = mergesort(v[:m])
        d = mergesort(v[m:])
        return merge(e, d)

def pegaTempOrd(x,par):
  t1=time.time()
  x(par)
  t2=time.time()
  return t2-t1

def pegaTempBusca(x,par1,par2):
  t1=time.time()
  x(par1, par2)
  t2=time.time()
  return t2-t1
    
def quicksort(lista):   
    if len(lista) <= 1: 
        return lista
    
    pivô = lista[0]
    iguais  = [x for x in lista if x == pivô]
    menores = [x for x in lista if x <  pivô]
    maiores = [x for x in lista if x >  pivô]
    return quicksort(menores) + \
           iguais + quicksort(maiores)

def calcula(tempord,tamanho):
  tempo=0
  contador=0
  while (tempo<=tempord):
    y=random.randint(0,tamanho)
    tempo+=pegaTempBusca(buscaseq,l,y)-pegaTempBusca(buscab,y,listaordenada)
    contador+=1
  return contador
  
  

tamanho=0
l=[]
while(tamanho <=20000):
  tamanho+=5000
  print("\nNumero de elementos: ",tamanho)
  l+=[random.randint(0,tamanho) for x in range (tamanho)]
  listaordenada=quicksort(l)

  ## QUICKSORT // pronto
  tempord=(pegaTempOrd(quicksort, list(l)))
  print(f'QUICKSORT: {calcula(tempord,tamanho)}  ||  ORDENAÇÃO: {tempord:.3f}')

  ## INSERÇÃO  //pronto
  tempord=(pegaTempOrd(insercao, list(l)))
  print(f'INSERÇÃO: {calcula(tempord,tamanho)}  ||  ORDENAÇÃO: {tempord:.3f}')


  ## SELECAO  //pronto
  tempord=(pegaTempOrd(selecao, list(l)))
  print(f'SELECAO: {calcula(tempord,tamanho)}  ||  ORDENAÇÃO: {tempord:.3f}')

  ## MERGE  //pronto
  tempord=(pegaTempOrd(mergesort, list(l)))
  print(f'MERGESORT: {calcula(tempord,tamanho)}  ||  ORDENAÇÃO: {tempord:.3f}')








  






