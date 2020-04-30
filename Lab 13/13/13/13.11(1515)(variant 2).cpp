#include <iostream> 
#include <string>

using namespace std;

int main5(void) {
	int n, m, i, x, counter, j = 0, person;
	cin >> m;
	while (m--) {
		cin >> n;
		x = n;
		counter = 0;
		do
		{
			n = x;
			person = 0;
			for (int i = 2; i <= n; i++)
				person = (person + 2) % i;
			counter++;
			x = person+1;
		} while (person+1 != n);
		j++;
		cout << "Case " + to_string(j) + ": " << counter - 1 << " " << person+1 << endl;
	}
	system("pause");
	return 0;
}