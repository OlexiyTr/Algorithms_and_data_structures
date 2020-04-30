#include <iostream>
#include <vector>
#include <string.h>

using namespace std;

class Node {
public:
	int next[10];
	int out, leaf;
	Node(){
		for (int i = 0; i < 10; i++) next[i] = -1;
		out = leaf = 0;
	}
};

class Tree1 {
public:
	vector<Node> tree;

	Tree1();
	void Insert(char *s);
	int CheckTrie(void);
};

Tree1::Tree1() {
	tree.clear();
	tree.resize(1);
}

void Tree1::Insert(char *s) {
	int v = 0;
	for (int i = 0; i < strlen(s); ++i) {
		char c = s[i] - '0';
		if (tree[v].next[c] == -1) {
			tree[v].next[c] = tree.size();
			tree[v].out++;
			tree.push_back(Node());
		}
		v = tree[v].next[c];
	}
	tree[v].leaf++;
}

int Tree1::CheckTrie(void) {
	for (int i = 0; i < tree.size(); i++)
		if ((tree[i].leaf > 1) || ((tree[i].leaf == 1) && (tree[i].out)))
			return 1;
	return 0;
}

int main1(void) {
	int tests, n;
	char number[10];
	Tree1 *t;
	scanf("%d", &tests);
	while (tests--)
	{
		scanf("%d\n", &n);
		t = new Tree1();
		for (int i = 0; i < n; i++){
			gets_s(number);
			t->Insert(number);
		}
		if (t->CheckTrie()) printf("NO\n"); else printf("YES\n");
	}
	return 0;
}