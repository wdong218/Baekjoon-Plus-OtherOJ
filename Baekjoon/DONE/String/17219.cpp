#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    unordered_map<string, string> site;

    int n,m;
    cin >> n>>m;

    for (int i = 0; i < n; i++) {
        string key, value;
        cin >> key >> value;
        site[key] = value;
    }
    string a;
    for (int i = 0; i < m; i++) {
        cin >> a;
        cout << site[a] << endl;
    }
}