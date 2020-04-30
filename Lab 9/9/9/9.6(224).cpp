#include <iostream> 
#include <limits.h> 
#include <list> 
#include <stack> 
#include <vector> 

using namespace std;

int val1, val2, val3;
int pr1, pr2, pr3;
float max_score = 0;

class AdjListNode {
	int v;
	float weight[4];

public:
	AdjListNode(int _v, int _w, int _pod1, int _pod2, int _pod3)
	{
		v = _v;
		weight[0] = _w; weight[1] = _pod1*0.01; weight[2] = _pod2*0.01; weight[3] = _pod3*0.01;
	}
	int getV() { return v; }
	float getWeight() { return weight[0] + weight[1] * pr1*val1 + weight[2] * pr2*val2 + weight[3] * pr3*val3; }
};

class Graph {
	int V;
	list<AdjListNode>* adj;

public:
	Graph(int V);
	~Graph();

	void addEdge(int u, int v, int weight, int pod1, int pod2, int pod3);
	void MaxScore(int u, int finish, float score, vector<bool> visited);
	int get_V() { return V; }
};

using namespace std;

Graph::Graph(int V)
{
	this->V = V;
	adj = new list<AdjListNode>[V];
}

Graph::~Graph()
{
	delete[] adj;
}

void Graph::addEdge(int u, int v, int weight, int pod1, int pod2, int pod3)
{
	AdjListNode node(v, weight, pod1, pod2, pod3);
	adj[u].push_back(node);
}

void Graph::MaxScore(int u, int finish, float score, vector<bool> visited) {
	list<AdjListNode>::iterator i;
	if (visited[u])
		return;
	else
		visited[u] = true;
	if (u == finish) {
		if (max_score < score)
			max_score = score;
		return;
	}
	if (score <= max_score)
		return;
	for (i = adj[u].begin(); i != adj[u].end(); ++i) {
		AdjListNode node = *i;
		MaxScore(node.getV(), finish, score - node.getWeight(), visited);
	}
}

int main()
{
	int N, M;
	int i;
	scanf("%d %d", &N, &M);
	scanf("%d %d %d", &pr1, &pr2, &pr3);
	scanf("%d %d %d", &val1, &val2, &val3);
	int s_1 = pr1;int s_2 = pr2;int s_3 = pr3;
	Graph g(N);
	int lst[510][3];
	lst[0][0] = 0; lst[0][1] = 0; lst[0][2] = 0;
	lst[N - 1][0] = 0; lst[N - 1][1] = 0; lst[N - 1][2] = 0;
	for (i = 0; i < N + 2 - 4; i++)
		scanf("%d %d %d", &lst[i + 1][0], &lst[i + 1][1], &lst[i + 1][2]);
	for (i = 0; i < M; i++) {
		int u, v, w;
		scanf("%d %d %d", &u, &v, &w);
		g.addEdge(u - 1, v - 1, w, lst[v - 1][0], lst[v - 1][1], lst[v - 1][2]);
	}
	vector< bool > visited(g.get_V(), false);
	for (pr1 = s_1; pr1 >= 0;pr1-=s_1)
		for (pr2 = s_2;pr2 >= 0;pr2-=s_2)
			for (pr3 = s_3;pr3 >= 0;pr3-=s_3) {
				g.MaxScore(0, N-1, pr1*val1 + pr2*val2 + pr3*val3, visited);
			}
	if (max_score <= 0)
		printf("0.00");
	else
		printf("%.2f", max_score);
	system("pause");
	return 0;
}