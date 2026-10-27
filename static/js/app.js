/**
 * KTU ScholarOS - Main Application Coordinator (B.Tech 2024 Scheme)
 * Controls CIE calculator, S1-S4 5-Module PYQ Master, 
 * 120 Activity Points Auditor (Three-Group Rule), 10-Mark Answer Architect.
 */

const AppState = {
    currentView: 'calculator',
    audioEnabled: true,
    audioCtx: null,
    courses: [],
    selectedCourse: null,
    selectedBranch: 'all',
    selectedSemester: 'all',
    activityGroups: [],
    userActivities: [
        { group_id: 'group-1', name: 'Emergency Response / CPR / First Aid / Fire Safety Training', points: 20 },
        { group_id: 'group-1', name: 'Acquiring Valid Four-Wheeler (LMV) Driving License', points: 15 },
        { group_id: 'group-2', name: 'Elected College Union Office Bearer (Chairman, Gen Sec, Councilor)', points: 30 },
        { group_id: 'group-3', name: '12-Week NPTEL / SWAYAM Online Course (Elite / Gold)', points: 50 }
    ]
};

// Web Audio API Synthesizer
function playSound(type = 'click') {
    if (!AppState.audioEnabled) return;
    try {
        if (!AppState.audioCtx) {
            AppState.audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        }
        if (AppState.audioCtx.state === 'suspended') AppState.audioCtx.resume();
        const ctx = AppState.audioCtx;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);
        const now = ctx.currentTime;

        if (type === 'click') {
            osc.frequency.setValueAtTime(560, now);
            gain.gain.setValueAtTime(0.06, now);
            gain.gain.linearRampToValueAtTime(0.001, now + 0.04);
            osc.start(now);
            osc.stop(now + 0.04);
        } else if (type === 'success') {
            osc.frequency.setValueAtTime(523, now);
            osc.frequency.setValueAtTime(659, now + 0.07);
            gain.gain.setValueAtTime(0.08, now);
            gain.gain.linearRampToValueAtTime(0.001, now + 0.2);
            osc.start(now);
            osc.stop(now + 0.2);
        }
    } catch (e) {
        // audio muted
    }
}

function toggleAudioFeedback() {
    AppState.audioEnabled = !AppState.audioEnabled;
    const btn = document.getElementById('btn-sound-toggle');
    if (btn) {
        btn.innerHTML = AppState.audioEnabled ? 
            '<i class="fa-solid fa-volume-high text-cyan-400"></i>' : 
            '<i class="fa-solid fa-volume-xmark text-slate-500"></i>';
    }
    showToast(AppState.audioEnabled ? 'Audio feedback enabled' : 'Audio muted');
}

function showToast(message, type = 'info') {
    const container = document.getElementById('toast-container');
    if (!container) return;
    const toast = document.createElement('div');
    toast.className = 'toast';
    const icon = type === 'success' ? '<i class="fa-solid fa-circle-check text-emerald-400"></i>' : '<i class="fa-solid fa-circle-info text-cyan-400"></i>';
    toast.innerHTML = `${icon} <span>${message}</span>`;
    container.appendChild(toast);
    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transition = 'all 0.2s ease';
        setTimeout(() => toast.remove(), 200);
    }, 2500);
}

// =========================================================================
// THEME MANAGER & PRESET SWITCHER
// =========================================================================
const THEMES = ['obsidian-indigo', 'cosmic-aurora', 'linear-titanium', 'emerald-matrix'];

function setAppTheme(themeName, silent = false) {
    if (!THEMES.includes(themeName)) themeName = 'obsidian-indigo';
    document.documentElement.setAttribute('data-theme', themeName);
    localStorage.setItem('ktu_scholar_theme', themeName);
    AppState.theme = themeName;

    THEMES.forEach(t => {
        const btn = document.getElementById(`theme-btn-${t}`);
        if (btn) {
            btn.classList.toggle('active', t === themeName);
        }
    });

    if (!silent) {
        playSound('click');
        const themeLabels = {
            'obsidian-indigo': 'Royal Obsidian (Indigo & Amber)',
            'cosmic-aurora': 'Cosmic Aurora (Nordic Teal)',
            'linear-titanium': 'Linear Titanium (Carbon & Gold)',
            'emerald-matrix': 'Oxford Emerald (Scholar Jade)'
        };
        showToast(`Theme switched to ${themeLabels[themeName] || themeName}`);
    }
}

function initAppTheme() {
    const saved = localStorage.getItem('ktu_scholar_theme') || 'obsidian-indigo';
    setAppTheme(saved, true);
}

// View Router
function switchView(viewName) {
    playSound('click');
    const views = ['calculator', 'courses', 'roadmap', 'simulations', 'activity', 'answers', 'notes'];
    views.forEach(v => {
        const sec = document.getElementById(`view-${v}`);
        const btn = document.getElementById(`nav-btn-${v}`);
        if (sec) sec.classList.toggle('hidden', v !== viewName);
        if (btn) btn.classList.toggle('active', v === viewName);
    });

    AppState.currentView = viewName;

    if (viewName === 'courses') {
        if (!AppState.courses || AppState.courses.length === 0) {
            filterCourses();
        } else {
            const currentSelected = document.getElementById('course-selector-dropdown')?.value;
            loadCourseDetails(currentSelected || AppState.courses[0].id);
        }
    } else if (viewName === 'answers') {
        loadAnswerBlueprints();
    } else if (viewName === 'activity') {
        auditActivities();
    } else if (viewName === 'notes' && window.NotesEngine) {
        window.NotesEngine.loadNotes();
    }
}

// =========================================================================
// MODULE 1: CIE & SUPPLY RISK PREDICTOR
// =========================================================================
async function runCIECalculation() {
    const s1 = parseFloat(document.getElementById('input-series1')?.value || 32);
    const s2 = parseFloat(document.getElementById('input-series2')?.value || 36);
    const assign = parseFloat(document.getElementById('input-assignment')?.value || 12);
    const att = parseFloat(document.getElementById('input-attendance')?.value || 86);

    document.getElementById('label-series1').innerText = `${s1} / 50`;
    document.getElementById('label-series2').innerText = `${s2} / 50`;
    document.getElementById('label-assignment').innerText = `${assign} / 15`;
    document.getElementById('label-attendance').innerText = `${att} %`;

    try {
        const res = await fetch('/api/calculator/cie', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ series1: s1, series2: s2, assignment: assign, attendance_pct: att })
        });
        const data = await res.json();
        
        if (data.status === 'success') {
            document.getElementById('out-series-contrib').innerText = `${data.cie_breakdown.series_marks} / 25`;
            document.getElementById('out-assign-contrib').innerText = `${data.cie_breakdown.assignment_marks} / 15`;
            document.getElementById('out-att-contrib').innerText = `${data.cie_breakdown.attendance_marks} / 10`;
            document.getElementById('out-total-cie').innerText = `${data.cie_total} / 50`;

            const riskBadge = document.getElementById('calculator-risk-badge');
            if (data.supply_risk === 'LOW') {
                riskBadge.className = 'px-4 py-2 rounded-xl text-center font-mono font-bold text-xs bg-emerald-500/10 border border-emerald-500/40 text-emerald-400';
                riskBadge.innerText = 'LOW SUPPLY RISK';
            } else if (data.supply_risk === 'MODERATE RISK') {
                riskBadge.className = 'px-4 py-2 rounded-xl text-center font-mono font-bold text-xs bg-amber-500/10 border border-amber-500/40 text-amber-400';
                riskBadge.innerText = 'MODERATE SUPPLY RISK';
            } else {
                riskBadge.className = 'px-4 py-2 rounded-xl text-center font-mono font-bold text-xs bg-rose-500/10 border border-rose-500/40 text-rose-400';
                riskBadge.innerText = 'HIGH SUPPLY RISK!';
            }

            document.getElementById('calculator-advice-text').innerText = data.risk_advice;

            const tbody = document.getElementById('grade-targets-table');
            if (tbody) {
                tbody.innerHTML = data.grade_targets.map(g => {
                    const isPass = (typeof g.min_esa_required === 'number' && g.min_esa_required <= 60);
                    return `
                        <div class="p-3 flex items-center justify-between hover:bg-slate-800/40 transition-colors">
                            <div class="flex items-center gap-2.5">
                                <span class="w-7 h-7 rounded bg-slate-800 flex items-center justify-center font-bold font-mono text-cyan-400 border border-slate-700">${g.grade}</span>
                                <div>
                                    <span class="font-bold text-slate-200">${g.desc}</span>
                                    <span class="text-[11px] font-mono text-slate-500 ml-2">(Req: ${g.target_pct}% Aggregate)</span>
                                </div>
                            </div>
                            <div class="text-right font-mono">
                                <span class="font-bold text-sm ${isPass ? 'text-emerald-400' : 'text-amber-400'}">
                                    ${typeof g.min_esa_required === 'number' ? g.min_esa_required + ' / 100' : g.min_esa_required}
                                </span>
                            </div>
                        </div>
                    `;
                }).join('');
            }
        }
    } catch (e) {
        console.error('CIE calculation error', e);
    }
}

// =========================================================================
// MODULE 2: 5-BRANCH S1-S8 5-MODULE SYLLABUS & PYQ MASTER
// =========================================================================
async function setBranchFilter(branchId) {
    playSound('click');
    AppState.selectedBranch = branchId;
    
    // Update branch pill UI
    const branches = ['all', 'cse', 'ece', 'eee', 'mech', 'ce_cn'];
    branches.forEach(b => {
        const pill = document.getElementById(`pill-branch-${b}`);
        if (pill) {
            if (b === branchId) {
                pill.className = 'branch-pill-btn px-3 py-1 rounded-full text-xs font-semibold theme-pill-active border';
            } else {
                pill.className = 'branch-pill-btn px-3 py-1 rounded-full text-xs font-semibold bg-slate-800/80 text-slate-300 hover:bg-slate-700/80 border border-transparent';
            }
        }
    });

    await filterCourses();
}

async function filterCourses() {
    const semDropdown = document.getElementById('semester-filter-dropdown');
    const selectedSem = semDropdown ? semDropdown.value : 'all';
    AppState.selectedSemester = selectedSem;

    try {
        const url = `/api/courses?branch=${AppState.selectedBranch || 'all'}&semester=${selectedSem || 'all'}`;
        const res = await fetch(url);
        const data = await res.json();
        
        if (data.status === 'success') {
            AppState.courses = data.courses;
            const courseSelect = document.getElementById('course-selector-dropdown');
            if (courseSelect) {
                if (data.courses.length === 0) {
                    courseSelect.innerHTML = '<option value="">No courses found</option>';
                    const deck = document.getElementById('course-modules-deck');
                    if (deck) {
                        deck.innerHTML = `
                            <div class="glass-card p-8 text-center text-slate-400 space-y-2">
                                <i class="fa-solid fa-folder-open text-2xl text-slate-500"></i>
                                <p class="text-sm font-medium">No courses matching selected branch and semester.</p>
                                <p class="text-xs text-slate-500">Try selecting "All Semesters" or a different branch.</p>
                            </div>
                        `;
                    }
                    document.getElementById('course-title-header').innerText = 'No Courses Found';
                    document.getElementById('course-meta-header').innerText = 'Adjust branch or semester filters';
                    document.getElementById('course-credits-badge').innerText = '0 Credits';
                    return;
                }

                courseSelect.innerHTML = data.courses.map(c => 
                    `<option value="${c.id}">${c.code}: ${c.title} (${c.semester})</option>`
                ).join('');

                // Load first matching course
                await loadCourseDetails(data.courses[0].id);
            }
        }
    } catch (e) {
        console.error('Failed to filter courses', e);
    }
}

async function loadCourseDetails(courseId) {
    if (!courseId) return;
    playSound('click');
    try {
        const res = await fetch(`/api/courses/${courseId}`);
        const data = await res.json();
        
        if (data.status === 'success') {
            const course = data.course;
            AppState.selectedCourse = course;

            // Sync dropdown value if not already matching
            const dropdown = document.getElementById('course-selector-dropdown');
            if (dropdown && dropdown.value !== course.id) {
                dropdown.value = course.id;
            }

            document.getElementById('course-title-header').innerText = `${course.code}: ${course.title}`;
            document.getElementById('course-meta-header').innerText = `${course.semester} • ${course.branch} (${course.category})`;
            document.getElementById('course-credits-badge').innerText = `${course.credits} Credits • 5 Modules`;

            const deck = document.getElementById('course-modules-deck');
            if (!deck) return;

            deck.innerHTML = course.modules.map(m => `
                <div class="glass-card p-5 space-y-3">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-2">
                        <div class="flex items-center gap-2.5">
                            <span class="w-8 h-8 rounded-lg bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center text-xs font-mono font-bold text-cyan-400">M${m.module_no}</span>
                            <h3 class="text-sm font-bold text-slate-100">${m.title}</h3>
                        </div>
                        <span class="text-xs font-mono text-emerald-400 font-semibold">${m.weightage_marks} Marks Weightage</span>
                    </div>

                    <p class="text-xs text-slate-400 leading-relaxed"><b class="text-slate-300">Syllabus:</b> ${m.syllabus}</p>

                    <div class="pt-2 border-t border-slate-800 space-y-2">
                        <div class="text-xs font-mono text-cyan-400 font-bold uppercase flex items-center gap-1.5">
                            <i class="fa-solid fa-fire text-amber-400"></i>
                            <span>High-Yield Repeated KTU Exam Questions:</span>
                        </div>
                        <div class="space-y-2">
                            ${m.high_yield_pyqs.map(p => `
                                <div class="p-3 rounded-lg bg-slate-900/90 border border-slate-800/80 flex items-start justify-between gap-3 text-xs">
                                    <div class="space-y-1">
                                        <p class="text-slate-200 leading-snug font-medium">${p.q}</p>
                                        <span class="badge-neon-amber text-[10px]"><i class="fa-solid fa-repeat mr-1"></i>${p.frequency}</span>
                                    </div>
                                    <span class="font-mono font-bold text-purple-400 shrink-0">${p.marks}m</span>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                </div>
            `).join('');
        }
    } catch (e) {
        console.error('Failed to load course details', e);
    }
}

// =========================================================================
// MODULE 3: 10-MARK ANSWER ARCHITECT
// =========================================================================
async function loadAnswerBlueprints() {
    try {
        const res = await fetch('/api/answers/blueprints');
        const data = await res.json();
        
        if (data.status === 'success') {
            const container = document.getElementById('answer-blueprints-deck');
            if (!container) return;

            container.innerHTML = data.blueprints.map(b => `
                <div class="glass-card p-6 space-y-4">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                        <div>
                            <span class="badge-neon-cyan">${b.subject}</span>
                            <h3 class="text-base font-bold text-slate-100 mt-1">${b.question}</h3>
                        </div>
                        <span class="font-mono text-sm font-bold text-purple-400 px-3 py-1 bg-purple-500/10 rounded border border-purple-500/30">${b.marks} Marks Full Answer</span>
                    </div>

                    <div class="space-y-3">
                        ${b.blueprint.map(sec => `
                            <div class="p-3.5 rounded-lg bg-slate-900/80 border border-slate-800/80 space-y-1.5">
                                <div class="flex items-center justify-between text-xs font-mono">
                                    <span class="font-bold text-emerald-400">${sec.section}</span>
                                    <div class="flex gap-3 text-slate-400">
                                        <span>Time: <b class="text-slate-200">${sec.recommended_time}</b></span>
                                        <span>Marks: <b class="text-cyan-400">${sec.marks_allocated}m</b></span>
                                    </div>
                                </div>
                                <p class="text-xs text-slate-300 leading-relaxed font-sans whitespace-pre-line">${sec.content}</p>
                            </div>
                        `).join('')}
                    </div>
                </div>
            `).join('');
        }
    } catch (e) {
        console.error('Failed to load answer blueprints', e);
    }
}

// =========================================================================
// MODULE 4: REVISED KTU 2024 SCHEME 120 ACTIVITY POINTS (THREE-GROUP RULE)
// =========================================================================
async function auditActivities() {
    try {
        if (AppState.activityGroups.length === 0) {
            const resDir = await fetch('/api/activity_points');
            const dataDir = await resDir.json();
            if (dataDir.status === 'success') {
                AppState.activityGroups = dataDir.groups;
            }
        }

        const res = await fetch('/api/activity_points/audit', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_activities: AppState.userActivities })
        });
        const data = await res.json();
        
        if (data.status === 'success') {
            document.getElementById('activity-total-points').innerText = `${data.total_verified_points} / 120`;
            document.getElementById('activity-overall-pct').innerText = `${data.overall_progress_pct}%`;
            document.getElementById('activity-progress-bar').style.width = `${data.overall_progress_pct}%`;

            // Compliance status banner
            const banner = document.getElementById('activity-compliance-banner');
            if (banner) {
                if (data.is_degree_eligible) {
                    banner.className = 'p-3.5 rounded-lg border text-xs font-mono flex items-center justify-between bg-emerald-950/40 border-emerald-500/40 text-emerald-300';
                    banner.innerHTML = `
                        <div class="flex items-center gap-2">
                            <i class="fa-solid fa-circle-check text-emerald-400 text-base"></i>
                            <span>${data.verdict}</span>
                        </div>
                        <span class="badge-neon-emerald">DEGREE CLEARED</span>
                    `;
                } else {
                    banner.className = 'p-3.5 rounded-lg border text-xs font-mono flex items-center justify-between bg-amber-950/40 border-amber-500/40 text-amber-300';
                    banner.innerHTML = `
                        <div class="flex items-center gap-2">
                            <i class="fa-solid fa-triangle-exclamation text-amber-400 text-base"></i>
                            <span>${data.verdict}</span>
                        </div>
                        <span class="badge-neon-amber">DEFICIT PENDING</span>
                    `;
                }
            }

            // Render the 3 Activity Group Cards
            const deck = document.getElementById('activity-groups-deck');
            if (!deck) return;

            deck.innerHTML = AppState.activityGroups.map(grp => {
                const auditG = data.group_breakdowns.find(b => b.group_id === grp.group_id) || { capped_points: 0, has_met_minimum: false };
                const isMet = auditG.has_met_minimum;

                return `
                    <div class="glass-card p-5 space-y-4 border ${isMet ? 'border-emerald-500/30' : 'border-amber-500/30'}">
                        <div class="space-y-1">
                            <div class="flex items-center justify-between text-xs font-mono">
                                <span class="badge-neon-${isMet ? 'emerald' : 'amber'}">${isMet ? 'MINIMUM MET' : 'DEFICIT'}</span>
                                <span class="font-bold text-sm ${isMet ? 'text-emerald-400' : 'text-amber-400'} font-mono">${auditG.capped_points} / 40 min</span>
                            </div>
                            <h3 class="text-sm font-bold text-slate-100">${grp.group_name.split(':')[0]}</h3>
                            <p class="text-[11px] text-slate-400 leading-snug">${grp.focus}</p>
                        </div>

                        <!-- Mini Progress bar for this group -->
                        <div class="w-full bg-slate-800 rounded-full h-2 overflow-hidden border border-slate-700">
                            <div class="h-full bg-gradient-to-r from-cyan-400 to-emerald-400 transition-all duration-300" style="width: ${auditG.progress_pct}%"></div>
                        </div>

                        <div class="pt-2 border-t border-slate-800 space-y-2 max-h-72 overflow-y-auto">
                            ${grp.activities.map(act => {
                                const isChecked = AppState.userActivities.some(u => u.name === act.name);
                                return `
                                    <label class="flex items-start gap-2.5 text-xs text-slate-300 cursor-pointer hover:text-white transition-colors p-1.5 rounded hover:bg-slate-800/40">
                                        <input type="checkbox" class="accent-cyan-400 mt-0.5" 
                                               ${isChecked ? 'checked' : ''}
                                               onchange="toggleActivity('${grp.group_id}', '${act.name}', ${act.points}, this.checked)">
                                        <div class="flex-1">
                                            <div class="flex justify-between items-center">
                                                <span class="font-medium text-slate-200">${act.name}</span>
                                                <span class="font-mono font-bold text-cyan-400 ml-1">+${act.points}</span>
                                            </div>
                                            <span class="text-[10px] text-slate-500 font-mono block mt-0.5">Proof: ${act.doc_req}</span>
                                        </div>
                                    </label>
                                `;
                            }).join('')}
                        </div>
                    </div>
                `;
            }).join('');
        }
    } catch (e) {
        console.error('Activity audit error', e);
    }
}

function toggleActivity(groupId, actName, pts, isChecked) {
    playSound('click');
    if (isChecked) {
        AppState.userActivities.push({ group_id: groupId, name: actName, points: pts });
    } else {
        AppState.userActivities = AppState.userActivities.filter(a => a.name !== actName);
    }
    auditActivities();
}

// Global search handler
function handleGlobalSearch(q) {
    const query = q.trim().toLowerCase();
    if (!query) return;
    
    // Quick course shortcuts
    if (query.includes('mat') || query.includes('calc') || query.includes('linear')) {
        switchView('courses');
        loadCourseDetails('mat101-calc');
    } else if (query.includes('c prog') || query.includes('cprog') || query.includes('c language')) {
        switchView('courses');
        loadCourseDetails('est102-cprog');
    } else if (query.includes('ds') || query.includes('data struct') || query.includes('stack') || query.includes('tree')) {
        switchView('courses');
        loadCourseDetails('cst201-ds');
    } else if (query.includes('logic') || query.includes('lsd') || query.includes('kmap') || query.includes('gate') || query.includes('flip')) {
        switchView('courses');
        loadCourseDetails('cst203-lsd');
    } else if (query.includes('coa') || query.includes('booth') || query.includes('cache') || query.includes('arch')) {
        switchView('courses');
        loadCourseDetails('cst202-coa');
    } else if (query.includes('dbms') || query.includes('sql') || query.includes('normaliz')) {
        switchView('courses');
        loadCourseDetails('cst204-dbms');
    } else if (query.includes('os') || query.includes('operat') || query.includes('schedul') || query.includes('banker')) {
        switchView('courses');
        loadCourseDetails('cst206-os');
    } else if (query.includes('flat') || query.includes('automata') || query.includes('dfa') || query.includes('turing')) {
        switchView('courses');
        loadCourseDetails('cst301-flat');
    } else if (query.includes('ai') || query.includes('artificial') || query.includes('heuristic') || query.includes('a*')) {
        switchView('courses');
        loadCourseDetails('cst401-ai');
    } else if (query.includes('ssd') || query.includes('solid state') || query.includes('mosfet') || query.includes('diode') || query.includes('pn junction')) {
        switchView('courses');
        loadCourseDetails('ect201-ssd');
    } else if (query.includes('dsp') || query.includes('digital signal') || query.includes('fft') || query.includes('dft') || query.includes('z-transform')) {
        switchView('courses');
        loadCourseDetails('ect303-dsp');
    } else if (query.includes('circuit') || query.includes('thevenin') || query.includes('norton') || query.includes('laplace') || query.includes('mesh')) {
        switchView('courses');
        loadCourseDetails('eet201-circuits');
    } else if (query.includes('power system') || query.includes('transmission line') || query.includes('sag') || query.includes('corona') || query.includes('insulator')) {
        switchView('courses');
        loadCourseDetails('eet301-power');
    } else if (query.includes('thermo') || query.includes('carnot') || query.includes('entropy') || query.includes('otto') || query.includes('diesel')) {
        switchView('courses');
        loadCourseDetails('met203-thermo');
    } else if (query.includes('heat') || query.includes('mass transfer') || query.includes('conduction') || query.includes('fourier') || query.includes('nusselt')) {
        switchView('courses');
        loadCourseDetails('met302-hmt');
    } else if (query.includes('solid') || query.includes('sfd') || query.includes('bmd') || query.includes('bending') || query.includes('shear force')) {
        switchView('courses');
        loadCourseDetails('cet201-solids');
    } else if (query.includes('crypto') || query.includes('rsa') || query.includes('des') || query.includes('aes') || query.includes('network security')) {
        switchView('courses');
        loadCourseDetails('cnt301-crypto');
    } else if (query.includes('internal') || query.includes('cie') || query.includes('mark') || query.includes('supply')) {
        switchView('calculator');
    } else if (query.includes('activity') || query.includes('points') || query.includes('nss') || query.includes('nptel')) {
        switchView('activity');
    } else if (query.includes('roadmap') || query.includes('credit') || query.includes('170') || query.includes('degree')) {
        switchView('roadmap');
    } else if (query.includes('answer') || query.includes('blueprint') || query.includes('10-mark') || query.includes('10 mark')) {
        switchView('answers');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    initAppTheme();
    runCIECalculation();
    auditActivities();
    filterCourses();
});
