"""
CSE Courses Builder (S3 to S8) for KTU 2024 Scheme
"""

def get_cse_courses():
    courses = []

    def make_c(cid, code, title, credits, sem, cat, mods):
        return {
            "id": cid,
            "code": code,
            "title": title,
            "credits": credits,
            "semester": sem,
            "branch": "Computer Science & Engineering",
            "branch_id": "cse",
            "category": cat,
            "modules": mods
        }

    # S3
    courses.append(make_c(
        "mat203-dms", "MAT 203", "Discrete Mathematical Structures", 4, "Semester 3", "BSC",
        [
            {"module_no": 1, "title": "Mathematical Logic & Proofs", "syllabus": "Propositional logic, Truth tables, Tautologies, Logical equivalences, Predicates and quantifiers, Rules of inference, Methods of proof (Direct, Contradiction, Induction).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Show that ((p -> q) ^ (q -> r)) -> (p -> r) is a tautology using truth tables and rules of inference.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Sets, Relations & Functions", "syllabus": "Set operations, Relations: Reflexive, Symmetric, Transitive, Equivalence relations, Partitions, Partial orderings, Hasse diagrams, Functions: Injective, Surjective, Bijective, Pigeonhole principle.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Draw Hasse diagram of divisibility on D36 = {1, 2, 3, 4, 6, 9, 12, 18, 36} and find maximal, minimal, greatest, and least elements.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Lattices & Boolean Algebra", "syllabus": "Lattices as posets, Properties of lattices, Sublattices, Distributive and Complemented lattices, Modular lattices, Boolean algebra: Laws, Duality principle, Boolean functions representation.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Prove that every distributive lattice is modular. Is the converse true? Justify with counterexample.", "marks": 10, "frequency": "Repeated 7 times"}]},
            {"module_no": 4, "title": "Group Theory & Algebraic Structures", "syllabus": "Semigroups, Monoids, Groups: Abelian groups, Subgroups, Cyclic groups, Cosets, Lagrange's theorem, Group homomorphisms, Rings and Fields.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "State and prove Lagrange's theorem for finite groups. Explain why order of any subgroup divides order of the group.", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}]},
            {"module_no": 5, "title": "Recurrence Relations & Generating Functions", "syllabus": "Solving linear recurrence relations with constant coefficients (Homogeneous and non-homogeneous), Generating functions, Inclusion-exclusion principle.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Solve recurrence relation a_n - 7a_{n-1} + 12a_{n-2} = 0 with a_0 = 2, a_1 = 5.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    courses.append(make_c(
        "cst201-ds", "CST 201", "Data Structures", 4, "Semester 3", "PCC",
        [
            {"module_no": 1, "title": "Basic Concepts & Stacks", "syllabus": "Complexity, Asymptotic Notations. Stacks: Infix to Postfix conversion, Postfix evaluation.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Convert infix expression ((A + B) * C - (D - E)) ^ (F + G) to postfix showing stack trace.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Queues & Linked Lists", "syllabus": "Circular Queue, Deque, Priority Queue. Singly & Doubly Linked Lists, Polynomial Addition.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Circular Queue operations with C code and array wrapping.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Binary Trees & BST", "syllabus": "Tree terminology, Binary Trees: Traversals. Binary Search Trees (BST): Insertion, Deletion, Search.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Construct a Binary Tree given Inorder and Preorder traversals.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Graphs & Spanning Trees", "syllabus": "Representations, BFS & DFS, Prim's and Kruskal's MST algorithms, AVL Tree rotations.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Trace Kruskal's algorithm on a weighted connected graph.", "marks": 10, "frequency": "Repeated 7 times"}]},
            {"module_no": 5, "title": "Sorting & Hashing", "syllabus": "Quick Sort, Merge Sort, Heap Sort. Hash Tables, Collision Resolution techniques.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Quick Sort partition algorithm with Best/Worst case complexity.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    courses.append(make_c(
        "cst203-lsd", "CST 203", "Logic System Design", 4, "Semester 3", "PCC",
        [
            {"module_no": 1, "title": "Number Systems & Codes", "syllabus": "Binary, Octal, Hexadecimal, 1's and 2's complement arithmetic, BCD, Gray code, Error detecting codes (Parity, Hamming).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain 7-bit Hamming code error detection and correction with an example.", "marks": 10, "frequency": "Repeated 7 times"}]},
            {"module_no": 2, "title": "Boolean Algebra & K-Map Minimization", "syllabus": "Canonical SOP/POS forms, 4-variable Karnaugh Maps, Don't care conditions, Quine-McCluskey tabular reduction.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Simplify F(A, B, C, D) = Sigma m(0, 2, 5, 7, 8, 10, 13, 15) using 4-variable K-Map and draw logic circuit.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Combinational Logic Circuits", "syllabus": "Full Adder, Parallel Adder, Look-ahead carry adder, Decoders, Multiplexers, De-multiplexers, Code Converters.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Implement 16:1 MUX using 4:1 multiplexers only.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Sequential Circuits & Flip-Flops", "syllabus": "Latches, SR, JK, Master-Slave JK, D, and T Flip-Flops, Race-around condition, Excitation tables.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain race-around condition in JK flip-flop and how Master-Slave configuration solves it.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 5, "title": "Counters, Registers & PLDs", "syllabus": "Synchronous and Asynchronous Counters, Modulo-N Counters, Shift Registers, PROM, PLA, PAL.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Design a Mod-6 synchronous counter using JK flip-flops with state table and excitation diagrams.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    courses.append(make_c(
        "cst205-oops-java", "CST 205", "Object Oriented Programming using Java", 4, "Semester 3", "PCC",
        [
            {"module_no": 1, "title": "Introduction to Java & OOP", "syllabus": "OOP paradigms, JVM architecture, Bytecode, Primitive data types, Operators, Control statements, Classes, Objects, Constructors, Garbage collection, this keyword.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain JVM architecture with Classloader, Bytecode Verifier, and Execution Engine. Write a Java program demonstrating constructor overloading.", "marks": 10, "frequency": "Repeated 7 times"}]},
            {"module_no": 2, "title": "Inheritance & Polymorphism", "syllabus": "Inheritance types (Single, Multilevel, Hierarchical), super keyword, Method overriding, Dynamic method dispatch, Abstract classes, Interfaces, Multiple inheritance in Java.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain dynamic method dispatch (runtime polymorphism) in Java with an illustrative program.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 3, "title": "Packages & Exception Handling", "syllabus": "Creating and importing packages, Access protection, Exception hierarchy, Checked vs unchecked exceptions, try-catch-finally blocks, throw, throws, User-defined exceptions.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Write a Java program to define and throw a custom InvalidAgeException when age is less than 18.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Multithreading & Generics", "syllabus": "Thread lifecycle, Creating threads (Thread class and Runnable interface), Thread priorities, Synchronization, Inter-thread communication (wait, notify, notifyAll), Generics.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Solve the classic Producer-Consumer problem in Java using synchronized methods and wait/notify mechanism.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 5, "title": "Java Collections & GUI (Swing)", "syllabus": "Collections framework: ArrayList, LinkedList, HashSet, HashMap, Iterators, Swing fundamentals: JFrame, JPanel, JButton, JTextField, Event handling: ActionListener.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Write a Java Swing GUI application with two buttons and a text field that increments and decrements a counter on button clicks.", "marks": 10, "frequency": "Repeated 7 times"}]}
        ]
    ))

    # S4
    courses.append(make_c(
        "cst202-coa", "CST 202", "Computer Organization & Architecture", 4, "Semester 4", "PCC",
        [
            {"module_no": 1, "title": "Basic Structure & Addressing Modes", "syllabus": "Von Neumann model, Memory addressing, Addressing modes (Immediate, Direct, Indirect, Indexed), RISC vs CISC.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain various addressing modes with effective address formulas and code examples.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Arithmetic Operations & Booth's Algorithm", "syllabus": "Fast adders, Booth's signed multiplication algorithm, Restoring and Non-restoring division.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Multiply (-5) and (+7) using Booth's Algorithm in 5-bit binary.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Control Unit Design", "syllabus": "Single bus CPU, Instruction execution sequence, Hardwired vs Microprogrammed control units.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Write complete control sequence for instruction ADD (R1), R2 on single-bus CPU.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Memory Hierarchy & Cache Mapping", "syllabus": "Cache mapping (Direct, Associative, Set-Associative), Replacement policies, Virtual memory.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Direct and 4-way Set Associative cache mapping with tag, set, offset calculations.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 5, "title": "Pipelining & DMA", "syllabus": "Pipeline hazards (Structural, Data, Control), Direct Memory Access (DMA) controller.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain pipeline hazards and how forwarding and branch prediction mitigate stalls.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    courses.append(make_c(
        "cst204-dbms", "CST 204", "Database Management Systems", 4, "Semester 4", "PCC",
        [
            {"module_no": 1, "title": "Database Architecture & ER Modeling", "syllabus": "Three-schema architecture, Data independence, ER modeling, Strong and Weak entities, Extended ER features.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Draw an ER diagram for a University Management System specifying cardinalities and primary keys.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Relational Model & Relational Algebra", "syllabus": "Relational constraints, Select, Project, Join operations, Tuple Relational Calculus, Domain Relational Calculus.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Natural Join, Theta Join, and Outer Joins with relational algebra syntax and tables.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 3, "title": "SQL & Normalization", "syllabus": "Complex SQL queries, Aggregation, Views, Triggers, Functional Dependencies, 1NF, 2NF, 3NF, BCNF.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Normalize relation R(A, B, C, D, E) with F = {A->BC, CD->E, B->D, E->A} to 3NF and BCNF.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 4, "title": "Transaction Processing & Concurrency", "syllabus": "ACID properties, Serializability, Conflict serializability, Two-Phase Locking (2PL), Deadlock handling.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Test whether the schedule S: r1(x), r2(y), w1(x), r2(x), w2(y) is conflict serializable using precedence graph.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "Storage & Indexing", "syllabus": "File organization, RAID levels, Primary/Clustering/Secondary indexes, B-Trees and B+ Trees.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain B+ Tree structure and trace insertion of keys into an empty B+ Tree of order 4.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    courses.append(make_c(
        "cst206-os", "CST 206", "Operating Systems", 4, "Semester 4", "PCC",
        [
            {"module_no": 1, "title": "OS Overview & System Calls", "syllabus": "Dual-mode operation, System calls (fork, exec, wait), OS structures (Monolithic, Microkernel).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain the step-by-step mechanism of system call execution and context switching.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Process Management & Scheduling", "syllabus": "PCB, Process states, CPU Scheduling algorithms: FCFS, SJF, Priority, Round Robin.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Given 5 processes with arrival and burst times, draw Gantt chart and calculate average turnaround and waiting time for Round Robin (q=3).", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Synchronization & Deadlocks", "syllabus": "Critical Section problem, Peterson's algorithm, Semaphores, Classic synchronization problems (Dining Philosophers, Producer-Consumer), Banker's Algorithm.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Apply Banker's Algorithm to determine if the system is in a safe state and handle resource request vector.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 4, "title": "Memory Management & Virtual Memory", "syllabus": "Paging, Segmentation, TLB, Page replacement algorithms (FIFO, LRU, Optimal), Thrashing.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Calculate number of page faults for reference string 7,0,1,2,0,3,0,4,2,3,0,3,2 with 3 frames using LRU and FIFO.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 5, "title": "File Systems & Disk Scheduling", "syllabus": "File allocation methods (Contiguous, Linked, Indexed), Disk scheduling (FCFS, SSTF, SCAN, C-SCAN).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Evaluate total head movements for disk queue requests using SSTF, SCAN, and C-SCAN.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    courses.append(make_c(
        "mat206-graph-num", "MAT 206", "Graph Theory & Number Theory", 4, "Semester 4", "BSC",
        [
            {"module_no": 1, "title": "Introduction to Graphs", "syllabus": "Graphs, Subgraphs, Walks, Paths, Cycles, Connected components, Euler graphs, Hamiltonian paths, Konigsberg bridge problem.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "State and prove Euler's theorem for existence of Eulerian circuit in a connected graph.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Trees & Connectivity", "syllabus": "Trees: Characterizations of trees, Spanning trees, Fundamental cutsets and circuits, Cayley's tree formula, Connectivity: Vertex and edge connectivity.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Prove that every tree with n vertices has exactly n - 1 edges.", "marks": 7, "frequency": "Repeated 7 times"}]},
            {"module_no": 3, "title": "Planarity & Graph Coloring", "syllabus": "Planar graphs, Euler's formula for planar graphs (v - e + f = 2), Kuratowski's theorem, Dual graphs, Vertex coloring, Chromatic number, Four color theorem.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "State and prove Euler's formula for connected planar graphs. Hence show that K5 and K3,3 are non-planar.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 4, "title": "Divisibility & Modular Congruence", "syllabus": "Divisibility, Division algorithm, Euclidean algorithm, Linear Diophantine equations, Prime numbers, Congruences, Chinese Remainder Theorem.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Solve system of linear congruences using Chinese Remainder Theorem: x = 2 (mod 3), x = 3 (mod 5), x = 2 (mod 7).", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}]},
            {"module_no": 5, "title": "Number Theoretic Functions & Cryptography", "syllabus": "Euler's totient function, Fermat's Little Theorem, Wilson's theorem, Primitive roots, Cryptographic foundations: Diffie-Hellman and RSA algorithm.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "In RSA cryptosystem with p = 7, q = 11, e = 13, encrypt message M = 9 and find decryption key d.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    # S5
    courses.append(make_c(
        "cst301-flat", "CST 301", "Formal Languages & Automata Theory", 4, "Semester 5", "PCC",
        [
            {"module_no": 1, "title": "Finite Automata & Regular Expressions", "syllabus": "DFA, NFA, Equivalence of DFA and NFA, NFA to DFA conversion, Regular Expressions, Arden's theorem.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Convert given NFA with epsilon transitions into an equivalent DFA.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 2, "title": "Regular Languages & Pumping Lemma", "syllabus": "Pumping Lemma for regular languages, Closure properties of regular languages, DFA state minimization (Table filling).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Prove that L = {0^n 1^n | n >= 1} is not regular using Pumping Lemma.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 3, "title": "Context-Free Grammars & Normal Forms", "syllabus": "CFG, Derivation trees, Ambiguity, Chomsky Normal Form (CNF), Greibach Normal Form (GNF).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Convert CFG into Chomsky Normal Form (CNF) after eliminating null and unit productions.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Pushdown Automata (PDA)", "syllabus": "Deterministic and Non-deterministic PDA, Equivalence of PDA and CFG, Pumping Lemma for CFLs.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Design PDA accepting language L = {w c w^R | w in {a, b}*} by empty stack.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "Turing Machines & Decidability", "syllabus": "Turing Machine model, Design of TM for arithmetic and languages, Halting problem, Undecidability, Post Correspondence Problem (PCP).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Design Turing Machine to compute 2's complement of a binary string.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    courses.append(make_c(
        "cst303-cn", "CST 303", "Computer Networks", 4, "Semester 5", "PCC",
        [
            {"module_no": 1, "title": "Network Architecture & Physical Layer", "syllabus": "OSI 7-layer reference model, TCP/IP protocol suite, Guided and unguided transmission media, Circuit switching vs Packet switching, Transmission impairments.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Compare OSI and TCP/IP reference models with neat architectural diagrams and function of each layer.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Data Link Layer & Medium Access Control", "syllabus": "Framing, Error detection (CRC, Checksum), Sliding Window protocols (Go-Back-N, Selective Repeat), Random access protocols: ALOHA, CSMA/CD, Ethernet IEEE 802.3.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Cyclic Redundancy Check (CRC) error detection with generator polynomial x^4 + x + 1 and data word 1101011011.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Network Layer & IP Addressing", "syllabus": "IPv4 addressing, Subnetting, VLSM, CIDR, IPv6 architecture, Routing algorithms: Distance Vector Routing (Bellman-Ford), Link State Routing (Dijkstra's algorithm), Count-to-infinity problem.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Apply Dijkstra's algorithm to compute shortest path tree from source node A in a 6-node network.", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}]},
            {"module_no": 4, "title": "Transport Layer Protocols", "syllabus": "Process-to-process delivery, UDP header, TCP segments, TCP 3-way handshake connection establishment, Flow control (Sliding window), Congestion control: AIMD, Slow start, Fast retransmit.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain TCP congestion control mechanism with Slow Start, Congestion Avoidance, Fast Retransmit, and Fast Recovery phases.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 5, "title": "Application Layer & Network Services", "syllabus": "Domain Name System (DNS), HTTP/1.1 vs HTTP/2, Electronic Mail (SMTP, POP3, IMAP), Dynamic Host Configuration Protocol (DHCP), Network Address Translation (NAT).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain DNS message resolution process (Iterative vs Recursive queries) with step-by-step diagram.", "marks": 10, "frequency": "Repeated 7 times"}]}
        ]
    ))

    courses.append(make_c(
        "cst305-ss", "CST 305", "System Software", 4, "Semester 5", "PCC",
        [
            {"module_no": 1, "title": "Introduction to System Software & SIC Architecture", "syllabus": "System software vs application software, Simplified Instructional Computer (SIC) architecture: Registers, Memory, Instruction formats, Addressing modes, SIC/XE architecture.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Differentiate between SIC and SIC/XE machine architectures in terms of registers, addressing modes, and instruction formats.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Assemblers", "syllabus": "Two-pass assembler design, Symbol table (SYMTAB), Opcode table (OPTAB), Location counter (LOCCTR), Pass 1 and Pass 2 algorithms, Object program generation (Header, Text, End records).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain data structures and algorithms of Pass 1 and Pass 2 of a two-pass assembler with flowchart.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Loaders & Linkers", "syllabus": "Basic loader functions, Absolute loaders, Relocating loaders (Bit mask, Modification record), Direct linking loaders, Dynamic linking, Comparison of linkage editor and linking loader.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain the design and algorithm of an absolute loader with object program record structure.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Macro Processors", "syllabus": "Macro definition and call, Macro expansion, One-pass macro processor design: NAMTAB, DEFTAB, ARGTAB, Conditional macro expansion, Keyword parameters, Concatenation of macro parameters.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain data structures and algorithm of a one-pass macro processor handling definition and invocation.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "Compilers & Debuggers", "syllabus": "Overview of compiler phases, Lexical analysis, Syntax analysis, Code generation, Text editors: Structure and user interface, Interactive debugging systems: Breakpoints, Trace facilities.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain six phases of a compiler with input, output, and error handling for assignment statement: position = initial + rate * 60.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    courses.append(make_c(
        "cst307-micro", "CST 307", "Microprocessors & Microcontrollers", 4, "Semester 5", "PCC",
        [
            {"module_no": 1, "title": "8086 Internal Architecture", "syllabus": "8086 internal architecture, BIU and EU, Register organization, Memory segmentation, Pin definitions, Maximum and Minimum modes of operation.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain 8086 architecture with BIU, EU, register sets, and physical address calculation.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 2, "title": "8086 Instruction Set & Assembly", "syllabus": "Addressing modes, Data transfer, Arithmetic, Logical, Shift, Rotate, String manipulation instructions, Assembly language programming.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Write an 8086 assembly program to sort an array of N 16-bit numbers in ascending order using Bubble Sort.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 3, "title": "Interrupts & Peripheral Interfacing", "syllabus": "8086 interrupt structure, Interrupt Vector Table (IVT), Programmable Peripheral Interface 8255, Programmable Interrupt Controller 8259.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain internal architecture of 8255 PPI and its modes of operation (Mode 0, Mode 1, Mode 2).", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "8051 Microcontroller Architecture", "syllabus": "8051 architecture, Memory organization, Special Function Registers (SFRs), I/O ports, Timers and counters, Serial communication.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain 8051 memory organization (internal RAM, SFRs, external memory) with neat memory map.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "8051 Interfacing & Embedded Applications", "syllabus": "Interfacing LCD displays, Stepper motors, Matrix keypads, ADC 0808, DAC 0800 with 8051 using embedded C programs.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Draw interfacing diagram of stepper motor with 8051 and write embedded C program for clockwise rotation.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    # S6
    courses.append(make_c(
        "cst304-cgip", "CST 304", "Computer Graphics & Image Processing", 4, "Semester 6", "PCC",
        [
            {"module_no": 1, "title": "2D Graphics & Rasterization", "syllabus": "DDA line drawing, Bresenham's line and circle drawing algorithms, Midpoint circle algorithm, Scanline polygon filling.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive Bresenham's Line Drawing algorithm for lines with slope |m| < 1 with decision parameter derivation.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 2, "title": "2D/3D Transformations & Clipping", "syllabus": "2D transformations: Translation, Rotation, Scaling, Reflection, Shear, Cohen-Sutherland line clipping, Sutherland-Hodgman polygon clipping, 3D viewing.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Cohen-Sutherland Line Clipping algorithm with 4-bit region codes and step-by-step intersection calculations.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Digital Image Fundamentals", "syllabus": "Sampling and quantization, Spatial resolution, Gray level transformation functions, Histogram equalization, Image smoothing and sharpening filters.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Perform histogram equalization on a given 3-bit 8x8 image with gray level distribution table.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 4, "title": "Image Segmentation & Edge Detection", "syllabus": "Point, line, and edge detection, Gradient operators: Sobel, Prewitt, Laplacian, Canny edge detector, Thresholding: Global and Otsu's method.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Canny Edge Detection algorithm steps: Gaussian smoothing, Gradient calculation, Non-maximum suppression, Hysteresis thresholding.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "Morphological Image Processing", "syllabus": "Dilation, Erosion, Opening, Closing, Hit-or-Miss transform, Boundary extraction, Morphological skeleton, Image compression overview.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain morphological Dilation and Erosion operations with structuring elements and mathematical definitions.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    courses.append(make_c(
        "cst302-cd", "CST 302", "Compiler Design", 4, "Semester 6", "PCC",
        [
            {"module_no": 1, "title": "Lexical Analysis", "syllabus": "Structure of compiler, Lexical analyzer generator LEX, Regular expressions to DFA, Transition diagrams, Input buffering, Sentinels.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain transition from regular expressions to minimized DFA with subset construction and state reduction.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Syntax Analysis & Top-Down Parsing", "syllabus": "Context-free grammars, Ambiguity, Left recursion elimination, Left factoring, LL(1) grammars, First and Follow sets, Recursive descent parser.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Construct LL(1) parsing table for given arithmetic grammar after eliminating left recursion and left factoring.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Bottom-Up Parsing", "syllabus": "LR parsing engine, Shift-Reduce conflicts, SLR(1), Canonical LR(1), LALR(1) parsing tables, YACC parser generator tool.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Construct SLR(1) parsing table for grammar S -> CC, C -> cC | d.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 4, "title": "Syntax-Directed Translation & Intermediate Code", "syllabus": "Syntax-Directed Definitions (SDD), Inherited and Synthesized attributes, Three-address code, Quadruples, Triples, Type checking.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Generate three-address code, quadruples, and triples for expression x = (a + b) * -(c / d).", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "Code Optimization & Generation", "syllabus": "Basic blocks and Flow graphs, DAG representation of basic blocks, Loop optimization, Peephole optimization, Machine code generation.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Construct DAG for basic block and perform local optimizations (common subexpression elimination, dead code elimination).", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    courses.append(make_c(
        "cst306-daa", "CST 306", "Algorithm Analysis & Design", 4, "Semester 6", "PCC",
        [
            {"module_no": 1, "title": "Divide and Conquer & Recurrences", "syllabus": "Recurrence relations: Master theorem, Substitution method, Recursion tree, Merge sort, Quick sort, Strassen's matrix multiplication.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Solve recurrence T(n) = 3T(n/2) + n^2 using Master Theorem and verify with recursion tree.", "marks": 7, "frequency": "Repeated 7 times"}]},
            {"module_no": 2, "title": "Greedy Method", "syllabus": "Greedy strategy, Fractional knapsack problem, Job sequencing with deadlines, Huffman coding algorithm, Minimum Spanning Trees (Prim and Kruskal).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Construct optimal Huffman prefix code tree for characters {a, b, c, d, e, f} with given frequencies.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 3, "title": "Dynamic Programming", "syllabus": "Principle of optimality, 0/1 Knapsack, Bellman-Ford shortest paths, Floyd-Warshall all-pairs shortest paths, Longest Common Subsequence (LCS), Matrix chain multiplication.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Find optimal parenthesization of 4 matrices with dimensions <10, 100, 5, 50, 1> using Matrix Chain Multiplication.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 4, "title": "Backtracking & Branch and Bound", "syllabus": "State space tree, N-Queens problem, Subset sum problem, Graph coloring, Traveling Salesperson Problem (TSP) using Branch and Bound (Least cost).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Solve 4-Queens problem using backtracking showing state space search tree with bounding functions.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "Complexity Classes & NP-Completeness", "syllabus": "Deterministic vs non-deterministic algorithms, P, NP, NP-Hard, NP-Complete, Cook's theorem, Reductions: 3-SAT to Vertex Cover, Approximation algorithms for Vertex Cover.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Prove that Circuit-SAT is NP-complete. Differentiate between NP-Hard and NP-Complete classes.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    # S7
    courses.append(make_c(
        "cst401-ai", "CST 401", "Artificial Intelligence", 4, "Semester 7", "PCC",
        [
            {"module_no": 1, "title": "Search Strategies & Problem Solving", "syllabus": "Uninformed search (BFS, DFS, IDDFS), Heuristic search (Greedy Best-First, A* Search), Admissibility and Monotonicity of heuristics.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain A* search algorithm and prove that A* is admissible when heuristic h(n) never overestimates true cost.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 2, "title": "Adversarial Search & Games", "syllabus": "Game theory, Minimax algorithm, Alpha-Beta pruning, Constraint Satisfaction Problems (CSP), Forward checking, Backtracking search.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Trace Minimax algorithm with Alpha-Beta pruning on a 4-ply game tree to identify pruned branches.", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Knowledge Representation & Logic", "syllabus": "Propositional logic, First-Order Logic (FOL), Unification algorithm, Resolution refutation, Horn clauses, Forward and backward chaining.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Convert FOL sentences to Clause Form (CNF) and prove query using Resolution Refutation.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Probabilistic Reasoning & Bayesian Networks", "syllabus": "Uncertainty, Prior and conditional probability, Bayes' Rule, Bayesian Belief Networks (BBN), Conditional independence, Markov decision process overview.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Construct a Bayesian Belief Network for medical diagnosis and calculate joint probability distributions.", "marks": 10, "frequency": "Repeated 7 times"}]},
            {"module_no": 5, "title": "Machine Learning Foundations in AI", "syllabus": "Supervised learning, Decision Trees (ID3 algorithm, Information Gain, Entropy), K-Nearest Neighbors, Reinforcement learning: Q-Learning concepts.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Construct a Decision Tree using ID3 algorithm calculating Entropy and Information Gain for play-tennis dataset.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    courses.append(make_c(
        "cst403-cns", "CST 403", "Cryptography & Cyber Security", 4, "Semester 7", "PCC",
        [
            {"module_no": 1, "title": "Symmetric Ciphers & Block Encryption", "syllabus": "Classical ciphers, DES algorithm architecture, Triple DES, AES encryption rounds, Modes of operation (ECB, CBC, CFB, OFB, CTR).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain AES encryption algorithm with SubBytes, ShiftRows, MixColumns, and AddRoundKey transformations.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Public Key Cryptography & Key Management", "syllabus": "Principles of public key cryptosystems, RSA algorithm, Diffie-Hellman key exchange, Elliptic Curve Cryptography (ECC), Digital certificates (X.509).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Diffie-Hellman Key Exchange algorithm and show how Man-in-the-Middle attack compromises it.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 3, "title": "Cryptographic Hash Functions & Signatures", "syllabus": "Message authentication requirements, HMAC, SHA-256 and SHA-512 algorithms, Digital Signature Standard (DSS/DSA), Kerberos authentication.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain SHA-512 architecture and compression function processing 1024-bit message blocks.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Network & Transport Layer Security", "syllabus": "IPSec (AH and ESP, Transport and Tunnel modes), SSL/TLS handshake protocol, HTTPS, Wireless network security (WPA2, WPA3).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain TLS Handshake Protocol step-by-step for establishing an encrypted web browsing session.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "System Security & Defenses", "syllabus": "Intrusion Detection Systems (Host and Network IDS), Firewalls: Packet filtering, Stateful inspection, Application proxies, Honeypots, Indian IT Act 2000.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Differentiate between Packet Filtering Firewalls and Stateful Inspection Firewalls with traffic examples.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    # S8
    courses.append(make_c(
        "cst402-dist-cloud", "CST 402", "Distributed Computing & Cloud Architecture", 4, "Semester 8", "PCC",
        [
            {"module_no": 1, "title": "Distributed Systems Models & Clocks", "syllabus": "Architectural models, Lamport logical clocks, Vector clocks, Chandy-Lamport distributed snapshot algorithm, Termination detection.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Lamport logical clock synchronization algorithm and total ordering of events with timing diagrams.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Mutual Exclusion & Consensus", "syllabus": "Distributed mutual exclusion: Ricart-Agrawala algorithm, Maekawa's algorithm, Consensus protocols: Paxos algorithm, Byzantine Generals problem.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Ricart-Agrawala algorithm for distributed mutual exclusion with message exchanges and proofs of correctness.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 3, "title": "Cloud Computing Infrastructure", "syllabus": "NIST cloud reference model, SPI service model (SaaS, PaaS, IaaS), Hypervisor technologies: Type 1 bare-metal vs Type 2 hosted, Containerization vs VM.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Compare hardware virtualization (hypervisors) and container-based virtualization (Docker) in terms of overhead and scalability.", "marks": 10, "frequency": "Repeated 7 times"}]},
            {"module_no": 4, "title": "Distributed File Systems & Big Data", "syllabus": "Google File System (GFS) architecture, Hadoop Distributed File System (HDFS), MapReduce programming model, CAP theorem in distributed data stores.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain HDFS architecture with NameNode, DataNodes, Secondary NameNode, and block replication strategy.", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}]},
            {"module_no": 5, "title": "Kubernetes & Cloud Native Deployments", "syllabus": "Kubernetes architecture: Control Plane, Kubelet, Pods, Services, Deployments, ReplicaSets, Horizontal Pod Autoscaling (HPA), Microservices architecture.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Kubernetes control plane components (API Server, etcd, Controller Manager, Scheduler) and Pod lifecycle.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    return courses
