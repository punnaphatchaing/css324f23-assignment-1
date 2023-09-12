import water3 as problem
import utils
import ucs

state = (8,0,0)

goal_node, n_visits = ucs.uniform_cost_graph_search(problem)
if goal_node is not None:
    print("")
    print("Solution")
    print("========")
    utils.print_solution(goal_node)
    problem.successors(state)
    print("========")
    print("Path cost = %d" % goal_node[3])
    print("Number of Visited States = %d" % n_visits)
else:
    print("No solutions found")
