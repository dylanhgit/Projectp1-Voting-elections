from data import load_votes, save_votes, load_voters, save_voters

class Candidate:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.votes = 0

    def vote(self):
        self.votes += 1

class Election:
    def __init__(self):
        self.candidates = {
            1: Candidate("Dylan", 1),
            2: Candidate("Josh", 2),
            3: Candidate("Will", 3),
            4: Candidate("Colby", 4)
        }
        self.load_votes()
        self.voters = load_voters()

    def vote_for_candidate(self, candidate_id, voter_id):
        if voter_id in self.voters:
            return False
        if candidate_id in self.candidates:
            self.candidates[candidate_id].vote()
            self.voters.append(voter_id)
            self.save_votes()
            save_voters(self.voters)
            return True
        return False

    def load_votes(self):
        votes = load_votes()
        for id, vote_count in votes.items():
            self.candidates[id].votes = vote_count

    def save_votes(self):
        votes = {id: candidate.votes for id, candidate in self.candidates.items()}
        save_votes(votes)

    def get_vote_summary(self):
        return {candidate.name: candidate.votes for candidate in self.candidates.values()}
      
