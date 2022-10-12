import java.util.Hashtable;
import java.util.Random;
import java.util.Vector;

public class Markov {

	// Hashmap
	static Hashtable<String, Vector<String>> chain;
	static Random rnd;

    public Markov() {
        chain = new Hashtable<String, Vector<String>>();
        // Create the first two entries (k:_start, k:_end)
            chain.put("_start", new Vector<String>());
            chain.put("_end", new Vector<String>());
        rnd = new Random();
    }

	/*
	 * Add words
	 */
	public static void addPhrase(String phrase) {
		// put each word into an array
		String[] words = phrase.split(" ");

		// Loop through each word, check if it's already added
		// if its added, then get the suffix vector and add the word
		// if it hasn't been added then add the word to the list
		// if its the first or last word then select the _start / _end key

		for (int i = 0; i < words.length; i++) {

      // Handle case of first or last word in phrase
			if (i == 0) {
				Vector<String> startWords = chain.get("_start");
				startWords.add(words[i]);
			} else if (i == words.length-1) {
				Vector<String> endWords = chain.get("_end");
				endWords.add(words[i]);
			}

      // Handle any word that has a word after it
      if (i < words.length - 1) {
				Vector<String> suffix = chain.get(words[i]);
        if (suffix == null) {
          // If the word isn't in the chain yet,
          // add key=word,vector=<word after>
					suffix = new Vector<String>();
					suffix.add(words[i+1]);
					chain.put(words[i], suffix);
				} else {
          // Otherwise add <word after> to vector
					suffix.add(words[i+1]);
					chain.put(words[i], suffix);
				}
			}
		}
	}


	/*
	 * Generate a markov phrase
	 */
	public static String generateSentence() {

		// Vector to hold the phrase
		Vector<String> newPhrase = new Vector<String>();

		// String for the next word
		String nextWord = "";

		// Select the first word
		Vector<String> startWords = chain.get("_start");
		int startWordsLen = startWords.size();
		nextWord = startWords.get(rnd.nextInt(startWordsLen));
		newPhrase.add(nextWord);

		// Keep looping through the words until we've reached the end
		while (nextWord.charAt(nextWord.length()-1) != '.') {
			Vector<String> wordSelection = chain.get(nextWord);
      if (wordSelection == null) {
        break;
      }
      int wordSelectionLen = wordSelection.size();
			nextWord = wordSelection.get(rnd.nextInt(wordSelectionLen));
			newPhrase.add(nextWord);
		}

		return String.join(" ", newPhrase);
	}
}