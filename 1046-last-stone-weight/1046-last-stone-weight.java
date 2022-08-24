class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
        
        for (int i : stones) {
            pq.add(i);
        }
        
        while (pq.size() != 1) {
            pq.add(pq.poll() - pq.poll());
        }
        
        return pq.poll();
    }
}