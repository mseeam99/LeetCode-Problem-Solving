static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        int currentSum = 0;
        int count = 0;
        for(int i=0; i<arr.size(); i++){
            if(i<k){
                currentSum+=arr.at(i);
            }else{
                if((currentSum / k) >= threshold){
                    count++;
                }
                currentSum-=arr.at(i-k);
                currentSum+=arr.at(i);
            }
        }
        if((currentSum / k) >= threshold){
            count++;
        }
        return count;
    }
};

/*
class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {

        vector<int>tempVector;
        int count = 0;

        for(int i=0; i<arr.size()-k+1; i++){
            for(int j=i; j<i+k; j++){
                tempVector.push_back(arr[j]);
            }

            int tempSum = std::accumulate(tempVector.begin(),tempVector.end(),0);
            int average = tempSum / k;
            
            if (average >= threshold){
                count++;
            }
            tempVector.clear();
        }
        return count;
    }
};
*/

/*
class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {

        vector<int> firstVector;
        int count = 0;

        for (int i=0; i<k; i++){
            firstVector.push_back(arr.at(i));
        }

        int summation = (std::accumulate(firstVector.begin(),firstVector.end(),0));
        int average = summation / k;
        if (average >= threshold){
            count++;
        }

        for (int i = 0; i<arr.size()-k; i++){
            firstVector.erase(firstVector.begin());
            firstVector.insert(firstVector.end(),arr.at(i+k));
            int summation = (std::accumulate(firstVector.begin(),firstVector.end(),0));
            int average = summation / k;
            if (average >= threshold){
                count++;
            }
        }
        return count;
    }
};
*/






