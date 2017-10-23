#include<cstdio>
#include<algorithm>
using namespace std;

typedef long long ll;
const ll MOD = 1e9 + 7;
const int NMAX = 11111;
ll p2[NMAX];
ll A[NMAX];

int main(){
	freopen("small.in", "r", stdin);
	freopen("small.out", "w", stdout);

	p2[0] = 1;
	for (int i = 1; i <= 10000; i++)
		p2[i] = p2[i - 1] * 2 % MOD;

	int T; scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++){
		int N; scanf("%d", &N);
		for (int i = 1; i <= N; i++) scanf("%lld", A + i);

		ll ans = 0;
		for (int i = 1; i <= N; i++) for (int j = i + 1; j <= N; j++){
			ll cur = A[j] - A[i];
			ll det = p2[j - i - 1];
			ans = (ans + cur*det%MOD) % MOD;
		}
		printf("Case #%d: %lld\n", tc, ans);
	}
}
