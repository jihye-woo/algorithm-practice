class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder(s.length());
        char[] answer = new char[s.length()];
        int local_idx = 0;
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(Character.isWhitespace(c)) {
                sb.append(c);
                local_idx = 0;
            } else {
                if(local_idx % 2 == 0){
                    sb.append(Character.toUpperCase(c));
                } else {
                    sb.append(Character.toLowerCase(c));
                }
                local_idx++;
            }
        }
        return sb.toString();
    }
}