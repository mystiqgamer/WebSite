from flask import Blueprint, jsonify, request
import uuid
import datetime

notes_bp = Blueprint("notes_bp", __name__)

USER_NOTES = [
    {
        "id": "note-ktu-1",
        "title": "CST 201: Infix to Postfix Algorithm Revision",
        "updated_at": "2026-10-27T12:00:00Z",
        "content": r"""# CST 201: Infix to Postfix Conversion Summary

## Core Rules for Exam:
1. Operands are directly placed into output string.
2. Operator precedence: `^` (highest, Right-to-Left) > `* /` (Left-to-Right) > `+ -` (lowest).
3. If incoming operator has higher precedence than stack top, **PUSH**.
4. If incoming operator has less than or equal precedence, **POP** and output until a lower precedence operator is encountered.

## Example:
Converting `A + B * C`:
- Token `A` $\to$ Output `A`
- Token `+` $\to$ Push `+`
- Token `B` $\to$ Output `A B`
- Token `*` $\to$ Push `*` (precedence `*` > `+`)
- Token `C` $\to$ Output `A B C`
- End of expression $\to$ Pop all: Output `A B C * +`
""",
        "tags": ["Data Structures", "Module 1", "KTU PYQ"]
    },
    {
        "id": "note-ktu-2",
        "title": "CST 206: Banker's Algorithm Safe State Steps",
        "updated_at": "2026-10-27T11:45:00Z",
        "content": r"""# CST 206: Banker's Deadlock Avoidance Notes

## Need Matrix Calculation:
$$\text{Need}[i][j] = \text{Max}[i][j] - \text{Allocation}[i][j]$$

## Safety Step:
Find process $P_i$ such that:
$$\text{Finish}[i] == \text{false} \quad \text{and} \quad \text{Need}_i \le \text{Work}$$
Then:
$$\text{Work} = \text{Work} + \text{Allocation}_i, \quad \text{Finish}[i] = \text{true}$$

*Tip for 10-mark question: Always draw the Safe Sequence clearly inside a box: $\langle P_1, P_3, P_4, P_0, P_2 \rangle$*
""",
        "tags": ["Operating Systems", "Module 3", "10-Mark Model"]
    }
]

@notes_bp.route("/api/notes", methods=["GET"])
def get_notes():
    return jsonify({
        "status": "success",
        "notes": USER_NOTES
    })

@notes_bp.route("/api/notes", methods=["POST"])
def save_note():
    data = request.get_json(silent=True) or {}
    note_id = data.get("id")
    title = data.get("title", "Untitled Revision Note").strip()
    content = data.get("content", "").strip()
    tags = data.get("tags", ["Revision"])
    
    now_str = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

    if note_id:
        existing = next((n for n in USER_NOTES if n["id"] == note_id), None)
        if existing:
            existing["title"] = title
            existing["content"] = content
            existing["tags"] = tags
            existing["updated_at"] = now_str
            return jsonify({"status": "success", "note": existing})

    new_note = {
        "id": f"note-{uuid.uuid4().hex[:6]}",
        "title": title,
        "content": content,
        "tags": tags,
        "updated_at": now_str
    }
    USER_NOTES.insert(0, new_note)
    return jsonify({"status": "success", "note": new_note})

@notes_bp.route("/api/notes/<note_id>", methods=["DELETE"])
def delete_note(note_id):
    global USER_NOTES
    USER_NOTES = [n for n in USER_NOTES if n["id"] != note_id]
    return jsonify({"status": "success", "message": f"Note '{note_id}' removed"})
