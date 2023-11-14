class Solution {
public:
    int minimumRefill(vector<int>& plants, int capacityA, int capacityB) {
        int left = 0;
        int right = plants.size() - 1;
        int a = capacityA;     
        int b = capacityB;
        int count = 0;

        while (left < right){   
            if (a < plants[left]){
                count += 1;
                a = capacityA;
            }
            a -= plants[left];              
            
            if (b < plants[right]){
                count += 1;
                b = capacityB;}
             
            b -= plants[right];
            right -= 1;
            left += 1;
               
        }   
        if (left == right){
                if (a < plants[left] && b < plants[left]){
                    count += 1;                    
                }
            }   
        return count;
    }
};