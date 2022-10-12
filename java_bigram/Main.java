import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.Files;
import java.util.List;
import java.util.Arrays;

class Main {

	public static void main(String[] args) throws IOException {

        Markov markov = new Markov();

        Path path = Paths.get("sayings.txt");

        try(BufferedReader br = Files.newBufferedReader(path)) {
        String line;
        while((line = br.readLine()) != null){
            markov.addPhrase(line);
        }
        }

        System.out.println("Markov chain is ready! Press enter to generate new wise sayings.");

        while (true) {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        in.readLine();
        System.out.println(markov.generateSentence());
        }
	}
}