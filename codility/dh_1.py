from typing import List, Text


class NoAgentFoundException(Exception):
    pass


class Agent(object):
    def __str__(self) -> str:
        return "<Agent: {}>".format(self._name)

    def __init__(self, name: str, skills: List, load: int):
        self.name: str = name
        self.skills: List[str] = skills
        self.load: int = load


class Ticket(object):
    def __init__(self, id: int, restrictions: List):
        self.id: int = id
        self.restrictions: List = restrictions


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        return [agent for agent in agents if agent.load < 3]

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NotImplemented


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        avaliable_agents: List[Agent] = self._filter_loaded_agents(agents)
        if avaliable_agents:
            return sorted(avaliable_agents, key=lambda agent: agent.load)[0]
        raise NoAgentFoundException()


class LeastFlexibleAgent(FinderPolicy):
    
    def _filter_skills_not_available_agents(self, ticket: Ticket, agents: List[Agent]) -> List[Agent]:
        ret = []
        for agent in agents:
            if all(
                True if restriction in agent.skills else False
                for restriction in ticket.restrictions
            ):
                ret.append(agent)
        return ret

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        available_agents: List[Agent] = self._filter_skills_not_available_agents(ticket, agents)
        available_agents: List[Agent] = self._filter_loaded_agents(available_agents)

        if available_agents:
            return sorted(available_agents, key=lambda agent: (len(agent.skills), agent.load))[0]
            
        raise NoAgentFoundException()
