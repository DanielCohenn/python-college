
class Poll:
    def __init__(self, question: str, options):
        self.poll_results = {"question": question, "options": {i: 0 for i in iter(options)}}

    def vote(self, vote_option: str):
        if vote_option in self.poll_results["options"]:
            self.poll_results["options"][vote_option] += 1
        else:
            print("option is not valid")

    def add_option(self, new_option: str):
        if not new_option in self.poll_results["options"]:
            self.poll_results["options"].update({new_option: 0})

    def remove_option(self, remove_option: str):
        #add if
        del(self.poll_results["options"][remove_option])

    def get_votes(self):
        votes = []
        results = dict(self.poll_results["options"])
        while results.keys():
            votes.append(results.popitem())
        votes.sort(key=lambda tup: tup[1])
        votes.reverse()
        return votes

    def get_winner(self):
        winner = self.get_votes()[0]
        return winner[0]


def cast_multiple_votes(poll, votes):
    for vote in votes:
        poll.vote(vote)


