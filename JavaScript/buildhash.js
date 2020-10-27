class HashTable {
    constructor(size) {
    this.data = new Array(size);
    }

    _hash(key) {
        let hash = 0;
        for (let i=0; i<key.length; i++) {
            hash = (hash +key.charCodeAt(i)*i)%
            this.data.length
            // console.log(hash)
        }
        return hash;
    }

    set(key, value) {
        let address = this._hash(key)
        if (!this.data[address]) {
            this.data[address] = [];
        }
        this.data[address].push([key, value])
        return this.data
    }

    get(key) {
        let address = this._hash(key)
        const currentbucket = this.data[address];
        if (currentbucket.length) {
            for (let i=0; i<currentbucket.length; i++) {
                if (currentbucket[i][0]===key){
                    return currentbucket[i][1]
                }
            }
        }
        return undefined
        console.log(currentbucket)
    }

    keys() {
        const keysArray = [];
        for (let i=0; i<this.data.length; i++) {
            if (this.data[i]) {
                keysArray.push(this.data[i][0][0])
            }
        }
        return keysArray
    }
}

const myHashTable = new HashTable(50);
myHashTable._hash('grapes');
myHashTable.set('grapes', 10000);
myHashTable.set('apples', 54);
myHashTable.set('oranges', 5);
myHashTable.get('grapes');

console.log(myHashTable.keys())