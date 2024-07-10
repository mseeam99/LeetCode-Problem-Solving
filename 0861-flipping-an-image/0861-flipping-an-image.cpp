static const bool Booster = [](){
    #pragma GCC optimize("OFast")
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return true;
}();

class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& image) {

        for(int i=0; i<image.size(); i++){
            reverse(image[i].begin(),image[i].end());
        }

        for(int i=0;i<image.size();i++){
            for(int j=0;j<image[i].size();j++){
                if(image[i][j] == 1){
                    image[i][j] = 0;
                }else if(image[i][j] == 0){
                    image[i][j] = 1;
                }
            }
        }
        return image;
    }
};

