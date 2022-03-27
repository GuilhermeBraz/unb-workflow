#include <bits/stdc++.h>

//TB = 2 * A + 100
//following = B 
//followers = A
int main(){
int A, B, TB, RB;

scanf("%d %d", &A, &B);

TB = 2*A + 100;
RB = TB-B;
printf("%d\n",RB);

return 0;
}
