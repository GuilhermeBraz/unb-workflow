#include <bits/stdc++.h>

using namespace std;

int main()
{

int N, A[1000];

cin >> N;

int sum, Msum = 0, gcd, k=2, maior=0;

for(int i =0; i<N; i++)
	cin >> A[i]; 

for(int i =0; i < 1000; i++){
	sum =0;
	for(int j =0; j < N; j++)
	{
		if(A[j]%k==0){
//			cout<< A[i]%k <<'\n';
			sum++;
		}
	}
	if(sum>=Msum)
	{
		Msum=sum;
	       	gcd=k;
	//	cout<<Msum<<':'<<gcd<<'\n';
	}
		k++;
}
cout<<gcd<<'\n';

return 0;

}

