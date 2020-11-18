function TreeNode(value) { 
	this.value = value; 
	this.left = null; 
	this.right = null;
}

// Make a perfect Binary Tree first (completely filled bottom layer with 0 or 2 children each node)
// Perfect binary trees are very efficient// # of nodes = 2^n-1
// Full binary tree: 0 or 2 children but not necessary to have a completely filled bottom layer

class BSTree { 
	constructor() { 
        this.root = null; 
    }
	insert(value) { 
		const node = new TreeNode(value); 
		if (this.root === null) { 
			this.root = node 
		} else { 
			let current_node = this.root; 
			while(true) { 
				if (value < current_node.value) { 
				// move left 
					if (!current_node.left) { 
						current_node.left = node; 
						return this 
					} 
					current_node = current_node.left 
				} else { 
				// move right 
					if (!current_node.right) { 
						current_node.right = node 
						return this 
					} 
					current_node = current_node.right 
				} 
			} 
		} 
	}
	
 lookup(value) { 
	if (!this.root) { 
		return false; 
	} 
	let current_node = this.root; 
	while(current_node) { 
		if (value < current_node.value) { 
			current_node = current_node.left; 
		} else if (value > current_node.value) { 
			current_node = current_node.right; 
		} else if (value === current_node.value) { 
			return current_node 
		} 
	} 
	return false 
	}

}

function travese(node) { 
	const tree = {value: node.value}; 
	tree.left = node.left === null ? null: 
	travese(node.left); 
	tree.right = node.right === null ? null: 
	travese(node.right); return tree;
	}
	
const tree = new BSTree();
tree.insert(9)
tree.insert(4)
tree.insert(1)
tree.insert(6)
tree.insert(20)
tree.insert(170)
// tree.lookup(10)

console.log(travese(tree.root))

console.log(tree)