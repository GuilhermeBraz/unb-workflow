#include<iostream>
#include<math.h>

using namespace std;
void checkCube(int C)
{
    int cube;
 
    // Iterate from 1-C
    for (int i = 0; i <= C; i++) {
 
        // Find the cube of
        // every number
        cube = i * i * i;
 
        // Check if cube equals
        // C or not
        if (cube == C) {
            cout <<"Yes" << "\n";
            return;
        }
        else if (cube > C) {
            cout <<"No" <<"\n";
            return;
        }
    }
}

int main()
{ 
    int N, Q, A[1000001];

    cin >> N >> Q;

    for (int i = 0; i < N; i++)
    {
        /* code */
        cin >> A[i];
    }

    // solve(Q, A);
    
    int L, R, C ;   
    for (int i = 0; i < Q; i++)
    {
        C=1;
        cin >> L >> R;
        for(int j = L-1; j<R; j++)
        {
            C = C*A[j];
        }
        checkCube(C);      
    }
    
    return 0;
}