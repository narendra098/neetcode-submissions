class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = Arrays.stream(nums).boxed().collect(Collectors.toSet());
        int ans = 0;
        for(int num: nums){
            if(!set.contains(num-1)){
                int start = num;
                int len = 0;
                while(set.contains(start)){
                    start++;
                    len++;
                }
                ans = Math.max(ans, len);
            }
        }
        return ans;
    }
}
