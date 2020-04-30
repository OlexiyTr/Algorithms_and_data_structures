#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cctype>
#include <cstring>

using namespace std;

int main(void) {
	string strok;
	int i, N, M, brackets = 0, magic_br = 0;
	cin >> N >> M;
	for (i = 0; i < N;i++) {
		if (i % 72 == 0)
			cin >> strok;
		switch (strok[i % 72]) {
		case '(': brackets++;
			break;
		case ')': brackets--;
			break;
		case ']': 
			brackets--;
			magic_br++;
			break;
		}
		if (brackets < 0 || magic_br > M) {
			cout << 0;
			return 0;
		}
	}
	cout << 1 << endl;
	cout << brackets + 1;
	for (i = 0; i < magic_br-1;i++) {
		cout << 1 << "\n";
	}
	system("pause");
	return 0;
}