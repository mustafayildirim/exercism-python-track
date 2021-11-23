class Team(object):
    def __init__(self, name):
        self.name = name
        self.mp = 0
        self.w = 0
        self.l = 0
        self.d = 0
        self.p = 0

    def __eq__(self, other):
        return self.name==other

    def __lt__(self, other):
        if self.p!=other.p:
            return self.p > other.p
        else:
            return self.name < other.name

    def __repr__(self):
        return f'{self.name:<30} |{self.mp:>3} |{self.w:>3} |{self.d:>3} |{self.l:>3} |{self.p:>3}'


def tally(tournament_results):
    league = []
    if not tournament_results:
        return output(league)
    
    for l in tournament_results:
        home, visitor, outcome = l.split(";")
        if home not in league:
            league.append(Team(home))
        if visitor not in league:
            league.append(Team(visitor))
        h = league[league.index(home)]
        v = league[league.index(visitor)]
                    
        if outcome == 'win':
            h.w += 1
            v.l += 1
        elif outcome == 'loss':
            h.l += 1
            v.w += 1
        elif outcome == 'draw':
            h.d += 1
            v.d += 1
        h.mp, h.p = h.mp+1, h.w*3 + h.d
        v.mp, v.p = v.mp+1, v.w*3 + v.d        

    return output(league)

def output(league):
    result = ["Team                           | MP |  W |  D |  L |  P"]
    for t in sorted(league):
        result.append(repr(t))
    return result
