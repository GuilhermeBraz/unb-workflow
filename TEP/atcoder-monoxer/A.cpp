#include<iostream>
#include<math.h>

using namespace std;
int main()
{
int n;

scanf("%d",&n);

if( pow(2,n) > (n*n))
{
    cout << "Yes" << "\n";
}
else
{
    cout << "No" << "\n";
}

return 0;
}