#include<bits/stdc++.h> 

using namespace std;

int main()
{   int n, t, dls[100000], jls[100000], m, intersection;
    cin>>t;
    for(int k=0; k<t; k++)
    {   
        intersection = 0;
        cin>>n;
        for(int i=0; i<n; i++)
        {
            cin>>dls[i];
        }
        cin>>m;
        for(int i=0; i<m; i++)
        {
            cin>>jls[i];
        }
        if(n>m)
        {
            for(int i =0; i<n; i++)
            {
                for(int j=0; j<m; j++)
                {
                    if(dls[i]-jls[j] == 0 || (dls[i]-jls[j])%2 == 0)
                    {
                        intersection++;
                    }
                }
            }
        }
        else
        {
            for(int i =0; i<m; i++)
            {
                for(int j=0; j<n; j++)
                {
                    if(jls[i]-dls[j] == 0 || (jls[i]-dls[j])%2 == 0)
                    {
                        intersection++;
                    }
                }
            }
        }
    
        printf("%d\n", intersection);   
    
    }


    return 0;
}