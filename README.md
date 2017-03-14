# Blocks-world-problem
Solution to the blocks world problem(AI) using Python(version 2.7)

-----------------
PROBLEM STATEMENT
-----------------
The blocks world is one of the most famous planning domains in artificial intelligence. Let's say that we have a number of uniform blocks(cubes) and they can all be placed on a table. Each block is placed on another block or on the table(free block). There is only one action available for the agent to solve the problem : either place a block that doesn't have other blocks stacked on top of it on another block with the same behaviour, or on the table. The initial and the goal state are described by the exact position of each block. The cost of each action(moving a block) is 1. A solution to the blocks world problem is a sequence of actions that allows us to start from an initial state and end up to a goal state. Therefore, the optimal solution is the solution with the minimum cost (or else the minimum actions required to get from the initial state to the goal state).

---------------------------------------
Using Algorithm A* to solve the problem
---------------------------------------
A* is an informed search algorithm, or a best-first search, meaning that it solves problems by searching among all possible paths to the solution (goal) for the one that incurs the smallest cost (least distance travelled, shortest time, etc.), and among these paths it first considers the ones that appear to lead most quickly to the solution. It is formulated in terms of weighted graphs: starting from a specific node of a graph, it constructs a tree of paths starting from that node, expanding paths one step at a time, until one of its paths ends at the predetermined goal node.

At each iteration of its main loop, A* needs to determine which of its partial paths to expand into one or more longer paths. It does so based on an estimate of the cost (total weight) still to go to the goal node. Specifically, A* selects the path that minimizes

   f(n) = g(n) + h(n)

where n is the last node on the path, g(n) is the cost of the path from the start node to n, and h(n) is a heuristic that estimates the cost of the cheapest path from n to the goal. The heuristic is problem-specific. For the algorithm to find the actual shortest path, the heuristic function must be admissible, meaning that it never overestimates the actual cost to get to the nearest goal node.

Typical implementations of A* use a priority queue to perform the repeated selection of minimum (estimated) cost nodes to expand. This priority queue is known as the open set or fringe. At each step of the algorithm, the node with the lowest f(x) value is removed from the queue, the f and g values of its neighbors are updated accordingly, and these neighbors are added to the queue. The algorithm continues until a goal node has a lower f value than any node in the queue (or until the queue is empty).[a] The f value of the goal is then the length of the shortest path, since h at the goal is zero in an admissible heuristic.

The algorithm described so far gives us only the length of the shortest path. To find the actual sequence of steps, the algorithm can be easily revised so that each node on the path keeps track of its predecessor. After this algorithm is run, the ending node will point to its predecessor, and so on, until some node's predecessor is the start node.

------
States
------
The basic idea of finding a solution to this problem is first of all a good representation of a state. The state is represented
by the exact positions of the blocks(some are free on the table while others are on top of a block etc). In python, I represented the state as a tuple of tuples where the inner tuples represent the position of a cube. For example, if our state is the following tuple of tuples -> ((1,2),(2,3),(3,0),(4,5),(5,0)) , the information that we acquire from that, is that block 1 is on top of block 2, block 2 is on top of block 3, block 3 is on the table, block 4 is on top of block 5 and block 5 is on the table. If we want to associate that with the example of the picture, let's say that block 1 = A, block 2 = B, block 3 = C, block 4 = D, block 5 = E (also table = 0).

-------
Actions
-------
The actions that I used , are inside a list of tuples(named PossibleActions) where each tuple represents an action. The first member of the tuple represents the block that is about to move, and the second member of the tuple represents the block(or table) that will have the block(first member of the tuple) stacked on top of it. For example, if PossibleActions = [(1,2),(3,0)]
that means that we have 2 actions : the first action will move block 1 on top of block 2 and the second action will move block 3 on the table. Each action(tuple) inside the PossibleActions list, is checked by an IsValid function that returns true if the action is valid or else false(e.g : you cannot move a block that has other blocks stacked on top of it). After that, we have
a list of all the valid actions(list of tuples) and we are ready to move on and apply those actions to a state.

-------------------
Heuristic Functions
-------------------
I used two heuristic functions :

H1 : checks how many blocks have different positions comparing the state that we are in the node and the Goal State(basically how many blocks are NOT where they should be in the current node-state). H1 is admissible because it never overestimates the cost of reaching the goal and is also consistent because for every node N and each successor P of N, the estimated cost of reaching the goal from N is no greater than the step cost of getting to P plus the estimated cost of reaching the goal from P.

H2: Manhattan distance

Of those two, heuristic function H1 seemed to be giving better results and by that I mean less explored nodes, therefore, less execution time


