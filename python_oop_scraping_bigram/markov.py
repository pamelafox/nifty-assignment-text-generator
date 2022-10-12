import random

class MarkovChain:

    def __init__(self):
        self.chain = {"_start": [], "_end": []}

    def add_phrase(self, phrase):
        words = phrase.lower().strip().split(" ")

        # Loop through each word, check if it's already added
		# if its added, then get the suffix vector and add the word
		# if it hasn't been added then add the word to the list
		# if its the first or last word then select the _start / _end key
        i = 0
        while i < len(words) - 1:
            bigram = f"{words[i]} {words[i + 1]}"
            # Handle case of first or last bigram in phrase
            if i == 0:
                start_words = self.chain.get("_start")
                start_words.append(bigram)
			# Add word_after (or _end) to chain for this bigram
            word_after = "_end"
            if i < len(words) - 2:
                word_after = words[i + 2]
            bigram = bigram
            if bigram not in self.chain:
                self.chain[bigram] = []
            self.chain[bigram].append(word_after)
            i += 1

    def generate_phrase(self):
        """Generate a Markov phrase"""
        new_phrase = []

		# Select the first bigram
        start_bigram = random.choice(self.chain.get("_start"))
        new_phrase.append(start_bigram)

	    # Keep looping through the words until we
        # can't come up with another word or each an "end" marker
        prev_bigram = start_bigram
        prev_word = start_bigram.split(" ")[1]
        new_word = ""
        num_forks = 0
        while True:
            prev_bigram = prev_bigram
            new_words = self.chain.get(prev_bigram)
            if new_words is None:
                break
            if len(new_words) > 1:
                num_forks += 1
            new_word = random.choice(new_words)
            if new_word == "_end":
                break
            new_phrase.append(new_word)
            prev_bigram = prev_word + " " + new_word
            prev_word = new_word

        return f'{" ".join(new_phrase)} [forks: {num_forks}]'