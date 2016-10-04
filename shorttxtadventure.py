
from Tkinter import *
import tkMessageBox

class Room():
        def __init__(self,text="placeholder", list=[],accessible = 0):
            self.description = text
            self.roomcontents = list
            self.accessible = accessible

class Item():
        def __init__(self,text="Placeholder", quest=0, appearance="none",gettable=0):
            self.name= text
            self.puzzlenumber = quest
            self.look = appearance
            self.gettable = gettable
       
class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.player()
        self.itemplacer()
        self.housebuilder()
        self.interface()
        self.mainloop()
        

    def player(self):
        list1 = []
        self.playerlocation = 0
        self.playerinventory = list1
    
    def itemplacer(self):
        Shiny = Item("Something Shiny",2,"It's really hard to tell from here. Looks preeeeetttty shiny though. Maybe you should get it down somehow.",0)
        Key = Item("Key",0,"A small brass key",0)
        Lock = Item("Lock",0,"A rusty old lock",0)
        Fish = Item("Fish",1,"A very smelly red Herring",1)
        Microwave = Item("Microwave",1,"A Microwave. It's got a popcorn setting. What else do you need?",0)
        self.kitchenlist=[Shiny,Lock,Key,Microwave,Fish]
        
        
        Book = Item("Book",99,"It seems like it's bound in some sort of leather... Is it... Is it human flesh? The cover is embossed with the title: The Tome of Stupidity.",1)
        self.librarylist=[Book]
        
        
        Plunger = Item("Plunger",2,"A standard plunger. Wooden dowel handle. Rubber... plunge? Is that part called a plunge? Oh well. Only slightly used.",1)
        Mirror = Item("Mirror",98,"It could use some windex. Your beautiful mug still reflects at you. Wow. So beautiful.",0)
        Toilet = Item("Toiler",97,"The ol' throne. It's not clogged. Don't even think about it.",0)
        self.lavatorylist=[Plunger,Mirror,Toilet]
       
    
        Cards = Item("Cards",400, "A deck of Hoyle playing cards. The Queens are all missing.",1)
        Board = Item("Dart Board",401,"A well worn Dart Board. No darts in sight or you'd take a break and have a game.",0)
        self.parlorlist = [Cards,Board]
        
        Pillow = Item("Pillow",600, "A purple velvety throw pillow. So velvety.",1)
        self.masterlist = [Pillow]
        
        Spork = Item("Spork",200,"A titanium spork from what you're sure is the Star Trek Collector's Series.",1)
        self.dininglist = [Spork]
        
        Clock = Item("Clock",300,"A Cuckoo Clock of unknown origins. It doesn't seem to be working anymore.",0)
        self.guestlist = [Clock]
        
        Desk = Item("Desk",200,"A nice cherry desk. It has a very tempting locked drawer that's rather loose. If only you could pry it open",0)
        Drill = Item("Drill",100,"A full charged cordless drill. How convenient.",1)
        self.officelist = [Desk,Drill]
        
        Bust = Item("Bust",100,"It appears to be a bust of Friedrich Nietzche. Heavy. Marble. Probably good for smashing things. It's attached to the pedestal it's on really well though and the whole business is bolted down.",1)
        Door = Item("Basement Door",500,"The door to the basement is of very solid constuction. You'll need something really heavy to smash through it.",0)
        self.entrywaylist = [Bust,Door]
        
       
    def showinventory(self):
        itemnames=[]
        x = len(self.playerinventory)
        for i in range (x):
            itemnames.append(self.playerinventory[i].name)
        tkMessageBox.showinfo("Inventory", itemnames)
        print "Inventory"
    
    def movewest(self):
        target = self.houselist[self.playerlocation-1]
        if self.playerlocation in (0,3,6):
            tkMessageBox.showinfo("Sorry","You run into the wall. It hurts a bit")
        elif target.accessible ==0:
            tkMessageBox.showinfo("Sorry","You can't go that way yet.")
        else:
            self.playerlocation = self.playerlocation - 1
            self.text.delete(1.0,END)
            self.text.insert(INSERT,self.getdescription())
            
    def movenorth(self):
        target = self.houselist[self.playerlocation+3]
        if self.playerlocation in (2,6,7,8):
            tkMessageBox.showinfo("Sorry","You can't go that way!")
        elif target.accessible ==0:
            tkMessageBox.showinfo("Sorry","You can't go that way yet.")
        else:
            self.playerlocation = self.playerlocation + 3
            self.text.delete(1.0,END)
            self.text.insert(INSERT,self.getdescription())
    
    def moveeast(self):
        target = self.houselist[self.playerlocation+1]
        if self.playerlocation in (2,5,8):
            tkMessageBox.showinfo("Sorry","You can't walk through walls and the windows are shut tight!")
        elif target.accessible ==0:
            tkMessageBox.showinfo("Sorry","You can't go that way yet.")
        else:
            self.playerlocation = self.playerlocation + 1
            self.text.delete(1.0,END)
            self.text.insert(INSERT,self.getdescription())
    
    def movesouth(self):
        target = self.houselist[self.playerlocation-3]
        if self.playerlocation in (0,1,2,4,5):
            tkMessageBox.showinfo("Sorry","You can't go that way!")
        elif target.accessible ==0:
            tkMessageBox.showinfo("Sorry","You can't go that way yet.")
        else:
            self.playerlocation = self.playerlocation - 3
            self.text.delete(1.0,END)
            self.text.insert(INSERT,self.getdescription())
            
    def housebuilder(self):
        kitchen = Room("You're in the kitchen. It's pretty snazzy with travertine floors and an island in the middle, full range and everything. There's some stainless steel appliances and a nice looking microwave in particular. On the island there's a red fish of some sort. And out of the corner of your eye, up high, on top of a shelf and just out of reach there's something shiny. The door to your north is locked tight but there's a doorway to the east wide open.",self.kitchenlist,1)
        library = Room("You're surrounded by books. Floor to ceiling on every wall. There's one of those slidey ladders like you see in movies and a fancy leather chair for sitting in with a pipe and a brandy. On a pedestal there's a lone book. Worth a look-see perhaps? Besides the way you came there's a door open to the east.",self.librarylist,1)
        lavatory = Room("It's your typical creepy bathroom. Some cobwebs. A toilet. A Plunger. A mirror. Some funny writing on the ground. Probably just an Elder Sign or some other symbol meant to conjure Cthulhu. The only exit is the way you came.", self.lavatorylist,1)
        parlor = Room("Ah the parlor. Where Colonel Mustard with the revolver, oh wrong game. There's a Piano and liquor cabinet, sadly devoid of liquor? There's a dart board and a deck of playing cards in one corner. To the north is a rather pointless room. To the east is a good place to sleep.",self.parlorlist,0)
        master = Room("There's a fancy king-sized here with all the posh accessories one would expect in a quasi-haunted house. There's an especially nice pillow. Back west is the parlor, to the east is a large bright room. So inviting. To the north you hear a humming.",self.masterlist,1)
        dining = Room("The first thing you notice is the opulence of the chandelier and the ridiculously long table. The next thing you notice is the conspicuous spork at the lordly seat at the end of the table.",self.dininglist,1)
        guest = Room("This is clearly the guest room. There's a sign on the wall that says guest room. Also there's what must be a horribly obnoxious cuckoo clock on the wall.",self.guestlist,1)
        office = Room("There's an ominous crack of thunder and lightning flashes through the windows as you enter. There's a printer and 286 here and a whole stack of the old continuous paper for the printer. Nightmares of papercuts from pulling the sides off come back suddenly. The desk on which the computer sits is very handsome.",self.officelist,1)
        entryway= Room("You find yourself in the entray way to the house opposite from the corner where you entered. There's a door here that certainly leads outside and another that leads deeper into the bowels of this awful, yet relatively cozy home. You can hear Julio's pained croaks from behind the basement door, but it's locked! You must get to him.",self.entrywaylist,1)
        self.houselist = [kitchen,library,lavatory,parlor,master,dining,guest,office,entryway]
        
        
    def puzzlesuccess(self,solution):
        if solution == 0:
            tkMessageBox.showinfo("Something's changed","The door to the North is now unlocked!")
            self.houselist[3].accessible = 1
            self.houselist[0].description = "The smell of fish has become oppressive in the kitchen and the travertine floors have lost their charm. You feel the need to move on, and in a hurry. A room beckons from the north while the evil knowledge of the library still awaits you to the east."
            self.text.delete(1.0,END)
            self.text.insert(INSERT,self.getdescription())
        elif solution == 1:
            tkMessageBox.showinfo("Success?","Mmmmm Hot Herring")
        elif solution == 2:
            tkMessageBox.showinfo("That's using your noggin!","You whack at the top of the shelf and the shiny object comes flying down. It's a key.")
            self.playerinventory.append(self.kitchenlist[2])
            del self.kitchenlist[2]
        elif solution == 200:
            tkMessageBox.showinfo("Aye Captain","The spork wedges perfectly into the drawer. A little pressure and it comes sliding right out revealing a drill.")
            self.houselist[7].description = "The printer and the 286 are witnesses to your violation of the desk. The drill awaits. To the west is still that pointless room. To the south, well let's just not worry about it. To the east you can hear the croaking of Julio."
            self.text.delete(1.0,END)
            self.text.insert(INSERT,self.getdescription())
            self.officelist[1].gettable=1
        elif solution == 100:
            tkMessageBox.showinfo("Power Tools!","There's a flurry of dust but you get the bust off the pedestal in no time.")
            self.entrywaylist[0].puzzlenumber = 500
            self.entrywaylist[0].gettable = 1
        elif solution == 500:
            tkMessageBox.showinfo("You win. Kinda","You bash Nietzsche through the door. Your route to the basement is open finally. As you're about to descend into the dark and rescue Julio the front door flies open behind you. It's the police. They arrest you on the spot for breaking and entering and you spend the night in jail. You know better...")
            self.quit()
        else:
            pass
        
    def lookat(self):
        list=[]
        objlist=[]
        target = self.houselist[self.playerlocation]
        items = target.roomcontents
        
        x = len(items)
        y = len(self.playerinventory)
        
        
        for i in range (x):
            list.append(items[i].name)
            objlist.append(items[i])
        for i in range (y):
            list.append(str(self.playerinventory[i].name))
            objlist.append(self.playerinventory[i])
            
        if str(self.lookat.get()) in list:
            z = list.index(str(self.lookat.get()))
            tkMessageBox.showinfo("A gander:",objlist[z].look)
        else:
            tkMessageBox.showinfo("Why?","Surely you have better things to do.")
            
    def use(self):
        list=[]
        objlist=[]
        target = self.houselist[self.playerlocation]
        items = target.roomcontents
        
        x = len(items)
        y = len(self.playerinventory)
        
        
        for i in range (x):
            list.append(items[i].name)
            objlist.append(items[i])
        for i in range (y):
            list.append(str(self.playerinventory[i].name))
            objlist.append(self.playerinventory[i])
            
        
        string = str(self.use.get())
        stringtwo = str(self.usewith.get())
        if string in list and stringtwo in list:
            a = list.index(string)
            b = list.index(stringtwo)
            if objlist[a].puzzlenumber == objlist[b].puzzlenumber:    
                tkMessageBox.showinfo("Success!","That was dangerous but it worked.")
                self.puzzlesuccess(objlist[a].puzzlenumber)
                if objlist[a] in self.playerinventory:
                    z= self.playerinventory.index(objlist[a])
                    del self.playerinventory[z]
                else: 
                    z = self.playerinventory.index(objlist[b])
                    del self.playerinventory[z]
            else:
                tkMessageBox.showinfo("Sorry.","You can't do that")
        else:
            tkMessageBox.showinfo("Sorry.","You can't do that")
            
    def get(self):
        target = self.houselist[self.playerlocation]
        item = target.roomcontents
        x = len(item)
        targetlist=[]
        currentitems =[]
        for i in range (x):
            targetlist.append(item[i].name)
        y = len(self.playerinventory)
        for i in range(y):
            currentitems.append(self.playerinventory[i].name)
        if str(self.get.get()) in currentitems:
            tkMessageBox.showinfo("What?","You already have that! So greedy.")
        else:
            if str(self.get.get()) in targetlist:
                i= targetlist.index(str(self.get.get()))
                if str(self.get.get()) in str(item[i].name) and item[i].gettable==1:
                    self.playerinventory.append(item[i])
                    tkMessageBox.showinfo("Success","You got the %s" % str(item[i].name))
                    del self.houselist[self.playerlocation].roomcontents[i]  #Removes item from room
                else:
                    tkMessageBox.showinfo("Failure","Why would you want to get that? Weirdo...")
            else: 
                tkMessageBox.showinfo("Failure","You can't pick that up or it's not here.")
      
    def help(self):
        tkMessageBox.showinfo("Help?","The game is pretty simple. Put two  words (First letter capitalized) into the two boxes after the use button, hit the button, and you'll use the items together if you can. Enter a word and hit 'get' or 'look at' and you'll pick up an item or get an item description if available. You need to combine the right items to progress. Find your frog!")
        
    def getdescription(self):
        target = self.houselist[self.playerlocation]
        return target.description
    
    def interface(self):
        m1 = PanedWindow(orient=HORIZONTAL)
        m1.grid()
        m2 = PanedWindow(orient=HORIZONTAL)
        m2.grid()
        m3 = PanedWindow()
        m3.grid()
        
        
    
        self.text = Text(self, wrap=WORD)
        self.text.insert(INSERT,self.getdescription())
        self.text.update_idletasks()
        self.text.pack()
       
       
        
        usebutton = Button(text="Use", command = self.use)
        usebutton.grid(row=0,column=0)
        self.use = Entry(self,bd=5)
        self.use.grid(row=0,column=1)
        usewithlable = Label(self,text="with")
        self.usewith = Entry(self,bd=5)
        usewithlable.grid(row=0,column=2)
        self.usewith.grid(row=0,column=3)
        getbutton = Button(text="Get", command = self.get)
        getbutton.grid(row=1,column=0)
        self.get = Entry(self,bd=5)
        self.get.grid(row=1,column=1)
        lookatbutton = Button(text ="Look at", command = self.lookat)
        lookatbutton.grid(row=2,column=0)
        self.lookat = Entry(self,bd=5)
        self.lookat.grid(row=2,column=1)
    
        
        
        inventory = Button(text="Inventory", command = self.showinventory)
        inventory.grid()
        
        help = Button(text="Help", command = self.help)
        help.grid()
        
        movementw = Button(text="West", command = self.movewest)
        movementn = Button(text="North", command = self.movenorth)
        movements = Button(text="South", command = self.movesouth)
        movemente = Button(text="East", command = self.moveeast)
        movementw.grid()
        movementn.grid()
        movements.grid()
        movemente.grid()
        
        
        m1.add(self.text)
        m2.add(usebutton)
        m2.add(self.use)
        m2.add(usewithlable)
        m2.add(self.usewith)
        m2.add(getbutton)
        m2.add(self.get)
        m2.add(lookatbutton)
        m2.add(self.lookat)
        m2.add(inventory)
        m2.add(help)
        m3.add(movementw)
        m3.add(movementn)
        m3.add(movements)
        m3.add(movemente)
        tkMessageBox.showinfo("The Skinny", "Your pet frog Julio leapt away from you on one of your nightly walks. Unfortunately, he seemed to make his way straight into the creepy old hosue at the end of the street. Undaunted, you went around back and found a door that was so conveniently unlocked. Find Julio and get out!")
        
def main():
  
  game = App()
  
  

main()