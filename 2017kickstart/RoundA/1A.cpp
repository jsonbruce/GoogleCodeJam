#include <bits/stdc++.h>
using namespace std;

constexpr int MOD = 1000000007;

int main()
{
    int T;
    scanf("%d",&T);
    for (int tt = 1; tt <= T; tt++)
    {
        printf("Case #%d: ", tt);
        int aa, bb;
        scanf("%d%d",&aa,&bb);
        unsigned __int128 a = aa, b = bb;
        if (a < b) swap(a, b);
        printf("%d\n", (unsigned)((b-1)*b*(b+1)*(2*a-b)/12 % MOD));
    }
}
