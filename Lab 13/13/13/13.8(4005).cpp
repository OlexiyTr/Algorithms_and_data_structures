#include <iostream> 
#include <string>
#include <queue>

using namespace std;

int main1(void) {
	int n, i, el, f_c, s_c;
	queue<int> first, second;
	cin >> n;
	for (i = 0;i < n / 2;i++) {
		cin >> el;
		first.push(el);
	}
	for (i = 0;i < n / 2;i++) {
		cin >> el;
		second.push(el);
	}
	i = 0;
	while (i<200000)
	{
		i++;
		f_c = first.front();
		first.pop();
		s_c = second.front();
		second.pop();
		if (f_c == 0 && s_c == n - 1) {
			first.push(f_c);
			first.push(s_c);
		}
		else if (f_c == n - 1 && s_c == 0) {
			second.push(f_c);
			second.push(s_c);
		}
		else if (f_c > s_c) {
			first.push(f_c);
			first.push(s_c);
		}
		else {
			second.push(f_c);
			second.push(s_c);
		}
		if (first.empty()) {
			cout << "second " << i;
			return 0;
		}
		else if (second.empty()) {
			cout << "first " << i;
			return 0;
		}
	}
	cout << "draw";
	return 0;
}