/**
 * SynapseScholar OS - Autonomous Hypothesis & Research Gap Radar
 * Detects structural voids in the academic literature graph and synthesizes testable empirical hypotheses.
 */

window.HypothesesEngine = (function() {
    let gaps = [];

    async function init() {
        await loadHypotheses();
    }

    async function loadHypotheses() {
        try {
            const res = await fetch('/api/hypotheses');
            const data = await res.json();
            if (data.status === 'success') {
                gaps = data.gaps;
                renderHypothesesCards(gaps);
            }
        } catch (e) {
            console.error('Failed to load hypotheses', e);
        }
    }

    function renderHypothesesCards(gapList) {
        const container = document.getElementById('hypotheses-list');
        if (!container) return;

        if (gapList.length === 0) {
            container.innerHTML = `<div class="col-span-3 text-center py-12 text-slate-500">No active gaps found. Generate one above!</div>`;
            return;
        }

        container.innerHTML = gapList.map(g => `
            <div class="glass-card flex flex-col justify-between space-y-4 hover:border-amber-500/40 transition-all">
                <div class="space-y-3">
                    <div class="flex items-center justify-between text-xs font-mono">
                        <span class="badge-neon-amber">Opportunity: ${g.opportunity_score}%</span>
                        <button onclick="window.HypothesesEngine.voteHypothesis('${g.id}')" class="text-slate-400 hover:text-amber-400 transition-colors flex items-center gap-1">
                            <i class="fa-solid fa-thumbs-up text-xs"></i>
                            <span id="endorse-count-${g.id}" class="font-bold">${g.endorsements || 1}</span>
                        </button>
                    </div>

                    <h3 class="text-sm font-bold text-slate-100 hover:text-amber-400 transition-colors leading-snug">${g.title}</h3>
                    
                    <div class="p-2 rounded bg-slate-900/90 border border-slate-800 text-[11px] font-mono text-cyan-300">
                        ${g.domain_a} <span class="text-slate-500">×</span> ${g.domain_b}
                    </div>

                    <p class="text-xs text-slate-300 leading-relaxed font-serif italic">
                        "${g.proposed_hypothesis}"
                    </p>

                    <div class="pt-2 border-t border-slate-800 text-xs text-slate-400 space-y-1.5">
                        <div class="font-mono text-[11px] text-slate-300 font-bold uppercase">Experimental Protocol:</div>
                        <p class="text-[11px] text-slate-400">Dataset: <b class="text-slate-200">${g.experiment_protocol.target_dataset}</b></p>
                        <p class="text-[11px] text-slate-400">Sample: <b class="text-slate-200">${g.experiment_protocol.sample_size}</b></p>
                        <div class="flex flex-wrap gap-1 pt-1">
                            ${g.experiment_protocol.metrics.map(m => `<span class="text-[9px] px-1.5 py-0.5 rounded bg-slate-800 text-slate-300 font-mono">${m}</span>`).join('')}
                        </div>
                    </div>
                </div>

                <div class="pt-3 border-t border-slate-800 flex justify-between items-center text-xs">
                    <span class="text-[11px] text-slate-500 font-mono">Baseline: ${g.experiment_protocol.baseline_comparison.slice(0, 32)}...</span>
                    <button onclick="draftNoteForHypothesis('${g.id}')" class="btn-cyber-secondary py-1 px-2 text-[11px]">
                        <i class="fa-solid fa-pen-to-square"></i> Draft Note
                    </button>
                </div>
            </div>
        `).join('');
    }

    async function voteHypothesis(gapId) {
        playSound('pulse');
        try {
            const res = await fetch(`/api/hypotheses/${gapId}/vote`, { method: 'POST' });
            const data = await res.json();
            if (data.status === 'success') {
                const countElem = document.getElementById(`endorse-count-${gapId}`);
                if (countElem) countElem.innerText = data.endorsements;
                showToast('Hypothesis endorsed by peer review!', 'success');
            }
        } catch (e) {
            console.error('Failed to endorse hypothesis', e);
        }
    }

    async function submitHypothesis() {
        const domainA = document.getElementById('hypo-domain-a')?.value.trim();
        const domainB = document.getElementById('hypo-domain-b')?.value.trim();
        if (!domainA || !domainB) {
            showToast('Please specify both disciplines or domain targets', 'warn');
            return;
        }

        playSound('pulse');
        showToast('Synthesizing cross-domain literature void...', 'info');

        try {
            const res = await fetch('/api/hypotheses/generate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ domain_a: domainA, domain_b: domainB })
            });
            const data = await res.json();
            
            if (data.status === 'success') {
                playSound('success');
                showToast('New testable hypothesis generated!', 'success');
                toggleSynthesizerForm();
                await loadHypotheses();
            }
        } catch (e) {
            console.error('Failed to generate hypothesis', e);
        }
    }

    return {
        init,
        loadHypotheses,
        voteHypothesis,
        submitHypothesis
    };
})();

// Global hypothesis triggers
function toggleSynthesizerForm() {
    playSound('click');
    const form = document.getElementById('hypothesis-synthesizer-form');
    if (form) form.classList.toggle('hidden');
}

function submitNewHypothesis() {
    if (window.HypothesesEngine) window.HypothesesEngine.submitHypothesis();
}

function draftNoteForHypothesis(gapId) {
    switchView('notes');
    if (window.NotesEngine) {
        window.NotesEngine.createDraftFromGap(gapId);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    window.HypothesesEngine.init();
});
