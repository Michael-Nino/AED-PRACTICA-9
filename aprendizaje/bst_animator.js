// Practica 09 BST -- SIS210 UNAP -- APAZA SORITJA MICHAEL ANTHONY

class BSTAnimator {
    constructor(bst, renderFn, codePanel, logPanel, statsBar, svgEl) {
        this.bst = bst;
        this.renderFn = renderFn;
        this.codePanel = codePanel;
        this.logPanel = logPanel;
        this.statsBar = statsBar;
        this.svgEl = svgEl;
        this.animating = false;
    }

    _render(highlights) {
        this.renderFn(this.bst, this.svgEl, highlights);
    }

    animateInsert(val) {
        if (this.animating) return;
        this.animating = true;
        this.codePanel.showCode('insert');

        const { steps } = this.bst.insert(val);
        this._scheduleSteps(steps, 350, () => {
            this._render({});
            this._updateStats();
            this._addLog(`Insertado: ${val}`, 'insert');
            this.animating = false;
        });
    }

    animateSearch(val) {
        if (this.animating) return;
        this.animating = true;
        this.codePanel.showCode('search');

        const { found, steps } = this.bst.search(val);
        this._scheduleSteps(steps, 350, () => {
            this._render(found ? { [val]: 'found' } : {});
            this._addLog(`Buscado: ${val} — ${found ? 'encontrado' : 'no encontrado'}`, 'search');
            this._updateStats();
            this.animating = false;
        });
    }

    animateDelete(val) {
        if (this.animating) return;
        this.animating = true;
        this.codePanel.showCode('delete');

        const { success, steps } = this.bst.delete(val);
        if (!success) {
            this._addLog(`Error: ${val} no encontrado`, 'error');
            this.animating = false;
            return;
        }

        this._scheduleSteps(steps, 350, () => {
            this._render({});
            this._addLog(`Eliminado: ${val}`, 'delete');
            this._updateStats();
            this.animating = false;
        });
    }

    animateTraversal(type) {
        if (this.animating) return;
        this.animating = true;

        let values = [];
        const typeNames = {
            inOrder: 'In-Order', preOrder: 'Pre-Order',
            postOrder: 'Post-Order', bfs: 'BFS'
        };
        const complexities = {
            inOrder: 'O(n)', preOrder: 'O(n)',
            postOrder: 'O(n)', bfs: 'O(n)'
        };

        this.codePanel.showCode(type);
        const totalLines = this.codePanel.lineCount(type);

        switch (type) {
            case 'inOrder':  values = this.bst.inOrder();  break;
            case 'preOrder': values = this.bst.preOrder(); break;
            case 'postOrder':values = this.bst.postOrder();break;
            case 'bfs':      values = this.bst.bfs();      break;
        }

        let i = 0;
        const next = () => {
            if (i < values.length) {
                const v = values[i];
                this._render({ [v]: 'traversal' });
                this._addLog(`${typeNames[type]}: visitando ${v}`, 'traversal');
                const line = (i % totalLines) + 1;
                this.codePanel.highlightLine(line);
                i++;
                setTimeout(next, 380);
            } else {
                this._render({});
                this._addLog(`${typeNames[type]}: [${values.join(', ')}]`, 'traversal');
                const el = document.getElementById('traversal-result');
                if (el) {
                    el.innerHTML = `<strong>${typeNames[type]}</strong>: [${values.join(', ')}] &nbsp;|&nbsp; Complejidad: ${complexities[type]}`;
                }
                this._updateStats();
                this.codePanel.clearHighlight();
                this.animating = false;
            }
        };
        next();
    }

    _scheduleSteps(steps, delay, callback) {
        let i = 0;
        const run = () => {
            if (i < steps.length) {
                const s = steps[i];
                this.codePanel.highlightLine(s.codeLine || 0);

                const hl = {};
                switch (s.action) {
                    case 'go-left':
                    case 'go-right':
                        hl[s.nodeVal] = 'active';
                        break;
                    case 'found':
                        hl[s.nodeVal] = 'found';
                        break;
                    case 'insert':
                        hl[s.nodeVal] = 'traversal';
                        break;
                    case 'delete':
                    case 'case-leaf':
                    case 'case-one-child':
                    case 'case-two-children':
                    case 'replace-with-successor':
                        hl[s.nodeVal] = 'deleted';
                        break;
                }
                this._render(hl);
                i++;
                setTimeout(run, delay);
            } else {
                callback();
            }
        };
        run();
    }

    _updateStats() {
        if (!this.statsBar) return;
        const n = this.statsBar.querySelector('#stat-nodes');
        const h = this.statsBar.querySelector('#stat-height');
        const io = this.statsBar.querySelector('#stat-inorder');
        if (n) n.textContent = this.bst.size();
        if (h) h.textContent = this.bst.height();
        if (io) io.textContent = '[' + this.bst.inOrder().join(', ') + ']';
    }

    _addLog(msg, type) {
        if (!this.logPanel) return;
        const entries = this.logPanel.querySelector('#log-entries');
        if (!entries) return;
        const ts = new Date().toTimeString().slice(0, 8);
        const div = document.createElement('div');
        div.className = 'log-entry log-' + (type || 'info');
        div.textContent = '[' + ts + '] ' + msg;
        entries.appendChild(div);
        entries.scrollTop = entries.scrollHeight;
    }
}
