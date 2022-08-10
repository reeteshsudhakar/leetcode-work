class MinStack {
    
    Stack<MinPair> stack;

    public MinStack() {
        this.stack = new Stack<>();
    }
    
    public void push(int val) {
        int min;
        if (this.stack.isEmpty() || this.stack.peek().getMin() > val) {
            min = val;
        } else {
            min = this.stack.peek().getMin();
        }
        
        this.stack.push(new MinPair(val, min));
    }
    
    public void pop() {
        this.stack.pop();
    }
    
    public int top() {
        return this.stack.peek().getVal();
    }
    
    public int getMin() {
        return this.stack.peek().getMin();
    }
}

class MinPair {
    private int val;
    private int min;
    
    public MinPair(int val, int min) {
        this.val = val;
        this.min = min;
    }
    
    public int getVal() {
        return this.val;
    }
    
    public int getMin() {
        return this.min;
    }
}