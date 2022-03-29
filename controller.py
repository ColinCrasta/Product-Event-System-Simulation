import time
import numpy
from model import *  # imports all methods from model.py
from testing import *  # imports all methods from testing.py


class Controller:


    def __init__(self):
        self.counter = 0
        self.bufferList = []
        self.inspectorList = []
        self.workstationList = []

        # Buffer declarations

        self.buffer1 = Buffer(1, 1)
        self.bufferList.append(self.buffer1)

        self.buffer2 = Buffer(1, 2)
        self.bufferList.append(self.buffer2)

        self.buffer3 = Buffer(2, 3)
        self.bufferList.append(self.buffer3)

        self.buffer4 = Buffer(1, 4)
        self.bufferList.append(self.buffer4)

        self.buffer5 = Buffer(3, 5)
        self.bufferList.append(self.buffer5)



        # Inspector declarations
        self.inspector1 = Inspector(1)
        self.inspectorList.append(self.inspector1)
        self.inspector1.addBuffer(self.buffer1)
        self.inspector1.addBuffer(self.buffer2)
        self.inspector1.addBuffer(self.buffer4)

        self.inspector2 = Inspector(2)
        self.inspectorList.append(self.inspector2)
        self.inspector2.addBuffer(self.buffer3)
        self.inspector2.addBuffer(self.buffer5)


        # Workstation declaration
        self.workstation1 = WorkStation(1)
        self.workstation1.addBuffer(self.buffer1)
        self.workstationList.append(self.workstation1)

        self.workstation2 = WorkStation(2)
        self.workstation2.addBuffer(self.buffer2)
        self.workstation2.addBuffer(self.buffer3)
        self.workstationList.append(self.workstation2)

        self.workstation3 = WorkStation(3)
        self.workstation3.addBuffer(self.buffer4)
        self.workstation3.addBuffer(self.buffer5)
        self.workstationList.append(self.workstation3)


        self.run()


    def run(self):

        #The amount of products the user wants before the simulation ends
        limit = int(input("Enter the amount of products you want to create: "))
        timer = 0

        #generates the components for the inspectors
        for i in self.inspectorList:
            i.generateComponent()
            i.generateServiceTime()
        print('\n')

        #Runs the simulation until the amount of products asked for the user are created
        while (self.counter < limit ):
            self.checkInspectors()
            self.checkWorkstations()
            timer += 1
            #print(self.counter)

        #print(timer)
        print("Simulation is complete as", limit, 'products have been made.')



    def checkWorkstations(self):

        #Iterates through the workstations to see if any workstations have enough components to create a product
        for work in self.workstationList:
            if (work.getWorkstationID() == 1) and (self.buffer1.getStateValue() != 3):
                #removes components from buffer and adds it to the workstation while also changing their states
                comp = self.buffer1.removeObject()
                self.buffer1.setState()
                work.addComponent(comp)
                work.setState(State.Assembling)

                print('C' + str(comp.getComponentNum()), 'has been removed from buffer 1. Buffer 1:', self.buffer1.getState())
                print('W' + str(work.getWorkstationID()), 'has removed a C1 from buffer 1. W1:', work.getState())
                print('W' + str(work.getWorkstationID()), 'has created a P1')

                #Checks if a inspector that is blocked due to a lack of open buffers needs their state changed
                if (self.inspector1.getState() == State.Blocked):
                    self.inspector1.setState(State.Not_Blocked)
                    print('Inspector 1 is not blocked anymore. Inspector 1: State.Not_Blocked')
                print('\n')

                self.counter += 1
            elif (work.getWorkstationID() == 2) and \
                (self.buffer2.getStateValue() != 3) and \
                (self.buffer3.getStateValue() != 3):

                # removes components from buffer and adds it to the workstation while also changing their states
                comp1 = self.buffer2.removeObject()
                comp2 = self.buffer3.removeObject()

                self.buffer2.setState()
                self.buffer3.setState()
                work.setState(State.Assembling)

                print('C' + str(comp1.getComponentNum()),'and C' + str(comp2.getComponentNum()),
                      'have been removed from buffer 2 and 3.', 'Buffer 2:', self.buffer2.getState(),
                      'Buffer 3:', self.buffer3.getState())
                print('W' + str(work.getWorkstationID()), 'has removed a C1 and C2 from buffer 2 and 3. W2:', work.getState())
                print('W' + str(work.getWorkstationID()), 'has created a P2')

                # Checks if a inspector that is blocked due to a lack of open buffers needs their state changed
                if (self.inspector1.getState() == State.Blocked):
                    self.inspector1.setState(State.Not_Blocked)
                    print('Inspector 1 is not blocked anymore. Inspector 1: State.Not_Blocked')

                if (self.inspector2.getState() == State.Blocked) and (self.inspector2.getComponentType() == 2):
                    self.inspector2.setState(State.Not_Blocked)
                    print('Inspector 2 is not blocked anymore. Inspector 2: State.Not_Blocked')

                print('\n')
                self.counter += 1
            elif (work.getWorkstationID() == 3) and \
                (self.buffer4.getStateValue() != 3) and \
                (self.buffer5.getStateValue() != 3):

                    # removes components from buffer and adds it to the workstation while also changing their states
                    comp4 = self.buffer4.removeObject()
                    comp5 = self.buffer5.removeObject()

                    self.buffer4.setState()
                    self.buffer5.setState()
                    work.setState(State.Assembling)


                    print('C' + str(comp4.getComponentNum()),'and C' + str(comp5.getComponentNum()),
                          'have been removed from buffer 4 and 5.', 'Buffer 4:', self.buffer4.getState(),
                          'Buffer 5:', self.buffer5.getState())
                    print('W' + str(work.getWorkstationID()), 'has removed a C1 and C3 from buffer 4 and 5. W3:', work.getState())
                    print('W' + str(work.getWorkstationID()), 'has created a P3')

                    # Checks if a inspector that is blocked due to a lack of open buffers needs their state changed
                    if (self.inspector1.getState() == State.Blocked):
                        self.inspector1.setState(State.Not_Blocked)
                        print('Inspector 1 is not blocked anymore. Inspector 1: State.Not_Blocked')

                    if (self.inspector2.getState() == State.Blocked) and (self.inspector2.getComponentType() == 3):
                        self.inspector2.setState(State.Not_Blocked)
                        print('Inspector 2 is not blocked anymore. Inspector 2: State.Not_Blocked')
                    print('\n')
                    self.counter += 1
            else:
                #If the conditions reach this point then that means their buffers are somewhat empty, so if their
                # state is "assembling" then their state needs to be changed to "idle"
                if work.getState() != State.Idle:
                    work.setState(State.Idle)
                    print('W' + str(work.getWorkstationID()), 'is set to idle')
                    print('\n')


    def checkInspectors(self):
        # Iterates through the inspectors to see if any inspectors are available
        for inp in self.inspectorList:
            if inp.getState() == State.Not_Blocked:  # Checks if inspector is not blocked
                comp = inp.getComponent()

                self.done = False
                while self.done == False:  # Loops until buffer is filled with a component

                    # i.getBufferSize() tells how many buffers a inspector can send a component to.
                    randnum = random.randint(1, inp.getBufferSize()) - 1

                    # checks if the buffer has space and if it is the same type as the component
                    if (inp.getBuffer(randnum).getState() != State.Full) and (inp.
                        getBuffer(randnum).getComponentType() == comp.getComponentNum()):

                        # adds component to the buffer and changes the state
                        inp.getBuffer(randnum).addObject(comp)
                        inp.getBuffer(randnum).setState()

                        print('Inspector', inp.getID(), ' puts C' + str(comp.getComponentNum()),
                              ' in buffer', str(inp.getBuffer(randnum).getID()) +
                              '. Buffer', str(inp.getBuffer(randnum).getID()) + ':', inp.getBuffer(randnum).getState())


                        # Checking if there are any available buffers, otherwise the inpsector will be blocked
                        inp.generateComponent()  # Generates new component
                        print('\n')

                        if inp.getID() == 1:
                            if (self.buffer1.getStateValue() == 5) and (self.buffer2.getStateValue() == 5) and (self.buffer4.getStateValue() == 5 ):
                                inp.setState(State.Blocked)
                                print('Inspector', inp.getID(), ' is blocked and has C' + str(inp.getComponentType()), )
                        elif inp.getID() == 2:
                            if (self.buffer3.getStateValue() == 5) and (inp.getComponentType() == 2):
                                inp.setState(State.Blocked)
                                print('Inspector', inp.getID(), ' is blocked and has C' + str(inp.getComponentType()), )
                            elif (self.buffer5.getStateValue() == 5) and (inp.getComponentType() == 3):
                                inp.setState(State.Blocked)
                                print('Inspector', inp.getID(), ' is blocked and has C' + str(inp.getComponentType()), )

                        self.done = True

#Generates a number based on exponential distribution in seconds
def generate_random_number(filename):
    sum = 0
    minutes_array = open(filename).read().splitlines()
    counter = 0
    while (counter < 300):
        sum += float(minutes_array[counter])
        counter += 1

    datafile_mean = sum / 300
    arr = numpy.random.exponential(datafile_mean, 1)
    return arr[0]*60

if __name__ == '__main__':

    #Instantiates the controller class to start the simulation

    controller = Controller()


