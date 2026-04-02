class TrieNode{
    constructor() {
        this.children = new Map();
        this.endOfWord = false;
    }
}

class WordDictionary {
    constructor() {
        this.root = new TrieNode();
    }

    /**
     * @param {string} word
     * @return {void}
     */
    addWord(word) {
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
        function dfs(j, root) {
            let cur = root;
            for (let i = j; i < word.length; i++) {
                let char = word[i];
                if (char === '.') {
                    for (let value of cur.children.values()) {
                        if (dfs(i+1, value)) {
                            return true
                        }
                    }
                    return false;
                } else {
                    if (!cur.children.has(char)) {
                        return false;
                    }
                    cur = cur.children.get(char);
                }
            }
            return cur.endOfWord;
        }
        return dfs(0, this.root);
    }
}
