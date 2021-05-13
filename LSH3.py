class Bird:
    name = ''
    height = 0
    weight = 0
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight
    def printInfo(self):
        print('Info: ', self.name, self.height, self.weight)
    def breathing():
        print('Im breathing')
    def moving():
        print('Im moving')
    def drinking(self):
        print('Im drinking')
        self.weight+=1
    def dieing():
        m=random(1,5)
        if m==1:
            print('You died because of disease')
        if m==2:
            print('You died because of old age')
        if m==3:
            print('You died because of hunger')
        if m==4:
            print('You died because of thirst')
        if m==5:
            print('You died because of randomness')

class Swimming(Bird):
    oxygen=0
    def __init__(self,name,height,weight,oxygen):
        Bird.__init__(self,name,height,weight)
        self.oxygen=oxygen
    def printInfo(self):
        print('Info: ', self.name, self.height, self.weight, self.oxygen)
    def swimming():
        print('Im swimming')
    def diving(self):
        print('Im diving')
        self.oxygen-=1
        if self.oxygen==0:
            print('You died because of lack of oxygen')
            del self.name
    def eating(self):
        print('Im eating small fishes,seaweeds,worms and insects')
        self.weight+=1

class Wading(Bird):
    def eating(self):
        print('Im eating insects,worms and plants')
        self.weight+=1

class Landing(Bird):
    def eating(self):
        print('Im eating insects, worms,plants,seeds and berries')
        self.weight+=1
    def running():
        print('Im running')
        
class Raptors(Bird):
    speed=0
    def __init__(self,name,height,weight,speed):
        Bird.__init__(self,name,height,weight)
        self.speed=speed
    def printInfo(self):
        print('Info: ', self.name, self.height, self.weight, self.speed)
    def eatbird(self, eatingLanding):
        self.weight+=eatingLanding.weight
        if speed==0:
            print('You died because of crash')

class Scanning(Bird):
    def scanning():
        print('Im scanning')
    def eating(self):
        print('Im eating insects, worms,plants,seeds and berries')
        self.weight+=1
        
class Singing(Bird):
    singsong=0
    def __init__(self,name,height,weight,singsong):
        Bird.__init__(self,name,height,weight)
        self.singsong=singsong
    def printInfo(self):
        print('Info: ', self.name, self.height, self.weight, self.singsong)
    def singing():
        if singsong==0:
            print('I cant sing as my singsong is out')
        else:
            print('Im singing')
            singsong-=1
    def eating(self):
        print('Im eating insects, worms,plants,seeds and berries')
        self.weight+=1

swimming=[]
wading=[]
landing=[]
raptors=[]
scanning=[]
singing=[]
k=int(input('Enter needed number of birds'))
for l in range (0,k+1):
    question=input('Choose which bird you want:Swimming, Wading, Landing, Raptors, Scanning, Singing')
    n=input('Enter name')
    h=int(input('Enter height'))
    w=int(input('Enter weight'))
    if question=='Swimming':
        o=int(input('Enter level of oxygen'))
        swimming.append(Swimming(n,h,w,o))
    if question=='Wading':
        wading.append(Wading(n,h,w))  
    if question=='Landing':
        landing.append(Landing(n,h,w))
    if question=='Raptors':
        s=int(input('Enter speed'))
        raptors.append(Raptors(n,h,w,s))
    if question=='Scanning':
         scanning.append(Scanning(n,h,w))
    if question=='Singing':
         s=int(input('Enter singsong'))
         singing.append(Singing(n,h,w,s))
for i in range (0,len(swimming)):
    swimming[i].printInfo()
for i in range (0,len(wading)):
    wading[i].printInfo()
for i in range (0,len(landing)):
    landing[i].printInfo()
for i in range (0,len(raptors)):
    raptors[i].printInfo()
for i in range (0,len(scanning)):
    scanning[i].printInfo()
for i in range (0,len(singing)):
    singing[i].printInfo()
landing[0].drinking()
landing[0].printInfo()
swimming[0].diving()
swimming[0].printInfo()