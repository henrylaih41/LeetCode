class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> ans;
        int head = 0, tail = numbers.size() - 1, sum;
        while(head < tail){
            sum = numbers[head] + numbers[tail];
            if(sum == target)
                return {head + 1, tail + 1};
            else if(sum > target)
                tail--;
            else
                head ++;
        }
        
        return {};
    }
};
