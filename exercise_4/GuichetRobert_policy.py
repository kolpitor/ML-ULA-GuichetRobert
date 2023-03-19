from agent import Agent
import numpy as np

def GuichetRobert_policy(agent: Agent) -> str:
    """
    Policy of the agent
    return "left", "right", or "none"
    """
    actions = ["left", "right", "none"]

    #Get agents variables
    pos = agent.position
    known = agent.known_rewards

    """
    The agent gets rewarded every frame it stands on a reward tile
    so our stochastic policy is to have it move randomly as long as it's
    not standing on a reward tile

    The policy isn't far fetch but its use of randomness to act makes it a
    stochastic search policy
    """

    #Check if the agent is already standing on a reward
    if known[pos] != 0:
        #If it's on a reward let it stand there as long as the reward doesn't disapear
        index = 2
    else:
        #If it's not then move the agent in a random direction (i.e. left or right)
        index = np.random.randint(2)
        
    action = actions[index]
    
    assert action in actions
    return action