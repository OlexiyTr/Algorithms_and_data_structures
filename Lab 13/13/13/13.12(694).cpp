#include <cstdio>
#include <iostream> 
#include <string>
#include <deque>

using namespace std;

/*
dont work
bool mn = false;
long long Res = 0;
scanf("%d %d %d %d %d", &n, &a, &b, &c, &x);
for (i = 1; i <= n; i++) {
x = ((1LL * a * x * x + 1LL * b * x + c) / 100) % 1000000LL;
if (x % 5 < 2) {
if (!min.empty()) {
if (mn)
min.pop_front();
else
min.pop_back();
}
}
else {
if (!min.empty() && min.front() > x) {
min.push_front(x);
mn = true;
}
else {
min.push_back(x);
mn = false;
}
if (!min.empty()) Res += min.front();
}
}
*/

int main9() {
	deque<int> value, min;
	int x, i, n, a, b, c;
	long long Res = 0;
	scanf("%d %d %d %d %d", &n, &a, &b, &c, &x);
	for (i = 1; i <= n; i++) {
		x = ((1LL * a * x * x + 1LL * b * x + c) / 100) % 1000000LL;
		if (x % 5 < 2) {
			if (!value.empty()){
				if (value.front() == min.front()) 
					min.pop_front();
				value.pop_front();
			}
		}
		else {
			value.push_back(x);
			while (!min.empty() && (x < min.back())) 
				min.pop_back();
			min.push_back(x);
		}
		if (!min.empty()) Res += min.front();
	}
	printf("%lld\n", Res);
	system("pause");
	return 0;
}