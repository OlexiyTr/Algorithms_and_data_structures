#include <iostream>
#include <string>
#include <algorithm>
#include <stack>

using namespace std;

int main(void) {
	stack<int> s;
	int n, x, cur, ok,i;
	while (scanf("%d", &n), n){
		while (scanf("%d", &x), x){
			cur = ok = 1;
			while (!s.empty()) s.pop();
			for (i = 1; i < n; i++){
				for (;cur <= x; cur++) s.push(cur);
				if (s.top() != x) ok = 0;
				s.pop();
				scanf("%d", &x);
			}
			printf(ok ? "Yes\n" : "No\n");
		}
		printf("\n");
	}
}