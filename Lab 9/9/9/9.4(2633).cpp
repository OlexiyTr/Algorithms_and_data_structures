#include <cstdio>
#include <iostream>
using namespace std;

int mtx[7][14];
int arr[14];
int visited[14];

int min(int a, int b) {
	return a<b ? b : a;
}

int main() {
	int n;
	scanf("%d", &n);
	n = n;
	for (int i = 1; i <= n*2; i++) {
		scanf("%d", &arr[i]);
		mtx[0][i] = arr[i];
	}

	for (int i = 1; i <= n; i++)
		for (int j = 0; j <= n*2; j++) {
			mtx[i][j] = arr[j] + mtx[i - 1][j];
		}
	for (int i = 1; i <= n * 2; i++) {
		printf("%d ", mtx[n][i]);
	}
	system("pause");
	return 0;
}