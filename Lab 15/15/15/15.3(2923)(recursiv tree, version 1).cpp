#include <iostream>
#include <set>
#include <list>
#include <queue>

using namespace std;

#define MAX 1000010

int res[MAX];

class Node
{
public:
	int _key;
	set<int> _col;
	Node(int key) : _key(key) {};
	Node(int key, int color) {
		_key = key;
		_col.insert(color);
	}
};

class Tree {
public:
	Node* _V;
	list<Tree*> children;
	Tree(int key);
	Tree(int key, int color);
	void addChild(Tree* child);
	void add(int parent, int child, int color);
	void DFS(Tree* node);
	Tree* BFS(int v);
};

Tree::Tree(int key) {
	_V = new Node(key);
};
Tree::Tree(int key, int color) {
	_V = new Node(key, color);
};

Tree* Tree::BFS(int v) {
	queue<Tree*> que;
	Tree* node;
	que.push(this);
	while (!que.empty()) {
		node = que.front();
		que.pop();
		if (node->_V->_key == v)
			return node;
		for (list<Tree*>::iterator it = children.begin(); it != children.end();it++)
			que.push(*it);
	}
	return NULL;
}

void Tree::addChild(Tree* child) { children.push_front(child); }

void Tree::add(int parent, int child, int color) {
	Tree* par = BFS(parent), *tm;
	if (par != NULL)
		par->addChild(new Tree(child, color));
}

void Tree::DFS(Tree* node) {
	int i;
	Tree* to;
	for (list<Tree*>::iterator it = node->children.begin(); it != node->children.end(); ++it) {
		to = *it;
		DFS(to);
		if (node->_V->_col.size() < to->_V->_col.size()) 
			node->_V->_col.swap(to->_V->_col);
		node->_V->_col.insert(to->_V->_col.begin(), to->_V->_col.end());
	}
	res[node->_V->_key] = node->_V->_col.size();
}

int main2(void) {
	int n, p, c, i;
	scanf("%d", &n);
	scanf("%d %d", &p, &c);
	Tree* tree, *tmp;
	if (p == 0)
		tree = new Tree(1, c);
	else {
		tree = new Tree(p);
		tree->addChild(new Tree(1, c));
	}
	for (i = 2; i <= n; i++) {
		scanf("%d %d", &p, &c);
		if (p == 0)
			tree->_V->_col.insert(c);
		else if (i < p) {
			tree->_V->_col.insert(c);
			tmp = tree;
			tree = new Tree(p);
			tree->addChild(tmp);
		}
		else {
			tree->add(p, i, c);
		}
	}
	tree->DFS(tree);
	for (i = 1; i <= n; i++)
		printf("%d ", res[i]);
	printf("\n");
	system("pause");
	return 0;
}