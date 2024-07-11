static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    int numberOfAlternatingGroups(vector<int>& colors) {
        int count = 0;
        for(int i=0; i<colors.size(); i++){
            if(colors[i] != colors[(i+1) % colors.size()] && colors[(i+1)%colors.size()] != colors[(i+2)%colors.size()]){
                count++;
            }
        }
        return count;
    }
};