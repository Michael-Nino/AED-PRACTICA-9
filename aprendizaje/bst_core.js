// Practica 09 BST -- SIS210 UNAP -- APAZA SORITJA MICHAEL ANTHONY

class BST {
    constructor() {
        this.root = null;
    }

    insert(val) {
        const steps = [];
        if (this.root === null) {
            this.root = { val, left: null, right: null };
            steps.push({ nodeVal: val, action: 'insert', codeLine: 2 });
            return { success: true, steps };
        }
        this.root = this._insertRec(this.root, val, steps);
        return { success: true, steps };
    }

    _insertRec(node, val, steps) {
        if (node === null) {
            steps.push({ nodeVal: val, action: 'insert', codeLine: 3 });
            return { val, left: null, right: null };
        }
        if (val < node.val) {
            steps.push({ nodeVal: node.val, action: 'go-left', codeLine: 5 });
            node.left = this._insertRec(node.left, val, steps);
        } else if (val > node.val) {
            steps.push({ nodeVal: node.val, action: 'go-right', codeLine: 7 });
            node.right = this._insertRec(node.right, val, steps);
        } else {
            steps.push({ nodeVal: val, action: 'duplicate', codeLine: 9 });
        }
        return node;
    }

    search(val) {
        const steps = [];
        const result = this._searchRec(this.root, val, steps);
        return { found: result !== null, steps };
    }

    _searchRec(node, val, steps) {
        if (node === null) {
            steps.push({ nodeVal: val, action: 'not-found', codeLine: 2 });
            return null;
        }
        if (node.val === val) {
            steps.push({ nodeVal: val, action: 'found', codeLine: 2 });
            return node;
        }
        if (val < node.val) {
            steps.push({ nodeVal: node.val, action: 'go-left', codeLine: 5 });
            return this._searchRec(node.left, val, steps);
        }
        steps.push({ nodeVal: node.val, action: 'go-right', codeLine: 8 });
        return this._searchRec(node.right, val, steps);
    }

    delete(val) {
        const steps = [];
        if (this.root === null) {
            return { success: false, steps, delCase: 'none' };
        }
        if (!this._exists(this.root, val)) {
            steps.push({ nodeVal: val, action: 'not-found', codeLine: 0 });
            return { success: false, steps, delCase: 'none' };
        }
        const result = this._deleteRec(this.root, val, steps);
        this.root = result.node;
        return { success: true, steps, delCase: result.delCase };
    }

    _exists(node, val) {
        if (!node) return false;
        if (node.val === val) return true;
        if (val < node.val) return this._exists(node.left, val);
        return this._exists(node.right, val);
    }

    _deleteRec(node, val, steps) {
        if (node === null) return { node: null, delCase: 'none' };
        if (val < node.val) {
            steps.push({ nodeVal: node.val, action: 'go-left', codeLine: 2 });
            const res = this._deleteRec(node.left, val, steps);
            node.left = res.node;
            return { node, delCase: res.delCase };
        }
        if (val > node.val) {
            steps.push({ nodeVal: node.val, action: 'go-right', codeLine: 4 });
            const res = this._deleteRec(node.right, val, steps);
            node.right = res.node;
            return { node, delCase: res.delCase };
        }
        steps.push({ nodeVal: val, action: 'delete', codeLine: 6 });
        if (node.left === null && node.right === null) {
            steps.push({ nodeVal: val, action: 'case-leaf', codeLine: 8 });
            return { node: null, delCase: 'leaf' };
        }
        if (node.left === null) {
            steps.push({ nodeVal: val, action: 'case-one-child', codeLine: 11 });
            return { node: node.right, delCase: 'one-child' };
        }
        if (node.right === null) {
            steps.push({ nodeVal: val, action: 'case-one-child', codeLine: 14 });
            return { node: node.left, delCase: 'one-child' };
        }
        steps.push({ nodeVal: val, action: 'case-two-children', codeLine: 16 });
        const suc = this._minNode(node.right);
        node.val = suc.val;
        steps.push({ nodeVal: node.val, action: 'replace-with-successor', codeLine: 17 });
        const res = this._deleteRec(node.right, suc.val, steps);
        node.right = res.node;
        return { node, delCase: 'two-children' };
    }

    _minNode(node) {
        let cur = node;
        while (cur && cur.left) cur = cur.left;
        return cur;
    }

    inOrder() {
        const r = [];
        this._inOrderRec(this.root, r);
        return r;
    }

    _inOrderRec(node, r) {
        if (!node) return;
        this._inOrderRec(node.left, r);
        r.push(node.val);
        this._inOrderRec(node.right, r);
    }

    preOrder() {
        const r = [];
        this._preOrderRec(this.root, r);
        return r;
    }

    _preOrderRec(node, r) {
        if (!node) return;
        r.push(node.val);
        this._preOrderRec(node.left, r);
        this._preOrderRec(node.right, r);
    }

    postOrder() {
        const r = [];
        this._postOrderRec(this.root, r);
        return r;
    }

    _postOrderRec(node, r) {
        if (!node) return;
        this._postOrderRec(node.left, r);
        this._postOrderRec(node.right, r);
        r.push(node.val);
    }

    bfs() {
        const r = [];
        if (!this.root) return r;
        const q = [this.root];
        while (q.length) {
            const n = q.shift();
            r.push(n.val);
            if (n.left) q.push(n.left);
            if (n.right) q.push(n.right);
        }
        return r;
    }

    height() {
        return this._height(this.root);
    }

    _height(node) {
        if (!node) return -1;
        return 1 + Math.max(this._height(node.left), this._height(node.right));
    }

    size() {
        return this.inOrder().length;
    }

    findNode(val) {
        return this._findNode(this.root, val);
    }

    _findNode(node, val) {
        if (!node) return null;
        if (node.val === val) return node;
        if (val < node.val) return this._findNode(node.left, val);
        return this._findNode(node.right, val);
    }

    isLeaf(node) {
        return node && !node.left && !node.right;
    }

    getNodePositions(svgW, svgH) {
        const pos = new Map();
        if (!this.root) return pos;
        const h = this.height();
        const levelH = h <= 0 ? svgH - 60 : Math.min(82, Math.max(60, (svgH - 60) / (h + 1)));
        const inOrderVals = this.inOrder();
        const idxMap = new Map();
        inOrderVals.forEach((v, i) => idxMap.set(v, i));
        const n = inOrderVals.length;
        const pad = 40;
        const availW = svgW - 2 * pad;
        this._layoutPos(this.root, idxMap, n, availW, pad, 45, levelH, pos, null);
        return pos;
    }

    _layoutPos(node, idxMap, count, availW, pad, y, levelH, pos, parent) {
        if (!node) return;
        const frac = count <= 1 ? 0.5 : idxMap.get(node.val) / (count - 1);
        const x = pad + frac * availW;
        pos.set(node.val, { x, y, parentVal: parent });
        this._layoutPos(node.left, idxMap, count, availW, pad, y + levelH, levelH, pos, node.val);
        this._layoutPos(node.right, idxMap, count, availW, pad, y + levelH, levelH, pos, node.val);
    }

    clear() {
        this.root = null;
    }
}
