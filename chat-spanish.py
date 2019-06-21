print ("Iniciar chat con el chatbot")
#s = statement
#first question response
#print("s="+"")

s=""
while s=="":
    s = raw_input("Dice Hola a el chatbot!")

input_response=[("Hola","Hola, que tal? Me llamo Sara, y tu?"),("hola","Hola, que tal? Me llamo Sara, y tu?"),
("Hola, que tal?","Hola, que tal? me llamo Sara, y tu?"),("hola, que tal?","Hola, que tal? Me llamo Sara, y tu?"),
("Hola, que tal? Como te llama?","Hola, que tal? Me llamo Sara, y tu?"),
("hola, que tal? Como te llama?","Hola, que tal? Me llamo Sara, y tu?"),
("Hola, Como estas?","Hola, que tal? Me llamo Sara, y tu?"),("hola, Como estas?","Hola, que tal? Me llamo Sara, y tu?"),
("Hola, como es cosas con vos? Como te llama?","Hola, que tal? Me llamo Sara, y vos?"),
("Hola, como es cosas con vos? Como te llama?","Hola, que tal? Me llamo Sara, y vos?"),
("Hola, que tu haces con tu tiempo libero?",
 "Pues, hago bailar, salir con mis amigos y escuchar musica, y leer tambien y tu?"),
("hola, que tu haces con tu tiempo libero?",
 "Pues, hago bailar, salir con mis amigos y escuchar musica, y leer tambien y tu?"),
("Hola, pasa contigo?","No mucho, solo aqui escuchando musica."),("hola, pasa contigo?","No mucho, solo aqui escuchando musica.")]

outputted=False
for pair in input_response:
    if pair[0] == s:
        outputted=True
        print(pair[1])
if not outputted:
    print("Perdon, no entiendo.")

#if s == "Hola":
    #print("Hola, que tal? Me llamo Sara, y tu?")#
#elif s == "hola":#or"hola!":
    #print("Hola, que tal? Me llamo Sara, y tu?")#
#elif s == "Hola, que tal?":
 #   print("Hola, que tal? Me llamo Sara, y tu?")
#elif s == "hola que tal?":
    #print("Hola, que tal? Me llamo Sara, y tu?")#
#elif s == "hola, que tal? Como te llama?":
 #   print("Hola, que tal? Me llamo Sara, y tu?")#
#elif s == "hola, Como estas?":
 #   print("Hola, que tal? Me llamo Sara, y tu?")#--
#elif s == "hola, como es cosas con vos? Como te llama?":
  #  print("Hola, que tal? Me llamo Sara, y vos?")#--
#elif s == "Hola, que tu haces con tu tiempo libero?":
 #   print("Pues, hago bailar, salir con mis amigos y escuchar musica, y leer tambien y tu?")#--
#elif s == "Hola, que pasa contigo?":#or"Hola que pasa contigo?":
   # print("No mucho, solo aqui escuchando musica.")
#else:
  #  print("Perdon, no entiendo.")
#2nd input from user
y = raw_input()
#import string import random y = string.ascii_letters name = str(input("me llamo"))
#if len(y)>len("Me llamo ") and (y[0:len("Me llamo ")]=="Me llamo " or y[0:len("Me llamo ")]=="me llamo "):
if y == "Me llamo"or "me llamo":#,name:
    print("Ay, que bonito!")
elif y == "me llamo":
    print("Ay, que bonito!")
elif y == "Que tipo musica te gusta?":
    print("Pues, me gusta muchos tipos de musica. Reggaeton, Salsa, Merengue, un poco de todo, y a ti? jajajaja")
elif y == "Cuanto anos tienes?":
    print("Tengo veintiuno anos, y ti?")
elif y == "que tu haces con tu tiempo libero?": #or "Que tu haces con tu tiempo libero?":
    print("Pues, hago bailar, salir con mis amigos y escuchar musica, y leer tambien y tu?")
elif y == "Haces bailar? Porque escuchas Salsa":
    print("No mucho ahora, no tengo mucho tiempo con mi curso y mi trabajos pero cuando puedo salgo bailando con mis amigos. Amo bailar!")
elif y == "haces bailar?" or "haces bailar, porque escuchas Salsa":
    print("No mucho ahora, no tengo mucho tiempo con mi curso y mi trabajos pero cuando puedo salgo bailando con mis amigos. Amo bailar! Y ti? Haces bailar?")
else:
    print("Perdon, no entiendo.")
k = raw_input()
if k == "que tu haces con tu tiempo libero?"or"Que tu haces con tu tiempo libero?":
    print("Pues, hago bailar, salir con mis amigos y escuchar musica, y leer tambien y tu?")
elif k == "Haces bailar?"or"Haces bailar? porque escuchas Salsa.":
    print("No mucho ahora, no tengo mucho tiempo con mi curso y mi trabajos pero cuando puedo salgo bailando con mis amigos. Amo bailar!")

j = raw_input()
#import string import random y = string.ascii_letters name = str(input("me gusta"))
if j == "Me gusta hacer":#name
    print("que genial, me gustaria hacer mas deportes en el futuro. Cuando tengo tiempo.")
elif j == "Puedo veer un foto de tu?":
    print("No")
elif j ==  "Adios":
    print("Adios")
else:
    print("Perdon, no entiendo.")

l = raw_input()
if l =="Hablas algo ingles?":
    print("No mucho, puedes me ayudar? Mi nivel es muy bajo")
else:
    print("Perdon, no entiendo.")
s = raw_input("Dice Hola a el chatbot!")

#y = (string.ascii_letters)
#y = import string(raw_input("Me llamo es",y))
#if  name == "Me llamo es" name:
 #  print(name"Ay, que bonito!")
   #"Me gusta"
   #"Hago"
