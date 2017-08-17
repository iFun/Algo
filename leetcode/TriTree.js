class Node {
  constructor() {
    this.map = new Map()
    this.endOfWord = false

  }
}

class TriTree {
  constructor() {
    this.rootNode = new Node()
  }

  insert(value) {
    if (!value) {
      return;
    }
    let current = this.rootNode

    for (let char of value) {
      if (!current.map.has(char)) {
        current.map.set(char, new Node())
      }
      current = current.map.get(char)
    }
    current.endOfWord = true
  }
  print() {
    console.log(this.rootNode)
  }

  searchFullWord(value) {
    if (!value) {
      return;
    }
    const result = basicSearch(value)
    return result === false ? result : result.endOfWord
  }
  basicSearch(value) {
    let current = this.rootNode
    for (let char of value) {
      if (!current.map.has(char)) {
        return false
      }
      current = current.map.get(char)
    }
    return current
  }
  prefix(value) {
    if (!value) {
      return;
    }
    let result = this.basicSearch(value)
    if (!result) {
      return result
    }
    const words = []
    this.recFindAllWords(result, words, value)
    return words
  }
  recFindAllWords(currentNode, words, currentWord) {
    if (currentNode.endOfWord) {
      words.push(currentWord)
    }
    if (currentNode.map.size === 0) {
      return;
    }
    for (var [key, value] of currentNode.map) {
      this.recFindAllWords(value, words, currentWord + key)
    }
  }
}

var test = new TriTree()
test.insert('billguo')
test.insert('billcheng')
test.insert('billpppp')
test.insert('billllll')
test.insert('biasd')
console.log(test.prefix('bill'))
//test.print()
