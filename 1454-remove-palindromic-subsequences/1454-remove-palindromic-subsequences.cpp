class Solution {
public:
    int removePalindromeSub(string s) {
        int result = 1;
        if(checkPalindrome(s)){
            result = 1;
        }else{
            result = 2;
        }
        return result;   
    }

    bool checkPalindrome(string recievedString){
        string actualString = recievedString;
        reverse(recievedString.begin(),recievedString.end());
        bool answer = false;
        if(actualString == recievedString){
            answer = true;
        }else{
            answer = false;
        }
        return answer;
    }
};