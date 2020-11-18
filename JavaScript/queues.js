// comes from linked list idea

class make_node {
    constructor(value) {
        this.value = value,
        this.next = null;
    }
}

class queue {
    constructor() {
        this.first = null;
        this.last = null;
        this.length = 0;
    }

    peek() {
        return this.first;
    }

    enqueue(value) {
        const node_toadd = new make_node(value);
        if (this.length === 0) {
            this.first = node_toadd;
            this.last = node_toadd;
        } else {
            this.last.next = node_toadd;
            this.last 
        }
        this.length++
        return this
    }

    dequeue() {
        if (this.length === 0) {
            return null;
        } 
        if (this.length === 1) {
            console.log("length is one")
            this.last = null;
        }
        // const hold_pointer = this.first;
        this.first = this.first.next;
        this.length--;
        // return hold_pointer;
    }

}

const myqueue = new queue();
myqueue.enqueue("Shantanu")
myqueue.enqueue("Viransh")
myqueue.dequeue()
myqueue.dequeue()
console.log(myqueue)

// Simple exercises:

// Implement queues using stacks??

