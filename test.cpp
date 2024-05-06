#include <bits/stdc++.h>
using namespace std;


void calMN(ll k){
    double delta = 1 + 4*(k - 0.5);
    ll n = (1 + sqrt(delta))/2;
    double m;
    while(n >= 2){
        m =(double) (n + 2*k - 1)/(2 * n - 1);
        if(m < 2){
            cout << -1 << ' ' << -1 << endl;
            return ;
        }
        ll test = m;
        if(m == test){
            if(m > n){
                ll flag = m;
                m = n;
                n = flag;
            }
            cout << m-1 << ' ' << n-1 << endl;
            return;
        }
        else{
            n--;
        }
    }
    cout << -1 << ' ' << -1 << endl;
}