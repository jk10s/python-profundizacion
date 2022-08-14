import random

def generar():

    mayusculas = ["A","B","C","D","E","F","G"]
    minusculas = ["a","b","c","d","e","f","g"]
    simbolos = ["#","$","%","&"]
    numeros =["1","2","3","4","5","6","7","8","9"]

    caracteres= mayusculas+minusculas+simbolos+numeros
    contra=[]
    for i in range(15):
        caracteresrandom=random.choice(caracteres)
        contra.append(caracteresrandom)
    contra="".join(contra)
    return contra

    
def main():
    contrase = generar()
    print(contrase)
    
if __name__ == '__main__':
    main()
