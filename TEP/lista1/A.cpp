//Problem
//We have removed A balls from a box that contained NNN balls and then put BBB new balls into that box. How many balls does the box contain now?
#include <iostream>
#include <cmath>

using namespace std;

int main(){
	int N, A, B;
	
	cin >> N >> A >> B;
	
	//remove A balls then add B balls
	N = N - A + B;
	
	cout << N << '\n';
		
	
	return 0;
}
