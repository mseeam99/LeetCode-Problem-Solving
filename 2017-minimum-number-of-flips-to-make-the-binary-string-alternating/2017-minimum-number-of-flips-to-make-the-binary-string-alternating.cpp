static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    int minFlips(string s) {

        int actualSizeAsK = s.size();
        s += s;

        string first  = "";
        string second = "";

        for(int i=0; i<s.size(); i++){
            if (i%2 == 0){
                first +="0";
                second+="1";
            }else{
                first +="1";
                second+="0";
            }
        }
        
        int finalFirstChangeCount  = 0;
        int finalSecondChangeCount = 0;

        int leftPointer  = 0;
        int rightPointer = 0;

        for(rightPointer = 0; rightPointer<actualSizeAsK; rightPointer++){
            if(s[rightPointer] != first[rightPointer]){
                finalFirstChangeCount++;
            }
            if(s[rightPointer] != second[rightPointer]){
                finalSecondChangeCount++;
            }
        }

        int minChanges = min(finalFirstChangeCount, finalSecondChangeCount);

        rightPointer = actualSizeAsK;

        while(rightPointer < s.size()){
    
            if(s[rightPointer] != first[rightPointer]){
                finalFirstChangeCount++;
            }

            if(s[leftPointer] != first[leftPointer]){
                finalFirstChangeCount--;
            }

            if(s[rightPointer] != second[rightPointer]){
                finalSecondChangeCount++;
            }

            if(s[leftPointer] != second[leftPointer]){
                finalSecondChangeCount--;
            }

            leftPointer++;
            rightPointer++;

            minChanges = min({minChanges, finalFirstChangeCount, finalSecondChangeCount});  
        }

        return minChanges;

    }
};