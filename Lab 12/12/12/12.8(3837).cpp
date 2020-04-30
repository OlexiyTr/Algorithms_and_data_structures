#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cctype>

using namespace std;

string str;
vector<string> res;

void step(int &pos, int d) {
	res[d] += str[pos];
	cout << "res:\n";
	for (int i = 0; i<res.size();i++)
		cout << res[i] << endl;
	cout << " str: " << str << endl;
	--pos;
	if (islower(str[pos + 1]))
		return;
	step(pos, d + 1);
	step(pos, d + 1);
}

int main4() {
	int tc;
	cin >> tc;
	while (tc--) {
		cin >> str;
		int len = str.size();
		res.assign(len, "");
		int pos = len - 1;
		step(pos, 0);
		for (vector<string>::reverse_iterator it = res.rbegin(); it != res.rend(); ++it)
			cout << *it;
		cout << endl;
	}
	system("pause");
	return 0;
}