import grpc
from concurrent import futures
import time

# https://towardsdatascience.com/solving-the-new-york-times-spelling-bee-puzzle-in-python-511bcb5ea65e
import bees_pb2
import bees_pb2_grpc


class WordChecker(bees_pb2_grpc.BeesServicer):

    def __init__(self, *args, **kwargs):
        pass

    def CheckWord(self, request, context):
        input1 = request.inputWord
        list_to_check = list(set[input1])
        central = list_to_check[3]
        accept = solve_spelling_bee(list_to_check, central)
        if input1 in accept:
            return bees_pb2.WordInDict

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bees_pb2_grpc.add_BeesServicer_to_server(WordChecker(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

channel = grpc.insecure_channel('localhost:50051')
stub = bees_pb2_grpc.BeesStub(channel)

#
# class SpellingBee():
#     def CheckWord(self):
#         print()


word_file = open('words_dictionary.json', "r")

wordlist = []

for word in word_file:
    wordlist.append(str(word).lower()[:-1])


def solve_spelling_bee(letters_list, center_letter):
    '''Takes in a list of strings for letters_list and a single character string for center_letter.
       Returns a list of words from wordlist which contain the center letter, have a length of at
       least 4, and do not contain any unacceptable letters.'''

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']

    unacceptable_letters = [l for l in alphabet if l not in letters_list]
    acceptable_words = []

    for word in wordlist:
        if center_letter in word:
            if word not in acceptable_words:
                if len(word) > 3:
                    if any(l in unacceptable_letters for l in word) == False:
                        acceptable_words.append(word)
    print(acceptable_words)
    return acceptable_words


WordChecker.CheckWord(stub.CheckWord)

#
# acceptable = solve_spelling_bee()
#
#
# letters_list = ['a', 'c', 'n', 'l', 'i', 'f', 'u']
# center_letter = 'l'
# solve_spelling_bee(letters_list, center_letter)
