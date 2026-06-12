// Practica 09 BST -- SIS210 UNAP -- APAZA SORITJA MICHAEL ANTHONY

function renderTree(bst, svgEl, highlightedNodes = {}) {
    const w = svgEl.clientWidth || 800;
    const h = svgEl.clientHeight || 500;
    const ns = 'http://www.w3.org/2000/svg';

    svgEl.innerHTML = '';

    const defs = document.createElementNS(ns, 'defs');
    const marker = document.createElementNS(ns, 'marker');
    marker.setAttribute('id', 'arrow');
    marker.setAttribute('viewBox', '0 0 10 10');
    marker.setAttribute('refX', '20');
    marker.setAttribute('refY', '5');
    marker.setAttribute('markerWidth', '6');
    marker.setAttribute('markerHeight', '6');
    marker.setAttribute('orient', 'auto-start-reverse');
    const path = document.createElementNS(ns, 'path');
    path.setAttribute('d', 'M 0 0 L 10 5 L 0 10 z');
    path.setAttribute('fill', '#2a2d3a');
    marker.appendChild(path);
    defs.appendChild(marker);
    svgEl.appendChild(defs);

    if (!bst.root) {
        const txt = document.createElementNS(ns, 'text');
        txt.setAttribute('x', w / 2);
        txt.setAttribute('y', h / 2 - 10);
        txt.setAttribute('text-anchor', 'middle');
        txt.setAttribute('fill', '#5a6278');
        txt.setAttribute('font-size', '16');
        txt.setAttribute('font-family', 'var(--font-mono)');
        txt.textContent = 'Arbol vacio';
        svgEl.appendChild(txt);
        const sub = document.createElementNS(ns, 'text');
        sub.setAttribute('x', w / 2);
        sub.setAttribute('y', h / 2 + 16);
        sub.setAttribute('text-anchor', 'middle');
        sub.setAttribute('fill', '#3b4253');
        sub.setAttribute('font-size', '12');
        sub.setAttribute('font-family', 'var(--font-mono)');
        sub.textContent = 'Ingrese un valor e inserte';
        svgEl.appendChild(sub);
        return;
    }

    const pos = bst.getNodePositions(w, h);
    const count = pos.size;
    const radius = count <= 12 ? 22 : count <= 20 ? 18 : 15;

    const edges = [];
    for (const [val, p] of pos) {
        if (p.parentVal !== null && pos.has(p.parentVal)) {
            const parent = pos.get(p.parentVal);
            edges.push({ x1: parent.x, y1: parent.y + radius, x2: p.x, y2: p.y - radius,
                         parentVal: p.parentVal, childVal: val });
        }
    }
    edges.sort((a, b) => a.parentVal - b.parentVal);

    for (const e of edges) {
        const line = document.createElementNS(ns, 'line');
        line.setAttribute('x1', e.x1);
        line.setAttribute('y1', e.y1);
        line.setAttribute('x2', e.x2);
        line.setAttribute('y2', e.y2);
        line.classList.add('edge');
        const pNode = highlightedNodes[e.parentVal];
        const cNode = highlightedNodes[e.childVal];
        if (pNode === 'active' || cNode === 'active' ||
            pNode === 'found' || cNode === 'found' ||
            pNode === 'traversal' || cNode === 'traversal') {
            line.classList.add('edge-highlight');
        }
        svgEl.appendChild(line);
    }

    for (const [val, p] of pos) {
        const g = document.createElementNS(ns, 'g');

        const hl = highlightedNodes[val];
        let nodeClass = 'node-normal';
        if (hl === 'active') {
            nodeClass = 'node-active';
        } else if (hl === 'found') {
            nodeClass = 'node-found';
        } else if (hl === 'traversal') {
            nodeClass = 'node-traversal';
        } else if (hl === 'deleted') {
            nodeClass = 'node-deleted';
        } else if (val === (bst.root ? bst.root.val : null)) {
            nodeClass = 'node-root';
        } else {
            const node = bst.findNode(val);
            if (node && bst.isLeaf(node)) {
                nodeClass = 'node-leaf';
            }
        }
        g.classList.add(nodeClass);

        const circle = document.createElementNS(ns, 'circle');
        circle.setAttribute('cx', p.x);
        circle.setAttribute('cy', p.y);
        circle.setAttribute('r', radius);

        const text = document.createElementNS(ns, 'text');
        text.setAttribute('x', p.x);
        text.setAttribute('y', p.y);
        text.setAttribute('text-anchor', 'middle');
        text.setAttribute('dominant-baseline', 'central');
        text.setAttribute('fill', '#ffffff');
        text.setAttribute('font-size', radius <= 16 ? '10px' : '12px');
        text.setAttribute('font-family', 'JetBrains Mono, Fira Code, monospace');
        text.setAttribute('font-weight', '600');
        text.setAttribute('pointer-events', 'none');
        text.textContent = val;

        g.appendChild(circle);
        g.appendChild(text);
        svgEl.appendChild(g);
    }
}
