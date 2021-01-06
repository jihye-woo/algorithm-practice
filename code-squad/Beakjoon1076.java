
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Map;

public class Beakjoon1076 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Map<String, Integer> colors = Map.of(
                "black",    0,
                "brown",    1,
                "red",      2,
                "orange",   3,
                "yellow",   4,
                "green",    5,
                "blue",     6,
                "violet",   7,
                "grey",     8,
                "white",  9
        );

        int[] inputColorValue = new int[3];
        for (int i = 0; i < 3; i++) {
            String color = br.readLine();
            inputColorValue[i] = colors.get(color);
        }

        long resistance = (inputColorValue[0] * 10 + inputColorValue[1]);
        long multiply = (long) Math.pow(10, inputColorValue[2]);
        System.out.println(resistance * multiply);
        br.close();
    }
}

