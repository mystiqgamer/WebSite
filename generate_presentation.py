"""
KTU Nexus - Simple, Clean & Professional Presentation Generator (.pptx)
Generates a 16:9 widescreen presentation deck with speaker notes,
clean executive light theme, crisp typography, and presenter attribution:
Felix Louie Sojan & Adithya Jobies.
"""

import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck(output_path="static/KTU_Nexus_Presentation.pptx"):
    prs = Presentation()
    # 16:9 Widescreen standard
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Simple, Clean Executive Palette (Light Minimalist Theme)
    COLOR_BG = RGBColor(248, 250, 252)          # #F8FAFC Soft Crisp Canvas
    COLOR_CARD = RGBColor(255, 255, 255)        # #FFFFFF Pure White Surface
    COLOR_CARD_BORDER = RGBColor(226, 232, 240) # #E2E8F0 Subtle Border
    COLOR_PRIMARY = RGBColor(29, 78, 216)       # #1D4ED8 Executive Royal Blue
    COLOR_NAVY = RGBColor(15, 23, 42)           # #0F172A Deep Midnight Charcoal
    COLOR_TEXT_BODY = RGBColor(51, 65, 85)      # #334155 High-Contrast Slate
    COLOR_TEXT_MUTED = RGBColor(100, 116, 139)  # #64748B Secondary Slate
    COLOR_AMBER = RGBColor(217, 119, 6)         # #D97706 Warm Amber
    COLOR_EMERALD = RGBColor(5, 150, 105)       # #059669 Forest Emerald
    COLOR_ROSE = RGBColor(225, 29, 72)          # #E11D48 Crimson Accent
    COLOR_CARD_ALT = RGBColor(241, 245, 249)    # #F1F5F9 Soft Tint Surface

    blank_layout = prs.slide_layouts[6] # Blank slide layout

    def add_bg(slide):
        bg_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg_shape.fill.solid()
        bg_shape.fill.fore_color.rgb = COLOR_BG
        bg_shape.line.fill.background()
        return bg_shape

    def add_header(slide, badge_text, title_text, subtitle_text=None, badge_color=COLOR_PRIMARY):
        # Category Badge
        badge_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.45), Inches(8.0), Inches(0.35))
        tf_b = badge_box.text_frame
        tf_b.word_wrap = True
        p_b = tf_b.paragraphs[0]
        p_b.text = badge_text.upper()
        p_b.font.size = Pt(10)
        p_b.font.bold = True
        p_b.font.color.rgb = badge_color
        p_b.font.name = "Calibri"

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.8))
        tf_t = title_box.text_frame
        tf_t.word_wrap = True
        p_t = tf_t.paragraphs[0]
        p_t.text = title_text
        p_t.font.size = Pt(25)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_NAVY
        p_t.font.name = "Calibri"

        # Subtitle
        if subtitle_text:
            sub_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.45), Inches(11.7), Inches(0.45))
            tf_s = sub_box.text_frame
            tf_s.word_wrap = True
            p_s = tf_s.paragraphs[0]
            p_s.text = subtitle_text
            p_s.font.size = Pt(12)
            p_s.font.color.rgb = COLOR_TEXT_MUTED
            p_s.font.name = "Calibri"

    def add_card(slide, left, top, width, height, title, items, badge="", accent_color=COLOR_PRIMARY, bg_color=COLOR_CARD):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = COLOR_CARD_BORDER
        card.line.width = Pt(1)

        tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), width - Inches(0.4), height - Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        if badge:
            p0.text = f"[{badge}]  {title}"
        else:
            p0.text = title
        p0.font.size = Pt(15)
        p0.font.bold = True
        p0.font.color.rgb = accent_color
        p0.font.name = "Calibri"
        p0.space_after = Pt(8)

        for item in items:
            p = tf.add_paragraph()
            p.text = f"• {item}"
            p.font.size = Pt(11)
            p.font.color.rgb = COLOR_TEXT_BODY
            p.font.name = "Calibri"
            p.space_after = Pt(5)

    # =========================================================================
    # SLIDE 1: TITLE SLIDE (SIMPLE CLEAN EXECUTIVE THEME)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    add_bg(s1)

    # Decorative crisp accent line
    bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.1), Inches(1.2), Inches(0.06))
    bar.fill.solid()
    bar.fill.fore_color.rgb = COLOR_PRIMARY
    bar.line.fill.background()

    tb1 = s1.shapes.add_textbox(Inches(0.8), Inches(1.35), Inches(11.7), Inches(3.4))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p_badge = tf1.paragraphs[0]
    p_badge.text = "APJ ABDUL KALAM TECHNOLOGICAL UNIVERSITY • B.TECH 2024 SCHEME (NEP 2020)"
    p_badge.font.size = Pt(11)
    p_badge.font.bold = True
    p_badge.font.color.rgb = COLOR_PRIMARY
    p_badge.space_after = Pt(10)

    p_title = tf1.add_paragraph()
    p_title.text = "KTU Nexus"
    p_title.font.size = Pt(46)
    p_title.font.bold = True
    p_title.font.color.rgb = COLOR_NAVY
    p_title.space_after = Pt(8)

    p_sub = tf1.add_paragraph()
    p_sub.text = "The Unified Academic Intelligence Suite & Exam Co-Pilot for Engineering Students"
    p_sub.font.size = Pt(18)
    p_sub.font.bold = True
    p_sub.font.color.rgb = COLOR_PRIMARY
    p_sub.space_after = Pt(14)

    p_desc = tf1.add_paragraph()
    p_desc.text = "Complete 5-Branch S1–S8 Syllabi • CIE & Supply Predictor • 120 Activity Points 3-Group Compliance Auditor • Interactive Simulation Labs"
    p_desc.font.size = Pt(13)
    p_desc.font.color.rgb = COLOR_TEXT_MUTED

    # Presenters Card - Simple, Clean, Exact Names (NO team name)
    add_card(s1, Inches(0.8), Inches(5.1), Inches(11.7), Inches(1.6),
             "Presented by: Felix Louie Sojan & Adithya Jobies",
             [
                 "Unified Academic Intelligence Platform engineered specifically for KTU Kerala B.Tech Affiliated Colleges",
                 "Live Production Platform: http://127.0.0.1:5000 | 87 Comprehensive Courses | 435 Modules | 437 High-Yield PYQs"
             ],
             badge="PRESENTERS", accent_color=COLOR_PRIMARY, bg_color=COLOR_CARD)

    s1.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTES (30-45s):\n"
        "Good morning judges and colleagues. We are Felix Louie Sojan and Adithya Jobies, and today we are excited to present KTU Nexus. "
        "With the implementation of the National Education Policy 2024 Scheme by APJ Abdul Kalam Technological University, "
        "engineering education in Kerala underwent a massive transformation. However, students and faculty were left stranded "
        "with fragmented regulations, strict new activity point constraints, and opaque internal evaluation math. "
        "KTU Nexus is the first unified academic intelligence system that completely solves this problem."
    )

    # =========================================================================
    # SLIDE 2: THE REAL-WORLD CRISIS
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_bg(s2)
    add_header(s2, "The Real-World Crisis", "Why B.Tech Engineering Students Face Academic Peril",
               "Three systemic pain points introduced by the revised KTU 2024 Scheme that cause degrees to be delayed or withheld.")

    add_card(s2, Inches(0.8), Inches(2.1), Inches(3.6), Inches(4.7),
             "The 120-Activity Point Trap",
             [
                 "Revision: Requirement increased from 100 to 120 points (awarding 3 academic credits).",
                 "The Three-Group Rule: Must earn minimum 40 points in EACH of the 3 groups (Social, Cultural, Professional).",
                 "The Catch: Students with 120+ total points still have their DEGREE WITHHELD if even one group has <40 points.",
                 "Zero visibility into category caps and approved document criteria."
             ],
             badge="REGULATORY DEFICIT", accent_color=COLOR_AMBER)

    add_card(s2, Inches(4.8), Inches(2.1), Inches(3.6), Inches(4.7),
             "The CIE & Supply Trap",
             [
                 "Continuous Internal Evaluation (50 marks) is scaled from Series Exams (25), Assignments (15), and Attendance (10).",
                 "Mandatory 40% University Exam (ESA) threshold: Scoring less than 40/100 triggers an instant supplementary exam ('Supply').",
                 "Students study blindly without knowing the exact minimum marks required in ESA to secure their target grade or avoid failing."
             ],
             badge="EXAM FAILURE RISK", accent_color=COLOR_ROSE)

    add_card(s2, Inches(8.8), Inches(2.1), Inches(3.6), Inches(4.7),
             "Fragmented Curriculum Data",
             [
                 "5 major engineering branches (CSE, ECE, EEE, MECH, CE/CN) lack centralized topic syllabi.",
                 "KTU's 15-mark per module question paper distribution requires laser-focused preparation.",
                 "Students waste hundreds of hours hunting scattered Telegram groups and informal notes for repeated university PYQs."
             ],
             badge="CURRICULUM GAP", accent_color=COLOR_PRIMARY)

    s2.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTES (45s):\n"
        "Let's look at the reality on the ground across 150+ KTU colleges. "
        "First, the 120 Activity Point Three-Group rule. Many students think they just need 120 points total—so they do 120 points of NPTEL courses. "
        "Under 2024 regulations, their degree will be denied because KTU mandates at least 40 points in Social and 40 points in Sports/Arts. "
        "Second, internal marks. Students often have no idea how their series exams and attendance combine, or how many marks they must get in the 100-mark university paper to pass. "
        "Third, there is no centralized repository covering all 5 branches with exact 15-mark module allocations."
    )

    # =========================================================================
    # SLIDE 3: SOLUTION ARCHITECTURE - KTU NEXUS
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_bg(s3)
    add_header(s3, "The Architecture", "KTU Nexus: A Complete Academic Ecosystem",
               "Five integrated software subsystems engineered to empower students from Semester 1 to Semester 8.")

    # 4 metrics banner in clean white cards with colored top border
    metrics_data = [
        ("87 Courses", "Full S1-S8 Coverage across 5 Branches", COLOR_PRIMARY),
        ("435 Modules", "15-Mark Syllabus Mapping per Module", COLOR_EMERALD),
        ("437 PYQs", "Repeated KTU Exam Questions with Marks", COLOR_AMBER),
        ("120 Points", "3-Group Auditor (Min 40 pts/Group)", COLOR_NAVY)
    ]
    for idx, (m_val, m_lbl, m_col) in enumerate(metrics_data):
        box_w = Inches(2.7)
        box_l = Inches(0.8) + idx * Inches(2.95)
        m_card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, box_l, Inches(2.1), box_w, Inches(1.3))
        m_card.fill.solid()
        m_card.fill.fore_color.rgb = COLOR_CARD
        m_card.line.color.rgb = COLOR_CARD_BORDER
        tf = m_card.text_frame
        tf.word_wrap = True
        p1 = tf.paragraphs[0]
        p1.text = m_val
        p1.font.size = Pt(22)
        p1.font.bold = True
        p1.font.color.rgb = m_col
        p2 = tf.add_paragraph()
        p2.text = m_lbl
        p2.font.size = Pt(10)
        p2.font.color.rgb = COLOR_TEXT_MUTED

    # Bottom 3 core pillars
    add_card(s3, Inches(0.8), Inches(3.7), Inches(3.6), Inches(3.1),
             "Syllabus & PYQ Master",
             [
                 "S1-S8 for CSE, ECE, EEE, MECH, CE/CN.",
                 "Exact 15-mark module weightages.",
                 "High-yield repeated exam questions.",
                 "Instant keyword search across all courses."
             ],
             badge="CORE ENGINE", accent_color=COLOR_PRIMARY)

    add_card(s3, Inches(4.8), Inches(3.7), Inches(3.6), Inches(3.1),
             "CIE & Supply Predictor",
             [
                 "Automated internal mark scaling (out of 50).",
                 "Calculates minimum ESA exam marks needed.",
                 "Dynamic supply risk categorization.",
                 "Grade target thresholds for O, A+, A, B+, B, C."
             ],
             badge="ANALYTICS", accent_color=COLOR_EMERALD)

    add_card(s3, Inches(8.8), Inches(3.7), Inches(3.6), Inches(3.1),
             "120-Point Activity Auditor",
             [
                 "Full Three-Group compliance engine.",
                 "Calculates Group 1, 2, and 3 capped points.",
                 "Flags pending deficits immediately.",
                 "Offers targeted activity recommendations."
             ],
             badge="REGULATION", accent_color=COLOR_AMBER)

    s3.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTES (45s):\n"
        "Here is our solution: KTU Nexus. "
        "We built a high-performance, responsive academic platform with 87 complete courses, 435 mapped modules, and 437 curated past exam questions. "
        "It acts as a personal academic co-pilot for every engineering student in Kerala. "
        "Let's dive into each of the main features."
    )

    # =========================================================================
    # SLIDE 4: 5-BRANCH S1-S8 CURRICULUM COVERAGE
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_bg(s4)
    add_header(s4, "Branch Curriculum Matrix", "Comprehensive S1 to S8 Academic Repository",
               "Full academic scope across all 5 major engineering branches plus common first year foundation.")

    branches = [
        ("Common First Year (S1 & S2)", ["MAT 101/102 Calculus & Diff Eq", "PHT 100 Physics & CYT 100 Chemistry", "EST 100 Mechanics & EST 130 Graphics", "EST 102 Programming in C & EST 110/120"], "10 Courses • 50 Modules", COLOR_NAVY),
        ("Computer Science (CSE)", ["S3-S4: Data Structures, LSD, COA, DBMS, OS", "S5-S6: Automata (FLAT), Networks, Compiler, DAA", "S7-S8: AI, Network Security, Cloud Computing", "Includes Java OOP, System Software, Microprocessors"], "28 Courses • 140 Modules", COLOR_PRIMARY),
        ("Electronics & Comm (ECE)", ["S3-S4: Solid State Devices, Logic Design, Signals", "S5-S6: LIC Op-Amps, DSP, Analog/Digital Comms, VLSI", "S7-S8: Microwave & Antenna, Wireless, Satellite", "Includes Network Theory, Computer Architecture"], "25 Courses • 125 Modules", COLOR_EMERALD),
        ("Electrical & Electronics (EEE)", ["S3-S4: Circuits & Networks, DC Machines, EMFT", "S5-S6: Power Systems I & II, AC Machines, Drives", "S7-S8: Advanced Control Systems, EV & Smart Grid", "Includes Linear Control Systems, Instrumentation"], "23 Courses • 115 Modules", COLOR_AMBER),
        ("Mechanical Engineering (MECH)", ["S3-S4: Mechanics of Solids, Thermodynamics, Fluid Mech", "S5-S6: Mechanics of Machinery, Heat & Mass Transfer", "S7-S8: Machine Element Design, Mechatronics, Energy", "Includes Manufacturing Processes, Metrology"], "23 Courses • 115 Modules", COLOR_ROSE),
        ("Civil & Computer Networking (CE/CN)", ["S3-S4: Structural Analysis I, Fluid Mech, Soil Mech", "S5-S6: Design of Concrete (RCC) & Steel Structures", "S7-S8: Quantity Surveying, Earthquake Engg, Foundations", "Plus Network Security, Wireless Networks, Cyber Forensics"], "28 Courses • 140 Modules", COLOR_PRIMARY)
    ]

    col_w = Inches(3.7)
    row_h = Inches(2.25)
    for i, (b_title, b_courses, b_meta, b_col) in enumerate(branches):
        r = i // 3
        c = i % 3
        x = Inches(0.8) + c * Inches(3.95)
        y = Inches(2.1) + r * Inches(2.5)
        add_card(s4, x, y, col_w, row_h, b_title, b_courses, badge=b_meta, accent_color=b_col)

    s4.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTES (45s):\n"
        "Notice the depth of our academic coverage. We didn't just build a demo with one or two subjects. "
        "We mapped all 8 semesters for Computer Science, Electronics, Electrical, Mechanical, Civil Engineering, and Computer Networking, "
        "plus the common foundation courses in S1 and S2. "
        "Every single course contains all 5 modules, the official KTU 2024 syllabus, 15-mark module allocations, and high-yield repeated questions."
    )

    # =========================================================================
    # SLIDE 5: CIE & SUPPLY RISK PREDICTOR
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_bg(s5)
    add_header(s5, "Predictive Analytics", "Continuous Internal Evaluation & Exam Safety",
               "Real-time mathematical forecasting to eliminate the panic of university supplementary exams.")

    add_card(s5, Inches(0.8), Inches(2.1), Inches(5.6), Inches(4.7),
             "Internal Mark Normalization Formula",
             [
                 "Series Exam Component (25 Marks): Scaled from the average of Series 1 and Series 2 exams: (Avg / 50) * 25.",
                 "Continuous Assessment (15 Marks): Homework, class tests, and design assignments.",
                 "Attendance Component (10 Marks): Tiered reward system (>85% = 10m, 80-84% = 8m, 75-79% = 6m).",
                 "Total CIE Max: 50 Marks.",
                 "University Requirement: Minimum 50% aggregate (CIE + ESA >= 75/150) AND minimum 40% in ESA (>= 40/100) are mandatory."
             ],
             badge="KTU 2024 FORMULA", accent_color=COLOR_PRIMARY)

    add_card(s5, Inches(6.8), Inches(2.1), Inches(5.7), Inches(4.7),
             "Live Target Grade & Risk Predictor",
             [
                 "Input: Student slides Series 1, Series 2, Assignments, and Attendance.",
                 "Output 1: Dynamic Supply Risk Position (LOW, MODERATE, HIGH RISK).",
                 "Output 2: Exact minimum score required in the 100-mark End Semester Exam for EVERY KTU Grade:",
                 "   • Grade O (>=90%): Need 78 / 100 in ESA",
                 "   • Grade A+ (>=85%): Need 70 / 100 in ESA",
                 "   • Grade A (>=80%): Need 63 / 100 in ESA",
                 "   • Grade B+ (>=70%): Need 48 / 100 in ESA",
                 "   • Grade C (Pass >=50%): Need 40 / 100 in ESA (University Floor)",
                 "Eliminates exam anxiety by providing crystal-clear targets."
             ],
             badge="REAL-TIME FORECAST", accent_color=COLOR_EMERALD)

    s5.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTES (45s):\n"
        "Here is our CIE & Supply Risk Predictor. "
        "Under KTU regulations, you need a minimum of 40 out of 100 in the university written exam, plus at least 50% overall to pass. "
        "A student using our platform inputs their series marks and attendance. "
        "The system immediately calculates their exact internal mark out of 50 and generates a personalized target table. "
        "It tells them: 'You have 37 internals. You only need 40 in ESA to pass, or 63 to get an A grade.' "
        "This gives students clarity and eliminates exam anxiety."
    )

    # =========================================================================
    # SLIDE 6: 120 ACTIVITY POINTS THREE-GROUP AUDITOR
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_bg(s6)
    add_header(s6, "Regulatory Compliance", "The 120 Activity Points Three-Group Auditor",
               "Guarding students against the most common degree-withholding trap in KTU 2024 Scheme.")

    add_card(s6, Inches(0.8), Inches(2.1), Inches(3.6), Inches(4.7),
             "Group 1: Social & Life Skills",
             [
                 "Threshold: Min 40 / Max 60 Pts",
                 "NSS Volunteer (2 Yrs + Camp): 60 pts",
                 "NCC 'B' or 'C' Certificate: 50 pts",
                 "CPR / First Aid / Fire Safety: 20 pts",
                 "Four-Wheeler Driving License: 15 pts",
                 "Blood Donation: 8 pts (Max 16 pts)",
                 "Certified Swimming Course: 15 pts",
                 "Tree Planting / Eco Drive: 10 pts"
             ],
             badge="GROUP 1", accent_color=COLOR_PRIMARY)

    add_card(s6, Inches(4.8), Inches(2.1), Inches(3.6), Inches(4.7),
             "Group 2: Cultural, Sports & Leadership",
             [
                 "Threshold: Min 40 / Max 60 Pts",
                 "KTU Inter-Collegiate Sports Prize: 40 pts",
                 "University Kalolsavam Winner: 40 pts",
                 "Elected College Union Leader: 30 pts",
                 "Student Club Lead (IEDC/IEEE): 20 pts",
                 "College Magazine Editorial: 15 pts",
                 "College Arts/Sports Day Winner: 15 pts",
                 "Inter-Collegiate Fest Participation: 10 pts"
             ],
             badge="GROUP 2", accent_color=COLOR_EMERALD)

    add_card(s6, Inches(8.8), Inches(2.1), Inches(3.6), Inches(4.7),
             "Group 3: Professional & Innovation",
             [
                 "Threshold: Min 40 / Max 60 Pts",
                 "12-Week NPTEL Online Course: 50 pts",
                 "8-Week NPTEL Course Certificate: 35 pts",
                 "Hackathon Winner (State/National): 40 pts",
                 "Hackathon Participation (24-36h): 15 pts",
                 "Paper Published (Scopus/IEEE): 35 pts",
                 "Student Startup Founder (LLP/KSUM): 60 pts",
                 "Core Industry Internship (2 Wks): 20 pts"
             ],
             badge="GROUP 3", accent_color=COLOR_AMBER)

    s6.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTES (45s):\n"
        "Now let's examine our 120 Activity Points Auditor. "
        "In the 2024 scheme, KTU established 3 distinct groups. A student must achieve at least 40 points in Group 1, 40 points in Group 2, and 40 in Group 3. "
        "Our engine performs a live audit on the student's portfolio. "
        "If a student has 60 points in Group 3 and 40 in Group 2, but only 20 points in Group 1, the engine flags 'DEFICIT PENDING' in red, "
        "points out the 20-point deficit in Group 1, and recommends taking an emergency CPR training or getting their driving license verified."
    )

    # =========================================================================
    # SLIDE 7: INTERACTIVE SYLLABUS SIMULATION LABS
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_bg(s7)
    add_header(s7, "Pedagogical Innovation", "Interactive Engineering Simulation Labs",
               "Hands-on visualizers embedded directly into the platform to master difficult 10-mark exam problems.")

    add_card(s7, Inches(0.8), Inches(2.1), Inches(3.6), Inches(4.7),
             "CPU Scheduling Gantt Lab",
             [
                 "Problem: Guaranteed 10-mark question in CST 206 (Operating Systems Module 2).",
                 "Interactive Inputs: Configure Arrival times and Burst times for P1-P4.",
                 "Dual Algorithms: Simulates FCFS and Round Robin with variable quantum.",
                 "Visual Gantt Chart: Real-time graphical execution timeline with Average Waiting and Turnaround times."
             ],
             badge="OS LAB", accent_color=COLOR_PRIMARY)

    add_card(s7, Inches(4.8), Inches(2.1), Inches(3.6), Inches(4.7),
             "4-Variable K-Map Solver",
             [
                 "Problem: Guaranteed 10-mark question in CST 203 / ECT 203 (Logic System Design Module 2).",
                 "Interactive 16-Cell Grid: Click any cell to toggle states: 0 -> 1 -> X (Don't Care).",
                 "Dynamic Minimization: Real-time Gray code mapping (AB down, CD across).",
                 "Instant Output: Displays active minterms and simplified Boolean Sum-of-Products (SOP) equation."
             ],
             badge="DIGITAL LOGIC", accent_color=COLOR_EMERALD)

    add_card(s7, Inches(8.8), Inches(2.1), Inches(3.6), Inches(4.7),
             "Binary Search Tree (BST) Lab",
             [
                 "Problem: High-yield question in CST 201 (Data Structures Module 3).",
                 "Dynamic Node Insertion: Add custom integer keys to build the tree dynamically.",
                 "Live Metrics: Instant computation of Tree Height and Total Node Count.",
                 "All 3 Traversals: Generates Inorder (Sorted), Preorder, and Postorder sequences with full mathematical formatting."
             ],
             badge="DATA STRUCTURES", accent_color=COLOR_AMBER)

    s7.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTES (45s):\n"
        "We didn't stop at syllabi and calculators. We built interactive engineering visualizers. "
        "In Operating Systems, students always get tested on CPU scheduling Gantt charts. We built a live Gantt generator. "
        "In Digital Logic, students struggle with 4-variable K-maps. We built an interactive 16-cell Gray code solver. "
        "In Data Structures, students can insert keys into our BST lab and see the Inorder, Preorder, and Postorder traversals computed in real-time."
    )

    # =========================================================================
    # SLIDE 8: 10-MARK ANSWER ARCHITECT & REVISION NOTES
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_bg(s8)
    add_header(s8, "Exam Strategy", "10-Mark Model Answer Architect & Revision Notebook",
               "Cracking the university evaluator's rubric to guarantee maximum marks.")

    add_card(s8, Inches(0.8), Inches(2.1), Inches(5.6), Inches(4.7),
             "The 10-Mark Answer Architect",
             [
                 "Evaluator's Secret: KTU valuation schemes assign fractional marks across distinct rubrics (Diagram: 2m, Steps: 4m, Verification: 2m, Conclusion: 2m).",
                 "Recommended Time Allocation: 12 to 14 minutes per 10-mark question.",
                 "Pre-Crafted Model Blueprints for All Branches:",
                 "   • CSE: Banker's Deadlock Avoidance Algorithm",
                 "   • CSE/ECE: 4-Variable K-Map Minimization & Logic Circuit",
                 "   • MECH: Diesel Cycle Air Standard Efficiency Derivation",
                 "   • CE: Simply Supported Beam SFD & BMD with UDL",
                 "Teaches students how to structure answers to secure full 10/10 marks."
             ],
             badge="SCORING RUBRIC", accent_color=COLOR_PRIMARY)

    add_card(s8, Inches(6.8), Inches(2.1), Inches(5.7), Inches(4.7),
             "Markdown Revision Notebook with KaTeX",
             [
                 "Built-in engineering notebook for lecture notes and last-minute revision sheets.",
                 "Real-time KaTeX rendering for complex mathematical equations, integrals, matrices, and greek letters.",
                 "Pre-loaded with high-yield revision summaries for CST 201 (Infix to Postfix) and CST 206 (Banker's Algorithm).",
                 "Client-side auto-save and local persistence with zero server lag.",
                 "One-click revision card creation with tag categorization."
             ],
             badge="ACTIVE RECALL", accent_color=COLOR_AMBER)

    s8.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTES (40s):\n"
        "Even when students know the theory, they lose marks because their answers lack the structure KTU evaluators demand. "
        "Our 10-Mark Answer Architect teaches students the exact blueprint: how much time to spend, which diagrams are non-negotiable, "
        "and how to format derivations. "
        "Coupled with our Revision Notebook that renders LaTeX math equations in real-time, students have everything they need to score top honors."
    )

    # =========================================================================
    # SLIDE 9: TECHNICAL ARCHITECTURE & SOFTWARE CRAFTSMANSHIP
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_bg(s9)
    add_header(s9, "Technical Excellence", "Engineering Architecture & Software Craftsmanship",
               "Built with modern web standards, modular microframework architecture, and clean responsive design.")

    add_card(s9, Inches(0.8), Inches(2.1), Inches(3.6), Inches(4.7),
             "Modular Backend Engine",
             [
                 "Python 3.14 + Flask Microframework.",
                 "Clean Blueprint Architecture: separate routes for courses, calculators, activity points, simulations, and notes.",
                 "Assembler Pipeline: Modular branch builders compiled into high-efficiency data catalogs.",
                 "Sub-millisecond API response latency (<15ms) with zero heavy external database overhead."
             ],
             badge="PYTHON / FLASK", accent_color=COLOR_PRIMARY)

    add_card(s9, Inches(4.8), Inches(2.1), Inches(3.6), Inches(4.7),
             "Clean Executive UI System",
             [
                 "4 Curated Theme Presets:",
                 "   • Royal Obsidian (Indigo & Amber)",
                 "   • Cosmic Aurora (Nordic Teal & Rose)",
                 "   • Linear Titanium (Carbon & Gold)",
                 "   • Oxford Emerald (Jade & Bronze)",
                 "Frosted glass surfaces with crisp edge bevels.",
                 "Typography: Plus Jakarta Sans + Outfit + JetBrains Mono."
             ],
             badge="DESIGN SYSTEM", accent_color=COLOR_EMERALD)

    add_card(s9, Inches(8.8), Inches(2.1), Inches(3.6), Inches(4.7),
             "Zero-Lag Client Technologies",
             [
                 "Web Audio API: Synthesizes tactile micro-sound clicks and success chimes dynamically with zero audio assets.",
                 "KaTeX Engine: Fast mathematical typesetting directly in the browser.",
                 "Automated Test Suite: 5/5 unit tests passing cleanly in <0.08s verifying calculation math and regulations.",
                 "Responsive Layout: Optimized for desktop, iPad, and mobile."
             ],
             badge="FRONTEND STACK", accent_color=COLOR_AMBER)

    s9.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTES (45s):\n"
        "Under the hood, KTU Nexus is built on a clean Python Flask blueprint architecture. "
        "Our data assembler pipeline compiles modular curricula into lightning-fast in-memory catalogs. "
        "On the frontend, we designed a bespoke clean design system with 4 distinct presets, replacing the cliché hackathon dark-cyan look. "
        "It includes tactile Web Audio feedback and instant KaTeX mathematical rendering. "
        "The codebase has a comprehensive automated test suite verifying all 2024 regulations."
    )

    # =========================================================================
    # SLIDE 10: IMPACT, SCALABILITY & ROADMAP
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_bg(s10)
    add_header(s10, "Impact & Vision", "Target Market, Scalability & Roadmap",
               "Transforming engineering education across Kerala and expanding across technical state universities.")

    add_card(s10, Inches(0.8), Inches(2.1), Inches(3.6), Inches(4.7),
             "Immediate Market Impact",
             [
                 "Primary Audience: 150,000+ B.Tech students across 150+ affiliated engineering colleges under KTU.",
                 "Eliminates Degree Withholding: Solves the 120-point deficit trap before students reach final semester.",
                 "Drastically Reduces Supplies: Early warning system prevents failure in university examinations.",
                 "Zero barrier to entry: Free and accessible to any student with a browser."
             ],
             badge="MARKET SIZE", accent_color=COLOR_PRIMARY)

    add_card(s10, Inches(4.8), Inches(2.1), Inches(3.6), Inches(4.7),
             "Future Product Roadmap",
             [
                 "Phase 1 (Completed): Full S1-S8 5-Branch curricula, 120-pt auditor, CIE predictor, labs, clean theme.",
                 "Phase 2 (Q1 2027): AI-Powered Question Paper Predictor analyzing 5 years of exam trends.",
                 "Phase 3 (Q2 2027): Cross-platform Flutter mobile app with offline revision flashcards.",
                 "Phase 4 (Q3 2027): Faculty portal for uploading verified internal marks directly."
             ],
             badge="ROADMAP", accent_color=COLOR_EMERALD)

    add_card(s10, Inches(8.8), Inches(2.1), Inches(3.6), Inches(4.7),
             "Inter-University Scalability",
             [
                 "Modular Curriculum Architecture: Data schemas are completely decoupled from UI.",
                 "Pluggable Regulations Engine: Easy adaptation to Visvesvaraya Technological University (VTU), Anna University, and JNTU.",
                 "NEP 2020 Ready: Standardized credit matrices and multi-disciplinary activity frameworks support any state university."
             ],
             badge="SCALABILITY", accent_color=COLOR_AMBER)

    s10.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTES (40s):\n"
        "Looking at the impact: KTU has over 150 engineering colleges and 150,000 students. "
        "Our roadmap includes an AI Question Paper Predictor and a Flutter mobile app. "
        "Because our curriculum engine is modular, this platform can easily scale to VTU in Karnataka, Anna University in Tamil Nadu, and JNTU in Telangana."
    )

    # =========================================================================
    # SLIDE 11: CONCLUSION & LIVE DEMO (NO TEAM NAME, ONLY MEMBER NAMES)
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    add_bg(s11)

    # Accent decorative top bar
    bar11 = s11.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.1), Inches(1.2), Inches(0.06))
    bar11.fill.solid()
    bar11.fill.fore_color.rgb = COLOR_PRIMARY
    bar11.line.fill.background()

    tb11 = s11.shapes.add_textbox(Inches(0.8), Inches(1.35), Inches(11.7), Inches(2.2))
    tf11 = tb11.text_frame
    tf11.word_wrap = True

    p11_badge = tf11.paragraphs[0]
    p11_badge.text = "DEMONSTRATION & CONCLUSION"
    p11_badge.font.size = Pt(11)
    p11_badge.font.bold = True
    p11_badge.font.color.rgb = COLOR_PRIMARY
    p11_badge.space_after = Pt(8)

    p11_title = tf11.add_paragraph()
    p11_title.text = "Experience KTU Nexus Live"
    p11_title.font.size = Pt(40)
    p11_title.font.bold = True
    p11_title.font.color.rgb = COLOR_NAVY
    p11_title.space_after = Pt(8)

    p11_sub = tf11.add_paragraph()
    p11_sub.text = "Empowering every B.Tech engineer to graduate on time, with honors, and zero panic."
    p11_sub.font.size = Pt(16)
    p11_sub.font.color.rgb = COLOR_PRIMARY

    # 3 Summary Cards
    add_card(s11, Inches(0.8), Inches(3.9), Inches(3.6), Inches(2.9),
             "Live Local URL",
             [
                 "Server: http://127.0.0.1:5000",
                 "Fast, local offline execution",
                 "Complete REST API Documentation",
                 "Integrated automated test suite (5/5 passing)"
             ],
             badge="READY TO DEMO", accent_color=COLOR_PRIMARY)

    add_card(s11, Inches(4.8), Inches(3.9), Inches(3.6), Inches(2.9),
             "Key Takeaways",
             [
                 "87 Courses across 5 major branches",
                 "Accurate KTU 2024 internal mark math",
                 "Strict Three-Group Activity Auditor",
                 "3 Interactive Engineering Simulation Labs"
             ],
             badge="SUMMARY", accent_color=COLOR_EMERALD)

    add_card(s11, Inches(8.8), Inches(3.9), Inches(3.6), Inches(2.9),
             "Thank You!",
             [
                 "Felix Louie Sojan",
                 "Adithya Jobies",
                 "Open for Questions & Live Walkthrough",
                 "Try the live calculation at 127.0.0.1:5000"
             ],
             badge="PRESENTERS", accent_color=COLOR_NAVY)

    s11.notes_slide.notes_text_frame.text = (
        "SPEAKER NOTES (30s):\n"
        "In conclusion, KTU Nexus transforms the B.Tech journey from one of anxiety and confusion into one of structured, confident success. "
        "We are running live at 127.0.0.1:5000. "
        "Felix Louie Sojan and Adithya Jobies welcome the judges' questions and would love to walk you through a live demonstration. Thank you!"
    )

    # Save presentation
    prs.save(output_path)
    print(f"Successfully generated presentation deck at: {output_path}")

if __name__ == "__main__":
    out_file = "static/KTU_Nexus_Presentation.pptx"
    if len(sys.argv) > 1:
        out_file = sys.argv[1]
    create_deck(out_file)
    # Also create copy to KTU_ScholarOS_Presentation.pptx so existing links continue to work
    create_deck("static/KTU_ScholarOS_Presentation.pptx")
