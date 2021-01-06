import java.io.*;

public class Beakjoon1009 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            String[] inputs = br.readLine().split(" ");
            int a = Integer.parseInt(inputs[0]);
            int b = Integer.parseInt(inputs[1]);
            int target = a % 10;
            for (int j = 1; j < b; j++) {
                target = (target * a) % 10;
            }
            int result = (target == 0) ? 10 : target;
            System.out.println(result);
        }
        br.close();
    }
}
