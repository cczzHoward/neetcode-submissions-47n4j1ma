class TrieNode {
    constructor() {
        this.children = new Map();
        this.endOfWord = false;
    }
}

class PrefixTree {
    constructor() {
        this.root = new TrieNode();
    }

    /**
     * @param {string} word
     * @return {void}
     */
    insert(word) {
        let cur = this.root;
        for (let char of word) {
            if (!cur.children.has(char)) {
                cur.children.set(char, new TrieNode());
            }
            cur = cur.children.get(char);
        }
        cur.endOfWord = true;
    }

    /**
     * @param {string} word
     * @return {boolean}
     */
    search(word) {
        let cur = this.root;
        for (let char of word) {
            if (!cur.children.has(char)) {
                return false;
            }
            cur = cur.children.get(char);
        }
        return cur.endOfWord;
    }

    /**
     * @param {string} prefix
     * @return {boolean}
     */
    startsWith(prefix) {
        let cur = this.root;
        for (let char of prefix) {
            if (!cur.children.has(char)) {
                return false;
            }
            cur = cur.children.get(char);
        }
        return true;
    }
}
