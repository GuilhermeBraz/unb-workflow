#include<bits/stdc++.h>

using namespace std;

int main(){

	int N, i=0;
	
	cin >> N;

	while(N!=0){
	if(N%3==0){
		cout<<i<<'\n';
		i = 0;
		break;
	}
		N=N/10;
		i++;
	}
	if(i!=0)
		cout<<-1<<'\n';
	return 0;
}
