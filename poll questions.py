
class Poll:
    def __init__(self, poll_q, vote_option_list):
        self.poll_q = poll_q
        self.vote_option_list = vote_option_list
        count_list = []
        for n in range(len(self.vote_option_list)):
            count_list.append(0)
        self.votes_dict = {k: v for k, v in zip(self.vote_option_list, count_list)}
        print(f'New poll question: {self.poll_q}, vote options: {vote_option_list}')

    def vote(self, vote):
        for n in self.votes_dict:
            if vote == n:
                self.votes_dict[n] += 1

    def add_option(self, option):
        self.vote_option_list.append(option)
        return self.vote_option_list

    def remove_option(self, option):
        self.vote_option_list.append(option)
        return self.vote_option_list

    def get_votes(self):
        return self.votes_dict

    def get_winner(self):
        winner = max(self.votes_dict.items(), key=lambda x: x[1])[0]
        return winner

    def __str__(self):
        return f'the poll question was {self.poll_q}'


def cast_multiple_votes(poll, votes):
    for vote in votes:
        poll.vote(vote)


bridge_question = Poll('What is your favourite colour?', ['Blue', 'Yellow'])
cast_multiple_votes(bridge_question, ['Blue', 'Blue', 'Yellow'])
print(bridge_question.get_winner() == 'Blue')