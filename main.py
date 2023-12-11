import re
from os import system
from verifier_input import entrer_utilisateur

system("cls")
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
recuperer_chaine = ""

# chaine = ">5k <0y <3w <3k <6u <3q"
# chaine = "<14p <1v <1h >4o"
# chaine = "<1t >7h >3c <5y >13j <2c <5w >4a"
# chaine = ">3a >0a <1u <10k >1a <9j <0s <16u"
# chaine = ">1a >0a <3g <4m <3r"
chaine = entrer_utilisateur()


for item in chaine.split(" "):
    if item.startswith(">"):
        
        trouver_chiffre = re.findall("[0-9]+", item.replace(">",""))
        trouver_lettre = re.findall("[a-zA-Z]", item.replace(">",""))
        
        for i,item_1 in enumerate(alphabet):
            if item_1 == trouver_lettre[0]:                
                recuperer_chaine += alphabet[(i + int(trouver_chiffre[0]))]
            
            
    if item.startswith("<"):
        trouver_chiffre = re.findall("[0-9]+", item.replace("<",""))
        trouver_lettre = re.findall("[a-zA-Z]", item.replace("<",""))
        
        for i,item_1 in enumerate(alphabet):
            if item_1 == trouver_lettre[0]:                
                recuperer_chaine += alphabet[(i - int(trouver_chiffre[0]))]
        
print("\n", recuperer_chaine.upper(), "\n")