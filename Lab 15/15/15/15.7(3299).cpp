#include <iostream>
#include <vector>
#include <utility>

#define MAX 100010
#define LMAX 18

using namespace std;

vector<int> vec[MAX];
int arr_d[MAX], arr_f[MAX], mtr_u[MAX][LMAX], l, counter;

void dfs(int v, int p = 0, int len = 0) {
	int to;
	arr_d[v] = counter++; mtr_u[v][0] = p;
	for (int i = 1; i <= l; i++)
		mtr_u[v][i] = mtr_u[mtr_u[v][i - 1]][i - 1];
	for (int i = 0; i < vec[v].size(); i++) {
		to = vec[v][i];
		if (to != p) 
			dfs(to, v, len + 1);
	}
	arr_f[v] = counter++;
}

int compare(int a, int b) {
	return (arr_d[a] <= arr_d[b]) && (arr_f[a] >= arr_f[b]);
}

int LCA(int a, int b) {
	if (compare(a, b)) 
		return a;
	if (compare(b, a)) 
		return b;
	for (int i = l; i >= 0; i--)
		if (!compare(mtr_u[a][i], b)) 
			a = mtr_u[a][i];
	return mtr_u[a][0];
}

int main() {
	l = 1;
	int n, m, i, v, a1, a2;
	long long int x, y, z, sum;
	cin >> n >> m;
	while ((1 << l) <= n)  l++;
	for (i = 1; i <= n - 1; i++) {
		cin >> v;
		vec[v].push_back(i);
		vec[i].push_back(v);
	}
	counter = 0;
	dfs(0);
	cin >> a1 >> a2 >> x >> y >> z;
	v = sum = 0;
	for (i = 0; i < m; i++) {
		v = LCA((a1 + v) % n, a2);
		sum += v;
		a1 = (x * a1 + y * a2 + z) % n;
		a2 = (x * a2 + y * a1 + z) % n;
	}
	cout << sum;
	system("pause");
	return 0;
}