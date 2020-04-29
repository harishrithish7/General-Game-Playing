from prepare_environment import PrepareEnvironment
from agent_env import AgentEnv
from environment import Environment

state = PrepareEnvironment()
agent = AgentEnv(name=0,posx=0,posy=0,orientation =90)
score = Environment(state=state,agent=agent)
