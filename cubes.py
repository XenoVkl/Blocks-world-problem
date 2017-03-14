from search import * # This file imports utils.py so it should be in the same folder
import sys # System-specific parameters and functions


class Cubes(Problem):
    #Derived class of search.problem
    #Each state is represented as a tuple of tuples
    #Each inner tuple represents a position of a cube
    #depending on the number of cubes(let's say we have n cubes) we have n inner tupples(first tupple -> posision of cube 1(A) , second tupple ->position of cube 2(B) ....)
    #(e.g : (1,2) means that cube 1(A) is on top of cube 2(B) -- (3,0) means that cube 3(C) is on the table -- (4,3) means that cube 4(D) is on top of cube 3(C)...
    def __init__(self):
            super(Cubes,self).__init__(((1,2),(2,3),(3,0),(4,5),(5,0)),((1,0),(2,0),(3,4),(4,0),(5,1)))
            #for the example with 5 cubes we have cube 1 on cube 2(A on B),cube 2 on cube 3(B on C),cube 3 on the table(C on table),cube 4 on cube 5(D on E),cube 5 on the table(E on table)
            #goal_State- 1(A) on the table,2(B) on the table,3(C) on 4(D),4(D) on the table,5(E) on 1(A) ///(also make sure to check the .txt file for more info about the program)
			#so we have 1 as A , 2 as B ,3 as C, 4 as D, 5 as E , 6 as F etc....
			#for the actions we need to know that (1,2) means 1 on 2(put A on B) -- (3,0) means 3 on table(put C on the table) etc...
			#Please first check the actions function and then the __isvalid function
    def __isValid(self,state,action):
        i=0
        k=len(state)
        for s in state:
            if s[1]==0:   #check how many cubes are on the table
                i=i+1  
        if i==k:  #if all the cubes are on the table and the action is to put one cube on the table ,return False
            if action[1]==0:
                return False
                
                
        invalid=0 #just an invalid_counter (if the at end of this function invalid is not 0 then return False else return True
        for s in state:
            if s == action: #make sure not to make a move that will give you a state that you already were in(e.g (a,b) -> place a on b again -> (a,b))
                return False
            if(s[1]==action[0]): #if the cube we want to move is not the top of its "stack" then that is an invalid action so raise the invalid_counter
                invalid=invalid+1
            if(s[1]==action[1] and s[1]!= 0): #if we want to place a cube on top of another cube and that cube is not the top of its "stack" ,then that is an invalid
                #action so raise the invalid_counter (note : this applies to all cubes and not zero(table) because there are probably free spots in the table to place the cube)
                invalid=invalid+1
        if invalid != 0: #if invalid > 0 return False else True
            return False
        else:
                return True
            

    def actions(self,state):
        #possible actions - Each cube can be placed on another cube or on the table [e.g : (1,2) = place 1(A) on 2(B) -- (4,0) = place 4(D) on the table]
        l=len(state)
        l=l+1
        possibleActions=[]
        for x in range(1,l): #put every possible action in a list of tuples..Each action will be a tuple(1st item in the tuple is the cube that we want to place on top of the 2nd item of the tuple which is another cube or the table)
            for y in range (0,l):
                if y !=x: #dont include actions such as(1,1)=A on A ,(2,2)=B on B etc --we just need to place a cube on another cube or the table
                    tup=(x,y) #create the tuple(action) and put it in the list of all possible actions
                    possibleActions.append(tup)
        validActions = [] #empty list at first where we will store all the validActions -> final list = list of tuples
        for possibleAction in possibleActions: #for each possible action(tuple) in the possibleActions list check if every action is valid by using the __isValid function
            if self.__isValid(state,possibleAction) == True : #check which actions in the possibleActions list are valid and place them on the validActions list
                validActions.append(possibleAction)
        return validActions #return the list of all the valid actions

    def result(self,state,action):
        state2=[] 
    #we will convert the state in a list of lists(state2)
        for k in state:
            j=list(k)
            state2.append(j)
    #Depending on the action,make the necessary changes
        for s in state2:
            if s[0]==action[0]: #find the cube  that we want to change its position
                s[1]=action[1] #change the cube that it had the other cube on top of it (e.g. we have (1,2)= 1 on 2 and an action (1,4) = place 1 on 4 --- after the changes (1,2) will become (1,4))
                break
        state3=[] #convert again the list of lists into a tuple of tuples(the original type)
        for x in state2:
            k = tuple(x)
            state3.append(k)
        state4=tuple(state3)
        return state4 #return that state(type : tuple of tuples)
    #those changes were made in order to avoid any problems with the functions of class Problem


            




    
            
    
