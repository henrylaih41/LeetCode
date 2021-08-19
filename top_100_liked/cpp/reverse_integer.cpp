class Solution {
public:
    int reverse(int x) {
        int popped, rev = 0;
        while(x){
            popped = x % 10;
            x /= 10;
            if(rev > INT_MAX/10 || rev == INT_MAX/10 && popped > 7)
                return 0;
            if(-rev > INT_MAX/10 || -rev == INT_MAX/10 && -popped > 8)
                return 0;
            rev = rev * 10 + popped;
        }
        return rev;
    }
};
