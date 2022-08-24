class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> map = new HashMap<>();
        
        for (String word : words) {
            map.put(word, map.getOrDefault(word, 0) + 1);
        }
        
        Queue<Pair> pq = new PriorityQueue<>((a, b) -> a.frequency == b.frequency ? a.word.compareTo(b.word) : b.frequency - a.frequency);
        
        List<String> result = new ArrayList<>();
        
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            pq.add(new Pair(entry.getKey(), entry.getValue()));
        }
        
        for (int i = 0; i < k; i++) {
            result.add(pq.poll().word);
        }
        
        return result;
        
    }
    
    class Pair {
        String word;
        int frequency;
        
        Pair(String word, int frequency) {
            this.word = word;
            this.frequency = frequency;
        }
    }
}