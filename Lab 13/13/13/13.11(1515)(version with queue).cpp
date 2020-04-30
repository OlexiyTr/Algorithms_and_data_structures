#include <iostream> 
#include <string>
#include <queue>

using namespace std;

int j = 1;

void step(int x, int num) {
	queue<int> qe;
	for (int i = 1; i <= x;i++)
		qe.push(i);
	while (qe.size() > 1)
	{
		qe.push(qe.front());
		qe.pop();
		qe.pop();
	}
	if (qe.front() == x) {
		printf("Case %d: %d %d\n", j, num-1, x);
		return;
	}
	else
		step(qe.front(), num + 1);
}

int main8(void) {
	int n, m, i, x, counter;
	queue<int> dq;
	cin >> m;
	while (m--){
		cin >> n;
		step(n, 1);
		j++;
	}
	system("pause");
	return 0;
}