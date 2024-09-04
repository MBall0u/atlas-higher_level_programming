#!/usr/bin/python3
class candidate:
    def candidate(self, name):
        self.name = name
        self.votes = 0

class votingbooth:
    def __init__(self):
        self.candidates = []

    def add_candidate(self, candidate):
        self.candidates.append(candidate)

    def cast_vote(self, candidate):
        candidate.votes += 1
    
    def display_votes(self):
        return self.candidates

JB = candidate("Joe Byron")
DT = candidate("Donald T. Glover")
KP = candidate("Koala Paris")

new_vote = votingbooth()
new_vote.add_candidate(JB)
new_vote.add_candidate(DT)
new_vote.add_candidate(KP)

for candidate in new_vote.display_votes():
    print("Candidate: {}, Votes: {}".format(candidate.name, candidate.votes))

for i in range(100):
    new_vote.cast_vote(DT)
    if i % 2 == 0:
        new_vote.cast_vote(JB)
    if i % 3 == 0:
        new_vote.cast_vote(KP)

for candidate in new_vote.display_votes():
    print("Candidate: {}, Votes: {}".format(candidate.name, candidate.votes))