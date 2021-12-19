from collections import deque
from words.word import Word


class WordDistanceMap(object):
    def __init__(self, word: Word):
        self.distances = {str(word): 1}
        queue = deque()
        queue.append(word)
        while len(queue) > 0:
            next_word: Word = queue.popleft()
            distance = self.distances.get(str(next_word))
            if distance is None:
                distance = 0
            distance = distance + 1
            for linked_word in next_word.linked_words:
                if linked_word not in self:
                    queue.append(linked_word)
                    self.distances[str(linked_word)] = distance

    def __len__(self):
        return len(self.distances)

    def __contains__(self, word: Word):
        return str(word) in self.distances

    def __getitem__(self, word: Word):
        return self.distances.get(str(word))

    def reachable(self, word: Word, maximum_ladder_length: int):
        distance = self.distances.get(str(word))
        if distance is None:
            return False
        return distance <= maximum_ladder_length
