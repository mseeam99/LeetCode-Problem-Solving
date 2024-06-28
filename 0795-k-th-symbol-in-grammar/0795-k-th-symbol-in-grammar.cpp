class Solution {
public:
    int kthGrammar(int n, int k) {
        
        // bc
        if(n==1) return 0;

        int len = pow(2,n-1);
        int mid = len/2;

        if(k <= mid){
            int ans1 = kthGrammar(n-1, k);
            return ans1;
        }
        else{
            int ans2 = !kthGrammar(n-1,k-mid);
            return ans2;
        }
    }
};