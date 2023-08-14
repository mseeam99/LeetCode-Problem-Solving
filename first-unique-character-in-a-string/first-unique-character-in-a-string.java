class Solution {
    public int firstUniqChar(String s) {
        
        int index = -1;
        
        for(int i=0;i<s.length();i++){
            boolean char_found = false;
            for(int j=0;j<s.length();j++){
                if(i!=j && s.charAt(i)==s.charAt(j)){
                    char_found=true;
                    break;
                }
            }
            
            if(char_found==false){
                index=i;
                return index;
            }
        }
        
        
        return index;
    }
}