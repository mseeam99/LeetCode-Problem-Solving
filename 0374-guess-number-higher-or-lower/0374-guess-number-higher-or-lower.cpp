static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {

        int left = 1;
        int right = n;
        int middle = 0;
        
        while (left <= right){

            middle = left + (right - left) / 2;

            if(guess(middle) == 0){
                return middle;
            }

            else if(guess(middle) == -1){
                right = middle - 1;
            }

            else if(guess(middle) == 1){
                left = middle + 1;
            }
        }

        return -1;
        
    }
};