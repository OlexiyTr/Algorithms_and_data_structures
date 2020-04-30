#include <iostream>
#include <cstdio>
#include <vector>
#include <stdio.h>
#include <cstring>

#define MAX 100010
#define min_el(a,b) ((a < b) ? a : b)

using namespace std;

struct Node {
	long long min, add;
	int Lpos, Rpos;
	Node* Left = NULL;
	Node* Right = NULL;
public:
	Node(long long _min, long long _add, Node* _Left, Node* _Right, int _Lpos, int _Rpos) :
		min(_min), add(_add), Left(_Left), Right(_Right), Lpos(_Lpos), Rpos(_Rpos) {}
	long long getMin() { return min; }
};

class Stack {
public:
	Node* top = NULL;
	Stack(vector<int> &v, int L, int R);
	Node* Create(vector<int> &v, int L, int R);
	void Add(Node *&tree, int L, int R, int value);
	bool empty();
	long long Top();
};

long long Stack::Top() {
	return this->top->min;
}

Stack::Stack(vector<int> &v, int L, int R) {
	top = Create(v, L, R);
}

Node* Stack::Create(vector<int> &v, int L, int R) {
	if (L == R) {
		Node *node = new Node(v[L], 0, NULL, NULL, L, L);
		return node;
	}
	int mid = (R + L) / 2;
	Node *Left = Create(v, L, mid);
	Node *Right = Create(v, mid + 1, R);
	Node *Tree = new Node(min_el(Left->min, Right->min),0,Left,Right,Left->Lpos,Right->Rpos);
	return Tree;
}

void Stack::Add(Node *&Tree, int L, int R, int value) {
	if (L < Tree->Lpos)
		L = Tree->Lpos;
	if (R > Tree->Rpos)
		R = Tree->Rpos;
	if (L > R) return;
	if (Tree->add) {
		if (Tree->Left != NULL)
			Tree->Left->add += Tree->add,
			Tree->Left->min += Tree->add;
		if (Tree->Right != NULL)
			Tree->Right->add += Tree->add,
			Tree->Right->min += Tree->add;
		Tree->add = 0;
	}
	if (Tree->Lpos == L && Tree->Rpos == R) {
		Tree->add += value;
		Tree->min += value;
		return;
	}
	Add(Tree->Left, L, R, value);
	Add(Tree->Right, L, R, value);
	Tree->min = min_el(Tree->Left->min, Tree->Right->min);
}

bool Stack::empty() {
	return top == NULL;
}

int i, k, n, p, sum;
char str[MAX];
vector<int> v;

int main1(void) {
	gets_s(str); int n = strlen(str);
	for (sum = i = 0; i < n; i++){
		if (str[i] == '(') sum++; else sum--;
		v.push_back(sum);
	}
	Stack s(v, 0, n - 1);
	scanf("%d", &k);
	while (k--){
		scanf("%d", &p);
		if (str[p] == '('){
			str[p] = ')';
			s.Add(s.top, p, n - 1, -2);
			sum -= 2;
		}
		else{
			str[p] = '(';
			s.Add(s.top, p, n - 1, 2);
			sum += 2;
		}
		if ((s.Top() >= 0) && (sum == 0)) printf("+\n");
			else printf("-\n");
		}
	system("pause");
	return 0;
}