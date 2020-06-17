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
    rate[name]= price
    items.append(name)

def getStock(name):
    '''This function returns available stock of item'''
    print(stock[name]+' available')

def setStock(name,newStock):
    name=name.title()
    global stock
    stock[name]=newStock

def getRate(name):
    '''This function returns available stock of item'''
    itemRate=str(rate[name])
    print(itemRate+' Rs only')

#Boutique

    
#Mens Collection
def getMensCollection():
    '''This function returns men's collection'''
    print(mensCollection)

def getMensPrice(name):
    '''This function returns available stock of item'''
    price=str(mensPrice[name])
    print(price+' Rs')

def getMensSize(name):
    '''This function returns available stock of item'''
    print(mensSize[name]+' size(s) available')

def addMensCollection(name,price):
    global mensPrice
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
    price=str(womensPrice[name])
    print(price+' Rs')

def getWomensSize(name):
    '''This function returns available stock of item'''
    print(womensSize[name]+' size(s) available')

def addWomensCollection(name,price):
    global womensPrice
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
stock={'Chicken Biryani':'50 kg','Beef Biryani':'50 kg'}

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
    print('Which records you want to see??')
    print('(1) Employee')
    print('(2) Catreen')
    print('(3) Boutique')
    print('If you want to exit press 0')
    print()
    choice=int(input('Enter the number of your choice: '))
    if choice==1:

    elif choice==2:

    elif choice==3:

    else choice==4:
        break
               



