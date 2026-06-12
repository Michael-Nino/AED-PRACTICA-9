// Practica 09 BST -- SIS210 UNAP -- APAZA SORITJA MICHAEL ANTHONY

const CODES = {
    insert: [
        "_insertRec(node, val, steps) {",
        "    if (node === null) {",
        "        return { val, left: null, right: null };",
        "    }",
        "    if (val < node.val) {",
        "        node.left = this._insertRec(node.left, val, steps);",
        "    } else if (val > node.val) {",
        "        node.right = this._insertRec(node.right, val, steps);",
        "    }",
        "    return node;",
        "}"
    ],
    search: [
        "_searchRec(node, val, steps) {",
        "    if (node === null || node.val === val) {",
        "        return node;",
        "    }",
        "    if (val < node.val) {",
        "        return this._searchRec(node.left, val, steps);",
        "    }",
        "    return this._searchRec(node.right, val, steps);",
        "}"
    ],
    delete: [
        "_deleteRec(node, val, steps) {",
        "    if (val < node.val) {",
        "        node.left = this._deleteRec(node.left, val, steps);",
        "    } else if (val > node.val) {",
        "        node.right = this._deleteRec(node.right, val, steps);",
        "    } else {",
        "        if (node.left === null && node.right === null) {",
        "            return null;",
        "        }",
        "        if (node.left === null) {",
        "            return node.right;",
        "        }",
        "        if (node.right === null) {",
        "            return node.left;",
        "        }",
        "        const suc = this._minNode(node.right);",
        "        node.val = suc.val;",
        "        node.right = this._deleteRec(node.right, suc.val, steps);",
        "    }",
        "    return node;",
        "}"
    ],
    inOrder: [
        "_inOrderRec(node, r) {",
        "    if (!node) return;",
        "    this._inOrderRec(node.left, r);",
        "    r.push(node.val);",
        "    this._inOrderRec(node.right, r);",
        "}"
    ],
    preOrder: [
        "_preOrderRec(node, r) {",
        "    if (!node) return;",
        "    r.push(node.val);",
        "    this._preOrderRec(node.left, r);",
        "    this._preOrderRec(node.right, r);",
        "}"
    ],
    postOrder: [
        "_postOrderRec(node, r) {",
        "    if (!node) return;",
        "    this._postOrderRec(node.left, r);",
        "    this._postOrderRec(node.right, r);",
        "    r.push(node.val);",
        "}"
    ],
    bfs: [
        "bfs() {",
        "    const r = [];",
        "    if (!this.root) return r;",
        "    const q = [this.root];",
        "    while (q.length) {",
        "        const n = q.shift();",
        "        r.push(n.val);",
        "        if (n.left) q.push(n.left);",
        "        if (n.right) q.push(n.right);",
        "    }",
        "    return r;",
        "}"
    ]
};

const OP_NAMES = {
    insert: 'Insercion',
    search: 'Busqueda',
    delete: 'Eliminacion',
    inOrder: 'Recorrido In-Order',
    preOrder: 'Recorrido Pre-Order',
    postOrder: 'Recorrido Post-Order',
    bfs: 'Recorrido BFS'
};

class CodePanel {
    constructor() {
        this.container = document.getElementById('code-lines');
        this.opNameEl = document.getElementById('code-operation-name');
    }

    showCode(op) {
        const lines = CODES[op];
        if (!lines) return;
        if (this.opNameEl) {
            this.opNameEl.textContent = OP_NAMES[op] || op;
        }
        if (!this.container) return;
        this.container.innerHTML = '';
        lines.forEach(line => {
            const d = document.createElement('div');
            d.className = 'code-line';
            d.textContent = line;
            this.container.appendChild(d);
        });
    }

    lineCount(op) {
        const lines = CODES[op];
        return lines ? lines.length : 0;
    }

    highlightLine(n) {
        if (!this.container) return;
        this.clearHighlight();
        if (n <= 0) return;
        const lines = this.container.querySelectorAll('.code-line');
        const idx = n - 1;
        if (idx >= 0 && idx < lines.length) {
            lines[idx].classList.add('code-line--active');
        }
    }

    clearHighlight() {
        if (!this.container) return;
        this.container.querySelectorAll('.code-line--active')
            .forEach(el => el.classList.remove('code-line--active'));
    }
}
