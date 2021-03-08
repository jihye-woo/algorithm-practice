import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

class Solution {

    Map<String, String> idMapper = new HashMap<>();
    List<Log> logs = new ArrayList<>();

    public String[] solution(String[] records) {

        for (String record : records) {
            String[] parsed = record.split(" ");

            if (!parsed[0].equals("Change")) { // "Enter" or "Leave" -> 로그 객체 만들기
                logs.add(new Log(parsed[1], parsed[0]));
            }
            if (parsed.length > 2) { // "Change" or "Enter" -> id : name 업데이트 혹은 추가
                idMapper.put(parsed[1], parsed[2]); // uid : name
            }
        }

        String[] answer = new String[logs.size()];

        return getLogMessages().toArray(answer);
    }

    private List<String> getLogMessages(){
//        String[] answer = new String[logs.size()];
//        for(Log log : logs){
//            log.getMessage(idMapper);
//        }
//        return answer;
        return logs.stream()
                .map(log -> log.getMessage(idMapper))
                .collect(Collectors.toList());
    }

}

class Log {
    private final String id;
    private final String action;

    Log(String id, String action) {
        this.id = id;
        this.action = action;
    }

    public String getId() {
        return id;
    }

    public String getAction() {
        if (action.equals("Enter")) {
            return "님이 들어왔습니다.";
        }
        return "님이 나갔습니다.";
    }

    public String getMessage(Map<String, String> idMapper){
        return idMapper.get(id) + getAction();
    }

}
