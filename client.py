import grpc

import bees_pb2
import bees_pb2_grpc
import pangrams



class WordCheckerClient(object):

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = bees_pb2_grpc.BeesStub(self.channel)

    def check_word(self, inputWord):
        checker_response = stub.CheckWord(bees_pb2.InputWord(word=inputWord))
        print(f'{checker_response}')
        return checker_response


def compare(list1, list2):
    if list1.issubset(list2):
        return True

def play():
    word = pangrams.random_pangram
    print("The pangram word")
    pangrams.print_pangram()
    print("Letters to play")
    letters = pangrams.letters_list(word)
    print(pangrams.print_available_letters())
    return letters


channel = grpc.insecure_channel('localhost:50051')
stub = bees_pb2_grpc.BeesStub(channel)

# get list of letters that are available in current game after random selection of pangram
main_list = play()

#get input from user of the word to check if exists in list of words
word = input("Enter your word: ")


if __name__ == '__main__':
    client = WordCheckerClient()
    result = client.check_word(word)
    print(f'{result}')


#list of letters of the user input needed to check if the word is eligible comparing to the pangram letters
user_letters = set(word)

# check eligibility
compare(user_letters, main_list)

