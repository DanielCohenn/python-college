class Poll:
    def __init__(self, question: str, options):
        """
        Take the poll question and the poll options that were given
        and putting them in a nested dicts
        example: {question: x, options: {A: 0, B: 0}}
        starting our options value from zero because no votes were given
        """
        self.poll_results = {"question": question, "options": {i: 0 for i in iter(options)}}

    def vote(self, vote_option: str):
        """
        The vote_option function takes votes from a given list one after the other
        with a function called cast_multiple_votes (line 47)
         """
        if vote_option in self.poll_results["options"]:
            self.poll_results["options"][vote_option] += 1
        else:
            print("option is not valid")

    def add_option(self, new_option: str):
        # Adding a poll option if the given new_option is not already there
        if not new_option in self.poll_results["options"]:
            self.poll_results["options"].update({new_option: 0})

    def remove_option(self, remove_option: str):
        # Removing a poll option from the options dict
        if remove_option in self.poll_results["options"]:
            del (self.poll_results["options"][remove_option])
        else:
            print("option is not valid")

    def get_votes(self):
        """
        The function get_votes takes the current situation of the poll
        according to the number of votes that were given to each option from
        the start to time we used that function, the function displaying the poll option and the
        number of votes in a list of tuples form when the option that came on top is displayed first
         """
        votes = []
        results = dict(self.poll_results["options"])
        print(results)
        while results.keys():
            votes.append(results.popitem())
        votes.sort(key=lambda tup: tup[1])
        votes.reverse()
        print(votes)
        return votes

    def get_winner(self):
        # Returning the winning poll option
        winner = self.get_votes()[0]
        return winner[0]


def cast_multiple_votes(poll: str, votes: list):
    # casting votes in a str form one after the other from a list of votes
    for vote in votes:
        poll.vote(vote)


"""
input/output example: 
bridge_question = Poll('What is your favourite colour?', ['Blue', 'Yellow'])
cast_multiple_votes(bridge_question, ['Blue', 'Blue', 'Yellow'])
bridge_question.get_winner() ==> output: 'Blue'
bridge_question.get_votes() ==> output: [('Blue', 2), ('Yellow', 1)]
"""
