# College-Projects
Repository theme: college projects writen in Python 3


## First project: "FourierSeries"
In this project I took 2 different time domain signals, first signal is a hat funciton with a global maximum of 1 
and the second signal is a step function with 1 as the constant value, and than we comput the fourier series of those signals
and plot how those signals can be represented with a fourier series.

libraries used: numpy, matplotlib.pyplot, matplotlib.cm

* first section - defining our time domain and its bounderis.
* second section - defining our hat and step function as explained above.
* third section - computing our fourier series for both the hat and rectangular functions.

* output:

![11111](https://user-images.githubusercontent.com/69191953/90231889-7f0d7a00-de24-11ea-9390-a2651e645703.png)

## Second project: "dealing_cards_from_deck"
This program generate a deck of 52 cards, various actions can be preformed on the deck as desired.
The progrem was writen with two classes, Card and Deck, our Deck class generate a deck with respect to the Card class.

libraries used: random

## Third project: "ploting_data_from_xl"
With this project we are working with an xl file contains data in 5 different columns,
we are spliting this data into 5 different arrays containing one column of data each.
We plot as a scatter graph our values of 'X' and 'Y' when each couple of (X, Y) gets a corresponding value of 'L'
that value dictates the color of each dot on the scatter graph.

libraries used: numpy, matplotlib.pyplot, pandas

* application - With this program we can extract data from an xl file and split it to different groups with the same 'features'.

![Untitled3](https://user-images.githubusercontent.com/69191953/90415401-b34d9880-e0b9-11ea-9c0a-01b3d4bd8d9a.png)

## Forth project: "poll_questions"
In this project we generate a poll questions with any desired number of answer options and starts our 
options value from zero because no votes were given. the class methods of class Poll are as follows:
* vote - the user puts the number of desired votes as a list (ex: ['X', 'X', 'Y'])
         the function cast_multiple_votes takes the list and inputs a vote one after the other to vote method.
* add_option - adding an answer option to our poll. 
* remove_option - removes an answer option from our poll.
* get_votes - display our answer options and votes in a list of touples when the first touple is the answer that got the most votes.
* get_winner - display the option that got the most votes.
