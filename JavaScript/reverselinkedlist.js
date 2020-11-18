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

    delete(position) {
        // const node = new make_node(value)
        if (position >= this.length) {
            console.log("Cannot delete: position do not exist")
        } else if (position === 0) {
            this.head = this.head.next;
        } else {
            const in_node = this.traverse(position-1);
            const del_node = in_node.next;
            in_node.next = del_node.next;
        }
        this.length--
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

    reverse() {
        let len_ = this.length;
        var i;
        var node_value;
        for (i=0; i<=len_; i++) {
            node_value = this.traverse(len_-1).value;
            this.node = node_value
            // console.log(make_node(node_value));
            // this.tail = node.next
        }
        // return this
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

console.log(myLinkedList.reverse().printLList())