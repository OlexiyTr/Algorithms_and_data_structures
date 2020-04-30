#include <iostream> 
#include <string>
#include <queue>

using namespace std;

int josephus(int n, int k)
{
	int p = 1;
	while (p <= n)
		p *= 2;
	return (2 * n) - p + 1;
}

int main7(void) {
	int n, m, i, x, counter, j = 0;
	queue<int> dq;
	cin >> m;
	while (m--) {
		cin >> n;
		x = n;
		counter = 0;
		do
		{
			counter++;
			n = x;
			x = josephus(n, 2);

		} while (x != n);
		j++;
		printf("Case %d: %d %d\n", j, counter-1, x);
	}
	system("pause");
	return 0;
}