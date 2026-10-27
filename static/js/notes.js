/**
 * SynapseScholar OS - Manuscript Studio & Citation Manager
 * Real-time Markdown + LaTeX manuscript editor with live KaTeX preview,
 * BibTeX citation export, and draft synchronization.
 */

window.NotesEngine = (function() {
    let notes = [];
    let currentNoteId = null;

    async function init() {
        await loadNotes();
    }

    async function loadNotes() {
        try {
            const res = await fetch('/api/notes');
            const data = await res.json();
            if (data.status === 'success') {
                notes = data.notes;
                renderNotesList(notes);
                if (notes.length > 0 && !currentNoteId) {
                    selectNote(notes[0].id);
                }
            }
        } catch (e) {
            console.error('Failed to load notes', e);
        }
    }

    function renderNotesList(noteList) {
        const container = document.getElementById('notes-sidebar-list');
        if (!container) return;

        if (noteList.length === 0) {
            container.innerHTML = `<div class="p-3 text-xs text-slate-500 italic">No notes created yet.</div>`;
            return;
        }

        container.innerHTML = noteList.map(n => `
            <div onclick="window.NotesEngine.selectNote('${n.id}')" 
                 class="p-3 rounded-lg border transition-all cursor-pointer ${n.id === currentNoteId ? 'bg-slate-800/90 border-cyan-500/50 shadow-sm' : 'bg-slate-900/60 border-slate-800 hover:bg-slate-800/60'}">
                <div class="flex items-center justify-between text-xs">
                    <h4 class="font-bold text-slate-200 truncate flex-1">${n.title}</h4>
                    <button onclick="event.stopPropagation(); window.NotesEngine.deleteNote('${n.id}')" class="text-slate-500 hover:text-rose-400 p-1">
                        <i class="fa-solid fa-trash-can text-[10px]"></i>
                    </button>
                </div>
                <p class="text-[11px] text-slate-400 line-clamp-1 mt-1">${n.content.replace(/[#*`$]/g, '').trim() || 'Empty draft'}</p>
                <div class="flex items-center justify-between text-[10px] font-mono text-slate-500 mt-2">
                    <span>${(n.tags || []).join(', ')}</span>
                    <span>${n.updated_at ? n.updated_at.split('T')[0] : ''}</span>
                </div>
            </div>
        `).join('');
    }

    function selectNote(noteId) {
        playSound('click');
        currentNoteId = noteId;
        const note = notes.find(n => n.id === noteId);
        if (!note) return;

        document.getElementById('note-title-input').value = note.title;
        document.getElementById('note-content-input').value = note.content;
        renderNotesList(notes);
        updatePreview();
    }

    function createNewNote() {
        playSound('click');
        currentNoteId = null;
        document.getElementById('note-title-input').value = 'Untitled Research Manuscript';
        document.getElementById('note-content-input').value = `# New Research Manuscript\n\n## Abstract\nFormulate your hypothesis and mathematical framework here...\n\n$$\\mathcal{L}_{\\text{total}} = \\int_0^T \\|x(t) - \\hat{x}(t)\\|^2 dt$$\n`;
        updatePreview();
        showToast('Created new blank manuscript draft', 'info');
    }

    function updatePreview() {
        const content = document.getElementById('note-content-input')?.value || '';
        const previewPane = document.getElementById('note-preview-pane');
        if (!previewPane) return;

        // Render Markdown via marked
        previewPane.innerHTML = marked.parse(content);

        // Render LaTeX equations via KaTeX
        if (window.renderMathInElement) {
            renderMathInElement(previewPane, {
                delimiters: [
                    { left: '$$', right: '$$', display: true },
                    { left: '$', right: '$', display: false }
                ],
                throwOnError: false
            });
        }
    }

    async function saveNote() {
        const title = document.getElementById('note-title-input')?.value.trim() || 'Untitled Manuscript';
        const content = document.getElementById('note-content-input')?.value || '';

        playSound('pulse');
        try {
            const res = await fetch('/api/notes', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    id: currentNoteId,
                    title: title,
                    content: content,
                    tags: ['Draft', 'Manuscript']
                })
            });
            const data = await res.json();
            
            if (data.status === 'success') {
                playSound('success');
                showToast('Manuscript draft saved!', 'success');
                currentNoteId = data.note.id;
                await loadNotes();
            }
        } catch (e) {
            console.error('Failed to save note', e);
        }
    }

    async function deleteNote(noteId) {
        playSound('click');
        try {
            await fetch(`/api/notes/${noteId}`, { method: 'DELETE' });
            showToast('Note deleted', 'info');
            if (currentNoteId === noteId) currentNoteId = null;
            await loadNotes();
        } catch (e) {
            console.error('Failed to delete note', e);
        }
    }

    function createDraftFromGap(gapId) {
        createNewNote();
        document.getElementById('note-title-input').value = `Research Proposal: Gap [${gapId}]`;
        document.getElementById('note-content-input').value = `# Research Proposal: Empirical Synthesis\n\n## Target Problem\nAddressing the unmapped literature gap between disparate disciplinary domains.\n\n## Testable Hypothesis\n$$\\Delta \\Phi(x) \\propto \\lim_{N \\to \\infty} \\frac{1}{N} \\sum_{i=1}^N \\nabla \\mathcal{L}_i$$\n\n## Experimental Protocol\n1. Sample preparation and statistical power calculation ($1 - \\beta > 0.85$).\n2. Controlled empirical evaluation against mono-disciplinary baselines.\n`;
        updatePreview();
    }

    async function exportBibtex() {
        playSound('pulse');
        try {
            const res = await fetch('/api/notes/export/bibtex');
            const data = await res.json();
            
            if (data.status === 'success') {
                // Copy to clipboard
                await navigator.clipboard.writeText(data.bibtex);
                showToast(`Copied ${data.count} BibTeX citations to clipboard!`, 'success');
                playSound('success');
            }
        } catch (e) {
            showToast('BibTeX export generated', 'info');
        }
    }

    return {
        init,
        loadNotes,
        selectNote,
        createNewNote,
        updatePreview,
        saveNote,
        deleteNote,
        createDraftFromGap,
        exportBibtex
    };
})();

// Global note triggers
function createNewNote() {
    if (window.NotesEngine) window.NotesEngine.createNewNote();
}

function updateNotePreview() {
    if (window.NotesEngine) window.NotesEngine.updatePreview();
}

function saveCurrentNote() {
    if (window.NotesEngine) window.NotesEngine.saveNote();
}

function exportAllBibtex() {
    if (window.NotesEngine) window.NotesEngine.exportBibtex();
}

document.addEventListener('DOMContentLoaded', () => {
    window.NotesEngine.init();
});
