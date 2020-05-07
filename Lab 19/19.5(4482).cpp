#include <math.h>
#include <iostream>
#include <cmath>
#include <string>
#include <vector>

using namespace std;

int comp(int a, int b) {
	return (a == b) ? a : 0;
}

class SegmentTree {
public:
	int k, n, size;
	vector<int> items;
	SegmentTree(vector<int> arr);
	void update(int i, int x);
	int sum(int left, int right);
};

SegmentTree::SegmentTree(vector<int> arr) {
	k = arr.size();
	n = 1 << (int)ceil(log2(k));
	int i;
	items.resize(2 * n);
	fill(items.begin(), items.end(), 0);
	for (i = 0; i < k;i++)
		items[n + i] = arr[i];
	for (i = n - 1; i > 0;i--)
		items[i] = comp(items[2 * i], items[2 * i + 1]);
	size = n;
}

void SegmentTree::update(int i, int x) {
	i += size;
	items[i] = x;
	while (i > 0)
	{
		i /= 2;
		items[i] = comp(items[2 * i], items[2 * i + 1]);
	}
}

int SegmentTree::sum(int left, int right) {
	left += size;
	right += size;
	int res = items[left];

	while (left <= right) {
		if (left % 2 == 1)
			res = comp(res, items[left]);
		if (right % 2 == 0)
			res = comp(res, items[right]);
		left = (left + 1) / 2;
		right = (right - 1) / 2;
	}
	return res;
}

int main3(void) {
	int n, m, k1, k2, k3, x;
	string str;
	scanf("%d", &n);
	vector<int> arr;
	for (int i = 0; i < n; i++) {
		scanf("%d", &x);
		arr.push_back(x);
	}
	scanf("%d", &m);
	SegmentTree tree = SegmentTree(arr);
	for (int i = 0; i < m; i++) {
		scanf("%d %d %d", &k1, &k2, &k3);
		if (k1 == 1)
			cout << ((tree.sum(k2 - 1, k3 - 1) != 0) ? "draw\n" : "wins\n");
		else if (k1 == 2)
			tree.update(k2 - 1, k3);
	}
	system("pause");
	return 0;
}