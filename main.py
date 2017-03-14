from cubes import *
p = Cubes();
def h1(n): #heuristic function depending on how many cubes are not in the position they should be
    error_cube_no=0
    current_state=n.state
    gstate=p.goal #get the current and the goal state and save them in two new variables
    L1=[] #convert them in lists of lists so we can make any changes we want
    L2=list(current_state)
    for x in L2:
        y=list(x)
        L1.append(y)
    L3=[]
    L4=list(gstate)
    for x in L4:
        y=list(x)
        L3.append(y)
    #L1 and L3 are Lists of lists that store the Current and the Goal state
    while L1 != []:
        i=L1.pop()
        j=L3.pop() #Each time ,remove the position of each last cube in the two lists and compare them
        #if they are not the same,that means that the cube is not where it should be so raise the error_cube_no
        if i != j:
            error_cube_no=error_cube_no+1
    return error_cube_no  #Return the sum of the position_errors of the cubes
        

def calculate_distance(L,y):  #a function to check the distance of a cube from the top cube of its stack (USED FOR H2 FUNCTION)
    x=y
    len1=0
    count=0
    while 1:
        for s in L: #take a cube's position(let's call it current cube)
            if s[1] == x: # if x is the cube that it's below the current cube
                    x=s[0]  #then make x our current cube and raise the len_counter
                    len1=len1+1
                    count=0
                    break
            else:
                count=count+1 #if x is not the cube that it's below the current cube , continue
                continue
        if count == 5 or count >5: #if there are no more cubes on top , break
            break
    return len1 #return the distance

def h2(n): #heuristic function that calculates the distance from a cube at the current state to the same cube at the goal state
    current_state=n.state
    gstate=p.goal #get the current and the goal state and save them in two new variables
    L1=[] #convert them in lists of lists so we can make any changes we want
    L2=list(current_state)
    for x in L2:
        y=list(x)
        L1.append(y)
    L3=[]
    L4=list(gstate)
    for x in L4:
        y=list(x)
        L3.append(y)
    #L1 and L3 are Lists of lists that store the Current and the Goal state
    el=len(L1)
    sum1=0
    for x in range(1,el+1): #for each cube that we have
        i=calculate_distance(L1,x) #calculate distance in the current state from cube X to the top of its stack
        j=calculate_distance(L3,x) #calculate distance in the goal state from cube X to the top of its stack
        res=i+j
        sum1=sum1+res+1 #sum1 is the total distance from cube x(current state) to cube x(goal state)
    return sum1


s=astar_search(p,h1)
sol=s.solution()
path=s.path()
print "Solution: \n+{0}+\n|Action\t|State\t	\t|Path Cost |\n+{0}+".format('-'*42)
for i in range(len(path)) :
	state = path[i].state
	cost = path[i].path_cost
	action = " "
	if i > 0 : # The initial state has not an action that results to it
		action = sol[i-1]
	print "|{0}\t|{1} \t|{2} \t |".format(action, state, cost)
print "+{0}+".format('-'*42)
