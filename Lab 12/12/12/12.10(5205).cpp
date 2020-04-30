#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cctype>
#include <cstring>

#define MAX 2010

using namespace std;

char st[MAX];
int matr[MAX][MAX];
int len;
const int mod = 301907;

int bracketsChecker(int n, int k){
	if (k < 0) 
		return 0;
	if (n == len) 
		return (k == 0);
	if (matr[n][k] != -1) 
		return matr[n][k];
	if (st[n] == '(')
		return matr[n][k] = bracketsChecker(n + 1, k + 1);
	else if (st[n] == ')')
		return matr[n][k] = bracketsChecker(n + 1, k - 1);
	return matr[n][k] = (bracketsChecker(n + 1, k - 1) + bracketsChecker(n + 1, k + 1)) % mod;
}

int main3(void) {
	cin >> st;
	len = strlen(st);
	memset(matr, -1, sizeof(matr));
	cout << bracketsChecker(0, 0);
	system("pause");
	return 0;
}