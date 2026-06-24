class Solution {
public:
    int maxArea(vector<int>& height) {
        int h,w,a;
        int left = 0, right = height.size()-1,best=0;
        while(left<right){
            w = right - left;
            h = min(height[left],height[right]);
            a = w * h;
            
            best = max(a,best);
    
            if(height[left]<height[right]){
                left++;
            }
            else{
                right--;
            }
        }
        return best;
    }
};