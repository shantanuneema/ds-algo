// linked list creation
// 10 -> 5 -> 16

// Javascript doesn't have linked list

class make_node {
    constructor(value) {
        this.value = value,
        this.next = null;
    }
}

class LinkedList {
    
    constructor(value, next) {
        this.head = {
            value: value,
            next: null
        }
        this.tail = this.head;
        this.length = 1;
    }

    append(value) {
        const node = new make_node(value)
        this.tail.next = node;
        this.tail = node;
        this.length++;
        return this
    }

    prepend(value) {
        const node = new make_node(value)
        node.next = this.head;
        this.head = node;
        this.length++;
        return this
    }

    insert(position, value) {
        const node = new make_node(value)
        if (position === 0) {
            this.prepend(value)
        } else if (position >= this.length) {
            this.append(value)
        } else {
            const in_node = this.traverse(position-1);
            const out_node = in_node.next;
            in_node.next = node;
            node.next = out_node
        }
        this.length++
        return this
    }

    traverse(index) {
        let counter = 0;
        let current_node = this.head;
        while (counter !== index) {
            current_node = current_node.next;
            counter++
        }
        return current_node
    }

    printLList() {
        const arr = [];
        let current_node = this.head;
        while (current_node !== null) {
            arr.push(current_node.value);
            current_node = current_node.next
        }
        return arr
    }

}

const myLinkedList = new LinkedList(10)
myLinkedList.append(5)
myLinkedList.append(16)
myLinkedList.prepend(1)
myLinkedList.insert(2,99)

console.log(myLinkedList.printLList())
