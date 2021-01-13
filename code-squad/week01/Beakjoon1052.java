
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Beakjoon1052 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");

        int N = Integer.parseInt(inputs[0]);
        final int K = Integer.parseInt(inputs[1]);

        PriorityQueue<Integer> heap = new PriorityQueue<Integer>();

        int level = 0;
        long answer = 0;

        // merge water buckets as mush as possible
        while (N + heap.size() > K && N > 1) {
            if (N % 2 != 0) { // N == odd number
                heap.add(level);
                N--; // N -> even number
            }
            level++;
            N /= 2;
        }
        if (N + heap.size() > K) {
            heap.add(level);

            // if still need to merge buckets
            while (heap.size() > K) {
                if (!heap.isEmpty()) {
                    int lowestLevel = heap.poll();
                    if (!heap.isEmpty()) {
                        int secondLowestLevel = heap.poll();
                        // if current bucket is equal to next bucket
                        if (lowestLevel == secondLowestLevel) {
                            // merge without buying the bucket
                            heap.add(++secondLowestLevel);
                        } else { // current bucket is smaller than the next bucket
                            heap.add(secondLowestLevel);
                            // buying the bucket, do not merge
                            answer += Math.pow(2, lowestLevel);
                            heap.add(++lowestLevel);
                        }
                    } else {
                        answer += Math.pow(2, lowestLevel);
                        heap.add(++lowestLevel);
                    }

                } else {
                    answer = -1;
                    break;
                }
            }
        }
        System.out.println(answer);
    }
}
