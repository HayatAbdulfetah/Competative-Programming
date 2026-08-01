#include<bits/stdc++.h>
using namespace std;
int main() {
    char last='\0';
    int ans=1,n;
    cin>>n;
    for(int i=0; i<n; i++) {
        string t;
        cin>>t;
        if(t[0]==last) {
            ans++;
        }
        last=t[1];
    }
    cout<<ans<<"\n";
    return 0;

}


// problem link --> https://codeforces.com/problemset/problem/344/A
