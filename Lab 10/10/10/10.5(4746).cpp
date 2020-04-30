#include <iostream>
#include <algorithm>

#define MAX 101

using namespace std;

bool comparator(const int x, const int y) {
	return x > y;
}

int main2() {
	int n, i, t = 0, Score = 0;
	cin >> n;
	int lst[MAX];
	for (i = 0; i < n;i++)
		cin >> lst[i];
	int ln = sizeof(lst) / sizeof(lst[0]);
	sort(lst, lst + n, comparator);
	for (i = 0; i < n;i++) {
		if (lst[i] - t <= 0)
			break;
		Score += lst[i] - t;
		t++;
	}
	cout << Score;
	system("pause");
	return 0;
}