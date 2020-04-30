#include <iostream> 
#include <string>
#include <queue>

using namespace std;

int main2(void) {
	int n, m, k, i, j;
	string first = "", second = "";
	queue <string> dq;
	while (scanf("%d %d %d", &n, &m, &k) == 1, n + m + k != 0)
	{
		for (i = 0;i < n;i++)
			dq.push("G");
		for (i;i < m+n;i++)
			dq.push("K");
		while (dq.size() > 1) {
			for (j = 0; j < 2;j++) {
				for (i = 0; i < k - 1;i++) {
					dq.push(dq.front());
					dq.pop();
				}
				first = second;
				second = dq.front();
				dq.pop();
			}
			if (first == second)
				dq.push("G");
			else
				dq.push("K");
		}
		if (dq.front() == "G")
			cout << "Gared" << endl;
		else
			cout << "Keka" << endl;
		dq.pop();
	}
	system("pause");
	return 0;
}