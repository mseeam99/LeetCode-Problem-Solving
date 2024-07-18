class Solution {
public:
    int divisorSubstrings(int num, int k) {

        int count = 0;

        string numberAsString = to_string(num);

        for(int i=0; i<numberAsString.size()-k+1; i++){

            string tempSubString = numberAsString.substr(i,k);

            int tempValue = stoi(tempSubString);

            if(tempValue != 0 && num % tempValue == 0 ){

                count++;

            }

        }

        return count;

    }

};
