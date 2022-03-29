import enum
import random
from controller import *  # imports all methods from controller.py
from enum import Enum


# Every possible state for the inspector, buffer, and workstation is in this class
class State(Enum):
    # Inspector States
    Blocked = 1
    Not_Blocked = 2
    Inspecting = 8

    # Buffer states
    Empty = 3
    Half_Full = 4
    Full = 5

    # Workstation states
    Assembling = 6
    Idle = 7


#Generic class for Inspector objects
class Component:

    def __init__(self, num):

        if num == -1:
            self.componentNum = random.randint(2, 3)  # component objects are randomly chosen with a random component number
        else:
            self.componentNum = num  # overrides object with a specified component number

    def getComponentNum(self):
        return self.componentNum

    def __str__(self):
        return "C" + str(self.componentNum)  # prints object's state as component number


#Generic class for Inspector objects
class Inspector:


    # The comp variable will be generated using generateComponent()
    def __init__(self, inspectorid):
        # Which types of components the Inspector can inspect
        self.bufferTypes =[]
        self.state = State.Not_Blocked
        self.inspectorID = inspectorid
        self.serviceTime = 0

        if self.inspectorID == 1:
            self.bufferTypes.append(1)
        elif self.inspectorID == 2:
            self.bufferTypes.append(2)
            self.bufferTypes.append(3)

        self.bufferList = []            #Which specific buffer objects an inspector can send components to



    def setState(self, newState):
        self.state = newState;

    def getState(self):
        return self.state

    #generates a service time
    def generateServiceTime(self, filename):
        self.serviceTime = generate_random_number(filename)

    def decrementServiceTime(self):
        self.serviceTime -= 1

    def getServiceTime(self):
        return self.serviceTime

    #creates a component object to inspect
    def generateComponent(self):

        if self.inspectorID == 1:
            self.comp = Component(1)
        elif self.inspectorID == 2:
            self.comp = Component(-1)

        print(self.__str__())

    def getID(self):
        return self.inspectorID

    def getComponent(self):
        return self.comp

#The type of component the inspector is currently handling
    def getComponentType(self):
        return self.comp.getComponentNum()

    def setComponent(self, component):
        self.comp = component;

    def addBuffer(self, buffer):

        self.bufferList.append(buffer)

    def getBuffer(self, index):

        return self.bufferList[index]

    def getBufferList(self):

        return self.bufferList

    def getBufferSize(self):

        return len(self.bufferList)

    def __str__(self):
        return "Inspector " + str(self.inspectorID) + " is working on: " + self.comp.__str__()



#Generic class for Inspector objects
class Buffer:


    # Input for componentType is a number between 1 and 3 to show which component this buffer will holds
    #The buffer variable will be filled using addObject()
    def __init__(self, componentType, id):
        self.state = State.Empty
        self.componentType = componentType
        self.ID = id
        self.buffer = []                    #Actual buffer to hold the component objects


    def getState(self):
        return self.state

    def getStateValue(self):
        return self.state.value

#Sets the state based on the size of the buffer list
    def setState(self):
        if len(self.buffer) == 0:
            self.state = State.Empty
        elif len(self.buffer) == 1:
            self.state = State.Half_Full
        elif len(self.buffer) == 2:
            self.state = State.Full

    def getComponentType(self):
        return self.componentType

    def bufferSize(self):
        return len(self.buffer)

    def addObject(self, component):
        self.buffer.append(component)

    def removeObject(self):
        return self.buffer.pop(0)

    def getID(self):
        return self.ID

    def __str__(self):
        return "Buffer state is " + str(self.state) + " and contains component type " + str(self.componentType)



#Generic class for Inspector objects
class WorkStation:


    # The comp variable will be filled using the addComponent() function
    # The buffers variable will be filled using the addBuffer() function
    def __init__(self, workstationid):
        self.buffers = []                           #Which buffers the workstation can take components from
        self.state = State.Idle
        self.workstationID = workstationid
        self.serviceTime = 0

        # generates a service time
    def generateServiceTime(self, filename):
        self.serviceTime = generate_random_number(filename)

    def decrementServiceTime(self):
        self.serviceTime -= 1

    def getServiceTime(self):
        return self.serviceTime

    def setState(self, newState):
        self.state = newState;

    def getState(self):
        return self.state

    def getWorkstationID(self):
        return self.workstationID

    def removeComponent(self):
        return self.comp

    def addComponent(self, component):
        self.comp = component;

    def addBuffer(self, buffer):
        self.buffers.append(buffer)

    def getBuffer(self):
        return self.buffers

    def __str__(self):
        return "Workstation " + self.workstationID + " is working on: " + self.comp.__str__()



