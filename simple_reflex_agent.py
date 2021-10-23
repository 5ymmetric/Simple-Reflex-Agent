# Author : Karthik Reddy Pagilla

class Agent:
    def __init__(self, initial_location):
        self.location = initial_location
        self.performace = 0
        self.actions = []
    
    def agent_function(self, percept):
        status = percept[1]
        location = percept[0]

        if (status == 'Dirty'):
            self.actions.append('Suck')
            return 'Suck'
        elif (location == 'A'):
            self.actions.append('Right')
            return 'Right'
        else:
            self.actions.append('Left')
            return 'Left'

class Environment:
    def __init__(self, agent, state):
        self.agent = agent
        self.state = state

    def percept(self, agent):
        return (agent.location, self.state[agent.location])

    def is_goal(self):
        if ((self.state['A'] == 'Clean') and (self.state['B'] == 'Clean')):
            return True
        else:
            return False

    def action(self):
        agent = self.agent
        percept = self.percept(agent)
        action = agent.agent_function(percept)

        if (action == 'Suck'):
            self.state[agent.location] = 'Clean'
        elif (action == 'Right'):
            agent.location = 'B'
        elif (action == 'Left'):
            agent.location = 'A'

        agent.performace += -1

    def run(self):
        step = 0
        while (step < 1000):
            if (self.is_goal()):
                break
            self.action()
            step += 1

def run_all_scenarios():
    scenario_counter = 1
    initial_state = {'A' : 'Dirty', 'B' : 'Dirty'}
    agent = Agent('A')
    
    print("="*50)
    print()

    while(scenario_counter < 9):
        print("Initial State: ", end="")
        print(initial_state)
        print("Agent Location: ", end="")
        print(agent.location)

        environment = Environment(agent, initial_state)
        environment.run()

        print()
        print("Action Sequence: ", end="")
        print(agent.actions)
        print()
        print("Performace Measure: ", end="")
        print(agent.performace)

        print()
        print("="*50)
        print()

        scenario_counter += 1

        if (scenario_counter % 2 == 0):
            agent = Agent('B')
            environment = Environment(agent, initial_state)
        else:
            agent = Agent('A')
            environment = Environment(agent, initial_state)

        if (scenario_counter < 3):
            initial_state = {'A' : 'Dirty', 'B' : 'Dirty'}
        elif (scenario_counter < 5):
            initial_state = {'A' : 'Dirty', 'B' : 'Clean'}
        elif (scenario_counter < 7):
            initial_state = {'A' : 'Clean', 'B' : 'Dirty'}
        else:
            initial_state = {'A' : 'Clean', 'B' : 'Clean'}

run_all_scenarios()