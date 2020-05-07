#include <math.h>
#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>

#define MAX 1000000
#define INF 2000000000

using namespace std;

struct node
{
	long long min, max;
} items[4 * MAX];

class SegmentTree {
public:
	int k, n, size;
	vector<pair<int, int> > items;
	SegmentTree(vector<pair<int, int> >);
	int MinMax(int left, int right);
	void update(int i, int x);
};

SegmentTree::SegmentTree(vector<pair<int, int> > arr) {
	k = arr.size();
	n = 1 << (int)ceil(log2(k));
	int i;
	items.resize(2 * n, make_pair(INF, -INF));
	for (i = 0; i < k;i++)
		items[n + i] = arr[i];
	for (i = n - 1; i > 0;i--)
		items[i].first = min(items[2 * i].first, items[2 * i + 1].first),
		items[i].second = max(items[2 * i].second, items[2 * i + 1].second);
	size = n;
}

int SegmentTree::MinMax(int left, int right) {
	int minRes = INF, maxRes = -INF;
	left += size, right += size;
	while (left <= right){
		if (left & 1)
			minRes = min(minRes, items[left].first),
			maxRes = max(maxRes, items[left].second);
		if (!(right & 1))
			minRes = min(minRes, items[right].first),
			maxRes = max(maxRes, items[right].second);
		left = (left + 1) / 2, right = (right - 1) / 2;
	}
	return maxRes - minRes;
}

void SegmentTree::update(int i, int x){
	i += size;
	items[i] = make_pair(x, x);
	while (i /= 2)
		items[i].first = min(items[2 * i].first, items[2 * i + 1].first),
		items[i].second = max(items[2 * i].second, items[2 * i + 1].second);
}
int main(void) {
	int i, x, y, k, ai;
	vector<pair<int, int> > arr;
	for (i = 1; i <= 100000; i++) {
		ai = (i * i) % 12345 + ((i * i) % 23456 * i) % 23456;
		arr.push_back(make_pair(ai, ai));
	}
	SegmentTree tree = SegmentTree(arr);
	scanf("%d", &k);
	while (k--){
		scanf("%d %d", &x, &y);
		if (x > 0) printf("%d\n", tree.MinMax(x-1, y-1));
		else tree.update(-x - 1, y);
	}
	system("pause");
	return 0;
}