class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> mpps = new HashMap<>();
        for(char ch:s.toCharArray()){
            mpps.put(ch, 1 + mpps.getOrDefault(ch, 0));
        }
        Map<Character, Integer> mppt = new HashMap<>();
        for(char ch:t.toCharArray()){
            mppt.put(ch, 1 + mppt.getOrDefault(ch, 0));
        }

        return mpps.equals(mppt);
    }
}
