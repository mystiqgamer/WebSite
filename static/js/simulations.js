/**
 * KTU ScholarOS - Interactive Syllabus Labs
 * CPU Scheduling Gantt Visualizer, 4-Variable K-Map Solver, and BST Traversal Engine.
 */

window.KTULabs = (function() {
    let activeKMapMinterms = new Set([0, 1, 2, 5, 8, 9, 10]);
    let activeKMapDontCares = new Set([3, 11]);
    let bstElements = [45, 23, 65, 12, 34, 55, 78];

    function init() {
        runCPUSchedulingSim();
        renderKMapGrid();
        runBSTSimulation();
    }

    // =========================================================================
    // 1. CPU SCHEDULING SIMULATOR
    // =========================================================================
    async function runCPUScheduling() {
        playSound('click');
        const p1_arr = parseInt(document.getElementById('p1-arr')?.value || 0);
        const p1_bur = parseInt(document.getElementById('p1-bur')?.value || 5);
        const p2_arr = parseInt(document.getElementById('p2-arr')?.value || 1);
        const p2_bur = parseInt(document.getElementById('p2-bur')?.value || 3);
        const p3_arr = parseInt(document.getElementById('p3-arr')?.value || 2);
        const p3_bur = parseInt(document.getElementById('p3-bur')?.value || 8);
        const p4_arr = parseInt(document.getElementById('p4-arr')?.value || 3);
        const p4_bur = parseInt(document.getElementById('p4-bur')?.value || 6);

        const quantum = parseInt(document.getElementById('input-rr-quantum')?.value || 2);

        const processes = [
            { name: "P1", arrival: p1_arr, burst: p1_bur },
            { name: "P2", arrival: p2_arr, burst: p2_bur },
            { name: "P3", arrival: p3_arr, burst: p3_bur },
            { name: "P4", arrival: p4_arr, burst: p4_bur }
        ];

        try {
            const res = await fetch('/api/simulations/cpu_scheduling', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ processes: processes, quantum: quantum })
            });
            const data = await res.json();
            
            if (data.status === 'success') {
                renderGantt('fcfs-gantt-bar', data.fcfs.gantt);
                document.getElementById('fcfs-metrics').innerText = `Avg Waiting: ${data.fcfs.avg_waiting} ms • Avg Turnaround: ${data.fcfs.avg_turnaround} ms`;

                renderGantt('rr-gantt-bar', data.round_robin.gantt);
                document.getElementById('rr-metrics').innerText = `Avg Waiting: ${data.round_robin.avg_waiting} ms • Avg Turnaround: ${data.round_robin.avg_turnaround} ms`;
            }
        } catch (e) {
            console.error('CPU simulation error', e);
        }
    }

    function renderGantt(containerId, ganttList) {
        const bar = document.getElementById(containerId);
        if (!bar || !ganttList || ganttList.length === 0) return;

        const totalDuration = ganttList[ganttList.length - 1].end;
        const colors = {
            'P1': 'bg-cyan-500/80 text-white',
            'P2': 'bg-emerald-500/80 text-white',
            'P3': 'bg-purple-500/80 text-white',
            'P4': 'bg-amber-500/80 text-white'
        };

        bar.innerHTML = ganttList.map(item => {
            const widthPct = ((item.duration / totalDuration) * 100).toFixed(1);
            const colorClass = colors[item.process] || 'bg-slate-700 text-white';
            return `
                <div class="h-full ${colorClass} flex flex-col items-center justify-center border-r border-slate-900/40 relative group" style="width: ${widthPct}%">
                    <span class="text-[11px] leading-none">${item.process}</span>
                    <span class="text-[9px] opacity-75 font-mono">${item.start}-${item.end}</span>
                </div>
            `;
        }).join('');
    }

    // =========================================================================
    // 2. 4-VARIABLE K-MAP MINIMIZER
    // =========================================================================
    function renderKMapGrid() {
        const container = document.getElementById('kmap-grid-container');
        if (!container) return;

        // Rows AB: 00, 01, 11, 10
        // Cols CD: 00, 01, 11, 10
        const row_codes = [0, 1, 3, 2];
        const col_codes = [0, 1, 3, 2];

        container.innerHTML = '';
        for (let r = 0; r < 4; r++) {
            for (let c = 0; c < 4; c++) {
                const minterm = (row_codes[r] << 2) | col_codes[c];
                const isOne = activeKMapMinterms.has(minterm);
                const isDontCare = activeKMapDontCares.has(minterm);

                const cell = document.createElement('div');
                cell.className = `h-14 rounded-lg flex flex-col items-center justify-center cursor-pointer border font-mono transition-all ${
                    isOne ? 'bg-cyan-500/30 border-cyan-400 text-cyan-300 font-bold shadow-sm' :
                    (isDontCare ? 'bg-amber-500/20 border-amber-400 text-amber-300 font-bold' : 'bg-slate-900 border-slate-800 text-slate-500 hover:border-slate-700')
                }`;
                cell.innerHTML = `
                    <span class="text-xs">${isOne ? '1' : (isDontCare ? 'X' : '0')}</span>
                    <span class="text-[9px] text-slate-500">m${minterm}</span>
                `;
                cell.onclick = () => toggleKMapCell(minterm);
                container.appendChild(cell);
            }
        }

        updateKMapLogic();
    }

    function toggleKMapCell(m) {
        playSound('click');
        if (activeKMapMinterms.has(m)) {
            activeKMapMinterms.delete(m);
            activeKMapDontCares.add(m);
        } else if (activeKMapDontCares.has(m)) {
            activeKMapDontCares.delete(m);
        } else {
            activeKMapMinterms.add(m);
        }
        renderKMapGrid();
    }

    async function updateKMapLogic() {
        const sortedM = Array.from(activeKMapMinterms).sort((a,b)=>a-b);
        document.getElementById('kmap-minterms-label').innerText = sortedM.join(', ') || 'None';

        try {
            const res = await fetch('/api/simulations/kmap', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    minterms: sortedM,
                    dont_cares: Array.from(activeKMapDontCares)
                })
            });
            const data = await res.json();
            if (data.status === 'success') {
                document.getElementById('kmap-result-expr').innerText = data.simplified_expression;
            }
        } catch (e) {
            console.error('KMap update error', e);
        }
    }

    function resetKMap() {
        playSound('click');
        activeKMapMinterms.clear();
        activeKMapDontCares.clear();
        renderKMapGrid();
    }

    // =========================================================================
    // 3. BINARY SEARCH TREE (BST)
    // =========================================================================
    async function runBSTSimulation() {
        try {
            const res = await fetch('/api/simulations/bst', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ elements: bstElements })
            });
            const data = await res.json();
            if (data.status === 'success') {
                document.getElementById('bst-height').innerText = data.tree_height;
                document.getElementById('bst-count').innerText = data.node_count;
                document.getElementById('bst-inorder').innerText = data.inorder.join(', ');
                document.getElementById('bst-preorder').innerText = data.preorder.join(', ');
                document.getElementById('bst-postorder').innerText = data.postorder.join(', ');
            }
        } catch (e) {
            console.error('BST simulation error', e);
        }
    }

    function insertBSTNode() {
        const input = document.getElementById('bst-new-val');
        const val = parseInt(input?.value);
        if (!isNaN(val)) {
            playSound('click');
            bstElements.push(val);
            if (input) input.value = '';
            runBSTSimulation();
            showToast(`Inserted ${val} into BST`, 'success');
        }
    }

    return {
        init,
        runCPUScheduling,
        resetKMap,
        insertBSTNode
    };
})();

// Lab Switcher
function switchLabTab(tabName) {
    playSound('click');
    const tabs = ['cpu', 'kmap', 'bst'];
    tabs.forEach(t => {
        const pane = document.getElementById(`lab-tab-${t}`);
        const btn = document.getElementById(`btn-lab-${t}`);
        if (pane) pane.classList.toggle('hidden', t !== tabName);
        if (btn) {
            btn.className = t === tabName ? 
                'px-3 py-1.5 rounded-lg text-xs font-semibold bg-cyan-500/20 text-cyan-400 border border-cyan-500/40' :
                'px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700';
        }
    });
}

function updateRRQuantum(val) {
    document.getElementById('label-rr-quantum').innerText = `${val} ms`;
    window.KTULabs.runCPUScheduling();
}

function runCPUSchedulingSim() {
    if (window.KTULabs) window.KTULabs.runCPUScheduling();
}

function resetKMap() {
    if (window.KTULabs) window.KTULabs.resetKMap();
}

function insertBSTNode() {
    if (window.KTULabs) window.KTULabs.insertBSTNode();
}

document.addEventListener('DOMContentLoaded', () => {
    window.KTULabs.init();
});
