#include<iostream>
#include<math.h>

using namespace std;

int solve(int n)
{
    int soma;
    
    if(n == 0)
     return soma;

    return soma = n + solve(n - 1);
}

int main()
{
    int n;

    cin >> n;

    cout << solve(n) <<"\n";

    return 0;
}