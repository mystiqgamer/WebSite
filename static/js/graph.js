/**
 * SynapseScholar OS - Dynamic Force-Directed Knowledge Graph Visualizer
 * Canvas-based spring-embedder physics, node dragging, zoom/pan, cluster categorization,
 * and animated interdisciplinary bridge pathfinding.
 */

window.GraphEngine = (function() {
    let canvas, ctx;
    let nodes = [];
    let edges = [];
    let nodeMap = {};
    let selectedNode = null;
    let hoveredNode = null;
    let draggedNode = null;

    // Viewport transform
    let scale = 1.0;
    let panX = 0;
    let panY = 0;
    let isPanning = false;
    let startPanX = 0, startPanY = 0;

    // Bridge highlighting
    let activeBridgePath = null;
    let pulsePhase = 0;

    // Discipline color scheme
    const DISCIPLINE_COLORS = {
        'AI': '#06b6d4',          // Cyan
        'AI/Physics': '#3b82f6',  // Blue
        'Bio': '#10b981',         // Emerald
        'Physics': '#f59e0b',     // Amber
        'Physics/Climate': '#ea580c',
        'Math/Epidemiology': '#ec4899', // Pink
        'Ecology': '#84cc16',     // Lime
        'Neuro': '#8b5cf6',       // Purple
        'Neuro/AI': '#a855f7',
        'CS/Math': '#6366f1',
        'Math/Stats': '#0ea5e9'
    };

    function init() {
        canvas = document.getElementById('graph-canvas');
        if (!canvas) return;
        ctx = canvas.getContext('2d');
        resizeCanvas();

        window.addEventListener('resize', resizeCanvas);
        setupInteractionListeners();
        fetchGraphData();
    }

    function resizeCanvas() {
        const container = document.getElementById('graph-canvas-container');
        if (!container || !canvas) return;
        canvas.width = container.clientWidth * window.devicePixelRatio;
        canvas.height = container.clientHeight * window.devicePixelRatio;
        ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
    }

    async function fetchGraphData(discipline = 'all') {
        try {
            const url = discipline === 'all' ? '/api/graph' : `/api/graph?discipline=${encodeURIComponent(discipline)}`;
            const res = await fetch(url);
            const data = await res.json();
            
            if (data.status === 'success') {
                processGraphData(data.graph);
                populateBridgeSelectors();
            }
        } catch (e) {
            console.error('Failed to load knowledge graph', e);
        }
    }

    function processGraphData(graph) {
        const w = canvas.width / window.devicePixelRatio;
        const h = canvas.height / window.devicePixelRatio;

        nodes = graph.nodes.map((n, i) => {
            const angle = (i / graph.nodes.length) * 2 * Math.PI;
            const radius = Math.min(w, h) * 0.35;
            return {
                ...n,
                x: w / 2 + Math.cos(angle) * radius + (Math.random() - 0.5) * 40,
                y: h / 2 + Math.sin(angle) * radius + (Math.random() - 0.5) * 40,
                vx: 0,
                vy: 0,
                radius: Math.max(12, Math.min(26, n.val || 16)),
                color: DISCIPLINE_COLORS[n.discipline] || '#06b6d4'
            };
        });

        nodeMap = {};
        nodes.forEach(n => nodeMap[n.id] = n);

        edges = graph.edges.map(e => ({
            ...e,
            sourceNode: nodeMap[e.source],
            targetNode: nodeMap[e.target]
        })).filter(e => e.sourceNode && e.targetNode);

        // Center transform
        panX = 0;
        panY = 0;
        scale = 1.0;

        startPhysicsLoop();
    }

    function populateBridgeSelectors() {
        const srcSelect = document.getElementById('bridge-source-select');
        const tgtSelect = document.getElementById('bridge-target-select');
        if (!srcSelect || !tgtSelect) return;

        srcSelect.innerHTML = nodes.map(n => `<option value="${n.id}">${n.label}</option>`).join('');
        tgtSelect.innerHTML = nodes.map(n => `<option value="${n.id}">${n.label}</option>`).join('');

        // Set defaults to interesting bridge: Transformers -> CRISPR
        if (nodeMap['n-transformers']) srcSelect.value = 'n-transformers';
        if (nodeMap['n-crispr']) tgtSelect.value = 'n-crispr';
    }

    // Force-Directed Physics Simulation Step
    function updatePhysics() {
        const repulsion = 450;
        const springLength = 110;
        const springK = 0.04;
        const damping = 0.88;
        const centerK = 0.015;

        const w = canvas.width / window.devicePixelRatio;
        const h = canvas.height / window.devicePixelRatio;
        const cx = w / 2;
        const cy = h / 2;

        // Node repulsion
        for (let i = 0; i < nodes.length; i++) {
            const n1 = nodes[i];
            for (let j = i + 1; j < nodes.length; j++) {
                const n2 = nodes[j];
                const dx = n2.x - n1.x;
                const dy = n2.y - n1.y;
                const dist = Math.sqrt(dx * dx + dy * dy) || 1;
                if (dist < 320) {
                    const force = (repulsion * repulsion) / (dist * dist);
                    const fx = (dx / dist) * force;
                    const fy = (dy / dist) * force;
                    n1.vx -= fx;
                    n1.vy -= fy;
                    n2.vx += fx;
                    n2.vy += fy;
                }
            }
        }

        // Edge spring attraction
        for (const e of edges) {
            const n1 = e.sourceNode;
            const n2 = e.targetNode;
            const dx = n2.x - n1.x;
            const dy = n2.y - n1.y;
            const dist = Math.sqrt(dx * dx + dy * dy) || 1;
            const force = (dist - springLength) * springK * (e.strength || 0.8);
            const fx = (dx / dist) * force;
            const fy = (dy / dist) * force;
            n1.vx += fx;
            n1.vy += fy;
            n2.vx -= fx;
            n2.vy -= fy;
        }

        // Centering force & update positions
        for (const n of nodes) {
            if (n === draggedNode) continue;
            n.vx += (cx - n.x) * centerK;
            n.vy += (cy - n.y) * centerK;
            n.vx *= damping;
            n.vy *= damping;
            n.x += n.vx;
            n.y += n.vy;
        }

        pulsePhase = (pulsePhase + 0.04) % (2 * Math.PI);
    }

    // Render Canvas Frame
    function render() {
        if (!ctx) return;
        const w = canvas.width / window.devicePixelRatio;
        const h = canvas.height / window.devicePixelRatio;

        ctx.clearRect(0, 0, w, h);

        ctx.save();
        ctx.translate(panX, panY);
        ctx.scale(scale, scale);

        // Draw Edges
        for (const e of edges) {
            const isBridge = activeBridgePath && activeBridgePath.some((nid, idx) => 
                idx < activeBridgePath.length - 1 &&
                ((e.source === nid && e.target === activeBridgePath[idx + 1]) ||
                 (e.target === nid && e.source === activeBridgePath[idx + 1]))
            );

            ctx.beginPath();
            ctx.moveTo(e.sourceNode.x, e.sourceNode.y);
            ctx.lineTo(e.targetNode.x, e.targetNode.y);

            if (isBridge) {
                ctx.strokeStyle = '#8b5cf6';
                ctx.lineWidth = 4 + Math.sin(pulsePhase) * 1.5;
                ctx.shadowColor = '#8b5cf6';
                ctx.shadowBlur = 12;
            } else {
                ctx.strokeStyle = 'rgba(255, 255, 255, 0.12)';
                ctx.lineWidth = 1.2;
                ctx.shadowBlur = 0;
            }
            ctx.stroke();
            ctx.shadowBlur = 0;
        }

        // Draw Nodes
        for (const n of nodes) {
            const isSelected = selectedNode && selectedNode.id === n.id;
            const isHovered = hoveredNode && hoveredNode.id === n.id;
            const isInBridge = activeBridgePath && activeBridgePath.includes(n.id);

            // Halo glow
            if (isSelected || isHovered || isInBridge) {
                ctx.beginPath();
                ctx.arc(n.x, n.y, n.radius + 8, 0, Math.PI * 2);
                ctx.fillStyle = isInBridge ? 'rgba(139, 92, 246, 0.35)' : 'rgba(6, 182, 212, 0.3)';
                ctx.fill();
            }

            // Node Core
            ctx.beginPath();
            ctx.arc(n.x, n.y, n.radius, 0, Math.PI * 2);
            ctx.fillStyle = isInBridge ? '#a855f7' : n.color;
            ctx.fill();
            ctx.strokeStyle = '#ffffff';
            ctx.lineWidth = isSelected ? 3 : 1.5;
            ctx.stroke();

            // Label
            ctx.font = `${isHovered || isSelected ? '600 12px' : '500 11px'} 'Inter', sans-serif`;
            ctx.fillStyle = isHovered || isSelected ? '#ffffff' : '#cbd5e1';
            ctx.textAlign = 'center';
            ctx.fillText(n.label, n.x, n.y + n.radius + 14);
        }

        ctx.restore();
    }

    let animationId = null;
    function startPhysicsLoop() {
        if (animationId) cancelAnimationFrame(animationId);
        function loop() {
            updatePhysics();
            render();
            animationId = requestAnimationFrame(loop);
        }
        loop();
    }

    // Interactive Listeners
    function setupInteractionListeners() {
        canvas.addEventListener('mousedown', onMouseDown);
        window.addEventListener('mousemove', onMouseMove);
        window.addEventListener('mouseup', onMouseUp);
        canvas.addEventListener('wheel', onWheel, { passive: false });
    }

    function getCanvasCoords(e) {
        const rect = canvas.getBoundingClientRect();
        return {
            x: (e.clientX - rect.left - panX) / scale,
            y: (e.clientY - rect.top - panY) / scale
        };
    }

    function findNodeAt(x, y) {
        for (let i = nodes.length - 1; i >= 0; i--) {
            const n = nodes[i];
            const dist = Math.hypot(n.x - x, n.y - y);
            if (dist <= n.radius + 6) return n;
        }
        return null;
    }

    function onMouseDown(e) {
        const coords = getCanvasCoords(e);
        const hit = findNodeAt(coords.x, coords.y);

        if (hit) {
            draggedNode = hit;
            selectNode(hit);
            playSound('click');
        } else {
            isPanning = true;
            startPanX = e.clientX - panX;
            startPanY = e.clientY - panY;
        }
    }

    function onMouseMove(e) {
        if (draggedNode) {
            const coords = getCanvasCoords(e);
            draggedNode.x = coords.x;
            draggedNode.y = coords.y;
            draggedNode.vx = 0;
            draggedNode.vy = 0;
            return;
        }

        if (isPanning) {
            panX = e.clientX - startPanX;
            panY = e.clientY - startPanY;
            return;
        }

        const coords = getCanvasCoords(e);
        const hit = findNodeAt(coords.x, coords.y);
        if (hit !== hoveredNode) {
            hoveredNode = hit;
            canvas.style.cursor = hit ? 'pointer' : 'grab';
        }
    }

    function onMouseUp() {
        draggedNode = null;
        isPanning = false;
    }

    function onWheel(e) {
        e.preventDefault();
        const zoomFactor = e.deltaY < 0 ? 1.08 : 0.92;
        zoom(zoomFactor);
    }

    function zoom(factor) {
        const newScale = Math.max(0.4, Math.min(2.8, scale * factor));
        scale = newScale;
    }

    function resetView() {
        scale = 1.0;
        panX = 0;
        panY = 0;
    }

    // Inspect Node Details
    function selectNode(node) {
        selectedNode = node;
        activeBridgePath = null; // Clear old bridge unless explicitly requested

        document.getElementById('inspect-badge').innerText = node.discipline;
        document.getElementById('inspect-cluster').innerText = node.cluster;
        document.getElementById('inspect-title').innerText = node.label;
        document.getElementById('inspect-desc').innerText = `Centrality index: ${node.val} | Connected academic citations: ${(node.citations || 10000).toLocaleString()}`;

        // Find neighbors
        const neighbors = edges
            .filter(e => e.source === node.id || e.target === node.id)
            .map(e => {
                const other = e.source === node.id ? e.targetNode : e.sourceNode;
                return `<div class="p-2 rounded bg-slate-800/80 border border-slate-700/60 flex items-center justify-between">
                    <span class="font-medium text-slate-200">${other.label}</span>
                    <span class="text-[10px] font-mono text-cyan-400">${e.type}</span>
                </div>`;
            });

        document.getElementById('inspect-neighbors').innerHTML = neighbors.join('') || '<span class="text-slate-500 italic">No direct edges</span>';
        document.getElementById('inspect-bridge-result').classList.add('hidden');
    }

    // Compute Interdisciplinary Bridge
    async function computeBridge(sourceId, targetId) {
        playSound('pulse');
        try {
            const res = await fetch(`/api/graph/bridge?source=${sourceId}&target=${targetId}`);
            const data = await res.json();
            
            if (data.status === 'success') {
                activeBridgePath = data.path_nodes.map(n => n.id);
                showToast(`Bridge found! ${data.hop_count} hops spanning ${data.cross_disciplines.join(' & ')}`, 'success');
                playSound('success');

                // Update Inspector with bridge synthesis
                document.getElementById('inspect-bridge-result').classList.remove('hidden');
                document.getElementById('inspect-bridge-text').innerText = data.synthesis_summary;
                document.getElementById('bridge-hops').innerText = data.hop_count;
                document.getElementById('bridge-synergy').innerText = data.synergy_score + '%';
            } else {
                showToast(data.message || 'No direct bridge path found', 'warn');
            }
        } catch (e) {
            console.error('Failed to compute bridge', e);
        }
    }

    function filterByDiscipline(discipline) {
        playSound('click');
        fetchGraphData(discipline);

        // Update active filter button styling
        document.querySelectorAll('.graph-filter-btn').forEach(btn => {
            if (btn.innerText.toLowerCase().includes(discipline.toLowerCase()) || (discipline === 'all' && btn.innerText.includes('All'))) {
                btn.className = 'graph-filter-btn px-3 py-1 rounded-full text-xs font-medium bg-cyan-500/20 text-cyan-400 border border-cyan-500/40';
            } else {
                btn.className = 'graph-filter-btn px-3 py-1 rounded-full text-xs font-medium bg-slate-800/80 text-slate-300 hover:bg-slate-700';
            }
        });
    }

    return {
        init,
        resizeCanvas,
        computeBridge,
        filterByDiscipline,
        zoom,
        resetView,
        getSelectedNode: () => selectedNode
    };
})();

// Global bridge button triggers
function filterGraph(discipline) {
    if (window.GraphEngine) window.GraphEngine.filterByDiscipline(discipline);
}

function computeBridgeFromDropdowns() {
    const src = document.getElementById('bridge-source-select')?.value;
    const tgt = document.getElementById('bridge-target-select')?.value;
    if (src && tgt && window.GraphEngine) {
        window.GraphEngine.computeBridge(src, tgt);
    }
}

function zoomGraph(factor) {
    if (window.GraphEngine) window.GraphEngine.zoom(factor);
}

function resetGraphView() {
    if (window.GraphEngine) window.GraphEngine.resetView();
}

function openSocraticFromInspection() {
    const node = window.GraphEngine?.getSelectedNode();
    switchView('socratic');
    if (node && window.SocraticEngine) {
        // Map node to paper
        const paperMap = {
            'n-transformers': 'paper-attn-2017',
            'n-alphafold': 'paper-alphafold-2021',
            'n-sir': 'paper-sir-1927',
            'n-chaos': 'paper-chaos-1963',
            'n-lotka': 'paper-lotka-1925',
            'n-crispr': 'paper-crispr-2012',
            'n-pinns': 'paper-pinn-2019',
            'n-free-energy': 'paper-free-energy-2010'
        };
        const pid = paperMap[node.id] || 'paper-attn-2017';
        window.SocraticEngine.loadPaper(pid);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    window.GraphEngine.init();
});
