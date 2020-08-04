
class Poll:
    def __init__(self, poll_q, vote_option_list):
        self.poll_q = poll_q
        self.vote_option_list = vote_option_list
        # generating a dictionary with the options to vote (keys) and reset the number of votes to zero
        count_list = [0 for n in range(len(self.vote_option_list))]
        self.votes_dict = {k: v for k, v in zip(self.vote_option_list, count_list)}
        print(f'New poll question: {self.poll_q}, vote options: {vote_option_list}')

    def vote(self, vote):
        # updating our vote dictionary according to the inputted votes
        for n in self.votes_dict:
            if vote == n:
                self.votes_dict[n] += 1

    def add_option(self, option):
        # adds a vote option
        self.vote_option_list.append(option)
        return self.vote_option_list

    def remove_option(self, option):
        # removes a vote option
        self.vote_option_list.append(option)
        return self.vote_option_list

    def get_votes(self):
        # giving us the current situation of the poll votes
        return self.votes_dict

    def get_winner(self):
        winner = max(self.votes_dict.items(), key=lambda x: x[1])[0]
        return winner

    def __str__(self):
        return f'the poll question was {self.poll_q}'


def cast_multiple_votes(poll, votes):
    # pushing votes one by one to our vote function
    for vote in votes:
        poll.vote(vote)


bridge_question = Poll('What is your favourite colour?', ['Blue', 'Yellow'])
cast_multiple_votes(bridge_question, ['Blue', 'Blue', 'Yellow'])
print(bridge_question.get_winner() == 'Blue')
