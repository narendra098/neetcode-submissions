class Solution {
    public String minWindow(String s, String t) {
        int have = 0;
        int need = 0;
        Map<Character, Integer> smap = new HashMap<>();
        Map<Character, Integer> tmap = new HashMap<>();
        int l = 0;
        int r = 0;
        int n = s.length();
        for(int i=0; i<t.length();i++){
            tmap.put(t.charAt(i), 1 + tmap.getOrDefault(t.charAt(i), 0));
        }
        need = tmap.size();
        int left = 0;
        int right = 0;
        int resLen = Integer.MAX_VALUE;
        while(r<n){
            smap.put(s.charAt(r), 1 + smap.getOrDefault(s.charAt(r), 0));
            if( tmap.containsKey(s.charAt(r)) && 
                smap.get(s.charAt(r)).intValue()==tmap.get(s.charAt(r)).intValue() ){
                have += 1;
            }
            while(have==need){
              if(r-l+1 < resLen){
                left = l;
                right = r;
                resLen = r - l + 1;
              }
              smap.put(s.charAt(l), smap.get(s.charAt(l))-1);
              if( tmap.containsKey(s.charAt(l)) && 
                    smap.get(s.charAt(l)) < tmap.get(s.charAt(l)) ){
                have -= 1;
              }
              l += 1;
            }
            r+=1;
        }
        return resLen != Integer.MAX_VALUE ? s.substring(left, right+1) : "";

    }
}
