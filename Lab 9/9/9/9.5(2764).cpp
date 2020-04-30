#include <iostream>
#include <stdio.h>
#include<fstream>

using namespace std;
#define LEN 1024

int N;
int fr[LEN];

bool check(int nf)
{
	for (int i = 0; i < N && fr[i] >= 0; i++) {
		if (i == nf) continue;
		if (fr[nf] == fr[i]) return false;  // Горизонталь
		if ((nf + fr[nf]) == (i + fr[i])) return false; // Нисходящая диагональ
		if ((nf - fr[nf]) == (i - fr[i])) return false; // Восходящая диагональ
	}
	return true;
}

bool line_up(int i)
{
	if (i > N - 1) return false;
	for (int j = 0; j < N; j++) {
		fr[i] = j;
		if (check(i) == true) {
			line_up(i + 1);
			break;
		}
	}
	return false;
}

int main()
{
	cin >> N;
	for (int i = 0; i < N; i++) fr[i] = -1;
	line_up(0);
	for (int i = N-1; i >= 0; i--) {
		cout << fr[i]+1 << " ";
	}
	system("pause");
	return 0;
}