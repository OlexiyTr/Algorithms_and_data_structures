#include <iostream> 
#include <cstdio>
#include <queue>
#include <algorithm>
using namespace std;

int main10()
{
	int n; 
	scanf("%u", &n);
	int *input = new int[n];
	for (int i = 0; i < n; i++)
		scanf("%d", input + i);
	int k; 
	scanf("%u", &k);
	queue<int> *sorting = new queue<int>[k];
	int *order = new int[n];
	int j;
	for (int i = 0; i < n; i++) {
		j = 0;
		while (1)
		{
			if (sorting[j].empty() || sorting[j].back() <= input[i]) {
				sorting[j].push(input[i]);
				order[i] = j + 1;
				break;
			}
			j++;
			if (j >= k) {
				cout << "NO";
				return 0;
			}
		}
	}

	cout << "YES" << endl;
	for (int i = 0; i < n; i++) {
		printf("I(%d)\n", order[i]);
	}
	for (int i = 0; i < n; i++) {
		queue<int>* minimum = min_element(sorting, sorting + k,
			[&](const queue<int> x, const queue<int> y) {
			return !x.empty() && !y.empty() && x.front() < y.front();
		});
		minimum->pop();
		printf("R(%d)\n", minimum - sorting + 1);
	}
	delete[] sorting;
	system("pause");
	return 0;
}