class Solution {
    public int reverse(int x) {
                
        String number_in_String = Integer.toString(x); 
        String answer = "";
        
        if(x>0){
            for(int i=number_in_String.length()-1;i>=0;i--){
                answer = answer + number_in_String.charAt(i);
            } 
        }else if(x<0){
            for(int i=number_in_String.length()-1;i>=1;i--){
                answer = answer + number_in_String.charAt(i);
            } 
        }else if(x==0){
            return 0;
        }
                
        int num1=0;
        
        try {
            num1 = Integer.parseInt(answer);
        } catch (NumberFormatException e) {
            return 0;
        }
        
        if(x<0){
           num1 = num1 * -1; 
            System.out.print(num1);
        }else if(x>0){
            num1=num1;
        }else if(x==0){
            num1=0;
        }
        
        return num1;
      
    }
}