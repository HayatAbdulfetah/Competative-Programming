#include<stdio.h>
int main() {
    int n,a=0,d=0;
    char str[n];
    scanf("%d",&n);
    scanf("%s",str);
    for(int i=0; str[i]!='\0'; i++) {
        if(str[i]=='A')
            a++;
        else
            d++;
 
    }
    if(a==d)
        printf("Friendship");
    else if(a>d)
    printf("Anton");
    else if(d>a)
    printf("Danik");
    return 0;
}

// problem link --> https://codeforces.com/problemset/problem/734/A
