#Employee
def getBasicSalary(name):
    name=name.title()
    print(basicSalary[name])

def getNetSalary(hours,basicSalary):
    '''This function takes overtime hours
    and basic salary of employee and return
    total salary''' 
    print(hours*overTimeRate +basicSalary)

def getOverTimeRate():
    '''This function returns overtime rate'''
    print(overTimeRate)

def getEmployeeList():
    print(listOfEmployee)

def setBasicSalary(name,newBasicSalary):
    name=name.title()
    global basicSalary
    basicSalary[name]= newBasicSalary
    
def addEmployee(name,salary):
    global basicSalary
    name=name.title()
    basicSalary[name]= salary
    listOfEmployee.append(name)
    
def setOverTimeRate(newOverTimeRate):
    '''This will take a new overtime hour (in numbers)'''
    global overTimeRate
    overTimeRate = newOverTimeRate

#Catreen
def getItem():
    '''This function returns items available'''
    print(items)

def addItem(name,price):
    global rate
    name=name.title()
    rate[name]= price
    items.append(name)

def getStock(name):
    '''This function returns available stock of item'''
    name=name.title()
    stockOfName=str(stock[name])
    print(stockOfName+' kg available')

def setStock(name,newStock):
    name=name.title()
    global stock
    stock[name]=newStock

def getRate(name):
    '''This function returns available stock of item'''
    name=name.title()
    itemRate=str(rate[name])
    print(itemRate+' Rs only')

#Boutique

    
#Mens Collection
def getMensCollection():
    '''This function returns men's collection'''
    print(mensCollection)

def getMensPrice(name):
    '''This function returns available stock of item'''
    name=name.title()
    price=str(mensPrice[name])
    print(price+' Rs')

def getMensSize(name):
    '''This function returns available stock of item'''
    name=name.title()
    print(mensSize[name]+' size(s) available')

def addMensCollection(name,price):
    global mensPrice
    name=name.title()
    mensPrice[name]= price
    mensCollection.append(name)

def setMensSize(name,sizes):
    name=name.title()
    global mensSize
    mensSize[name]=sizes

def setMensPrice(name,price):
    name=name.title()
    global mensPrice
    mensPrice[name]=price

#Womens Collection
def getWomensCollection():
    '''This function returns men's collection'''
    print(womensCollection)

def getWomensPrice(name):
    '''This function returns available stock of item'''
    name=name.title()
    price=str(womensPrice[name])
    print(price+' Rs')

def getWomensSize(name):
    '''This function returns available stock of item'''
    name=name.title()
    print(womensSize[name]+' size(s) available')

def addWomensCollection(name,price):
    global womensPrice
    name=name.title()
    womensPrice[name]= price
    womensCollection.append(name)

def setWomensSize(name,sizes):
    name=name.title()
    global womensSize
    womensSize[name]=sizes

def setWomensPrice(name,price):
    name=name.title()
    global womensPrice
    womensPrice[name]=price








#Employee
listOfEmployee=['Ali','Ahmed']
basicSalary={'Ali':12000,'Ahmed':10000}
overTimeRate= 50

#Catreen
items=['Chicken Biryani','Beef Biryani']
rate={'Chicken Biryani':100,'Beef Biryani':150}
stock={'Chicken Biryani':50,'Beef Biryani':50}

#Boutique
mensCollection=['Shalwar Qameez','Kurta','Unstitched']
mensPrice={'Shalwar Qameez':3000,'Kurta':1000,'Unstitched':2000}
mensSize={'Shalwar Qameez':'All','Kurta':'Small and Medium'}
womensCollection=['Shalwar Qameez','Emboided kurtis',\
                  'Bridal dress','Unstiched']
womensPrice={'Shalwar Qameez':3000,'Emboided kurtis':5000,\
             'Bridal dress':50000,'Unstiched':2000}
womensSize={'Shalwar Qameez':'Medium and large',\
            'Emboided kurtis':'Medium and large',\
             'Bridal dress':'Medium and large'}


#Loop
while True:
    print()
    print('Which records you want to see??')
    print('(1) Employee')
    print('(2) Catreen')
    print('(3) Boutique')
    print('Press 0 to exit program')
    print()
    choice=int(input('Enter the number of your choice: '))
    if choice==1:
        while True:
            print()
            print('Ok! What you want to do?')
            print("(1) Employee's name?" )
            print("(2) Wanna add any employee?" )
            print("(3) Wanna see basic salary of any employee?" )
            print("(4) Wanna see overtime rate of employee?" )
            print("(5) Wanna change overtime rate of employee?" )
            print("(6) Want to calculate net salary of any employee?" )
            print('Press 0 to exit Employee')
            print()
            eChoice= int(input('Enter number of the operation you want to perform: '))
            if eChoice==1:
                getEmployeeList()
            elif eChoice==2:
                name=input('Write name of employee: ')
                salary=int(input('Write basic salary of employee: '))
                addEmployee(name,salary)
            elif eChoice==3:
                name=input('Write name of employee: ')
                getBasicSalary(name)
            elif eChoice==4:
                getOverTimeRate()
            elif eChoice==5:
                newOverTimeRate=int(input('Enter new overtime rate: '))
                setOverTimeRate(newOverTimeRate)
            elif eChoice==6:
                hours=int(input('Enter number of overtime hours: '))
                basicSalary=int(input('Enter basic Salary: '))
                getNetSalary(hours,basicSalary)
            elif eChoice==0:
                break
    elif choice==2:
        while True:
            print()
            print('Ok! What you want to do?')
            print("(1) Available items" )
            print("(2) Stock of any item" )
            print("(3) Add an item" )
            print("(4) Edit stock of an item" )
            print("(5) Rate of any item" )
            print('Press 0 to exit Catreen')
            print()
            cChoice= int(input('Enter number of the operation you want to perform: '))
            if cChoice==1:
                getItem()
            elif cChoice==2:
                name=input('Enter name of item: ')
                getStock(name)
            elif cChoice==3:
                name=input('Enter name of item: ')
                price=int(input('Enter price of  item: '))
                addItem(name,price)
            elif cChoice==4:
                name=input('Enter name of item: ')
                newStock=int(input('Enter new stock: '))
                setStock(name,newStock)
            elif cChoice==5:
                name=input('Enter name of item: ')
                getRate(name)
            elif cChoice==0:
                break
    elif choice==3:
        print()
        print('Do you want to see..')
        print(" (1) Men's collection")
        print(" (2) Women's collection")
        print('Press 0 to exit Boutique')
        print()
        bChoice= int(input('Enter number of the operation you want to perform: '))
        while True:
            if bChoice==1:
                while True:
                    print()
                    print('Ok! What you want to do?')
                    print("(1) Men's collection" )
                    print("(2) Price of a collection" )
                    print("(3) Available sizes of a collection" )
                    print("(4) Add a collection" )
                    print("(5) Edit available sizes of a collection" )
                    print("(6) Edit price of a collection" )
                    print("Press 0 to exit Men's collection")
                    print()
                    mChoice= int(input('Enter number of the operation you want to perform: '))
                    if mChoice==1:
                        getMensCollection()
                    elif mChoice==2:
                        name=input('Enter name of collection: ')
                        getMensPrice(name)
                    elif mChoice==3:
                        name=input('Enter name of collection: ')
                        getMensSize(name)
                    elif mChoice==4:
                        name=input('Enter name of collection: ')
                        price=int(input('Enter price of collection: '))
                        addMensCollection(name,price)
                    elif mChoice==5:
                        name=input('Enter name of collection: ')
                        sizes=input('Enter all available sizes')
                        setMensSize(name,sizes)
                    elif mChoice==6:
                        name=input('Enter name of collection: ')
                        price=int(input('Enter new price of collection: '))
                        setMensPrice(name,price)
                    elif mChoice==0:
                        break
            elif bChoice==2:
                while True:
                    print()
                    print('Ok! What you want to do?')
                    print("(1) Women's collection" )
                    print("(2) Price of a collection" )
                    print("(3) Available sizes of a collection" )
                    print("(4) Add a collection" )
                    print("(5) Edit available sizes of a collection" )
                    print("(6) Edit price of a collection" )
                    print("Press 0 to exit Women's collection")
                    print()
                    wChoice= int(input('Enter number of the operation you want to perform: '))
                    if wChoice==1:
                        getWomensCollection()
                    elif wChoice==2:
                        name=input('Enter name of collection: ')
                        getWomensPrice(name)
                    elif wChoice==3:
                        name=input('Enter name of collection: ')
                        getWomensSize(name)
                    elif wChoice==4:
                        name=input('Enter name of collection: ')
                        price=int(input('Enter price of collection: '))
                        addWomensCollection(name,price)
                    elif wChoice==5:
                        name=input('Enter name of collection: ')
                        sizes=input('Enter all available sizes')
                        setWomensSize(name,sizes)
                    elif wChoice==6:
                        name=input('Enter name of collection: ')
                        price=int(input('Enter new price of collection: '))
                        setWomensPrice(name,price)
                    elif wChoice==0:
                        break
            elif bChoice==0:
                break
    elif choice==0:
        break
               



