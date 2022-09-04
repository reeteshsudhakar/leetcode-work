class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        
        PriorityQueue<Pair> pq = new PriorityQueue<>();
        
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            pq.add(new Pair(entry.getKey(), entry.getValue()));
        }
        
        int[] result = new int[k];
        
        for (int i = 0; i < k; i++) {
            result[i] = pq.poll().val;
        }
        
        return result;
    }
}

class Pair implements Comparable<Pair> {
    int val;
    int frequency;
    
    public Pair(int val, int frequency) {
        this.val = val;
        this.frequency = frequency;
    }
    
    public int compareTo(Pair pair) {
        return pair.frequency - this.frequency;
    }
}