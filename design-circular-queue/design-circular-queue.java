class MyCircularQueue {
    int[] queue;
    int head;
    int tail;
    int size;

    public MyCircularQueue(int k) {
        this.queue = new int[k];
        this.head = -1;
        this.tail = -1;
        this.size = k;
    }
    
    public boolean enQueue(int value) {
        if (this.isFull()) {
            return false;
        } else if (this.isEmpty()) {
            head = 0;
        }
        
        this.tail = (this.tail + 1) % size;
        this.queue[tail] = value;
        
        return true;

    }
    
    public boolean deQueue() {
        if (this.isEmpty()) {
            return false;
        } else if (this.head == this.tail) {
            this.head = -1;
            this.tail = -1;
            return true;
        }
        
        this.head = (this.head + 1) % size;
        return true;
    }
    
    public int Front() {
        if (this.isEmpty()) {
            return -1;
        } 
        
        return this.queue[head];
    }
    
    public int Rear() {
        if (this.isEmpty()) {
            return -1;
        }
        
        return this.queue[tail];
    }
    
    public boolean isEmpty() {
        return this.head == -1 && this.tail == -1;
    }
    
    public boolean isFull() {
        return (this.tail + 1) % size == head;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */