#include <stdio.h>
#include <string>
#include <stdlib.h>
#include <ctype.h> 
#include <math.h>
#include <iostream>

using namespace std;

#define MAX_UINT 0x100000000
#define MAX_LEN 10024
#define fun(x)  ( (x >= 0) ? x : (x+10) )
#define fun2(x)  ( (x >= 0) ? 0 : -1 )

string findSum(string str1, string str2)
{
	string str = "";
	int carry = 0;
	string::reverse_iterator  it1 = str1.rbegin(), it2 = str2.rbegin();
	for (it1,it2; it1 != str1.rend(); ++it1, ++it2){
		int sum = ((*it1 - '0') +
			(*it2 - '0') +
			carry);
		str.push_back(sum % 10 + '0');
		carry = sum / 10;
	}
	for (it2; it2 != str2.rend(); ++it2)
	{
		int sum = ((*it2 - '0') + carry);
		str.push_back(sum % 10 + '0');
		carry = sum / 10;
	}
	if (carry)
		str.push_back(carry + '0');
	reverse(str.begin(), str.end());
	return str;
}

string findSub(string str1, string str2)
{
	string str = "";
	int carry = 0;
	string::reverse_iterator  it1 = str1.rbegin(), it2 = str2.rbegin();
	for (it1, it2; it1 != str1.rend(); ++it1, ++it2) {
		int sub = ((*it2 - '0') - (*it1 - '0') + carry);
		str.push_back(fun(sub) + '0');
		carry = fun2(sub);
	}
	for (it2; it2 != str2.rend(); ++it2)
	{
		int sub = ((*it2 - '0') + carry);
		int x = fun(sub);
		str.push_back(fun(sub) + '0');
		carry = fun2(sub);
	}
	if (carry)
		str.push_back(carry + '0');
	reverse(str.begin(), str.end());
	return str;
}

int main1()
{
	string str1 = "12";
	string str2 = "198111";
	cout << findSub(str1, str2);
	string st(5,'0');
	cout << " " << st;
	system("pause");
	return 0;
}