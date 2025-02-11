#include<limits.h>
class Solution {
public:
     int reverse(int x) {
        int rev=0;
        while(x!=0){
            int dig=x%10;
            x/=10;
            if (rev > INT_MAX / 10 || (rev == INT_MAX / 10 && dig > 7)) {
            return 0;
            }
            if (rev < INT_MIN / 10 || (rev == INT_MIN / 10 && dig < -8)) {
            return 0;
            }
            rev=rev*10+dig;
        }
        return rev;
    }
}
int main() {
    int x;
    std::cout << "Enter an integer: ";
    std::cin >> x;
    std::cout << "Reversed: " << reverse(x) << std::endl;
    return 0;
}