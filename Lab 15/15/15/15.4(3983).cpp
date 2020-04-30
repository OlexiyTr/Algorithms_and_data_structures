#include <iostream>
#include <set>
#include <vector>
#include <stack>

using namespace std;

vector<int> col, r;
vector<vector<int> > g;
vector<stack<int> > vec;

void dfs(int v){
	int color = col[v];
	if (vec[color].empty())
		r[v] = -1;
	else
		r[v] = vec[color].top();
	vec[color].push(v);
	for (int i = 0; i < g[v].size(); i++){
		int to = g[v][i];
		dfs(to);
	}
	vec[color].pop();
}


int main(void) {
	int n, c, i, val;
	scanf("%d %d", &n, &c);
	g.resize(n + 1);
	for (i = 2; i <= n; i++) {
		scanf("%d", &val);
		g[val].push_back(i);
	}

	col.resize(n + 1);
	for (i = 1; i <= n; i++)
		scanf("%d", &col[i]);

	vec.resize(c + 1);
	r.resize(n + 1);
	dfs(1);


	for (i = 1; i <= n; i++)
		printf("%d ", r[i]);
	printf("\n");
	system("pause");
	return 0;
}