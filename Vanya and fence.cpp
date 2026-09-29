#include<iostream>
using namespace std;
int main(){
int n;
cin>>n;
int h;
cin>>h;
int arr[n];
int w=0;
for(int i=0;i<n;i++){
cin>>arr[i];
if(arr[i]>h){
w++;
}
w++;
}
cout<<w<<endl;
}

// Codeforces problem link --> https://codeforces.com/problemset/problem/677/A
