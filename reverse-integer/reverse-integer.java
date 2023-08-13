class Solution {
    public int reverse(int x) {
        
        System.out.print("int is: " + x + " ");
        
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
        
        System.out.print("String is: " + answer);
        
        int num1=0;
        
        try {
            num1 = Integer.parseInt(answer);
            System.out.println("Parsed integer: " + num1);
        } catch (NumberFormatException e) {
            System.out.println("Invalid input string");
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