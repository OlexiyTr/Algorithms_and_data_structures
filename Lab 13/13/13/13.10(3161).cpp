#include <iostream> 
#include <string>

using namespace std;

#define MAX 150001

struct Node
{
	int data;
	Node *next, *prev;

	Node() { prev = next = NULL; }
	Node(int item) {
		data = item;
		prev = next = NULL;
	}
};

class Deque {
private:
	Node *mFront, *mBack;
public:
	Deque() { mFront = mBack = NULL; }

	void push_back(int item) {
		Node *node = new Node(item);
		if (mFront == NULL)
			mFront = mBack = node;
		else {
			node->prev = mBack;
			node->next = NULL;
			mBack->next = node;
			mBack = node;
		}
	}

	void push_front(int item) {
		Node *node = new Node(item);
		if (mFront == NULL)
			mFront = mBack = node;
		else {
			node->next = mFront;
			node->prev = NULL;
			mFront->prev = node;
			mFront = node;
		}
	}

	int pop_front() {
		Node *node = mFront;
		int item = mFront->data;
		if (mFront == mBack)
			mFront = mBack = NULL;
		else {
			mFront = mFront->next;
			mFront->prev = NULL;
		}
		delete node;
		return item;
	}

	int pop_back() {
		Node *node = mBack;
		int item = mBack->data;
		if (mFront == mBack)
			mFront = mBack = NULL;
		else {
			mBack = mBack->prev;
			mBack->next = NULL;
		}
		delete node;
		return item;
	}

	int empty(void) { return mFront == NULL; }

	int front(void) { return mFront->data; }

	int back(void) { return mBack->data; };
};

int main(void) {
	Deque dq[MAX];
	int n, ind, item;
	string str;
	cin >> n;
	while (n--)
	{
		cin >> str >> ind;
		if (str == "pushback") {
			scanf("%d\n", &item);
			dq[ind].push_back(item);
		}
		else if (str == "pushfront") {
			scanf("%d\n", &item);
			dq[ind].push_front(item);
		}
		else if (str == "popfront") {
			if(!dq[ind].empty())
				cout << (int)dq[ind].pop_front() << endl;
		}
		else if (str == "popback") {
			if (!dq[ind].empty())
				cout << (int)dq[ind].pop_back() << endl;
		}
	}
	return 0;
}