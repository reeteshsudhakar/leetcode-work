class Solution {
    public int countPrimes(int n) {
        boolean[] primes = new boolean[n];
        
        for (int i = 2; i < n; i++) {
            primes[i] = true;
        }
        
        for (int i = 2; i * i < n; i++) {
            if (primes[i] == false) {
                continue;
            }
            
            for (int j = i * 2; j < n; j += i) {
                primes[j] = false;
            }
        }
        
        int counter = 0;
        
        for (boolean i : primes) {
            if (i) {
                counter++;
            }
        }
        
        return counter;
    }
}