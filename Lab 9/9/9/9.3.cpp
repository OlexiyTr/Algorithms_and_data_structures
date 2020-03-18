#include <string>
#include <stdlib.h>
#include <string.h>
#include <iostream> 
#include <vector> 
#include<algorithm> 

#define INF INT_MAX

using namespace std;

vector < vector<int> > a;      // Матрица эффективности a[разраб][задача]
vector<int> xy, yx;             // Паросочетания: xy[разраб], yx[задача]
vector<bool> vx, vy;            // Альтернирующее дерево vx[разраб], vy[задача]
vector<int> maxrow, mincol;     // Способности, изученность
//vector<int> minrow, maxcol;

int n;

bool dotry(int i) {
	if (vx[i]) return false;
	vx[i] = true;
	for (int j = 0; j<n; ++j)
		if (a[i][j] - maxrow[i] == 0)
			vy[j] = true;
	for (int j = 0; j<n; ++j)
		if (a[i][j] - maxrow[i] == 0 && yx[j] == -1) {
			xy[i] = j;
			yx[j] = i;
			return true;
		}
	for (int j = 0; j<n; ++j)
		if (a[i][j] - maxrow[i] == 0 && dotry(yx[j])) {
			xy[i] = j;
			yx[j] = i;
			return true;
		}
	return false;
}

int main() {

	cin >> n;
	a.resize(n);
	for (int i = 0; i<n; i++)
	{
		a[i].resize(n);
		for (int j = 0; j<n; j++)
		{
			cin >> a[i][j];
		}
	}

	mincol.assign(n, 0);
	maxrow.assign(n, INF);
	maxrow.resize(n);
	for (int i = 0; i<n; ++i)
		for (int j = 0; j < n; ++j) 
			maxrow[i] = min(maxrow[i], a[i][j]);
	xy.resize(n);
	yx.resize(n);
	xy.assign(n, -1);
	yx.assign(n, -1);
	for (int c = 0; c<n; ) {
		vx.assign(n, 0);
		vy.assign(n, 0);
		int k = 0;
		for (int i = 0; i<n; ++i)
			if (xy[i] == -1 && dotry(i))
				++k;
		c += k;
		if (k == 0) {
			int z = INF;
			for (int i = 0; i<n; ++i)
				if (vx[i])
					for (int j = 0; j<n; ++j)
						if (!vy[j])
							z = min(z, maxrow[i]  - a[i][j]);
			for (int i = 0; i<n; ++i) {
				if (vx[i]) maxrow[i] -= z;
			}
		}
	}

	int ans = 0;
	for (int i = 0; i<n; ++i)
		ans += a[i][xy[i]];
	printf("%d\n", ans);
	system("pause");
	return 0;
}