#include <math.h>
#include <iostream>
#include <cmath>
#include <string>
#include <vector>

using namespace std;

class SegmentTree {
public:
	int k, n, size;
	vector<int> items;
	SegmentTree(vector<int> arr);
	void update(int left, int right, int item);
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
		items[i] = items[2 * i] + items[2 * i + 1];
	size = n;
}

void SegmentTree::update(int left, int right, int item) {
	left += size;
	right += size;
	int i;
	for (i = left; i <= right;i++)
		items[i] = item;
	while (left > 0)
	{
		left /= 2;
		right /= 2;
		items[left] = items[left * 2] + items[left * 2 + 1];
		items[right] = items[right * 2] + items[right * 2 + 1];
		item = items[left * 2 + 2] + items[left * 2 + 3];
		for (i = left + 1;i < right;i++)
			items[i] = item;
	}
}

int SegmentTree::sum(int left, int right) {
	left += size;
	right += size;
	int res = 0;

	while (left <= right) {
		if (left % 2 == 1)
			res += items[left];
		if (right % 2 == 0)
			res += items[right];
		left = (left + 1) / 2;
		right = (right - 1) / 2;
	}
	return res;
}

int main1(void) {
	int n, m, k1, k2, k3, x;
	string str;
	scanf("%d %d", &n, &m);
	vector<int> arr;
	for (int i = 0; i < n; i++) {
		scanf("%d", &x);
		arr.push_back(x);
	}
	SegmentTree tree = SegmentTree(arr);
	for (int i = 0; i < m; i++) {
		cin >> str;
		if (str == "?") {
			scanf("%d %d", &k1, &k2);
			printf("%d\n", tree.sum(k1 - 1, k2 - 1));
		}
		else if (str == "=") {
			scanf("%d %d %d", &k1, &k2, &k3);
			tree.update(k1 - 1, k2 - 1, k3);
		}
	}
	system("pause");
	return 0;
}