class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> visited = new HashMap<Integer, Integer>();
        for(int i = 0; i< nums.length; i++){
            int a = target - nums[i];
            if(visited.containsKey(a)){
                return new int[]{ visited.get(a), i};
            }
            visited.put(nums[i], i);

        }
        return new int[]{0, 0};
    }
}