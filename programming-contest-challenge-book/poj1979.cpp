// http://poj.org/problem?id=1979

#include <iostream>

using namespace std;

char m[21][21];
int w, h;

int dfs(int x, int y) {
    if(m[y][x] == '#') {
        return 0;
    }
    m[y][x] = '#';
    int n = 1;

    if(x > 0) {
        n += dfs(x - 1, y);
    }
    if(x < w - 1) {
        n += dfs(x + 1, y);
    }
    if(y > 0) {
        n += dfs(x, y - 1);
    }
    if(y < h - 1) {
        n += dfs(x, y + 1);
    }
    return n;
}

int main(void) {    
    while(true) {
        cin >> w >> h;
        if(w == 0 && h == 0) {
            return 0;
        }
        int x, y;
        for(int i = 0; i < h; i++) {
            cin >> m[i];
            for(int j = 0; j < w; j++) {
                if(m[i][j] == '@') {
                    x = j;
                    y = i;
                    break;
                }
            }
        }
        cout << dfs(x, y) << endl;
    }
    return 0;
}