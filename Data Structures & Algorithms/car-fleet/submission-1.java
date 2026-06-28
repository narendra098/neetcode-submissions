class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int[][] pos_speed = new int[position.length][];
        for(int i=0;i<position.length;i++){
            pos_speed[i] = new int[]{position[i], speed[i]};
        }

        Arrays.sort(pos_speed, (a,b)->Integer.compare(b[0], a[0]));

        Stack<Double> stack = new Stack<>();
        for(int[] pair:pos_speed){
            stack.push((double) (target-pair[0])/pair[1]);
            if(stack.size() >=2 && stack.peek() <= stack.get(stack.size()-2)){
                stack.pop();
            }
        }
        
        return stack.size();
    }
}
