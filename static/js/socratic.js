/**
 * SynapseScholar OS - Adaptive Socratic Workbench
 * Tri-tier cognitive explainer (Feynman / Rigorous / Critique), diagnostic conceptual questions,
 * and prerequisite competence graphs.
 */

window.SocraticEngine = (function() {
    let currentPaperId = 'paper-attn-2017';
    let currentTier = 'feynman';
    let socraticData = null;
    let currentQuestionIndex = 0;

    async function init() {
        await populatePaperSelector();
        loadPaper(currentPaperId);
    }

    async function populatePaperSelector() {
        try {
            const res = await fetch('/api/papers');
            const data = await res.json();
            const select = document.getElementById('socratic-paper-select');
            if (!select || !data.papers) return;

            select.innerHTML = data.papers.map(p => `
                <option value="${p.id}">${p.title} (${p.discipline})</option>
            `).join('');
            select.value = currentPaperId;
        } catch (e) {
            console.error('Failed to populate socratic paper selector', e);
        }
    }

    async function loadPaper(paperId) {
        playSound('click');
        currentPaperId = paperId;
        const select = document.getElementById('socratic-paper-select');
        if (select) select.value = paperId;

        try {
            const res = await fetch(`/api/socratic/paper/${paperId}`);
            const data = await res.json();
            
            if (data.status === 'success') {
                socraticData = data.content;
                renderTierContent(currentTier);
                renderDiagnosticQuestion(0);
                loadPrerequisites(paperId);
            }
        } catch (e) {
            console.error('Failed to load socratic content', e);
        }
    }

    function setTier(tier) {
        playSound('click');
        currentTier = tier;

        const tiers = ['feynman', 'rigorous', 'critique'];
        tiers.forEach(t => {
            const btn = document.getElementById(`tab-${t}`);
            if (btn) {
                if (t === tier) {
                    btn.className = `tier-tab-btn active-${t}`;
                } else {
                    btn.className = 'tier-tab-btn';
                }
            }
        });

        renderTierContent(tier);
    }

    function renderTierContent(tier) {
        if (!socraticData) return;

        const titleElem = document.getElementById('socratic-content-title');
        const badgeElem = document.getElementById('socratic-content-badge');
        const bodyElem = document.getElementById('socratic-body-text');
        const takeawayElem = document.getElementById('socratic-takeaway-text');

        if (tier === 'feynman') {
            badgeElem.className = 'badge-neon-emerald';
            badgeElem.innerText = 'FEYNMAN INTUITION';
            titleElem.innerText = socraticData.feynman.title;
            
            const paragraphs = socraticData.feynman.explanation.split('\n\n');
            bodyElem.innerHTML = paragraphs.map(p => `<p class="leading-relaxed">${p}</p>`).join('');
            takeawayElem.innerText = socraticData.feynman.key_takeaway;

        } else if (tier === 'rigorous') {
            badgeElem.className = 'badge-neon-cyan';
            badgeElem.innerText = 'RIGOROUS FORMULATION';
            titleElem.innerText = socraticData.rigorous.title;
            
            bodyElem.innerHTML = `<div class="font-sans space-y-3">${marked.parse(socraticData.rigorous.derivation)}</div>`;
            takeawayElem.innerText = socraticData.rigorous.key_takeaway;

            // Render equations via KaTeX
            if (window.renderMathInElement) {
                renderMathInElement(bodyElem, {
                    delimiters: [
                        { left: '$$', right: '$$', display: true },
                        { left: '$', right: '$', display: false }
                    ],
                    throwOnError: false
                });
            }

        } else if (tier === 'critique') {
            badgeElem.className = 'badge-neon-rose text-rose-400 bg-rose-500/10 border-rose-500/30';
            badgeElem.innerText = 'PEER-REVIEW SCRUTINY';
            titleElem.innerText = socraticData.critique.title;

            bodyElem.innerHTML = `
                <div class="space-y-3">
                    <p class="text-xs text-slate-400">Critical examination of underlying assumptions, computational bottlenecks, and boundary failure modes:</p>
                    <ul class="space-y-2 list-disc list-inside text-slate-300">
                        ${socraticData.critique.points.map(pt => `<li class="leading-relaxed">${pt}</li>`).join('')}
                    </ul>
                </div>
            `;
            takeawayElem.innerText = socraticData.critique.key_takeaway;

            if (window.renderMathInElement) {
                renderMathInElement(bodyElem, {
                    delimiters: [
                        { left: '$$', right: '$$', display: true },
                        { left: '$', right: '$', display: false }
                    ],
                    throwOnError: false
                });
            }
        }
    }

    function renderDiagnosticQuestion(idx = 0) {
        if (!socraticData || !socraticData.questions || socraticData.questions.length === 0) return;
        currentQuestionIndex = idx;
        const q = socraticData.questions[idx];

        document.getElementById('socratic-q-number').innerText = `Challenge ${idx + 1} of ${socraticData.questions.length}`;
        document.getElementById('socratic-question-text').innerText = q.question;
        
        const feedbackCard = document.getElementById('socratic-feedback-card');
        feedbackCard.classList.add('hidden');

        const optionsContainer = document.getElementById('socratic-options-list');
        optionsContainer.innerHTML = q.options.map((opt, optIdx) => `
            <button onclick="window.SocraticEngine.evaluateAnswer('${q.id}', ${optIdx})" 
                    id="q-opt-${optIdx}"
                    class="w-full text-left p-3 rounded-lg bg-slate-900/80 hover:bg-slate-800 border border-slate-800 text-xs text-slate-200 transition-all flex items-start gap-2.5">
                <span class="w-5 h-5 rounded-full bg-slate-800 flex items-center justify-center font-mono text-[11px] text-slate-400 shrink-0">${String.fromCharCode(65 + optIdx)}</span>
                <span class="leading-snug">${opt}</span>
            </button>
        `).join('');
    }

    async function evaluateAnswer(questionId, selectedIdx) {
        playSound('click');
        try {
            const res = await fetch('/api/socratic/evaluate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    paper_id: currentPaperId,
                    question_id: questionId,
                    selected_index: selectedIdx
                })
            });
            const data = await res.json();
            
            if (data.status === 'success') {
                const isCorrect = data.is_correct;
                const feedbackCard = document.getElementById('socratic-feedback-card');
                feedbackCard.classList.remove('hidden');

                if (isCorrect) {
                    playSound('success');
                    feedbackCard.className = 'p-3.5 rounded-lg text-xs leading-relaxed bg-emerald-950/40 border border-emerald-500/40 text-emerald-200';
                    feedbackCard.innerHTML = `
                        <div class="font-bold flex items-center gap-1.5 text-emerald-400 mb-1">
                            <i class="fa-solid fa-circle-check"></i> ${data.feedback}
                        </div>
                        <p>${data.explanation}</p>
                    `;
                } else {
                    playSound('pulse');
                    feedbackCard.className = 'p-3.5 rounded-lg text-xs leading-relaxed bg-rose-950/40 border border-rose-500/40 text-rose-200';
                    feedbackCard.innerHTML = `
                        <div class="font-bold flex items-center gap-1.5 text-rose-400 mb-1">
                            <i class="fa-solid fa-triangle-exclamation"></i> ${data.feedback}
                        </div>
                        <p>${data.explanation}</p>
                    `;
                }

                // Highlight buttons
                const btn = document.getElementById(`q-opt-${selectedIdx}`);
                if (btn) {
                    btn.classList.add(isCorrect ? 'border-emerald-500' : 'border-rose-500');
                    btn.classList.add(isCorrect ? 'bg-emerald-950/30' : 'bg-rose-950/30');
                }
            }
        } catch (e) {
            console.error('Failed to evaluate question', e);
        }
    }

    async function loadPrerequisites(paperId) {
        // Map paper to concept
        const map = {
            'paper-attn-2017': 'n-transformers',
            'paper-alphafold-2021': 'n-alphafold',
            'paper-chaos-1963': 'n-chaos',
            'paper-sir-1927': 'n-sir'
        };
        const conceptId = map[paperId] || 'n-transformers';

        try {
            const res = await fetch(`/api/socratic/prerequisites/${conceptId}`);
            const data = await res.json();
            const container = document.getElementById('socratic-prereqs-list');
            if (!container || !data.prerequisites) return;

            container.innerHTML = data.prerequisites.map(p => {
                let badgeClass = 'text-slate-400 bg-slate-800';
                if (p.status === 'Mastered') badgeClass = 'text-emerald-400 bg-emerald-950/40 border border-emerald-500/30';
                if (p.status === 'Review Recommended') badgeClass = 'text-amber-400 bg-amber-950/40 border border-amber-500/30';
                if (p.status === 'Target Skill') badgeClass = 'text-cyan-400 bg-cyan-950/40 border border-cyan-500/30';

                return `
                    <div class="p-2.5 rounded-lg bg-slate-900/70 border border-slate-800 flex items-center justify-between text-xs">
                        <span class="text-slate-200 font-medium">${p.name}</span>
                        <span class="px-2 py-0.5 rounded text-[10px] font-mono ${badgeClass}">${p.status}</span>
                    </div>
                `;
            }).join('');
        } catch (e) {
            console.error('Failed to load prerequisites', e);
        }
    }

    return {
        init,
        loadPaper,
        setTier,
        evaluateAnswer,
        getCurrentPaper: () => currentPaperId
    };
})();

// Global Socratic triggers
function loadSocraticPaper(paperId) {
    if (window.SocraticEngine) window.SocraticEngine.loadPaper(paperId);
}

function setSocraticTier(tier) {
    if (window.SocraticEngine) window.SocraticEngine.setTier(tier);
}

function jumpToSimulationFromSocratic() {
    const pid = window.SocraticEngine?.getCurrentPaper() || 'paper-attn-2017';
    switchView('simulations');
    
    const simMap = {
        'paper-attn-2017': 'sim-transformer-attention',
        'paper-alphafold-2021': 'sim-transformer-attention',
        'paper-sir-1927': 'sim-epidemic-sir',
        'paper-chaos-1963': 'sim-lorenz-chaos',
        'paper-lotka-1925': 'sim-lotka-volterra'
    };
    const simId = simMap[pid] || 'sim-transformer-attention';
    if (window.SimulationsEngine) {
        window.SimulationsEngine.loadSimulation(simId);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    window.SocraticEngine.init();
});
