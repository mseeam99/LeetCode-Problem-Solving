static const bool Booster = [](){
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    int romanToInt(string s) {

        int value = 0;
        int i = 0;
        
        while (i < s.size()){
            if(s[i] == 'I' && s[i+1] =='V'){
                value = value + 4;
                i =  i + 2;
            }else if(s[i] == 'I' && s[i+1] =='X'){
                value = value + 9;
                i =  i + 2;
            }else if(s[i] == 'X' && s[i+1] =='L'){
                value = value + 40;
                i =  i + 2;
            }else if(s[i] == 'X' && s[i+1] =='C'){
                value = value + 90;
                i =  i + 2;
            }else if(s[i] == 'C' && s[i+1] =='D'){
                value = value + 400;
                i =  i + 2;
            }else if(s[i] == 'C' && s[i+1] =='M'){
                value = value + 900;
                i =  i + 2;
            }else if(s[i] == 'I'){
                value = value + 1;
                i =  i + 1;
            }else if(s[i] == 'V'){
                value = value + 5;
                i =  i + 1;
            }else if(s[i] == 'X'){
                value = value + 10;
                i =  i + 1;
            }else if(s[i] == 'L'){
                value = value + 50;
                i =  i + 1;
            }else if(s[i] == 'C'){
                value = value + 100;
                i =  i + 1;
            }else if(s[i] == 'D'){
                value = value + 500;
                i =  i + 1;
            }else if(s[i] == 'M'){
                value = value + 1000;
                i =  i + 1;
            }
        }
        return value;
    }
};