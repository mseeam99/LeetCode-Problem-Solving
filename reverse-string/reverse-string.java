class Solution {
    public void reverseString(char[] s) {
        int length = s.length;
        char[]answer = new char [length];
        int index = 0;
        for(int i=length-1;i>=0;i--){
            answer[index]=s[i];
            index++;
        }
        
        for(int i=0;i<answer.length;i++){
            s[i]=answer[i];
        }
    }
}