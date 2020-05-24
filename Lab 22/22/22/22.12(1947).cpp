#include <iostream>
#include <vector>
#include <set>

using namespace std;

struct vertex {
	int used, color;
	vector<int> g, gr;
};

vector <int> lst;
vector <vertex> v;
int a, b, n, m, color = 0;

void dfs_1(int i) {
	v[i].used = 1;
	for (int ii = 0; ii < v[i].g.size(); ii++) {
		int to = v[i].g[ii];
		if (!v[to].used) 
			dfs_1(to);
	}
	lst.push_back(i);
}

void dfs_2(int i, int color) {
	v[i].used = 2;
	v[i].color = color;
	for (int ii = 0; ii < v[i].gr.size(); ii++) {
		int to = v[i].gr[ii];
		if (v[to].used != 2) 
			dfs_2(to, color);
	}
}

int main() {
	scanf("%d %d", &n, &m);
	v.resize(n);
	while (m--) {
		scanf("%d %d", &a, &b);
		v[a - 1].g.push_back(b - 1);
		v[b - 1].gr.push_back(a - 1);
	}
	for (int i = 0; i < n; i++) 
		if (!v[i].used) 
			dfs_1(i);
	for (int i = lst.size() - 1; i >= 0; i--) 
		if (v[lst[i]].used != 2) 
			dfs_2(lst[i], color++);
	set <int> st[10000];
	for (int i = 0; i < n; i++)
		for (int j = 0; j < v[i].g.size(); j++)
			if (v[i].color != v[v[i].g[j]].color) 
				st[v[i].color].insert(v[v[i].g[j]].color);

	int ans = 0;
	for (int i = 0; i < 10000; i++) 
		ans += st[i].size();
	printf("%d\n", ans);
	return 0;
}