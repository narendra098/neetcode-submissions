class Solution {
    public List<Integer> majorityElement(int[] nums) {
        Integer n1 = -1;
        Integer cnt1 = 0;
        Integer n2 = -1;
        Integer cnt2 = 0;
        int n = nums.length;
        for(int num: nums){
            if(num == n1){
                cnt1++;
            }else if(num == n2){
                cnt2++;
            }else if(cnt1==0){
                n1 = num;
                cnt1 = 1;
            }else if(cnt2 == 0){
                n2 = num;
                cnt2 = 1;
            }else{
                cnt1--;
                cnt2--;
            }
        }

        cnt1 = 0;
        cnt2 = 0;
        for(int num:nums){
            if(num == n1){
                cnt1++;
            }else if(num==n2){
                cnt2++;
            }
        }

        List<Integer> res = new ArrayList<>();
        if(cnt1 > n/3){
            res.add(n1);
        }
        if(cnt2>n/3){
            res.add(n2);
        }
        return res;
        
    }
}