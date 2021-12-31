class MinStack {
    
    Stack<Integer> stack;
    PriorityQueue<Integer> priorityQueue;

    public MinStack() {
        this.stack = new Stack<>();
        this.priorityQueue = new PriorityQueue<>();
    }
    
    public void push(int val) {
        stack.push(val);
        priorityQueue.add(val);
    }
    
    public void pop() {
        int val = stack.pop();
        priorityQueue.remove(val);
        
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return priorityQueue.peek();
        
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */