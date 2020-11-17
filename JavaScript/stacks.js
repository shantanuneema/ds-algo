
class make_node {
    constructor(value) {
        this.value = value,
        this.next = null;
    }
}

class stack {
    constructor() {
        this.top = null;
        this.bottom = null;
        this.length = 0;
    }

    peek() {
        // to see the top value in the stack
        return this.top;
    }

    push(value) {
        // to push a new value on top (use of node like in linked list)
        const push_node = new make_node(value);
        if (this.length === 0) {
            this.top = push_node;
            this.bottom = push_node;
        } else {
            const hold_pointer = this.top;
            this.top = push_node;
            this.top.next = hold_pointer
        }
        this.length++
        return this;
    }

    pop() {
        // to take the top value removed from the stack
        if (!this.top) {
            return null;
        }
        if (this.top === this.bottom) {
            this.bottom = null;
        }
        const hold_pointer = this.top;
        this.top = this.top.next;
        this.length--
        return this
    }

}

// check above operations for stack
const mystack = new stack();
mystack.push("www.google.com")
mystack.push("www.yahoo.com")
mystack.push("www.discord.com")
// console.log(mystack.pop())

// Use of arrays to make stack (should be simpler than above):

class stack_arr {
    constructor() {
        this.array = [];
    }

    peek() {
        // to see the top value in the stack
        return this.array[this.array.length-1];
    }

    push(value) {
        // to push a new value on top (use of node like in linked list)
        this.array.push(value)
        return this;
    }

    pop() {
        // to take the top value removed from the stack
        this.array.pop()
        return this
    }

}

const mystack_ = new stack_arr();
mystack_.push("www.google.com")
mystack_.push("www.yahoo.com")
mystack_.push("www.discord.com")
mystack_.pop()
console.log(mystack_)