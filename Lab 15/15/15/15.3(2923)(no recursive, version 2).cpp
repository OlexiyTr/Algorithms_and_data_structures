#include <iostream>
#include <vector>
#include <set>
#define MAX 1000010

using namespace std;

int color[MAX], result[MAX];
vector<vector<int>> tree;
set<int> s[MAX];

void DFS(int v) {
	int i, to;
	s[v].insert(color[v]);
	for (i = 0; i < tree[v].size(); i++) {
		to = tree[v][i];
		DFS(to);
		if (s[v].size() < s[to].size()) s[v].swap(s[to]);
		s[v].insert(s[to].begin(), s[to].end());
		s[to].clear();
	}
	result[v] = s[v].size();
}

int main4() {
	int n, p, c;
	cin >> n;
	tree.resize(n + 1);
	for (int i = 1; i <= n; i++) {
		cin >> p >> c;
		tree[p].push_back(i);
		color[i] = c;
	}
	DFS(0);
	for (int i = 1; i <= n; i++)
		cout << result[i] << " ";
	return 0;
}