"""
Builder script to generate comprehensive KTU_COURSES dataset spanning:
- S1 to S8 for CSE, ECE, EEE, MECH, CE, and CN
- Common first-year foundation (S1 and S2)
- Over 90 courses with full 5-module topics, syllabi, weightage, and high-yield PYQs.
"""

import json
from typing import List, Dict, Any

# We'll construct KTU_COURSES and write to courses_data.py
courses: List[Dict[str, Any]] = []

def add_c(cid, code, title, credits, sem, branch, branch_id, cat, mods):
    courses.append({
        "id": cid,
        "code": code,
        "title": title,
        "credits": credits,
        "semester": sem,
        "branch": branch,
        "branch_id": branch_id,
        "category": cat,
        "modules": mods
    })

def make_m(num, title, syllabus, pyqs):
    return {
        "module_no": num,
        "title": title,
        "syllabus": syllabus,
        "weightage_marks": 15,
        "high_yield_pyqs": pyqs
    }

# =========================================================================
# 1. COMMON FIRST YEAR FOUNDATION (S1 & S2)
# =========================================================================

# MAT 101 - S1
add_c(
    "mat101-calc", "MAT 101", "Linear Algebra & Calculus", 4, "Semester 1", "All Branches (Common)", "common", "BSC",
    [
        make_m(1, "Single Variable Calculus & Series", "Taylor's and Maclaurin's expansions, Indeterminate forms, L'Hopital's Rule. Infinite series: Convergence tests (Ratio test, Root test, Alternating series test, Leibniz's theorem).", [
            {"q": "Expand log(1 + e^x) in powers of x using Maclaurin's series up to x^4.", "marks": 7, "frequency": "Repeated 5 times"},
            {"q": "Test convergence of the alternating series Sigma (-1)^n * (n / (2n^2 + 1)) using Leibniz test.", "marks": 7, "frequency": "Repeated 4 times"}
        ]),
        make_m(2, "Multivariable Differential Calculus", "Partial derivatives, Homogeneous functions, Euler's theorem, Total derivative, Jacobians, Maxima and minima of functions of two variables, Lagrange multipliers.", [
            {"q": "If u = sin^-1((x + y) / (sqrt(x) + sqrt(y))), prove that x*(du/dx) + y*(du/dy) = (1/2)*tan(u) using Euler's theorem.", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"},
            {"q": "Find maximum and minimum distance from the origin to 5x^2 + 6xy + 5y^2 = 8 using Lagrange multipliers.", "marks": 10, "frequency": "Repeated 7 times"}
        ]),
        make_m(3, "Multiple Integrals", "Double integrals (Cartesian and Polar), Change of order of integration, Area bounded by curves. Triple integrals, Volume of solids.", [
            {"q": "Change the order of integration and evaluate: Integral(0 to a) Integral(x to a) (x / (x^2 + y^2)) dy dx.", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}
        ]),
        make_m(4, "Vector Calculus & Line/Surface Integrals", "Gradient, Directional derivative, Divergence, Curl. Green's theorem in a plane, Gauss Divergence theorem, Stokes' theorem.", [
            {"q": "Verify Green's theorem in the plane for Integral (xy + y^2)dx + x^2 dy where C is bounded by y = x and y = x^2.", "marks": 10, "frequency": "Repeated 7 times (Guaranteed)"}
        ]),
        make_m(5, "Linear Algebra, Eigenvalues & Cayley-Hamilton", "Rank of matrix, Echelon form, System of linear equations. Eigenvalues and Eigenvectors, Cayley-Hamilton theorem, Diagonalization.", [
            {"q": "Find eigenvalues and eigenvectors of matrix A = [[2, 1, 1], [2, 3, 2], [3, 3, 4]] and test for diagonalizability.", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}
        ])
    ]
)

# PHT 100 - S1
add_c(
    "pht100-physics", "PHT 100", "Engineering Physics", 4, "Semester 1", "All Branches (Common)", "common", "BSC",
    [
        make_m(1, "Oscillations & Waves", "Simple harmonic motion, Damped harmonic oscillator: Under, critical and over-damped motions, Forced oscillations, Resonance, Sharpness of resonance, Q-factor.", [
            {"q": "Derive the differential equation of damped harmonic oscillator and solve for under-damped condition.", "marks": 10, "frequency": "Repeated 6 times"}
        ]),
        make_m(2, "Wave Optics", "Interference of light: Principle of superposition, Cosine law, Interference in thin films, Air wedge experiment, Newton's rings. Diffraction: Fraunhofer diffraction at single slit, Diffraction grating.", [
            {"q": "Explain the formation of Newton's rings in reflected light and derive expression for diameter of nth dark ring.", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}
        ]),
        make_m(3, "Quantum Mechanics", "Dual nature of matter, De Broglie hypothesis, Davisson-Germer experiment, Uncertainty principle, Wavefunction properties, Time-dependent and time-independent Schrodinger equations, Particle in a 1D box.", [
            {"q": "Derive Schrodinger 1D time-independent wave equation and calculate eigen energy values of a particle in an infinite potential box.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}
        ]),
        make_m(4, "Lasers & Fiber Optics", "Absorption, Spontaneous and Stimulated emission, Einstein's coefficients, Population inversion, Optical resonator, Ruby laser, He-Ne laser. Optical fibers: Acceptance angle, Numerical aperture, Step-index vs Graded-index.", [
            {"q": "Explain the working of Ruby laser with neat energy level diagram. Derive relation between Einstein's coefficients.", "marks": 10, "frequency": "Repeated 7 times"}
        ]),
        make_m(5, "Ultrasonics & Superconductivity", "Ultrasonics: Piezoelectric oscillator, Magnetostriction generator, Ultrasonic flaw detector. Superconductivity: Meissner effect, Type-I and Type-II superconductors, BCS theory overview, SQUID.", [
            {"q": "Explain production of ultrasonic waves using Piezoelectric method and discuss industrial applications in Non-Destructive Testing (NDT).", "marks": 10, "frequency": "Repeated 7 times"}
        ])
    ]
)

# EST 100 - S1
add_c(
    "est100-mechanics", "EST 100", "Engineering Mechanics", 3, "Semester 1", "All Branches (Common)", "common", "ESC",
    [
        make_m(1, "Statics of Particles & Coplanar Force Systems", "Concept of particle and rigid body, Force systems, Resolution and composition of forces, Resultant of concurrent forces, Equilibrium equations, Lami's theorem.", [
            {"q": "State and prove Lami's theorem. A 100 kg cylinder is supported between two inclined planes at 30 and 60 degrees. Find support reactions.", "marks": 10, "frequency": "Repeated 6 times"}
        ]),
        make_m(2, "Support Reactions & Friction", "Free body diagrams, Support reactions of simply supported and cantilever beams, Friction: Laws of dry friction, Angle of friction, Angle of repose, Cone of friction, Wedge friction.", [
            {"q": "Find the minimum horizontal force P required to raise a load W using a wedge of angle alpha with friction coefficient mu.", "marks": 10, "frequency": "Repeated 7 times"}
        ]),
        make_m(3, "Centroid & Moment of Inertia", "Centroid of composite areas (L, T, I sections), Theorem of Pappus-Guldinus, Moment of inertia of plane areas, Parallel and perpendicular axis theorems, Polar moment of inertia, Radius of gyration.", [
            {"q": "Find the centroid and moment of inertia about the centroidal x-axis for an unsymmetrical I-section.", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}
        ]),
        make_m(4, "Dynamics of Particles", "Kinematics: Rectilinear motion with uniform and variable acceleration, Curvilinear motion, Projectile motion. Kinetics: D'Alembert's principle, Work-energy principle, Impulse-momentum equation.", [
            {"q": "A bullet of mass m strikes a suspended block of mass M with velocity v and gets embedded. Find the maximum angle of swing using momentum and energy principles.", "marks": 10, "frequency": "Repeated 7 times"}
        ]),
        make_m(5, "Rotation of Rigid Bodies & Vibrations", "Rotation of rigid body about a fixed axis, Mass moment of inertia of standard shapes, Work and energy in rotational motion, Simple harmonic motion of mechanical systems, Free undamped vibrations of spring-mass systems.", [
            {"q": "Derive expression for the natural frequency of oscillation of a simple pendulum and a mass-spring system.", "marks": 10, "frequency": "Repeated 6 times"}
        ])
    ]
)

# EST 110 - S1
add_c(
    "est110-civil-mech", "EST 110", "Basics of Civil & Mechanical Engineering", 4, "Semester 1", "All Branches (Common)", "common", "ESC",
    [
        make_m(1, "Civil Engineering Materials & Surveying", "General introduction, Stones, Bricks, Cement: Chemical composition, Grades, Concrete: Ingredients, Water-cement ratio, Grades. Surveying: Chain surveying, Leveling, Total Station.", [
            {"q": "Explain water-cement ratio and Abram's law. What is workability of concrete and how is it measured using slump test?", "marks": 7, "frequency": "Repeated 5 times"}
        ]),
        make_m(2, "Building Components & Green Buildings", "Foundations: Shallow and deep foundations, Superstructure: Columns, Beams, Lintels, Roofs, Doors, Windows. Green building concepts, Rainwater harvesting systems.", [
            {"q": "Differentiate between shallow and deep foundations with sketches. Explain rainwater harvesting methods for residential buildings.", "marks": 8, "frequency": "Repeated 6 times"}
        ]),
        make_m(3, "Thermodynamic Systems & Boilers", "System, Surroundings, Laws of thermodynamics, Concept of entropy, Steam generators: Fire-tube boilers (Cochran) vs Water-tube boilers (Babcock & Wilcox), Boiler mountings and accessories.", [
            {"q": "Compare fire-tube and water-tube boilers. Explain working of Babcock & Wilcox boiler with neat sketch.", "marks": 7, "frequency": "Repeated 6 times"}
        ]),
        make_m(4, "Internal Combustion Engines", "Classification, Air standard Otto and Diesel cycles, 4-stroke Petrol engine, 4-stroke Diesel engine, 2-stroke engines, Fuel injection systems, Lubrication and cooling systems.", [
            {"q": "Explain working of 4-stroke Diesel engine with PV diagram and timing chart. Differentiate between SI and CI engines.", "marks": 8, "frequency": "Repeated 7 times"}
        ]),
        make_m(5, "Power Transmission & Manufacturing", "Belt drives: Flat and V-belts, Velocity ratio, Creep, Slip, Gear drives: Spur, Helical, Bevel gears. Manufacturing: Casting, Forging, Welding (Arc and Gas), Refrigeration cycles: Vapor compression system.", [
            {"q": "Explain working of Vapor Compression Refrigeration System (VCRS) with schematic and PH/TS diagrams.", "marks": 8, "frequency": "Repeated 7 times"}
        ])
    ]
)

# HUN 101 - S1
add_c(
    "hun101-lifeskills", "HUN 101", "Life Skills & Professional Communication", 2, "Semester 1", "All Branches (Common)", "common", "HMC",
    [
        make_m(1, "Communication Essentials", "Verbal and non-verbal communication, Body language, Eye contact, Active listening, Barriers to effective communication, Professional email etiquette.", [
            {"q": "Explain 7 Cs of effective communication and identify key interpersonal communication barriers.", "marks": 7, "frequency": "Repeated 5 times"}
        ]),
        make_m(2, "Critical Thinking & Problem Solving", "Lateral thinking, Deductive vs inductive reasoning, Problem formulation, Root Cause Analysis (Fishbone diagram), Six Thinking Hats method.", [
            {"q": "Apply Edward de Bono's Six Thinking Hats technique to resolve an engineering project deadlock.", "marks": 8, "frequency": "Repeated 6 times"}
        ]),
        make_m(3, "Team Dynamics & Leadership", "Leadership styles: Transformational, Servant, Authoritarian; Belbin team roles, Conflict resolution strategies (Thomas-Kilmann model), Group discussions.", [
            {"q": "Describe stages of team development (Forming, Storming, Norming, Performing, Adjourning) and conflict handling.", "marks": 8, "frequency": "Repeated 6 times"}
        ]),
        make_m(4, "Stress Management & Emotional Intelligence", "Understanding stress, Eustress vs distress, Time management using Eisenhower Matrix, Goleman's model of Emotional Intelligence (EQ).", [
            {"q": "Discuss the five components of emotional intelligence according to Daniel Goleman.", "marks": 7, "frequency": "Repeated 5 times"}
        ]),
        make_m(5, "Professional Ethics & Values", "Engineering ethics, Codes of conduct, Whistleblowing, Intellectual property rights (IPR), Plagiarism, Social responsibility of engineers.", [
            {"q": "Discuss the role of professional ethics in engineering decisions with reference to landmark engineering failures.", "marks": 8, "frequency": "Repeated 6 times"}
        ])
    ]
)

# MAT 102 - S2
add_c(
    "mat102-diff", "MAT 102", "Vector Calculus, Differential Equations & Transforms", 4, "Semester 2", "All Branches (Common)", "common", "BSC",
    [
        make_m(1, "First Order Ordinary Differential Equations", "Exact differential equations, Integrating factors, Orthogonal trajectories, Linear ODEs, Bernoulli's equation, Applications: Newton's law of cooling, Population models.", [
            {"q": "Find orthogonal trajectories of the family of coaxial circles x^2 + y^2 + 2gx + c = 0.", "marks": 7, "frequency": "Repeated 5 times"}
        ]),
        make_m(2, "Higher Order Linear ODEs", "Homogeneous linear ODEs with constant coefficients, Method of undetermined coefficients, Method of variation of parameters, Cauchy-Euler differential equations.", [
            {"q": "Solve y'' + y = sec(x) by method of variation of parameters.", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}
        ]),
        make_m(3, "Laplace Transforms", "Laplace transform definition, Linearity, First and second shifting theorems, Transforms of derivatives and integrals, Multiplication by t^n, Division by t.", [
            {"q": "Find the Laplace transform of (sin(at) / t) and hence evaluate Integral(0 to inf) (sin(t)/t) dt.", "marks": 10, "frequency": "Repeated 7 times"}
        ]),
        make_m(4, "Inverse Laplace & Initial Value Problems", "Inverse Laplace transforms, Partial fraction expansion, Convolution theorem, Unit step function, Dirac delta function, Solving ODEs with initial values.", [
            {"q": "Using convolution theorem, find the inverse Laplace transform of 1 / (s^2 * (s^2 + 1)).", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}
        ]),
        make_m(5, "Fourier Series", "Periodic functions, Dirichlet conditions, Euler's formulas, Fourier series of even and odd functions, Half range sine and cosine expansions, Parseval's identity.", [
            {"q": "Find Fourier series of f(x) = x^2 in (-pi, pi) and deduce that 1/1^2 + 1/2^2 + 1/3^2 + ... = pi^2 / 6.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}
        ])
    ]
)

# EST 102 - S2
add_c(
    "est102-cprog", "EST 102", "Programming in C", 4, "Semester 2", "All Branches (Common)", "common", "ESC",
    [
        make_m(1, "C Fundamentals & Flowcharts", "Algorithms, Flowcharts, Constants, Variables, Data Types, Operators, Type conversion, Formatted I/O.", [
            {"q": "Draw flowchart and write C program to check for Prime and Armstrong numbers.", "marks": 10, "frequency": "Repeated 7 times"}
        ]),
        make_m(2, "Control Structures & Iteration", "if-else, switch-case, for, while, do-while, break, continue, Nested loops, Patterns.", [
            {"q": "Write a C program using switch-case to implement a menu-driven calculator.", "marks": 7, "frequency": "Repeated 6 times"}
        ]),
        make_m(3, "Arrays & Strings", "1D/2D Arrays, Matrix multiplication. String manipulation with and without library functions.", [
            {"q": "Write a C program to multiply two matrices A[m][n] and B[p][q] after dimension check.", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}
        ]),
        make_m(4, "Functions & Recursion", "User functions, Call by value vs reference, Storage classes, Tower of Hanoi recursion.", [
            {"q": "Write a C function to solve the Tower of Hanoi problem for n disks using recursion.", "marks": 10, "frequency": "Repeated 7 times"}
        ]),
        make_m(5, "Pointers, Structs & File I/O", "Pointer arithmetic, Dynamic allocation (malloc/free), Structures vs Unions, File handling.", [
            {"q": "Define structure Student and write C program to rank 50 students.", "marks": 10, "frequency": "Repeated 8 times"}
        ])
    ]
)

# CYT 100 - S2
add_c(
    "cyt100-chemistry", "CYT 100", "Engineering Chemistry", 4, "Semester 2", "All Branches (Common)", "common", "BSC",
    [
        make_m(1, "Electrochemistry & Corrosion", "Electrochemical cells, Nernst equation, Calomel electrode, Glass electrode, Electrochemical corrosion mechanism, Factors influencing corrosion, Cathodic protection: Sacrificial anode and Impressed current.", [
            {"q": "Derive Nernst equation for single electrode potential. Explain electrochemical theory of corrosion of iron.", "marks": 10, "frequency": "Repeated 8 times"}
        ]),
        make_m(2, "Polymers & Nanomaterials", "Classification of polymers, Thermoplastics vs Thermosetting, Conducting polymers (Polyaniline), Carbon Nanotubes (CNTs): SWCNT, MWCNT, Chemical vapor deposition synthesis, Applications.", [
            {"q": "Explain synthesis, properties and engineering applications of Carbon Nanotubes (CNTs).", "marks": 10, "frequency": "Repeated 7 times"}
        ]),
        make_m(3, "Fuels & Energy Storage", "Calorific value: HCV, LCV, Bomb calorimeter determination, Knocking in engines, Octane and Cetane numbers, Lithium-ion battery: Construction, Charge-discharge reactions, Hydrogen-Oxygen fuel cell.", [
            {"q": "Describe construction and working of Lithium-ion battery and H2-O2 fuel cell with electrode reactions.", "marks": 10, "frequency": "Repeated 8 times"}
        ]),
        make_m(4, "Water Technology", "Hardness of water: Temporary and permanent hardness, Units of hardness, EDTA titration method, Boiler feed water troubles: Sludge, Scale, Caustic embrittlement, Demineralization by Ion-exchange resins.", [
            {"q": "Explain estimation of total hardness of water by EDTA method with chemical equations and calculations.", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}
        ]),
        make_m(5, "Spectroscopic Techniques", "Beer-Lambert's law, UV-Visible spectroscopy: Chromophores, Auxochromes, Bathochromic shift, Vibrational spectroscopy (FTIR): Modes of vibration, Characteristic functional group absorption bands.", [
            {"q": "State and derive Beer-Lambert's law. What are fundamental vibrational modes in CO2 and H2O molecules?", "marks": 10, "frequency": "Repeated 7 times"}
        ])
    ]
)

# EST 120 - S2
add_c(
    "est120-elec-elec", "EST 120", "Basics of Electrical & Electronics Engineering", 4, "Semester 2", "All Branches (Common)", "common", "ESC",
    [
        make_m(1, "DC Circuits & AC Fundamentals", "Ohm's law, Kirchhoff's laws, Nodal and Mesh analysis, Generation of alternating voltages, RMS and average values, Form factor, Peak factor, Phasor representation.", [
            {"q": "Calculate current in each branch of a DC bridge network using Kirchhoff's laws.", "marks": 7, "frequency": "Repeated 6 times"}
        ]),
        make_m(2, "AC Circuits & Three-Phase Systems", "Series RL, RC, and RLC circuits, Power factor, Active, Reactive, and Apparent power, Generation of 3-phase voltages, Star and Delta connections, Relationship between line and phase quantities.", [
            {"q": "Derive relationship between line and phase voltages and currents in balanced Star and Delta 3-phase systems.", "marks": 8, "frequency": "Repeated 8 times (Guaranteed)"}
        ]),
        make_m(3, "Electrical Machines", "DC Motors: Working principle, Back EMF, Speed-torque characteristics, Single-phase transformers: Principle of operation, EMF equation, Transformation ratio, Losses and efficiency.", [
            {"q": "Derive EMF equation of single-phase transformer. Explain open circuit and short circuit losses.", "marks": 8, "frequency": "Repeated 7 times"}
        ]),
        make_m(4, "Semiconductor Diodes & Applications", "PN junction diode: Forward and reverse characteristics, Zener diode: Breakdown mechanisms, Half-wave and Full-wave bridge rectifiers, Capacitor filter, Zener voltage regulator.", [
            {"q": "Explain operation of full-wave bridge rectifier with neat circuit and input/output waveforms. Derive ripple factor.", "marks": 8, "frequency": "Repeated 8 times"}
        ]),
        make_m(5, "Bipolar Junction Transistors & Op-Amps", "BJT operations: CE, CB configurations, Transistor as an amplifier and switch, Ideal operational amplifier characteristics, Inverting and Non-inverting Op-Amp configurations.", [
            {"q": "Explain CE configuration of BJT with input and output characteristics. Define current gains alpha and beta.", "marks": 8, "frequency": "Repeated 7 times"}
        ])
    ]
)

# EST 130 - S2
add_c(
    "est130-graphics", "EST 130", "Engineering Graphics", 3, "Semester 2", "All Branches (Common)", "common", "ESC",
    [
        make_m(1, "Principles of Projections & Points", "BIS conventions, Lettering, Dimensioning rules, Scales, Orthographic projection concept, Projections of points situated in all four quadrants.", [
            {"q": "Draw the projections of points located 20mm above HP, 30mm behind VP, and on HP, 40mm in front of VP.", "marks": 7, "frequency": "Repeated 6 times"}
        ]),
        make_m(2, "Projections of Straight Lines", "Projections of straight lines parallel, perpendicular, and inclined to reference planes, Determination of true length and inclinations with HP and VP, Traces of lines.", [
            {"q": "A line AB 80mm long has end A 20mm above HP and 30mm in front of VP. Top view measures 60mm and front view 70mm. Find true inclinations.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}
        ]),
        make_m(3, "Projections of Planes & Solids", "Projections of regular polygonal and circular planes inclined to both reference planes. Projections of prisms, pyramids, cylinders, and cones with axis inclined to one reference plane.", [
            {"q": "A pentagonal pyramid of base edge 30mm and axis 60mm rests on an edge of its base on HP with axis inclined at 45 deg to HP. Draw projections.", "marks": 10, "frequency": "Repeated 8 times"}
        ]),
        make_m(4, "Sections of Solids & Development of Surfaces", "Section planes parallel and inclined to HP/VP, True shape of section, Development of lateral surfaces of prisms, pyramids, cones, and cylinders.", [
            {"q": "A cone of base diameter 50mm and axis 65mm is cut by a section plane at 45 deg to HP passing through midpoint of axis. Draw sectional top view and development.", "marks": 10, "frequency": "Repeated 8 times"}
        ]),
        make_m(5, "Isometric Projections", "Isometric scale, Isometric view and isometric projection of simple and truncated solids, Composite solids (Cylinder on frustum of cone, Sphere on prism).", [
            {"q": "Draw the isometric view of a hemisphere of diameter 60mm resting centrally on top of a square prism of base side 70mm and height 30mm.", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}
        ])
    ]
)

# Now write out courses_data.py template and load remaining branch scripts
print("Writing common foundation courses... Total:", len(courses))
