#include <cstdio>
using namespace std;

int mtr[1024][1024];
int array[1024];

int max(int a, int b) {
	return a<b ? b : a;
}

int main() {
	int n;
	while (scanf("%d", &n) == 1) {
		int k;
		scanf("%d", &k);
		for (int i = 1; i <= k; i++) {
			scanf("%d", &array[i]);
		}
		for (int i = 1; i <= k; i++)
			for (int j = 0; j <= n; j++)
				if (array[i] <= j) {
					mtr[j][i] = max(mtr[j][i - 1], array[i] + mtr[j - array[i]][i - 1]);
				}
				else { mtr[j][i] = mtr[j][i - 1]; }
				printf("sum:%d\n", mtr[n][k]);
	}
	return 0;
}