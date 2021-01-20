import java.util.Stack;
class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        Stack<Integer> stack = new Stack<Integer>();

        for(int move : moves){
            int level = getLevel(board, move - 1);
            if(level >= 0){
                int target = board[level][move - 1];
                board[level][move - 1] = 0;
                stack.push(target);
                answer += updateStack(stack);
            }
        }
        return answer;
    }

    public int getLevel(int[][] board, int move){
        for(int i = 0; i < board.length; i++){
            if (board[i][move] > 0){
                return i;
            }
        }
        return -1;
    }

    public int updateStack(Stack<Integer> stack){
        int counter = 0;
        while(stack.size() > 1){
            Integer firstLast = stack.get(stack.size() - 1);
            Integer secondLast = stack.get(stack.size() - 2);
            if(Integer.compare(firstLast, secondLast) == 0){
                stack.pop();
                stack.pop();
                counter += 2;
            } else {
                break;
            }
        }
        return counter;

    }
}