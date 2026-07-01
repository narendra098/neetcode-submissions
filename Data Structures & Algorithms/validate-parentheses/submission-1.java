class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> mpp = new HashMap<>();
        mpp.put(')','(');
        mpp.put('}', '{');
        mpp.put(']','[');

        Stack<Character> stack = new Stack<>();
        for(char ch:s.toCharArray()){
            if(mpp.containsKey(ch)){
                if(!stack.isEmpty() && mpp.get(ch) == stack.peek()){
                    stack.pop();
                }
                else{
                    return false;
                }
            }else{
                stack.push(ch);
            }
        }

        return stack.isEmpty();
    }
}
