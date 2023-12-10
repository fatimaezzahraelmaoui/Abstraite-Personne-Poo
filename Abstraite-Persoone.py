
from abc import (ABCMeta, abstractmethod)
class Personne:
    nb = 0
    def __init__(self,nom,prenom,age):
        self.__Nom = nom
        self.__Prenon = prenom
        self.__Age = age
        self.__Code = Personne.nb
        Personne.nb += 1
    
    def getNom(self):
        return self.__Nom
    def setNom(self,nom):
        self.__Nom = nom
    
    def getPrenom(self):
        return self.__Prenon
    def setPrenom(self,prenom):
        self.__Prenon = prenom
    
    def getAge(self):
        return self.__Age
    def setAge(self,age):
        self.__Age = age
    
    def getCode(self):
        return self.__Code
    
    @abstractmethod
    def ToString(self):
        pass
    def Equals(self):
        pass

class Employe(Personne):
    nb = 0
    def __init__(self,nom,prenom,age,garde):
        super().__init__(nom,prenom,age)
        self.__Nom = nom
        self.__Prenon = prenom
        self.__Age = age
        self.__Code = Employe.nb
        Employe.nb += 1
        
        self.__Garde = garde
    
    def getGarde(self):
        return self.__Garde
    def setGarde(self,garde):
        self.__Garde = garde
    
    def ToString(self):
        return("votre Nom :",self.__Nom,"votre Prenom :",self.__Prenon ,
        "votre Code :",self.__Code,"votre Age :",self.__Age,"votre Garde :",self.__Garde)
        
    def Equals(self,code):
        if self.__Code == code :
            return True
        else:
            return False

class Eleve(Personne):
    nb = 0
    def __init__(self,nom,prenom,age,niveau,moyenne):
        super().__init__(nom,prenom,age)
        self.__Nom = nom
        self.__Prenon = prenom
        self.__Age = age
        self.__Code = Eleve.nb
        Eleve.nb += 0
        self.__Niveau = niveau
        self.__Moyenne = moyenne
        
    def getNiveau(self):
        return self.__Niveau
    def setNiveau(self,niveau):
        self.__Niveau = niveau
    def getMoyenne(self):
        return self.__Moyenne
    def setMoyenne(self,moyenne):
        self.__Moyenne = moyenne
    
    def ToString(self):
        return("votre Nom :",self.__Nom,"votre Prenom :",self.__Prenon,"votre Code :",self.__Code ,
        "votre Age :",self.__Age,"votre Niveau :",self.__Niveau,"votre Moyenne :",self.__Moyenne)
        
    def Equals(self,code):
        if self.__Code == code :
            return True
        else:
            return False
    
EM1= Employe("sara","elhassni",20,1)
print(EM1.ToString())
EM1.setNom("hafssa")
print(EM1.Equals(3))
print(EM1.nb)

S1 = Eleve("kawtar","soltane",19,"DEV102",17)
S2 = Eleve("sara","amrani",20,"bac",17)
S3 = Eleve("kawtar","khalil",23,"infirmiére",17)
S1.setAge(19)
print(S1.ToString())
print(S1.nb)
print(S2.ToString())
print(S2.nb)
print(S3.ToString())
print(S3.nb)