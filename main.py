def a_power_b(a,b):
    acum=1
    for i in range (0,b):
        acum = i*acum
    return acum

contp=0
contim=0
conte=0

while True:
    try:
        num1=int(input("Ingrese el valor de la base: "))
        num2=int(input("Ingrese el valor del exponente: "))
        c = a_power_b(num1,num2)
        print("El resultado de elevar",num1,"a",num2,"es:",c)
        if num1==0:
            break
        print("para terminar el proceso digite 0")
        if c % 2==0:
            contp += 1
        else:
            contim += 1
    except:
        print ( "Error al ingresar un valor, por favor ingresarlos de nuevo." )
        conte  +=  1

print("PROGRAMA FINALIZO")
print ( "Se calcularon" , contim + contp , "potencias" )
print ( contp,"resultado par." )
print ( contim , "resultado impar." )
print (  conte , "errores " )

