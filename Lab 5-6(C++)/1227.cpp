#include <iostream>
#include <vector>
#include <set>
#include <string>
using namespace std;

int main()
{
	string s;
	set<string> st;
	set<string>::iterator it;
	while (cin >> s)
	{
		string my_s = "";
		for (int i = 0; i<s.size(); i++)
		{
			char c = tolower(s[i]);
			if (c >= 97 && c <= 122)
				my_s += c;
			else if (my_s != "")
			{
				st.insert(my_s);
				my_s = "";
			}
		}
		if (my_s != "")
			st.insert(my_s);
	}
	for (it = st.begin(); it != st.end(); it++)
	{
		cout << *it << endl;
	}
}