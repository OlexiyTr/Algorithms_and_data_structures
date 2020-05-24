#include<iostream>
#include<vector>
#define GREY 1
#define BLACK 2

using namespace std;

vector<vector<int>> graph;
vector<int> ans;
vector<int> used;
int flag;

void dfs1(int i) {
	used[i] = GREY;
	for (int j = 0; j < graph[i].size(); j++) {
		int to = graph[i][j];
		if (used[to] == 1) { flag = 1; }
		if (used[to] == 0) dfs1(to);
	}
	used[i] = BLACK;
	ans.push_back(i);
}

int main2() {
	int n, m, x, y;
	scanf("%d %d", &n, &m);
	graph.resize(n + 1);
	used.resize(n + 1);
	for (int i = 0; i < m; i++) {
		scanf("%d %d", &x, &y);
		graph[x].push_back(y);
	}
	for (int i = 1; i <= n; i++)
		if (!used[i]) dfs1(i);
	if (flag) printf("-1\n");
	else
		for (int i = n - 1; i >= 0; i--)
			printf("%d ", ans[i]);
	printf("\n");
	return 0;
}