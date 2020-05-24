#include <stdio.h>
#include <vector>

using namespace std;

struct vertex {
	int used, color;
	vector<int> g, gr;
};

void dfs(int i);
void dfs_second(int i, int color);

vector <int> lst;
vector <vertex> v;

void dfs(int i) {
	v[i].used = 1;
	for (int ii = 0; ii < v[i].g.size(); ii++) {
		int to = v[i].g[ii];
		if (!v[to].used) dfs(to);
	}
	lst.push_back(i);
}

void dfs_second(int i, int color) {
	v[i].used = 2;
	v[i].color = color;
	for (int ii = 0; ii < v[i].gr.size(); ii++) {
		int to = v[i].gr[ii];
		if (v[to].used != 2) dfs_second(to, color);
	}
}

int main() {
	int n, m, color = 0;
	scanf("%d %d", &n, &m);
	v.resize(n);
	while (m--) {
		static int a, b;
		scanf("%d %d", &a, &b);
		v[a - 1].g.push_back(b - 1);
		v[b - 1].gr.push_back(a - 1);
	}
	for (int i = 0; i < n; i++) 
		if (!v[i].used) dfs(i);
	for (int i = lst.size() - 1; i >= 0; i--) 
		if (v[lst[i]].used != 2) dfs_second(lst[i], color++);
	printf("%d\n", color);
	return 0;
}