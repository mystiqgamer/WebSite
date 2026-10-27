"""
KTU ScholarOS - Comprehensive Course Database (B.Tech 2024 Scheme)
All semesters S1 to S8 across 5 major branches (CSE, ECE, EEE, MECH, CE/CN) and Common Foundation.
"""

from typing import List, Dict, Any

KTU_COURSES: List[Dict[str, Any]] = [
    {
        "id": 'mat101-calc',
        "code": 'MAT 101',
        "title": 'Linear Algebra & Calculus',
        "credits": 4,
        "semester": 'Semester 1',
        "branch": 'All Branches (Common)',
        "branch_id": 'common',
        "category": 'BSC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Single Variable Calculus & Series',
                "syllabus": "Taylor's and Maclaurin's expansions, Indeterminate forms, L'Hopital's Rule. Infinite series: Convergence tests (Ratio test, Root test, Alternating series test, Leibniz's theorem).",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Expand log(1 + e^x) in powers of x using Maclaurin's series up to x^4.", "marks": 7, "frequency": 'Repeated 5 times'},
                    {"q": 'Test convergence of the alternating series Sigma (-1)^n * (n / (2n^2 + 1)) using Leibniz test.', "marks": 7, "frequency": 'Repeated 4 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Multivariable Differential Calculus',
                "syllabus": "Partial derivatives, Homogeneous functions, Euler's theorem, Total derivative, Jacobians, Maxima and minima of functions of two variables, Lagrange multipliers.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "If u = sin^-1((x + y) / (sqrt(x) + sqrt(y))), prove that x*(du/dx) + y*(du/dy) = (1/2)*tan(u) using Euler's theorem.", "marks": 10, "frequency": 'Repeated 8 times (Guaranteed)'},
                    {"q": 'Find maximum and minimum distance from the origin to 5x^2 + 6xy + 5y^2 = 8 using Lagrange multipliers.', "marks": 10, "frequency": 'Repeated 7 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Multiple Integrals',
                "syllabus": 'Double integrals (Cartesian and Polar), Change of order of integration, Area bounded by curves. Triple integrals, Volume of solids.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Change the order of integration and evaluate: Integral(0 to a) Integral(x to a) (x / (x^2 + y^2)) dy dx.', "marks": 10, "frequency": 'Repeated 8 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Vector Calculus & Line/Surface Integrals',
                "syllabus": "Gradient, Directional derivative, Divergence, Curl. Green's theorem in a plane, Gauss Divergence theorem, Stokes' theorem.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Verify Green's theorem in the plane for Integral (xy + y^2)dx + x^2 dy where C is bounded by y = x and y = x^2.", "marks": 10, "frequency": 'Repeated 7 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Linear Algebra, Eigenvalues & Cayley-Hamilton',
                "syllabus": 'Rank of matrix, Echelon form, System of linear equations. Eigenvalues and Eigenvectors, Cayley-Hamilton theorem, Diagonalization.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Find eigenvalues and eigenvectors of matrix A = [[2, 1, 1], [2, 3, 2], [3, 3, 4]] and test for diagonalizability.', "marks": 10, "frequency": 'Repeated 8 times (Guaranteed)'},
                ]
            },
        ]
    },
    {
        "id": 'pht100-physics',
        "code": 'PHT 100',
        "title": 'Engineering Physics',
        "credits": 4,
        "semester": 'Semester 1',
        "branch": 'All Branches (Common)',
        "branch_id": 'common',
        "category": 'BSC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Oscillations & Waves',
                "syllabus": 'Simple harmonic motion, Damped harmonic oscillator: Under, critical and over-damped motions, Forced oscillations, Resonance, Sharpness of resonance, Q-factor.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive the differential equation of damped harmonic oscillator and solve for under-damped condition.', "marks": 10, "frequency": 'Repeated 6 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Wave Optics',
                "syllabus": "Interference of light: Principle of superposition, Cosine law, Interference in thin films, Air wedge experiment, Newton's rings. Diffraction: Fraunhofer diffraction at single slit, Diffraction grating.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Explain the formation of Newton's rings in reflected light and derive expression for diameter of nth dark ring.", "marks": 10, "frequency": 'Repeated 8 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Quantum Mechanics',
                "syllabus": 'Dual nature of matter, De Broglie hypothesis, Davisson-Germer experiment, Uncertainty principle, Wavefunction properties, Time-dependent and time-independent Schrodinger equations, Particle in a 1D box.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive Schrodinger 1D time-independent wave equation and calculate eigen energy values of a particle in an infinite potential box.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Lasers & Fiber Optics',
                "syllabus": "Absorption, Spontaneous and Stimulated emission, Einstein's coefficients, Population inversion, Optical resonator, Ruby laser, He-Ne laser. Optical fibers: Acceptance angle, Numerical aperture, Step-index vs Graded-index.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Explain the working of Ruby laser with neat energy level diagram. Derive relation between Einstein's coefficients.", "marks": 10, "frequency": 'Repeated 7 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Ultrasonics & Superconductivity',
                "syllabus": 'Ultrasonics: Piezoelectric oscillator, Magnetostriction generator, Ultrasonic flaw detector. Superconductivity: Meissner effect, Type-I and Type-II superconductors, BCS theory overview, SQUID.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain production of ultrasonic waves using Piezoelectric method and discuss industrial applications in Non-Destructive Testing (NDT).', "marks": 10, "frequency": 'Repeated 7 times'},
                ]
            },
        ]
    },
    {
        "id": 'est100-mechanics',
        "code": 'EST 100',
        "title": 'Engineering Mechanics',
        "credits": 3,
        "semester": 'Semester 1',
        "branch": 'All Branches (Common)',
        "branch_id": 'common',
        "category": 'ESC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Statics of Particles & Coplanar Force Systems',
                "syllabus": "Concept of particle and rigid body, Force systems, Resolution and composition of forces, Resultant of concurrent forces, Equilibrium equations, Lami's theorem.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "State and prove Lami's theorem. A 100 kg cylinder is supported between two inclined planes at 30 and 60 degrees. Find support reactions.", "marks": 10, "frequency": 'Repeated 6 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Support Reactions & Friction',
                "syllabus": 'Free body diagrams, Support reactions of simply supported and cantilever beams, Friction: Laws of dry friction, Angle of friction, Angle of repose, Cone of friction, Wedge friction.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Find the minimum horizontal force P required to raise a load W using a wedge of angle alpha with friction coefficient mu.', "marks": 10, "frequency": 'Repeated 7 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Centroid & Moment of Inertia',
                "syllabus": 'Centroid of composite areas (L, T, I sections), Theorem of Pappus-Guldinus, Moment of inertia of plane areas, Parallel and perpendicular axis theorems, Polar moment of inertia, Radius of gyration.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Find the centroid and moment of inertia about the centroidal x-axis for an unsymmetrical I-section.', "marks": 10, "frequency": 'Repeated 8 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Dynamics of Particles',
                "syllabus": "Kinematics: Rectilinear motion with uniform and variable acceleration, Curvilinear motion, Projectile motion. Kinetics: D'Alembert's principle, Work-energy principle, Impulse-momentum equation.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'A bullet of mass m strikes a suspended block of mass M with velocity v and gets embedded. Find the maximum angle of swing using momentum and energy principles.', "marks": 10, "frequency": 'Repeated 7 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Rotation of Rigid Bodies & Vibrations',
                "syllabus": 'Rotation of rigid body about a fixed axis, Mass moment of inertia of standard shapes, Work and energy in rotational motion, Simple harmonic motion of mechanical systems, Free undamped vibrations of spring-mass systems.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive expression for the natural frequency of oscillation of a simple pendulum and a mass-spring system.', "marks": 10, "frequency": 'Repeated 6 times'},
                ]
            },
        ]
    },
    {
        "id": 'est110-civil-mech',
        "code": 'EST 110',
        "title": 'Basics of Civil & Mechanical Engineering',
        "credits": 4,
        "semester": 'Semester 1',
        "branch": 'All Branches (Common)',
        "branch_id": 'common',
        "category": 'ESC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Civil Engineering Materials & Surveying',
                "syllabus": 'General introduction, Stones, Bricks, Cement: Chemical composition, Grades, Concrete: Ingredients, Water-cement ratio, Grades. Surveying: Chain surveying, Leveling, Total Station.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Explain water-cement ratio and Abram's law. What is workability of concrete and how is it measured using slump test?", "marks": 7, "frequency": 'Repeated 5 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Building Components & Green Buildings',
                "syllabus": 'Foundations: Shallow and deep foundations, Superstructure: Columns, Beams, Lintels, Roofs, Doors, Windows. Green building concepts, Rainwater harvesting systems.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Differentiate between shallow and deep foundations with sketches. Explain rainwater harvesting methods for residential buildings.', "marks": 8, "frequency": 'Repeated 6 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Thermodynamic Systems & Boilers',
                "syllabus": 'System, Surroundings, Laws of thermodynamics, Concept of entropy, Steam generators: Fire-tube boilers (Cochran) vs Water-tube boilers (Babcock & Wilcox), Boiler mountings and accessories.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Compare fire-tube and water-tube boilers. Explain working of Babcock & Wilcox boiler with neat sketch.', "marks": 7, "frequency": 'Repeated 6 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Internal Combustion Engines',
                "syllabus": 'Classification, Air standard Otto and Diesel cycles, 4-stroke Petrol engine, 4-stroke Diesel engine, 2-stroke engines, Fuel injection systems, Lubrication and cooling systems.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain working of 4-stroke Diesel engine with PV diagram and timing chart. Differentiate between SI and CI engines.', "marks": 8, "frequency": 'Repeated 7 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Power Transmission & Manufacturing',
                "syllabus": 'Belt drives: Flat and V-belts, Velocity ratio, Creep, Slip, Gear drives: Spur, Helical, Bevel gears. Manufacturing: Casting, Forging, Welding (Arc and Gas), Refrigeration cycles: Vapor compression system.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain working of Vapor Compression Refrigeration System (VCRS) with schematic and PH/TS diagrams.', "marks": 8, "frequency": 'Repeated 7 times'},
                ]
            },
        ]
    },
    {
        "id": 'hun101-lifeskills',
        "code": 'HUN 101',
        "title": 'Life Skills & Professional Communication',
        "credits": 2,
        "semester": 'Semester 1',
        "branch": 'All Branches (Common)',
        "branch_id": 'common',
        "category": 'HMC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Communication Essentials',
                "syllabus": 'Verbal and non-verbal communication, Body language, Eye contact, Active listening, Barriers to effective communication, Professional email etiquette.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain 7 Cs of effective communication and identify key interpersonal communication barriers.', "marks": 7, "frequency": 'Repeated 5 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Critical Thinking & Problem Solving',
                "syllabus": 'Lateral thinking, Deductive vs inductive reasoning, Problem formulation, Root Cause Analysis (Fishbone diagram), Six Thinking Hats method.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Apply Edward de Bono's Six Thinking Hats technique to resolve an engineering project deadlock.", "marks": 8, "frequency": 'Repeated 6 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Team Dynamics & Leadership',
                "syllabus": 'Leadership styles: Transformational, Servant, Authoritarian; Belbin team roles, Conflict resolution strategies (Thomas-Kilmann model), Group discussions.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Describe stages of team development (Forming, Storming, Norming, Performing, Adjourning) and conflict handling.', "marks": 8, "frequency": 'Repeated 6 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Stress Management & Emotional Intelligence',
                "syllabus": "Understanding stress, Eustress vs distress, Time management using Eisenhower Matrix, Goleman's model of Emotional Intelligence (EQ).",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Discuss the five components of emotional intelligence according to Daniel Goleman.', "marks": 7, "frequency": 'Repeated 5 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Professional Ethics & Values',
                "syllabus": 'Engineering ethics, Codes of conduct, Whistleblowing, Intellectual property rights (IPR), Plagiarism, Social responsibility of engineers.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Discuss the role of professional ethics in engineering decisions with reference to landmark engineering failures.', "marks": 8, "frequency": 'Repeated 6 times'},
                ]
            },
        ]
    },
    {
        "id": 'mat102-diff',
        "code": 'MAT 102',
        "title": 'Vector Calculus, Differential Equations & Transforms',
        "credits": 4,
        "semester": 'Semester 2',
        "branch": 'All Branches (Common)',
        "branch_id": 'common',
        "category": 'BSC',
        "modules": [
            {
                "module_no": 1,
                "title": 'First Order Ordinary Differential Equations',
                "syllabus": "Exact differential equations, Integrating factors, Orthogonal trajectories, Linear ODEs, Bernoulli's equation, Applications: Newton's law of cooling, Population models.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Find orthogonal trajectories of the family of coaxial circles x^2 + y^2 + 2gx + c = 0.', "marks": 7, "frequency": 'Repeated 5 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Higher Order Linear ODEs',
                "syllabus": 'Homogeneous linear ODEs with constant coefficients, Method of undetermined coefficients, Method of variation of parameters, Cauchy-Euler differential equations.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Solve y'' + y = sec(x) by method of variation of parameters.", "marks": 10, "frequency": 'Repeated 8 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Laplace Transforms',
                "syllabus": 'Laplace transform definition, Linearity, First and second shifting theorems, Transforms of derivatives and integrals, Multiplication by t^n, Division by t.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Find the Laplace transform of (sin(at) / t) and hence evaluate Integral(0 to inf) (sin(t)/t) dt.', "marks": 10, "frequency": 'Repeated 7 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Inverse Laplace & Initial Value Problems',
                "syllabus": 'Inverse Laplace transforms, Partial fraction expansion, Convolution theorem, Unit step function, Dirac delta function, Solving ODEs with initial values.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Using convolution theorem, find the inverse Laplace transform of 1 / (s^2 * (s^2 + 1)).', "marks": 10, "frequency": 'Repeated 8 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Fourier Series',
                "syllabus": "Periodic functions, Dirichlet conditions, Euler's formulas, Fourier series of even and odd functions, Half range sine and cosine expansions, Parseval's identity.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Find Fourier series of f(x) = x^2 in (-pi, pi) and deduce that 1/1^2 + 1/2^2 + 1/3^2 + ... = pi^2 / 6.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
        ]
    },
    {
        "id": 'est102-cprog',
        "code": 'EST 102',
        "title": 'Programming in C',
        "credits": 4,
        "semester": 'Semester 2',
        "branch": 'All Branches (Common)',
        "branch_id": 'common',
        "category": 'ESC',
        "modules": [
            {
                "module_no": 1,
                "title": 'C Fundamentals & Flowcharts',
                "syllabus": 'Algorithms, Flowcharts, Constants, Variables, Data Types, Operators, Type conversion, Formatted I/O.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Draw flowchart and write C program to check for Prime and Armstrong numbers.', "marks": 10, "frequency": 'Repeated 7 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Control Structures & Iteration',
                "syllabus": 'if-else, switch-case, for, while, do-while, break, continue, Nested loops, Patterns.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Write a C program using switch-case to implement a menu-driven calculator.', "marks": 7, "frequency": 'Repeated 6 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Arrays & Strings',
                "syllabus": '1D/2D Arrays, Matrix multiplication. String manipulation with and without library functions.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Write a C program to multiply two matrices A[m][n] and B[p][q] after dimension check.', "marks": 10, "frequency": 'Repeated 8 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Functions & Recursion',
                "syllabus": 'User functions, Call by value vs reference, Storage classes, Tower of Hanoi recursion.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Write a C function to solve the Tower of Hanoi problem for n disks using recursion.', "marks": 10, "frequency": 'Repeated 7 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Pointers, Structs & File I/O',
                "syllabus": 'Pointer arithmetic, Dynamic allocation (malloc/free), Structures vs Unions, File handling.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Define structure Student and write C program to rank 50 students.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'cyt100-chemistry',
        "code": 'CYT 100',
        "title": 'Engineering Chemistry',
        "credits": 4,
        "semester": 'Semester 2',
        "branch": 'All Branches (Common)',
        "branch_id": 'common',
        "category": 'BSC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Electrochemistry & Corrosion',
                "syllabus": 'Electrochemical cells, Nernst equation, Calomel electrode, Glass electrode, Electrochemical corrosion mechanism, Factors influencing corrosion, Cathodic protection: Sacrificial anode and Impressed current.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive Nernst equation for single electrode potential. Explain electrochemical theory of corrosion of iron.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Polymers & Nanomaterials',
                "syllabus": 'Classification of polymers, Thermoplastics vs Thermosetting, Conducting polymers (Polyaniline), Carbon Nanotubes (CNTs): SWCNT, MWCNT, Chemical vapor deposition synthesis, Applications.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain synthesis, properties and engineering applications of Carbon Nanotubes (CNTs).', "marks": 10, "frequency": 'Repeated 7 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Fuels & Energy Storage',
                "syllabus": 'Calorific value: HCV, LCV, Bomb calorimeter determination, Knocking in engines, Octane and Cetane numbers, Lithium-ion battery: Construction, Charge-discharge reactions, Hydrogen-Oxygen fuel cell.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Describe construction and working of Lithium-ion battery and H2-O2 fuel cell with electrode reactions.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Water Technology',
                "syllabus": 'Hardness of water: Temporary and permanent hardness, Units of hardness, EDTA titration method, Boiler feed water troubles: Sludge, Scale, Caustic embrittlement, Demineralization by Ion-exchange resins.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain estimation of total hardness of water by EDTA method with chemical equations and calculations.', "marks": 10, "frequency": 'Repeated 8 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Spectroscopic Techniques',
                "syllabus": "Beer-Lambert's law, UV-Visible spectroscopy: Chromophores, Auxochromes, Bathochromic shift, Vibrational spectroscopy (FTIR): Modes of vibration, Characteristic functional group absorption bands.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "State and derive Beer-Lambert's law. What are fundamental vibrational modes in CO2 and H2O molecules?", "marks": 10, "frequency": 'Repeated 7 times'},
                ]
            },
        ]
    },
    {
        "id": 'est120-elec-elec',
        "code": 'EST 120',
        "title": 'Basics of Electrical & Electronics Engineering',
        "credits": 4,
        "semester": 'Semester 2',
        "branch": 'All Branches (Common)',
        "branch_id": 'common',
        "category": 'ESC',
        "modules": [
            {
                "module_no": 1,
                "title": 'DC Circuits & AC Fundamentals',
                "syllabus": "Ohm's law, Kirchhoff's laws, Nodal and Mesh analysis, Generation of alternating voltages, RMS and average values, Form factor, Peak factor, Phasor representation.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Calculate current in each branch of a DC bridge network using Kirchhoff's laws.", "marks": 7, "frequency": 'Repeated 6 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'AC Circuits & Three-Phase Systems',
                "syllabus": 'Series RL, RC, and RLC circuits, Power factor, Active, Reactive, and Apparent power, Generation of 3-phase voltages, Star and Delta connections, Relationship between line and phase quantities.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive relationship between line and phase voltages and currents in balanced Star and Delta 3-phase systems.', "marks": 8, "frequency": 'Repeated 8 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Electrical Machines',
                "syllabus": 'DC Motors: Working principle, Back EMF, Speed-torque characteristics, Single-phase transformers: Principle of operation, EMF equation, Transformation ratio, Losses and efficiency.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive EMF equation of single-phase transformer. Explain open circuit and short circuit losses.', "marks": 8, "frequency": 'Repeated 7 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Semiconductor Diodes & Applications',
                "syllabus": 'PN junction diode: Forward and reverse characteristics, Zener diode: Breakdown mechanisms, Half-wave and Full-wave bridge rectifiers, Capacitor filter, Zener voltage regulator.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain operation of full-wave bridge rectifier with neat circuit and input/output waveforms. Derive ripple factor.', "marks": 8, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Bipolar Junction Transistors & Op-Amps',
                "syllabus": 'BJT operations: CE, CB configurations, Transistor as an amplifier and switch, Ideal operational amplifier characteristics, Inverting and Non-inverting Op-Amp configurations.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain CE configuration of BJT with input and output characteristics. Define current gains alpha and beta.', "marks": 8, "frequency": 'Repeated 7 times'},
                ]
            },
        ]
    },
    {
        "id": 'est130-graphics',
        "code": 'EST 130',
        "title": 'Engineering Graphics',
        "credits": 3,
        "semester": 'Semester 2',
        "branch": 'All Branches (Common)',
        "branch_id": 'common',
        "category": 'ESC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Principles of Projections & Points',
                "syllabus": 'BIS conventions, Lettering, Dimensioning rules, Scales, Orthographic projection concept, Projections of points situated in all four quadrants.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Draw the projections of points located 20mm above HP, 30mm behind VP, and on HP, 40mm in front of VP.', "marks": 7, "frequency": 'Repeated 6 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Projections of Straight Lines',
                "syllabus": 'Projections of straight lines parallel, perpendicular, and inclined to reference planes, Determination of true length and inclinations with HP and VP, Traces of lines.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'A line AB 80mm long has end A 20mm above HP and 30mm in front of VP. Top view measures 60mm and front view 70mm. Find true inclinations.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Projections of Planes & Solids',
                "syllabus": 'Projections of regular polygonal and circular planes inclined to both reference planes. Projections of prisms, pyramids, cylinders, and cones with axis inclined to one reference plane.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'A pentagonal pyramid of base edge 30mm and axis 60mm rests on an edge of its base on HP with axis inclined at 45 deg to HP. Draw projections.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Sections of Solids & Development of Surfaces',
                "syllabus": 'Section planes parallel and inclined to HP/VP, True shape of section, Development of lateral surfaces of prisms, pyramids, cones, and cylinders.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'A cone of base diameter 50mm and axis 65mm is cut by a section plane at 45 deg to HP passing through midpoint of axis. Draw sectional top view and development.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Isometric Projections',
                "syllabus": 'Isometric scale, Isometric view and isometric projection of simple and truncated solids, Composite solids (Cylinder on frustum of cone, Sphere on prism).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Draw the isometric view of a hemisphere of diameter 60mm resting centrally on top of a square prism of base side 70mm and height 30mm.', "marks": 10, "frequency": 'Repeated 8 times (Guaranteed)'},
                ]
            },
        ]
    },
    {
        "id": 'mat203-dms',
        "code": 'MAT 203',
        "title": 'Discrete Mathematical Structures',
        "credits": 4,
        "semester": 'Semester 3',
        "branch": 'Computer Science & Engineering',
        "branch_id": 'cse',
        "category": 'BSC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Mathematical Logic & Proofs',
                "syllabus": 'Propositional logic, Truth tables, Tautologies, Logical equivalences, Predicates and quantifiers, Rules of inference, Methods of proof (Direct, Contradiction, Induction).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Show that ((p -> q) ^ (q -> r)) -> (p -> r) is a tautology using truth tables and rules of inference.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Sets, Relations & Functions',
                "syllabus": 'Set operations, Relations: Reflexive, Symmetric, Transitive, Equivalence relations, Partitions, Partial orderings, Hasse diagrams, Functions: Injective, Surjective, Bijective, Pigeonhole principle.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Draw Hasse diagram of divisibility on D36 = {1, 2, 3, 4, 6, 9, 12, 18, 36} and find maximal, minimal, greatest, and least elements.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Lattices & Boolean Algebra',
                "syllabus": 'Lattices as posets, Properties of lattices, Sublattices, Distributive and Complemented lattices, Modular lattices, Boolean algebra: Laws, Duality principle, Boolean functions representation.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Prove that every distributive lattice is modular. Is the converse true? Justify with counterexample.', "marks": 10, "frequency": 'Repeated 7 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Group Theory & Algebraic Structures',
                "syllabus": "Semigroups, Monoids, Groups: Abelian groups, Subgroups, Cyclic groups, Cosets, Lagrange's theorem, Group homomorphisms, Rings and Fields.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "State and prove Lagrange's theorem for finite groups. Explain why order of any subgroup divides order of the group.", "marks": 10, "frequency": 'Repeated 8 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Recurrence Relations & Generating Functions',
                "syllabus": 'Solving linear recurrence relations with constant coefficients (Homogeneous and non-homogeneous), Generating functions, Inclusion-exclusion principle.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Solve recurrence relation a_n - 7a_{n-1} + 12a_{n-2} = 0 with a_0 = 2, a_1 = 5.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'cst201-ds',
        "code": 'CST 201',
        "title": 'Data Structures',
        "credits": 4,
        "semester": 'Semester 3',
        "branch": 'Computer Science & Engineering',
        "branch_id": 'cse',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Basic Concepts & Stacks',
                "syllabus": 'Complexity, Asymptotic Notations. Stacks: Infix to Postfix conversion, Postfix evaluation.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Convert infix expression ((A + B) * C - (D - E)) ^ (F + G) to postfix showing stack trace.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Queues & Linked Lists',
                "syllabus": 'Circular Queue, Deque, Priority Queue. Singly & Doubly Linked Lists, Polynomial Addition.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Circular Queue operations with C code and array wrapping.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Binary Trees & BST',
                "syllabus": 'Tree terminology, Binary Trees: Traversals. Binary Search Trees (BST): Insertion, Deletion, Search.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Construct a Binary Tree given Inorder and Preorder traversals.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Graphs & Spanning Trees',
                "syllabus": "Representations, BFS & DFS, Prim's and Kruskal's MST algorithms, AVL Tree rotations.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Trace Kruskal's algorithm on a weighted connected graph.", "marks": 10, "frequency": 'Repeated 7 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Sorting & Hashing',
                "syllabus": 'Quick Sort, Merge Sort, Heap Sort. Hash Tables, Collision Resolution techniques.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Quick Sort partition algorithm with Best/Worst case complexity.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'cst203-lsd',
        "code": 'CST 203',
        "title": 'Logic System Design',
        "credits": 4,
        "semester": 'Semester 3',
        "branch": 'Computer Science & Engineering',
        "branch_id": 'cse',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Number Systems & Codes',
                "syllabus": "Binary, Octal, Hexadecimal, 1's and 2's complement arithmetic, BCD, Gray code, Error detecting codes (Parity, Hamming).",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain 7-bit Hamming code error detection and correction with an example.', "marks": 10, "frequency": 'Repeated 7 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Boolean Algebra & K-Map Minimization',
                "syllabus": "Canonical SOP/POS forms, 4-variable Karnaugh Maps, Don't care conditions, Quine-McCluskey tabular reduction.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Simplify F(A, B, C, D) = Sigma m(0, 2, 5, 7, 8, 10, 13, 15) using 4-variable K-Map and draw logic circuit.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Combinational Logic Circuits',
                "syllabus": 'Full Adder, Parallel Adder, Look-ahead carry adder, Decoders, Multiplexers, De-multiplexers, Code Converters.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Implement 16:1 MUX using 4:1 multiplexers only.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Sequential Circuits & Flip-Flops',
                "syllabus": 'Latches, SR, JK, Master-Slave JK, D, and T Flip-Flops, Race-around condition, Excitation tables.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain race-around condition in JK flip-flop and how Master-Slave configuration solves it.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Counters, Registers & PLDs',
                "syllabus": 'Synchronous and Asynchronous Counters, Modulo-N Counters, Shift Registers, PROM, PLA, PAL.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Design a Mod-6 synchronous counter using JK flip-flops with state table and excitation diagrams.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'cst205-oops-java',
        "code": 'CST 205',
        "title": 'Object Oriented Programming using Java',
        "credits": 4,
        "semester": 'Semester 3',
        "branch": 'Computer Science & Engineering',
        "branch_id": 'cse',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Introduction to Java & OOP',
                "syllabus": 'OOP paradigms, JVM architecture, Bytecode, Primitive data types, Operators, Control statements, Classes, Objects, Constructors, Garbage collection, this keyword.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain JVM architecture with Classloader, Bytecode Verifier, and Execution Engine. Write a Java program demonstrating constructor overloading.', "marks": 10, "frequency": 'Repeated 7 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Inheritance & Polymorphism',
                "syllabus": 'Inheritance types (Single, Multilevel, Hierarchical), super keyword, Method overriding, Dynamic method dispatch, Abstract classes, Interfaces, Multiple inheritance in Java.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain dynamic method dispatch (runtime polymorphism) in Java with an illustrative program.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Packages & Exception Handling',
                "syllabus": 'Creating and importing packages, Access protection, Exception hierarchy, Checked vs unchecked exceptions, try-catch-finally blocks, throw, throws, User-defined exceptions.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Write a Java program to define and throw a custom InvalidAgeException when age is less than 18.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Multithreading & Generics',
                "syllabus": 'Thread lifecycle, Creating threads (Thread class and Runnable interface), Thread priorities, Synchronization, Inter-thread communication (wait, notify, notifyAll), Generics.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Solve the classic Producer-Consumer problem in Java using synchronized methods and wait/notify mechanism.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Java Collections & GUI (Swing)',
                "syllabus": 'Collections framework: ArrayList, LinkedList, HashSet, HashMap, Iterators, Swing fundamentals: JFrame, JPanel, JButton, JTextField, Event handling: ActionListener.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Write a Java Swing GUI application with two buttons and a text field that increments and decrements a counter on button clicks.', "marks": 10, "frequency": 'Repeated 7 times'},
                ]
            },
        ]
    },
    {
        "id": 'cst202-coa',
        "code": 'CST 202',
        "title": 'Computer Organization & Architecture',
        "credits": 4,
        "semester": 'Semester 4',
        "branch": 'Computer Science & Engineering',
        "branch_id": 'cse',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Basic Structure & Addressing Modes',
                "syllabus": 'Von Neumann model, Memory addressing, Addressing modes (Immediate, Direct, Indirect, Indexed), RISC vs CISC.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain various addressing modes with effective address formulas and code examples.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": "Arithmetic Operations & Booth's Algorithm",
                "syllabus": "Fast adders, Booth's signed multiplication algorithm, Restoring and Non-restoring division.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Multiply (-5) and (+7) using Booth's Algorithm in 5-bit binary.", "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Control Unit Design',
                "syllabus": 'Single bus CPU, Instruction execution sequence, Hardwired vs Microprogrammed control units.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Write complete control sequence for instruction ADD (R1), R2 on single-bus CPU.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Memory Hierarchy & Cache Mapping',
                "syllabus": 'Cache mapping (Direct, Associative, Set-Associative), Replacement policies, Virtual memory.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Direct and 4-way Set Associative cache mapping with tag, set, offset calculations.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Pipelining & DMA',
                "syllabus": 'Pipeline hazards (Structural, Data, Control), Direct Memory Access (DMA) controller.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain pipeline hazards and how forwarding and branch prediction mitigate stalls.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'cst204-dbms',
        "code": 'CST 204',
        "title": 'Database Management Systems',
        "credits": 4,
        "semester": 'Semester 4',
        "branch": 'Computer Science & Engineering',
        "branch_id": 'cse',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Database Architecture & ER Modeling',
                "syllabus": 'Three-schema architecture, Data independence, ER modeling, Strong and Weak entities, Extended ER features.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Draw an ER diagram for a University Management System specifying cardinalities and primary keys.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Relational Model & Relational Algebra',
                "syllabus": 'Relational constraints, Select, Project, Join operations, Tuple Relational Calculus, Domain Relational Calculus.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Natural Join, Theta Join, and Outer Joins with relational algebra syntax and tables.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'SQL & Normalization',
                "syllabus": 'Complex SQL queries, Aggregation, Views, Triggers, Functional Dependencies, 1NF, 2NF, 3NF, BCNF.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Normalize relation R(A, B, C, D, E) with F = {A->BC, CD->E, B->D, E->A} to 3NF and BCNF.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Transaction Processing & Concurrency',
                "syllabus": 'ACID properties, Serializability, Conflict serializability, Two-Phase Locking (2PL), Deadlock handling.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Test whether the schedule S: r1(x), r2(y), w1(x), r2(x), w2(y) is conflict serializable using precedence graph.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Storage & Indexing',
                "syllabus": 'File organization, RAID levels, Primary/Clustering/Secondary indexes, B-Trees and B+ Trees.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain B+ Tree structure and trace insertion of keys into an empty B+ Tree of order 4.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'cst206-os',
        "code": 'CST 206',
        "title": 'Operating Systems',
        "credits": 4,
        "semester": 'Semester 4',
        "branch": 'Computer Science & Engineering',
        "branch_id": 'cse',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'OS Overview & System Calls',
                "syllabus": 'Dual-mode operation, System calls (fork, exec, wait), OS structures (Monolithic, Microkernel).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain the step-by-step mechanism of system call execution and context switching.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Process Management & Scheduling',
                "syllabus": 'PCB, Process states, CPU Scheduling algorithms: FCFS, SJF, Priority, Round Robin.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Given 5 processes with arrival and burst times, draw Gantt chart and calculate average turnaround and waiting time for Round Robin (q=3).', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Synchronization & Deadlocks',
                "syllabus": "Critical Section problem, Peterson's algorithm, Semaphores, Classic synchronization problems (Dining Philosophers, Producer-Consumer), Banker's Algorithm.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Apply Banker's Algorithm to determine if the system is in a safe state and handle resource request vector.", "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Memory Management & Virtual Memory',
                "syllabus": 'Paging, Segmentation, TLB, Page replacement algorithms (FIFO, LRU, Optimal), Thrashing.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Calculate number of page faults for reference string 7,0,1,2,0,3,0,4,2,3,0,3,2 with 3 frames using LRU and FIFO.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'File Systems & Disk Scheduling',
                "syllabus": 'File allocation methods (Contiguous, Linked, Indexed), Disk scheduling (FCFS, SSTF, SCAN, C-SCAN).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Evaluate total head movements for disk queue requests using SSTF, SCAN, and C-SCAN.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'mat206-graph-num',
        "code": 'MAT 206',
        "title": 'Graph Theory & Number Theory',
        "credits": 4,
        "semester": 'Semester 4',
        "branch": 'Computer Science & Engineering',
        "branch_id": 'cse',
        "category": 'BSC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Introduction to Graphs',
                "syllabus": 'Graphs, Subgraphs, Walks, Paths, Cycles, Connected components, Euler graphs, Hamiltonian paths, Konigsberg bridge problem.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "State and prove Euler's theorem for existence of Eulerian circuit in a connected graph.", "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Trees & Connectivity',
                "syllabus": "Trees: Characterizations of trees, Spanning trees, Fundamental cutsets and circuits, Cayley's tree formula, Connectivity: Vertex and edge connectivity.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Prove that every tree with n vertices has exactly n - 1 edges.', "marks": 7, "frequency": 'Repeated 7 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Planarity & Graph Coloring',
                "syllabus": "Planar graphs, Euler's formula for planar graphs (v - e + f = 2), Kuratowski's theorem, Dual graphs, Vertex coloring, Chromatic number, Four color theorem.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "State and prove Euler's formula for connected planar graphs. Hence show that K5 and K3,3 are non-planar.", "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Divisibility & Modular Congruence',
                "syllabus": 'Divisibility, Division algorithm, Euclidean algorithm, Linear Diophantine equations, Prime numbers, Congruences, Chinese Remainder Theorem.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Solve system of linear congruences using Chinese Remainder Theorem: x = 2 (mod 3), x = 3 (mod 5), x = 2 (mod 7).', "marks": 10, "frequency": 'Repeated 8 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Number Theoretic Functions & Cryptography',
                "syllabus": "Euler's totient function, Fermat's Little Theorem, Wilson's theorem, Primitive roots, Cryptographic foundations: Diffie-Hellman and RSA algorithm.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'In RSA cryptosystem with p = 7, q = 11, e = 13, encrypt message M = 9 and find decryption key d.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'cst301-flat',
        "code": 'CST 301',
        "title": 'Formal Languages & Automata Theory',
        "credits": 4,
        "semester": 'Semester 5',
        "branch": 'Computer Science & Engineering',
        "branch_id": 'cse',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Finite Automata & Regular Expressions',
                "syllabus": "DFA, NFA, Equivalence of DFA and NFA, NFA to DFA conversion, Regular Expressions, Arden's theorem.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Convert given NFA with epsilon transitions into an equivalent DFA.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Regular Languages & Pumping Lemma',
                "syllabus": 'Pumping Lemma for regular languages, Closure properties of regular languages, DFA state minimization (Table filling).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Prove that L = {0^n 1^n | n >= 1} is not regular using Pumping Lemma.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Context-Free Grammars & Normal Forms',
                "syllabus": 'CFG, Derivation trees, Ambiguity, Chomsky Normal Form (CNF), Greibach Normal Form (GNF).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Convert CFG into Chomsky Normal Form (CNF) after eliminating null and unit productions.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Pushdown Automata (PDA)',
                "syllabus": 'Deterministic and Non-deterministic PDA, Equivalence of PDA and CFG, Pumping Lemma for CFLs.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Design PDA accepting language L = {w c w^R | w in {a, b}*} by empty stack.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Turing Machines & Decidability',
                "syllabus": 'Turing Machine model, Design of TM for arithmetic and languages, Halting problem, Undecidability, Post Correspondence Problem (PCP).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Design Turing Machine to compute 2's complement of a binary string.", "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'cst303-cn',
        "code": 'CST 303',
        "title": 'Computer Networks',
        "credits": 4,
        "semester": 'Semester 5',
        "branch": 'Computer Science & Engineering',
        "branch_id": 'cse',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Network Architecture & Physical Layer',
                "syllabus": 'OSI 7-layer reference model, TCP/IP protocol suite, Guided and unguided transmission media, Circuit switching vs Packet switching, Transmission impairments.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Compare OSI and TCP/IP reference models with neat architectural diagrams and function of each layer.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Data Link Layer & Medium Access Control',
                "syllabus": 'Framing, Error detection (CRC, Checksum), Sliding Window protocols (Go-Back-N, Selective Repeat), Random access protocols: ALOHA, CSMA/CD, Ethernet IEEE 802.3.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Cyclic Redundancy Check (CRC) error detection with generator polynomial x^4 + x + 1 and data word 1101011011.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Network Layer & IP Addressing',
                "syllabus": "IPv4 addressing, Subnetting, VLSM, CIDR, IPv6 architecture, Routing algorithms: Distance Vector Routing (Bellman-Ford), Link State Routing (Dijkstra's algorithm), Count-to-infinity problem.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Apply Dijkstra's algorithm to compute shortest path tree from source node A in a 6-node network.", "marks": 10, "frequency": 'Repeated 8 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Transport Layer Protocols',
                "syllabus": 'Process-to-process delivery, UDP header, TCP segments, TCP 3-way handshake connection establishment, Flow control (Sliding window), Congestion control: AIMD, Slow start, Fast retransmit.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain TCP congestion control mechanism with Slow Start, Congestion Avoidance, Fast Retransmit, and Fast Recovery phases.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Application Layer & Network Services',
                "syllabus": 'Domain Name System (DNS), HTTP/1.1 vs HTTP/2, Electronic Mail (SMTP, POP3, IMAP), Dynamic Host Configuration Protocol (DHCP), Network Address Translation (NAT).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain DNS message resolution process (Iterative vs Recursive queries) with step-by-step diagram.', "marks": 10, "frequency": 'Repeated 7 times'},
                ]
            },
        ]
    },
    {
        "id": 'cst305-ss',
        "code": 'CST 305',
        "title": 'System Software',
        "credits": 4,
        "semester": 'Semester 5',
        "branch": 'Computer Science & Engineering',
        "branch_id": 'cse',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Introduction to System Software & SIC Architecture',
                "syllabus": 'System software vs application software, Simplified Instructional Computer (SIC) architecture: Registers, Memory, Instruction formats, Addressing modes, SIC/XE architecture.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Differentiate between SIC and SIC/XE machine architectures in terms of registers, addressing modes, and instruction formats.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Assemblers',
                "syllabus": 'Two-pass assembler design, Symbol table (SYMTAB), Opcode table (OPTAB), Location counter (LOCCTR), Pass 1 and Pass 2 algorithms, Object program generation (Header, Text, End records).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain data structures and algorithms of Pass 1 and Pass 2 of a two-pass assembler with flowchart.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Loaders & Linkers',
                "syllabus": 'Basic loader functions, Absolute loaders, Relocating loaders (Bit mask, Modification record), Direct linking loaders, Dynamic linking, Comparison of linkage editor and linking loader.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain the design and algorithm of an absolute loader with object program record structure.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Macro Processors',
                "syllabus": 'Macro definition and call, Macro expansion, One-pass macro processor design: NAMTAB, DEFTAB, ARGTAB, Conditional macro expansion, Keyword parameters, Concatenation of macro parameters.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain data structures and algorithm of a one-pass macro processor handling definition and invocation.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Compilers & Debuggers',
                "syllabus": 'Overview of compiler phases, Lexical analysis, Syntax analysis, Code generation, Text editors: Structure and user interface, Interactive debugging systems: Breakpoints, Trace facilities.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain six phases of a compiler with input, output, and error handling for assignment statement: position = initial + rate * 60.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'cst307-micro',
        "code": 'CST 307',
        "title": 'Microprocessors & Microcontrollers',
        "credits": 4,
        "semester": 'Semester 5',
        "branch": 'Computer Science & Engineering',
        "branch_id": 'cse',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": '8086 Internal Architecture',
                "syllabus": '8086 internal architecture, BIU and EU, Register organization, Memory segmentation, Pin definitions, Maximum and Minimum modes of operation.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain 8086 architecture with BIU, EU, register sets, and physical address calculation.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 2,
                "title": '8086 Instruction Set & Assembly',
                "syllabus": 'Addressing modes, Data transfer, Arithmetic, Logical, Shift, Rotate, String manipulation instructions, Assembly language programming.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Write an 8086 assembly program to sort an array of N 16-bit numbers in ascending order using Bubble Sort.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Interrupts & Peripheral Interfacing',
                "syllabus": '8086 interrupt structure, Interrupt Vector Table (IVT), Programmable Peripheral Interface 8255, Programmable Interrupt Controller 8259.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain internal architecture of 8255 PPI and its modes of operation (Mode 0, Mode 1, Mode 2).', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": '8051 Microcontroller Architecture',
                "syllabus": '8051 architecture, Memory organization, Special Function Registers (SFRs), I/O ports, Timers and counters, Serial communication.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain 8051 memory organization (internal RAM, SFRs, external memory) with neat memory map.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": '8051 Interfacing & Embedded Applications',
                "syllabus": 'Interfacing LCD displays, Stepper motors, Matrix keypads, ADC 0808, DAC 0800 with 8051 using embedded C programs.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Draw interfacing diagram of stepper motor with 8051 and write embedded C program for clockwise rotation.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'cst304-cgip',
        "code": 'CST 304',
        "title": 'Computer Graphics & Image Processing',
        "credits": 4,
        "semester": 'Semester 6',
        "branch": 'Computer Science & Engineering',
        "branch_id": 'cse',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": '2D Graphics & Rasterization',
                "syllabus": "DDA line drawing, Bresenham's line and circle drawing algorithms, Midpoint circle algorithm, Scanline polygon filling.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Derive Bresenham's Line Drawing algorithm for lines with slope |m| < 1 with decision parameter derivation.", "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 2,
                "title": '2D/3D Transformations & Clipping',
                "syllabus": '2D transformations: Translation, Rotation, Scaling, Reflection, Shear, Cohen-Sutherland line clipping, Sutherland-Hodgman polygon clipping, 3D viewing.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Cohen-Sutherland Line Clipping algorithm with 4-bit region codes and step-by-step intersection calculations.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Digital Image Fundamentals',
                "syllabus": 'Sampling and quantization, Spatial resolution, Gray level transformation functions, Histogram equalization, Image smoothing and sharpening filters.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Perform histogram equalization on a given 3-bit 8x8 image with gray level distribution table.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Image Segmentation & Edge Detection',
                "syllabus": "Point, line, and edge detection, Gradient operators: Sobel, Prewitt, Laplacian, Canny edge detector, Thresholding: Global and Otsu's method.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Canny Edge Detection algorithm steps: Gaussian smoothing, Gradient calculation, Non-maximum suppression, Hysteresis thresholding.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Morphological Image Processing',
                "syllabus": 'Dilation, Erosion, Opening, Closing, Hit-or-Miss transform, Boundary extraction, Morphological skeleton, Image compression overview.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain morphological Dilation and Erosion operations with structuring elements and mathematical definitions.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'cst302-cd',
        "code": 'CST 302',
        "title": 'Compiler Design',
        "credits": 4,
        "semester": 'Semester 6',
        "branch": 'Computer Science & Engineering',
        "branch_id": 'cse',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Lexical Analysis',
                "syllabus": 'Structure of compiler, Lexical analyzer generator LEX, Regular expressions to DFA, Transition diagrams, Input buffering, Sentinels.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain transition from regular expressions to minimized DFA with subset construction and state reduction.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Syntax Analysis & Top-Down Parsing',
                "syllabus": 'Context-free grammars, Ambiguity, Left recursion elimination, Left factoring, LL(1) grammars, First and Follow sets, Recursive descent parser.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Construct LL(1) parsing table for given arithmetic grammar after eliminating left recursion and left factoring.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Bottom-Up Parsing',
                "syllabus": 'LR parsing engine, Shift-Reduce conflicts, SLR(1), Canonical LR(1), LALR(1) parsing tables, YACC parser generator tool.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Construct SLR(1) parsing table for grammar S -> CC, C -> cC | d.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Syntax-Directed Translation & Intermediate Code',
                "syllabus": 'Syntax-Directed Definitions (SDD), Inherited and Synthesized attributes, Three-address code, Quadruples, Triples, Type checking.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Generate three-address code, quadruples, and triples for expression x = (a + b) * -(c / d).', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Code Optimization & Generation',
                "syllabus": 'Basic blocks and Flow graphs, DAG representation of basic blocks, Loop optimization, Peephole optimization, Machine code generation.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Construct DAG for basic block and perform local optimizations (common subexpression elimination, dead code elimination).', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'cst306-daa',
        "code": 'CST 306',
        "title": 'Algorithm Analysis & Design',
        "credits": 4,
        "semester": 'Semester 6',
        "branch": 'Computer Science & Engineering',
        "branch_id": 'cse',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Divide and Conquer & Recurrences',
                "syllabus": "Recurrence relations: Master theorem, Substitution method, Recursion tree, Merge sort, Quick sort, Strassen's matrix multiplication.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Solve recurrence T(n) = 3T(n/2) + n^2 using Master Theorem and verify with recursion tree.', "marks": 7, "frequency": 'Repeated 7 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Greedy Method',
                "syllabus": 'Greedy strategy, Fractional knapsack problem, Job sequencing with deadlines, Huffman coding algorithm, Minimum Spanning Trees (Prim and Kruskal).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Construct optimal Huffman prefix code tree for characters {a, b, c, d, e, f} with given frequencies.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Dynamic Programming',
                "syllabus": 'Principle of optimality, 0/1 Knapsack, Bellman-Ford shortest paths, Floyd-Warshall all-pairs shortest paths, Longest Common Subsequence (LCS), Matrix chain multiplication.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Find optimal parenthesization of 4 matrices with dimensions <10, 100, 5, 50, 1> using Matrix Chain Multiplication.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Backtracking & Branch and Bound',
                "syllabus": 'State space tree, N-Queens problem, Subset sum problem, Graph coloring, Traveling Salesperson Problem (TSP) using Branch and Bound (Least cost).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Solve 4-Queens problem using backtracking showing state space search tree with bounding functions.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Complexity Classes & NP-Completeness',
                "syllabus": "Deterministic vs non-deterministic algorithms, P, NP, NP-Hard, NP-Complete, Cook's theorem, Reductions: 3-SAT to Vertex Cover, Approximation algorithms for Vertex Cover.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Prove that Circuit-SAT is NP-complete. Differentiate between NP-Hard and NP-Complete classes.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'cst401-ai',
        "code": 'CST 401',
        "title": 'Artificial Intelligence',
        "credits": 4,
        "semester": 'Semester 7',
        "branch": 'Computer Science & Engineering',
        "branch_id": 'cse',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Search Strategies & Problem Solving',
                "syllabus": 'Uninformed search (BFS, DFS, IDDFS), Heuristic search (Greedy Best-First, A* Search), Admissibility and Monotonicity of heuristics.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain A* search algorithm and prove that A* is admissible when heuristic h(n) never overestimates true cost.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Adversarial Search & Games',
                "syllabus": 'Game theory, Minimax algorithm, Alpha-Beta pruning, Constraint Satisfaction Problems (CSP), Forward checking, Backtracking search.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Trace Minimax algorithm with Alpha-Beta pruning on a 4-ply game tree to identify pruned branches.', "marks": 10, "frequency": 'Repeated 8 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Knowledge Representation & Logic',
                "syllabus": 'Propositional logic, First-Order Logic (FOL), Unification algorithm, Resolution refutation, Horn clauses, Forward and backward chaining.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Convert FOL sentences to Clause Form (CNF) and prove query using Resolution Refutation.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Probabilistic Reasoning & Bayesian Networks',
                "syllabus": "Uncertainty, Prior and conditional probability, Bayes' Rule, Bayesian Belief Networks (BBN), Conditional independence, Markov decision process overview.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Construct a Bayesian Belief Network for medical diagnosis and calculate joint probability distributions.', "marks": 10, "frequency": 'Repeated 7 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Machine Learning Foundations in AI',
                "syllabus": 'Supervised learning, Decision Trees (ID3 algorithm, Information Gain, Entropy), K-Nearest Neighbors, Reinforcement learning: Q-Learning concepts.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Construct a Decision Tree using ID3 algorithm calculating Entropy and Information Gain for play-tennis dataset.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'cst403-cns',
        "code": 'CST 403',
        "title": 'Cryptography & Cyber Security',
        "credits": 4,
        "semester": 'Semester 7',
        "branch": 'Computer Science & Engineering',
        "branch_id": 'cse',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Symmetric Ciphers & Block Encryption',
                "syllabus": 'Classical ciphers, DES algorithm architecture, Triple DES, AES encryption rounds, Modes of operation (ECB, CBC, CFB, OFB, CTR).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain AES encryption algorithm with SubBytes, ShiftRows, MixColumns, and AddRoundKey transformations.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Public Key Cryptography & Key Management',
                "syllabus": 'Principles of public key cryptosystems, RSA algorithm, Diffie-Hellman key exchange, Elliptic Curve Cryptography (ECC), Digital certificates (X.509).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Diffie-Hellman Key Exchange algorithm and show how Man-in-the-Middle attack compromises it.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Cryptographic Hash Functions & Signatures',
                "syllabus": 'Message authentication requirements, HMAC, SHA-256 and SHA-512 algorithms, Digital Signature Standard (DSS/DSA), Kerberos authentication.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain SHA-512 architecture and compression function processing 1024-bit message blocks.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Network & Transport Layer Security',
                "syllabus": 'IPSec (AH and ESP, Transport and Tunnel modes), SSL/TLS handshake protocol, HTTPS, Wireless network security (WPA2, WPA3).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain TLS Handshake Protocol step-by-step for establishing an encrypted web browsing session.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'System Security & Defenses',
                "syllabus": 'Intrusion Detection Systems (Host and Network IDS), Firewalls: Packet filtering, Stateful inspection, Application proxies, Honeypots, Indian IT Act 2000.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Differentiate between Packet Filtering Firewalls and Stateful Inspection Firewalls with traffic examples.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'cst402-dist-cloud',
        "code": 'CST 402',
        "title": 'Distributed Computing & Cloud Architecture',
        "credits": 4,
        "semester": 'Semester 8',
        "branch": 'Computer Science & Engineering',
        "branch_id": 'cse',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Distributed Systems Models & Clocks',
                "syllabus": 'Architectural models, Lamport logical clocks, Vector clocks, Chandy-Lamport distributed snapshot algorithm, Termination detection.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Lamport logical clock synchronization algorithm and total ordering of events with timing diagrams.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Mutual Exclusion & Consensus',
                "syllabus": "Distributed mutual exclusion: Ricart-Agrawala algorithm, Maekawa's algorithm, Consensus protocols: Paxos algorithm, Byzantine Generals problem.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Ricart-Agrawala algorithm for distributed mutual exclusion with message exchanges and proofs of correctness.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Cloud Computing Infrastructure',
                "syllabus": 'NIST cloud reference model, SPI service model (SaaS, PaaS, IaaS), Hypervisor technologies: Type 1 bare-metal vs Type 2 hosted, Containerization vs VM.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Compare hardware virtualization (hypervisors) and container-based virtualization (Docker) in terms of overhead and scalability.', "marks": 10, "frequency": 'Repeated 7 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Distributed File Systems & Big Data',
                "syllabus": 'Google File System (GFS) architecture, Hadoop Distributed File System (HDFS), MapReduce programming model, CAP theorem in distributed data stores.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain HDFS architecture with NameNode, DataNodes, Secondary NameNode, and block replication strategy.', "marks": 10, "frequency": 'Repeated 8 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Kubernetes & Cloud Native Deployments',
                "syllabus": 'Kubernetes architecture: Control Plane, Kubelet, Pods, Services, Deployments, ReplicaSets, Horizontal Pod Autoscaling (HPA), Microservices architecture.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Kubernetes control plane components (API Server, etcd, Controller Manager, Scheduler) and Pod lifecycle.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'mat201-pde-complex',
        "code": 'MAT 201',
        "title": 'Partial Differential Equations & Complex Analysis',
        "credits": 4,
        "semester": 'Semester 3',
        "branch": 'Electronics & Communication Engineering',
        "branch_id": 'ece',
        "category": 'BSC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Partial Differential Equations',
                "syllabus": "Formation of PDE, Solutions of first order linear PDEs: Lagrange's method, Charpit's method for non-linear first order PDEs.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Solve Lagrange's linear PDE: x(y^2 - z^2)p + y(z^2 - x^2)q = z(x^2 - y^2).", "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": '1D Wave & Heat Equations',
                "syllabus": 'Method of separation of variables, One-dimensional wave equation: Vibrating string, One-dimensional heat conduction equation with Dirichlet and Neumann boundary conditions.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Solve 1D wave equation d^2u/dt^2 = c^2 * d^2u/dx^2 for string with fixed ends and initial displacement f(x).', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Complex Analytic Functions',
                "syllabus": 'Functions of complex variables, Cauchy-Riemann equations in Cartesian and Polar forms, Analytic functions, Harmonic conjugate, Conformal mapping (w = z^2, w = e^z, Bilinear transformation).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Prove that u(x, y) = e^x * cos(y) is harmonic and find its harmonic conjugate v(x, y) to construct analytic function f(z).', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Complex Integration',
                "syllabus": "Line integrals in complex plane, Cauchy's integral theorem, Cauchy's integral formula for derivatives of analytic functions, Morera's theorem, Liouville's theorem.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Evaluate Integral_C (e^{2z} / (z + 1)^4) dz where C is circle |z| = 2 using Cauchy's integral formula.", "marks": 10, "frequency": 'Repeated 8 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Singularities & Residue Calculus',
                "syllabus": "Taylor's series, Laurent's series expansion, Zeros and poles, Essential singularities, Cauchy's residue theorem, Evaluation of real definite integrals around unit circle.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Evaluate Integral(0 to 2pi) (1 / (5 + 4*sin(theta))) d(theta) using contour integration and Cauchy's Residue Theorem.", "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
        ]
    },
    {
        "id": 'ect201-ssd',
        "code": 'ECT 201',
        "title": 'Solid State Devices',
        "credits": 4,
        "semester": 'Semester 3',
        "branch": 'Electronics & Communication Engineering',
        "branch_id": 'ece',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Semiconductor Physics',
                "syllabus": 'Carrier concentrations in intrinsic/extrinsic semiconductors, Fermi level, Drift and diffusion currents, Continuity equation.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive expression for carrier concentration in intrinsic semiconductor and locate Fermi energy level.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'PN Junction Diode',
                "syllabus": 'Built-in potential, Depletion width, V-I characteristics, Junction capacitance (Depletion and Diffusion), Breakdown (Zener & Avalanche).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive diode equation for ideal PN junction and explain reverse breakdown mechanisms.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Bipolar Junction Transistor',
                "syllabus": 'BJT fundamentals, Minority carrier distribution, Ebers-Moll model, Base width modulation (Early effect), Punch-through.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Early effect in BJT and derive terminal currents using Ebers-Moll model.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'MOSFET Fundamentals',
                "syllabus": 'MOS capacitor, Accumulation, Depletion, Inversion, Threshold voltage equation, Drain current equation in linear and saturation regions.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive drain current equation for n-channel enhancement MOSFET in saturation and triode regions.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Short Channel Effects & Special Devices',
                "syllabus": 'Drain Induced Barrier Lowering (DIBL), Velocity saturation, Hot carrier effects, FinFET, Tunnel FET, LED, Solar Cell.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Short Channel Effects (SCE) in MOSFETs: DIBL and sub-threshold conduction.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'ect203-lcd',
        "code": 'ECT 203',
        "title": 'Logic Circuit Design',
        "credits": 4,
        "semester": 'Semester 3',
        "branch": 'Electronics & Communication Engineering',
        "branch_id": 'ece',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Boolean Algebra & Optimization',
                "syllabus": "Boolean axioms, De Morgan's laws, SOP and POS canonical forms, 4 and 5-variable K-Maps with don't care conditions, Quine-McCluskey tabular reduction.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Minimize F(A, B, C, D) = Sigma m(1, 3, 7, 11, 15) + d(0, 2, 5) using Quine-McCluskey method.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Combinational Logic Design',
                "syllabus": 'Carry look-ahead adder, Magnitude comparators, Encoders, Priority encoders, Decoders, Multiplexers, De-multiplexers, Code converters (Gray to Binary).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Design a 4-bit Carry Look-Ahead (CLA) Adder and show that it operates faster than Ripple Carry Adder.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Sequential Logic & Latches',
                "syllabus": 'Latches vs Flip-flops, SR, JK, D, T flip-flops, Master-Slave JK flip-flop, Race-around condition, Characteristic and excitation equations.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Convert JK flip-flop to D flip-flop and T flip-flop showing excitation tables and K-Maps.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Synchronous & Asynchronous Counters',
                "syllabus": 'Design of synchronous mod-N counters, Ripple counters, Up/Down counters, Shift registers (SISO, SIPO, PISO, PIPO), Ring and Johnson counters.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Design a 3-bit synchronous Up-Down counter using T flip-flops with control input M.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Finite State Machines & PLDs',
                "syllabus": 'Mealy and Moore FSM models, State diagrams, State reduction, State assignment, Programmable Logic Arrays (PLA), Programmable Array Logic (PAL).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Design a Moore sequence detector to detect serial bit stream '1011' using D flip-flops.", "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
        ]
    },
    {
        "id": 'ect205-nt',
        "code": 'ECT 205',
        "title": 'Network Theory',
        "credits": 4,
        "semester": 'Semester 3',
        "branch": 'Electronics & Communication Engineering',
        "branch_id": 'ece',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Network Topology & Circuit Equations',
                "syllabus": 'Graph of a network, Tree, Co-tree, Incidence matrix, Fundamental cut-set matrix, Fundamental tie-set matrix, Node and Mesh formulations.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Draw graph for given electrical circuit, select a tree, and write fundamental tie-set and cut-set matrices.', "marks": 10, "frequency": 'Repeated 7 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Network Theorems in Frequency Domain',
                "syllabus": "Superposition theorem, Thevenin's theorem, Norton's theorem, Maximum power transfer theorem, Reciprocity theorem applied to AC and coupled circuits.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Find Thevenin's equivalent circuit across terminals AB for an AC circuit with dependent voltage and current sources.", "marks": 10, "frequency": 'Repeated 8 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Transient Analysis using Laplace Transforms',
                "syllabus": 'Transient response of series and parallel RL, RC, and RLC circuits with DC and sinusoidal excitations, Initial and final conditions.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'In a series RLC circuit with R = 2 ohm, L = 1 H, C = 0.5 F connected to DC supply V, find current i(t) for t > 0.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Two-Port Network Parameters',
                "syllabus": 'Z, Y, ABCD (Transmission), h, and g parameters, Relationships between parameters, Interconnection of two-port networks (Series, Parallel, Cascade).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive relationship between Transmission (ABCD) parameters and Impedance (Z) parameters of a two-port network.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Resonance & Filters',
                "syllabus": 'Series and Parallel resonance, Q-factor, Selectivity, Bandwidth, Constant-k and m-derived low-pass and high-pass passive filter prototypes.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Design a constant-k low-pass T-section filter with cut-off frequency 5 kHz and nominal design impedance 600 ohm.', "marks": 10, "frequency": 'Repeated 7 times'},
                ]
            },
        ]
    },
    {
        "id": 'ect202-analog-ckt',
        "code": 'ECT 202',
        "title": 'Analog Circuits',
        "credits": 4,
        "semester": 'Semester 4',
        "branch": 'Electronics & Communication Engineering',
        "branch_id": 'ece',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'BJT & MOSFET Small Signal Models',
                "syllabus": 'Biasing of BJT and MOSFET, Stability factor, Hybrid-pi model of BJT, Low frequency analysis of CE, CB, CC amplifiers, CS and CD MOSFET amplifiers.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive voltage gain, input impedance, and output impedance of CE amplifier using hybrid-pi small signal model.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Frequency Response of Amplifiers',
                "syllabus": "High frequency models of BJT and MOSFET, Miller's theorem, Low-frequency and high-frequency poles, Gain-bandwidth product, Multistage amplifiers.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "State and prove Miller's theorem. Determine high 3-dB cut-off frequency of a Common Emitter amplifier stage.", "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Feedback Amplifiers',
                "syllabus": 'General feedback structure, Properties of negative feedback, Feedback topologies: Voltage-series, Current-series, Voltage-shunt, Current-shunt, Stability analysis.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Analyze Voltage-Series negative feedback amplifier and prove that input impedance increases and output impedance decreases.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Oscillators & Waveform Generators',
                "syllabus": 'Barkhausen criteria for oscillation, RC phase shift oscillator, Wien bridge oscillator, Hartley, Colpitts, Crystal oscillators, Astable multivibrators.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive frequency of oscillation and minimum transistor gain h_fe required for sustained oscillations in RC phase shift oscillator.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Power Amplifiers & Tuned Amplifiers',
                "syllabus": 'Classification: Class A, Class B push-pull, Class AB, Class C, Conversion efficiency, Harmonic distortion, Single and double tuned amplifiers.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain operation of Class B push-pull power amplifier. Prove that maximum theoretical conversion efficiency is 78.5%.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'ect204-signals',
        "code": 'ECT 204',
        "title": 'Signals & Systems',
        "credits": 4,
        "semester": 'Semester 4',
        "branch": 'Electronics & Communication Engineering',
        "branch_id": 'ece',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Signal & System Foundations',
                "syllabus": 'Continuous-time and Discrete-time signals, Transformations, Energy and Power signals, LTI systems: Linearity, Time-invariance, Causality, BIBO stability.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Determine whether system y(t) = t * x(t) is linear, time-invariant, causal, and stable.', "marks": 7, "frequency": 'Repeated 6 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Convolution & Time-Domain Analysis',
                "syllabus": 'Impulse response, Continuous convolution integral, Discrete convolution sum, Properties of convolution, Step response, Interconnected LTI systems.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Compute convolution of x[n] = (0.5)^n * u[n] with h[n] = u[n] and plot output sequence.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Fourier Transform Analysis',
                "syllabus": "Continuous-Time Fourier Transform (CTFT), Properties: Duality, Time shifting, Frequency differentiation, Parseval's relation, Frequency response of LTI systems.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Find Fourier transform of rectangular pulse x(t) = 1 for |t| < T/2 and plot its sinc spectrum.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Laplace Transform in System Analysis',
                "syllabus": 'Laplace transform, Region of Convergence (ROC) properties, Inverse Laplace transform, Transfer function H(s), Pole-zero plots, Stability and causality.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Find transfer function and impulse response for differential equation y''(t) + 5y'(t) + 6y(t) = x'(t) + x(t).", "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Z-Transform & Discrete Frequency Response',
                "syllabus": 'Z-transform, ROC properties, Inverse Z-transform (Partial fractions, Residue), Discrete transfer function H(z), Stability analysis of discrete LTI systems.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Find inverse Z-transform of X(z) = z / (z - 1)(z - 2) for (a) |z| > 2, (b) 1 < |z| < 2, (c) |z| < 1.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
        ]
    },
    {
        "id": 'ect206-comp-micro',
        "code": 'ECT 206',
        "title": 'Computer Architecture & Microcontrollers',
        "credits": 4,
        "semester": 'Semester 4',
        "branch": 'Electronics & Communication Engineering',
        "branch_id": 'ece',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Computer Organization & Bus Structures',
                "syllabus": 'Functional units of a computer, Von Neumann architecture, Bus structures, Memory locations and addresses, Memory operations, Instructions and instruction sequencing.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Von Neumann architecture and memory addressing modes with register transfer notations.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Pipelining & Processing Unit',
                "syllabus": 'Fundamental concepts, Execution of a complete instruction, Multiple bus organization, Hardwired vs microprogrammed control, Pipelining hazards.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain pipeline hazards (structural, data, control hazards) and branch prediction mechanisms.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": '8051 Microcontroller Architecture',
                "syllabus": '8051 architecture, Memory organization, Special Function Registers, Port structure, Timers and counters, Serial interface, Interrupts.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain 8051 internal architecture with ALU, PC, DPTR, register banks, and PSW.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": '8051 Programming & Addressing Modes',
                "syllabus": 'Addressing modes of 8051, Instruction set: Data transfer, Arithmetic, Logical, Boolean, Branching instructions, Assembly programs.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Write an 8051 assembly program to generate square wave of 2 kHz frequency using Timer 0 in Mode 1.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'ARM Processor Architecture Basics',
                "syllabus": 'ARM design philosophy, RISC architecture, ARM Cortex-M architecture, Register set, Thumb-2 instruction set, Exception handling overview.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain ARM Cortex-M core registers and exception handling mechanism.', "marks": 10, "frequency": 'Repeated 7 times'},
                ]
            },
        ]
    },
    {
        "id": 'ect301-lic',
        "code": 'ECT 301',
        "title": 'Linear Integrated Circuits',
        "credits": 4,
        "semester": 'Semester 5',
        "branch": 'Electronics & Communication Engineering',
        "branch_id": 'ece',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Operational Amplifier Fundamentals',
                "syllabus": 'Differential amplifier, CMRR, Slew rate, Input offset voltage and current, Ideal and practical Op-Amp characteristics, Frequency compensation.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive expression for CMRR of differential amplifier. Explain high frequency compensation techniques.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Linear Applications of Op-Amp',
                "syllabus": 'Inverting and Non-inverting amplifiers, Summing amplifier, Instrumentation amplifier, Integrator, Differentiator, Log and antilog amplifiers.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive output voltage expression for three Op-Amp Instrumentation Amplifier and discuss CMRR advantages.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Non-Linear Applications & Comparators',
                "syllabus": 'Comparators, Schmitt trigger with hysteresis, Zero crossing detector, Peak detector, Precision rectifiers (Half-wave and Full-wave).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain inverting Schmitt trigger circuit. Derive expressions for Upper and Lower Threshold voltages (UTP and LTP).', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Active Filters & Waveform Generators',
                "syllabus": 'First and second-order low-pass and high-pass Butterworth filters, Astable and monostable multivibrators using Op-Amp, Triangular wave generator.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Design second-order Butterworth active lowpass filter with cut-off frequency 1 kHz and passband gain 2.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Timers, PLL & Voltage Regulators',
                "syllabus": 'IC 555 timer in astable and monostable modes, Phase Locked Loop (PLL IC 565), Lock range and Capture range, Voltage regulator IC 723.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain internal block diagram of IC 555 timer and derive frequency of oscillation in astable mode.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
        ]
    },
    {
        "id": 'ect303-dsp',
        "code": 'ECT 303',
        "title": 'Digital Signal Processing',
        "credits": 4,
        "semester": 'Semester 5',
        "branch": 'Electronics & Communication Engineering',
        "branch_id": 'ece',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Discrete Fourier Transform (DFT)',
                "syllabus": 'DFT definition, IDFT, Properties: Circular shift, Circular convolution, Linear convolution via DFT.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Compute 8-point DFT of x[n] = {1, 2, 2, 1, 0, 0, 0, 0} and explain circular shift property.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Fast Fourier Transform (FFT)',
                "syllabus": 'Radix-2 Decimation-in-Time (DIT) FFT, Decimation-in-Frequency (DIF) FFT, Butterfly operations, In-place computation, Computational complexity.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive Radix-2 DIT-FFT algorithm and draw complete 8-point butterfly signal flow graph.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'IIR Filter Design',
                "syllabus": 'Analog filter prototypes: Butterworth and Chebyshev, Bilinear Transformation, Impulse Invariant transformation, Frequency warping effect.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Design digital Butterworth lowpass filter with passband edge 0.2 pi, stopband edge 0.6 pi using Bilinear Transformation.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'FIR Filter Design',
                "syllabus": 'Linear phase conditions, Design of FIR filters using Windows (Rectangular, Hamming, Hanning, Blackman), Frequency sampling method.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Design linear phase FIR lowpass filter with cut-off frequency 0.5 rad/sample of length M = 7 using Hamming window.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Filter Structures & Finite Word Length Effects',
                "syllabus": 'Direct form I & II, Cascade, Parallel structures. Quantization errors, Limit cycle oscillations, Deadband effect.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Realize given second-order IIR system in Direct Form II and Cascade Form. Explain limit cycle oscillations.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'ect305-comms',
        "code": 'ECT 305',
        "title": 'Analog & Digital Communication',
        "credits": 4,
        "semester": 'Semester 5',
        "branch": 'Electronics & Communication Engineering',
        "branch_id": 'ece',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Continuous Wave Amplitude Modulation',
                "syllabus": 'AM fundamentals, DSB-SC, SSB-SC, VSB modulation, Envelop detectors, Costas loop, Superheterodyne AM receiver.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive expression for AM wave and explain envelope detection. Compare power and bandwidth of DSB-FC, DSB-SC, and SSB.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Angle Modulation & Demodulation',
                "syllabus": "Frequency Modulation (FM), Phase Modulation (PM), Carson's rule, Narrowband and Wideband FM, Armstrong indirect FM generation, Foster-Seeley discriminator.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Armstrong Indirect Method for FM generation with block diagram and frequency multipliers.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Pulse Modulation & Baseband Transmission',
                "syllabus": 'Sampling theorem, Aliasing, PAM, PWM, PPM, Pulse Code Modulation (PCM): Quantization noise, A-law and mu-law companding, Delta modulation.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain PCM transmission and reception. Derive expression for signal-to-quantization noise ratio (SQNR).', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Digital Bandpass Modulation Techniques',
                "syllabus": 'ASK, FSK, BPSK, QPSK, Constellation diagrams, Coherent detection of BPSK, Bit Error Rate (BER) comparisons.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain QPSK transmitter and receiver with constellation diagram and signal space analysis.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Spread Spectrum Systems',
                "syllabus": 'Pseudo-noise sequences, Direct Sequence Spread Spectrum (DSSS), Frequency Hopping Spread Spectrum (FHSS), Processing gain, Jamming margin.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Direct Sequence Spread Spectrum (DSSS) transmitter and receiver. Define processing gain.', "marks": 10, "frequency": 'Repeated 7 times'},
                ]
            },
        ]
    },
    {
        "id": 'ect302-emtl',
        "code": 'ECT 302',
        "title": 'Electromagnetics & Transmission Lines',
        "credits": 4,
        "semester": 'Semester 6',
        "branch": 'Electronics & Communication Engineering',
        "branch_id": 'ece',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Electrostatics & Magnetostatics',
                "syllabus": "Coulomb's law, Gauss's law, Divergence theorem, Biot-Savart law, Ampere's circuital law, Stokes' theorem, Magnetic boundary conditions.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "State and prove Gauss's Law in electrostatics. Derive continuity equation from Ampere's law.", "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": "Maxwell's Equations & Boundary Conditions",
                "syllabus": "Displacement current, Maxwell's equations in differential and integral forms, Electromagnetic boundary conditions at media interfaces.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Derive Maxwell's four equations in differential and phasor forms. Explain displacement current concept.", "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Electromagnetic Wave Propagation',
                "syllabus": 'Wave equation, Uniform plane waves in lossless and lossy media, Intrinsic impedance, Skin depth, Poynting vector and power flow.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'State and derive Poynting Theorem for electromagnetic energy flow in time-varying fields.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Transmission Line Equations',
                "syllabus": "Transmission line parameters, Telegrapher's equations, Characteristic impedance Z0, Propagation constant, Reflection coefficient, VSWR.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive transmission line equations and expressions for characteristic impedance Z0 and propagation constant gamma.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Smith Chart & Impedance Matching',
                "syllabus": 'Smith chart fundamentals, Reflection coefficient, Input impedance, Quarter-wave transformer, Single-stub matching.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain single-stub shunt impedance matching using Smith chart with an illustrative numerical problem.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'ect304-vlsi',
        "code": 'ECT 304',
        "title": 'VLSI Circuit Design',
        "credits": 4,
        "semester": 'Semester 6',
        "branch": 'Electronics & Communication Engineering',
        "branch_id": 'ece',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'MOS Transistor Physics & CMOS Inverter',
                "syllabus": 'MOS threshold voltage, I-V equations, Channel length modulation, Body effect, Static CMOS inverter: VTC characteristics, Noise margins, Propagation delays.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive switching threshold voltage V_th of static CMOS inverter and compute noise margins NM_H and NM_L.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Combinational CMOS Circuits',
                "syllabus": 'Static CMOS logic gates, Euler path for stick diagrams, Layout design rules (Lambda based), Dynamic CMOS logic: Pre-charge and evaluate, Domino logic.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Design CMOS complex logic gate for Y = !((A + B) * (C + D)). Draw Euler path and stick diagram.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Sequential Logic Circuits & Memory',
                "syllabus": 'Static latches and flip-flops, Transmission gate registers, Dynamic latches, SRAM 6T cell read/write operation, DRAM 1T cell refresh operation.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain 6T SRAM cell architecture. Detail read and write operational cycles with timing diagrams.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Data Path Subsystems',
                "syllabus": 'High-speed adders: Carry Lookahead, Carry Select, Carry Skip adders, Multipliers: Wallace Tree multiplier, Baugh-Wooley array multiplier, Barrel shifters.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Design 16-bit Carry Select Adder (CSA) and compare its propagation delay with Ripple Carry Adder.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'VLSI Testing & Design for Testability (DFT)',
                "syllabus": 'Fault models: Stuck-at-0 and Stuck-at-1 faults, D-algorithm for test generation, Scan-path architecture, Built-In Self-Test (BIST), Boundary Scan (JTAG).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Boundary Scan architecture (IEEE 1149.1) with TAP controller and instruction register.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'ect401-microwave',
        "code": 'ECT 401',
        "title": 'Microwave & Antenna Engineering',
        "credits": 4,
        "semester": 'Semester 7',
        "branch": 'Electronics & Communication Engineering',
        "branch_id": 'ece',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Microwave Waveguides & S-Parameters',
                "syllabus": 'Rectangular waveguides: TE and TM modes, Cut-off frequency, Wave impedance, S-parameters properties, Magic Tee, Directional couplers, Isolators.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive scattering matrix (S-matrix) of Magic Tee. Explain its application as a balanced duplexer.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Microwave Sources & Tubes',
                "syllabus": 'Two-cavity klystron amplifier, Velocity modulation, Reflex klystron oscillator, Magnetron, Gunn diode: Gunn effect, Ridley-Watkins-Hilsum theory.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain bunching process and velocity modulation in two-cavity klystron with Applegate diagram.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Antenna Fundamentals',
                "syllabus": 'Radiation mechanism, Current distribution on thin dipoles, Radiation patterns, Gain, Directivity, Radiation resistance, Friis transmission formula.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive radiation resistance and directivity of an oscillating half-wave dipole antenna (R_rad = 73 ohm).', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Wire & Aperture Antennas',
                "syllabus": 'Small loop antenna, Horn antennas: E-plane, H-plane sectoral horns, Parabolic reflector antennas: Cassegrain feed, Microstrip patch antenna design.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain working and feeding mechanisms of parabolic reflector antenna with aperture efficiency calculation.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Antenna Arrays & Wave Propagation',
                "syllabus": 'Two-element arrays, Uniform linear arrays: Broadside and End-fire arrays, Pattern multiplication, Ground wave, Sky wave, and Space wave propagation.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'State and explain principle of pattern multiplication. Find null directions for 4-element broadside array.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'ect403-wireless-comm',
        "code": 'ECT 403',
        "title": 'Wireless & Mobile Communication',
        "credits": 4,
        "semester": 'Semester 7',
        "branch": 'Electronics & Communication Engineering',
        "branch_id": 'ece',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Cellular Concept & System Design',
                "syllabus": 'Frequency reuse, Channel assignment strategies, Handoff strategies, Interference: Co-channel and Adjacent channel, Cell splitting, Sectoring.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain cellular frequency reuse concept. Derive expression for capacity improvement by cell splitting.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Mobile Radio Propagation & Fading',
                "syllabus": 'Free space propagation, Reflection, Diffraction, Scattering, Log-distance path loss model, Small-scale fading: Multipath, Doppler shift, Rayleigh and Rician distributions.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain small-scale multipath propagation mechanisms. Contrast Rayleigh and Rician fading distributions.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Multiple Access & Modulation Techniques',
                "syllabus": 'CDMA principles, PN sequences, Near-far problem, Orthogonal Frequency Division Multiplexing (OFDM), Cyclic prefix, PAPR reduction.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain OFDM transmitter and receiver architecture with cyclic prefix role in mitigating ISI.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Diversity, Equalization & MIMO',
                "syllabus": 'Equalization: Linear vs Decision feedback, Diversity: Space, Time, Frequency, Maximal Ratio Combining (MRC), MIMO systems: Spatial multiplexing, Beamforming.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain MIMO architecture. Differentiate between spatial multiplexing and space-time block coding (Alamouti scheme).', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": '4G LTE & 5G NR Standards',
                "syllabus": 'LTE architecture (E-UTRAN, EPC), 5G New Radio (NR) architecture, Massive MIMO, Millimeter-wave communication, Network Slicing, URLLC.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain 5G standalone architecture with Network Slicing and Service-Based Architecture (SBA).', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'ect402-opt-sat',
        "code": 'ECT 402',
        "title": 'Optical & Satellite Communication',
        "credits": 4,
        "semester": 'Semester 8',
        "branch": 'Electronics & Communication Engineering',
        "branch_id": 'ece',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Optical Fiber Transmission Principles',
                "syllabus": 'Ray theory, Numerical aperture, Acceptance angle, Single-mode and Multi-mode fibers, Attenuation mechanisms: Rayleigh scattering, Material absorption.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive expression for Numerical Aperture and acceptance angle of step-index optical fiber.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Dispersion & Optical Components',
                "syllabus": 'Intermodal dispersion, Intramodal dispersion (Material and Waveguide dispersion), Optical sources: Laser diode, Photodetectors: PIN and APD photodiodes.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Avalanche Photodiode (APD) operation, multiplication factor, and quantum efficiency.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Optical Link Design & WDM',
                "syllabus": 'Point-to-point link design, Power budget analysis, Rise-time budget, Wavelength Division Multiplexing (WDM) architecture, EDFA optical amplifiers.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Perform link power budget and rise-time budget analysis for a 50 km optical link operating at 2.5 Gbps.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Satellite Orbits & Mechanics',
                "syllabus": "Kepler's laws, Orbital elements, GEO, LEO, MEO orbits, Look angle determination: Azimuth and Elevation angles, Orbital perturbations.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "State Kepler's laws. Calculate look angles (azimuth and elevation) for a geostationary satellite from an earth station.", "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Satellite Subsystems & Link Budget',
                "syllabus": 'Spacecraft subsystems: TT&C, Power, Altitude control; Transponders, Earth station design, Satellite link budget: Carrier-to-Noise ratio (C/N), G/T ratio.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive satellite uplink and downlink budget equation for received Carrier-to-Noise ratio (C/N).', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'eet201-circuits',
        "code": 'EET 201',
        "title": 'Circuits & Networks',
        "credits": 4,
        "semester": 'Semester 3',
        "branch": 'Electrical & Electronics Engineering',
        "branch_id": 'eee',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Circuit Analysis Techniques',
                "syllabus": 'Mesh and Node analysis with dependent sources, Source transformations, Duality, Graph theory: Incidence matrix, Tie-set and cut-set matrices.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Find node voltages in a bridge circuit containing coupled inductors and dependent voltage sources.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Network Theorems',
                "syllabus": "Superposition, Thevenin's, Norton's, Maximum Power Transfer, Reciprocity, Millman's and Tellegen's theorems applied to AC and DC circuits.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'State and prove Maximum Power Transfer theorem for complex source and load impedances.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Transient Analysis',
                "syllabus": 'DC and sinusoidal response of RL, RC, and RLC series and parallel circuits using Laplace Transform, Initial and final conditions.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Find the transient capacitor voltage v_c(t) in an underdamped series RLC circuit excited by DC voltage V.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Two-Port Networks & Transformed Circuits',
                "syllabus": 'Z, Y, ABCD, h-parameters, Interrelationships, Condition for reciprocity and symmetry, Driving point and transfer impedances.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Determine Z-parameters of a symmetrical lattice network and verify condition for reciprocity.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Magnetic Circuits & 3-Phase Systems',
                "syllabus": 'Dot convention in coupled circuits, Coefficient of coupling, Series and parallel resonance, Unbalanced three-phase systems.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Write loop equations for magnetically coupled circuit using dot convention and calculate equivalent inductance.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'eet203-measurements',
        "code": 'EET 203',
        "title": 'Electrical Measurements & Instrumentation',
        "credits": 4,
        "semester": 'Semester 3',
        "branch": 'Electrical & Electronics Engineering',
        "branch_id": 'eee',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Indicating Instruments',
                "syllabus": 'Classification, Deflecting, controlling, and damping torques, PMMC instruments, Moving iron (Attraction and repulsion) instruments, Shunts and multipliers.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive torque equation of Moving Iron instrument. Explain why its scale is non-linear.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Measurement of Resistance & Bridges',
                "syllabus": "Measurement of low, medium, and high resistance: Kelvin's double bridge, Wheatstone bridge, Megger; AC bridges: Maxwell's, Hay's, Schering bridges.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Derive balance equation for Kelvin's Double Bridge for measurement of low resistance.", "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Power & Energy Measurement',
                "syllabus": 'Electrodynamometer wattmeter, Errors and compensation, Two-wattmeter method for balanced and unbalanced 3-phase power, Induction type energy meter.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Two-Wattmeter method for measuring 3-phase power. Derive expression for power factor in terms of wattmeter readings.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Instrument Transformers & Potentiometers',
                "syllabus": 'Current Transformers (CT), Potential Transformers (PT), Ratio and phase angle errors, DC potentiometers (Crompton potentiometer), AC potentiometers.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain working of Current Transformer (CT). Derive expressions for ratio and phase angle errors with phasor diagram.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Digital Instruments & Transducers',
                "syllabus": 'Digital voltmeters (Successive approximation, Dual slope), CRO, DSO, Transducers: LVDT, Strain gauges, Thermocouples, RTD.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain construction and working of Linear Variable Differential Transformer (LVDT) with characteristics.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'eet205-analog-elec',
        "code": 'EET 205',
        "title": 'Analog Electronics',
        "credits": 4,
        "semester": 'Semester 3',
        "branch": 'Electrical & Electronics Engineering',
        "branch_id": 'eee',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Diode Circuits & Power Supplies',
                "syllabus": 'Half wave, Full wave center tapped and bridge rectifiers with C, LC, and CLC filters, Ripple factor, Voltage regulation using Zener diode.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain working of full-wave bridge rectifier with capacitor filter and derive ripple factor expression.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Transistor Biasing & Small Signal Models',
                "syllabus": 'BJT biasing: Fixed bias, Collector to base bias, Self bias, Stability factors, Small signal h-parameter model for CE configuration.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Derive stability factors S, S', and S'' for voltage divider self-bias BJT circuit.", "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'FET & MOSFET Amplifiers',
                "syllabus": 'JFET construction, Drain and transfer characteristics, Pinch-off voltage, MOSFET: Depletion and Enhancement types, Small signal analysis of Common Source amplifier.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain drain and transfer characteristics of n-channel enhancement MOSFET. Derive transconductance g_m.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Feedback Amplifiers & Oscillators',
                "syllabus": 'Principle of negative feedback, Topologies: Voltage/Current Series/Shunt, Barkhausen criterion, RC phase shift oscillator, Hartley, Colpitts oscillators.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive expression for frequency of oscillation of Colpitts oscillator with BJT circuit.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Operational Amplifiers & Wave Shaping',
                "syllabus": 'Ideal Op-Amp characteristics, Inverting and non-inverting amplifiers, Summing amplifier, Differential amplifier, Schmitt trigger, Precision rectifiers.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain inverting Schmitt trigger using Op-Amp and derive expressions for threshold voltages V_UT and V_LT.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'eet202-dc-trans',
        "code": 'EET 202',
        "title": 'DC Machines & Transformers',
        "credits": 4,
        "semester": 'Semester 4',
        "branch": 'Electrical & Electronics Engineering',
        "branch_id": 'eee',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'DC Generators',
                "syllabus": 'Armature windings, EMF equation, Armature reaction, Demagnetizing and cross-magnetizing ampere-turns, Commutation, Characteristics of DC generators.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain armature reaction in DC generator. How are cross-magnetizing and demagnetizing effects mitigated using interpoles and compensating windings?', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 2,
                "title": 'DC Motors',
                "syllabus": 'Working principle, Back EMF, Torque equation, Motor characteristics, Starters: 3-point and 4-point starters, Speed control: Armature resistance and Field flux control, Ward-Leonard system.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Draw neat schematic of 3-point starter for DC shunt motor and explain functions of No-Volt Coil (NVC) and Overload Release (OLR).', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Testing of DC Machines',
                "syllabus": "Losses in DC machines, Efficiency calculation, Swinburne's test, Hopkinson's regenerative test, Field's test, Retardation test.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Explain Hopkinson's regenerative test for finding efficiency of two identical DC shunt machines.", "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Single-Phase Transformers',
                "syllabus": 'Core and Shell types, EMF equation, Equivalent circuit, Phasor diagrams on no-load and full load (lagging/leading pf), Voltage regulation, Maximum efficiency condition.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive condition for maximum efficiency of single-phase transformer. Draw its complete exact equivalent circuit.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Testing & Polyphase Transformers',
                "syllabus": "Open circuit (OC) and short circuit (SC) tests, Sumpner's back-to-back test, All-day efficiency, Auto-transformers, 3-phase transformer connections (Star-Star, Delta-Delta, Scott connection).",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Scott connection of two single-phase transformers for 3-phase to 2-phase conversion with phasor diagrams.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'eet204-emft',
        "code": 'EET 204',
        "title": 'Electromagnetic Field Theory',
        "credits": 4,
        "semester": 'Semester 4',
        "branch": 'Electrical & Electronics Engineering',
        "branch_id": 'eee',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Vector Analysis & Electrostatic Fields',
                "syllabus": "Coordinate systems (Cartesian, Cylindrical, Spherical), Coulomb's law, Electric field intensity, Gauss's law and applications, Divergence theorem, Electric potential.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "State and prove Gauss's Law in electrostatics. Apply it to find electric field due to an infinite line charge.", "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Conductors, Dielectrics & Capacitance',
                "syllabus": "Current density, Continuity equation, Polarization in dielectrics, Boundary conditions at dielectric interfaces, Poisson's and Laplace's equations, Capacitance of coaxial cable.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive boundary conditions for electric flux density D and field E across dielectric interface.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Magnetostatic Fields',
                "syllabus": "Biot-Savart's law, Ampere's circuital law and applications, Magnetic flux density, Vector magnetic potential, Stokes' theorem, Force on moving charge in magnetic field.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Derive expression for magnetic flux density B on the axis of a circular current loop using Biot-Savart's law.", "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Magnetic Forces, Materials & Inductance',
                "syllabus": 'Magnetic force on differential current element, Magnetization in materials, Boundary conditions for magnetic fields, Self and mutual inductances.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive expression for self-inductance of a toroid with rectangular cross-section.', "marks": 10, "frequency": 'Repeated 7 times'},
                ]
            },
            {
                "module_no": 5,
                "title": "Time-Varying Fields & Maxwell's Equations",
                "syllabus": "Faraday's law, Transformer and motional EMF, Displacement current density, Maxwell's equations in differential and integral forms, Poynting vector and theorem.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Derive Maxwell's equations in differential form from fundamental laws. Explain displacement current concept.", "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
        ]
    },
    {
        "id": 'eet301-power',
        "code": 'EET 301',
        "title": 'Power Systems I',
        "credits": 4,
        "semester": 'Semester 5',
        "branch": 'Electrical & Electronics Engineering',
        "branch_id": 'eee',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Transmission Line Parameters',
                "syllabus": 'Resistance, Inductance of single-phase and 3-phase lines with symmetrical and unsymmetrical spacing, Transposition, GMD and GMR, Capacitance calculations.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive expression for loop inductance of a 3-phase transposed overhead transmission line with unsymmetrical spacing.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Line Performance & Modeling',
                "syllabus": 'Short, medium (Nominal T and Pi), and long transmission lines (Rigorous solution), ABCD parameters, Ferranti effect, Surge Impedance Loading (SIL).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive ABCD constants for Nominal-Pi model of medium transmission line. Explain Ferranti effect.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Mechanical Design of Overhead Lines',
                "syllabus": 'Line supports, Conductor types (ACSR), Calculation of sag and tension with equal and unequal supports, Effect of wind and ice loading.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive sag formula for transmission line conductors supported between towers at unequal levels.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Insulators & Corona',
                "syllabus": 'Pin, Suspension, Strain insulators, Potential distribution over suspension insulator string, String efficiency, Methods of improving string efficiency (Guard ring), Corona.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Define string efficiency. Derive expression for voltage distribution in a 3-unit suspension insulator string.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Underground Cables & Distribution',
                "syllabus": 'Classification, Insulation resistance, Capacitance of single-core and 3-core belted cables, Grading of cables (Capacitance and Intersheath grading), Distribution systems.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Capacitance Grading of underground cables with mathematical derivations and stress distribution curves.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'eet303-ac-machines',
        "code": 'EET 303',
        "title": 'Induction Machines & Synchronous Machines',
        "credits": 4,
        "semester": 'Semester 5',
        "branch": 'Electrical & Electronics Engineering',
        "branch_id": 'eee',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": '3-Phase Induction Motors Fundamentals',
                "syllabus": 'Production of rotating magnetic field, Principle of operation, Slip, Torque equation, Torque-slip characteristics, Condition for maximum torque, Equivalent circuit.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive expression for torque developed by 3-phase induction motor and deduce condition for maximum starting torque.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Testing & Speed Control of Induction Motors',
                "syllabus": 'No-load and Blocked-rotor tests, Circle diagram, Starters (DOL, Star-Delta, Auto-transformer), Speed control: V/f control, Pole changing, Slip power recovery.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain circle diagram construction from no-load and blocked rotor test data to determine efficiency and power factor.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Single Phase Induction & Special Motors',
                "syllabus": 'Double field revolving theory, Starting methods: Split phase, Capacitor start/run, Shaded pole motors, Universal motor, Stepper motor.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Double Field Revolving Theory for single-phase induction motors with torque-speed curves.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Synchronous Alternators',
                "syllabus": 'Construction: Salient pole and cylindrical rotor, Armature winding factors (Pitch and distribution factors), EMF equation, Armature reaction, Voltage regulation: EMF, MMF, Potier methods.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Potier Reactance Method (Zero Power Factor Method) for voltage regulation of alternator with phasor diagram.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Synchronous Motors & Parallel Operation',
                "syllabus": 'Principle of operation, Methods of starting, V and Inverted V curves, Synchronous condenser, Parallel operation of alternators, Synchronizing power.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain V and Inverted-V curves of synchronous motor and its application as synchronous condenser for power factor correction.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'eet307-control',
        "code": 'EET 307',
        "title": 'Linear Control Systems',
        "credits": 4,
        "semester": 'Semester 5',
        "branch": 'Electrical & Electronics Engineering',
        "branch_id": 'eee',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'System Modeling & Transfer Functions',
                "syllabus": "Open-loop vs Closed-loop, Transfer function of physical systems (Electrical, Mechanical), Block diagram reduction, Mason's gain formula.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Find overall transfer function C(s)/R(s) of given multiple-feedback system using Mason's Gain Formula.", "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Time Domain Response',
                "syllabus": 'Standard test signals, Transient response of first and second order systems, Specifications: Rise time, Peak time, Peak overshoot, Settling time, Steady state error constants.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive expressions for Peak Time (t_p) and Maximum Percentage Overshoot (M_p) of second-order underdamped system.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Stability & Routh-Hurwitz Criterion',
                "syllabus": 'Concept of stability, BIBO stability, Routh-Hurwitz stability criterion, Special cases (Zero row, First column zero), Relative stability.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Determine stability and find range of K for system with characteristic equation s^4 + 6s^3 + 11s^2 + 6s + K = 0 using Routh array.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Root Locus Technique',
                "syllabus": 'Root locus concept, Rules for construction: Angle of asymptotes, Centroid, Breakaway and break-in points, Angles of departure and arrival.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Sketch complete root locus for unity feedback system with G(s) = K / [s(s + 2)(s^2 + 6s + 25)].', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Frequency Response Analysis',
                "syllabus": 'Bode plot: Gain margin and Phase margin, Nyquist stability criterion, Polar plots, Introduction to Lead, Lag, and Lag-Lead compensators.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Draw Bode plot for open-loop transfer function G(s)H(s) = 200 / [s(s + 2)(s + 10)] and determine Gain Margin and Phase Margin.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
        ]
    },
    {
        "id": 'eet302-power2',
        "code": 'EET 302',
        "title": 'Power Systems II',
        "credits": 4,
        "semester": 'Semester 6',
        "branch": 'Electrical & Electronics Engineering',
        "branch_id": 'eee',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Power System Modeling & Y-Bus',
                "syllabus": 'Per-unit system, Single-line diagram, Primitive network, Bus admittance matrix (Y_bus) formation by inspection and singular transformation.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Form Bus Admittance Matrix (Y_bus) for given 4-bus power system network by direct inspection.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Load Flow Studies',
                "syllabus": 'Classification of buses, Gauss-Seidel method, Newton-Raphson method in polar coordinates, Fast Decoupled load flow method.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Newton-Raphson load flow algorithm with Jacobian matrix structure in polar form.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Symmetrical & Unsymmetrical Fault Analysis',
                "syllabus": 'Symmetrical 3-phase fault, Symmetrical components (Positive, Negative, Zero sequence), Analysis of Single Line-to-Ground (LG), Line-to-Line (LL), and Double Line-to-Ground (LLG) faults.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive fault current expression for Single Line to Ground (LG) fault through impedance Z_f with sequence network interconnection.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Power System Stability',
                "syllabus": 'Steady-state and transient stability, Swing equation, Power angle curve, Equal Area Criterion, Critical clearing angle and critical clearing time.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive swing equation of a synchronous generator connected to infinite bus. State Equal Area Criterion.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Protection Schemes & Circuit Breakers',
                "syllabus": 'Overcurrent relays, Distance relays (Impedance, Mho), Differential protection of transformers and generators, Circuit breakers: Arc quenching principles, SF6 and Vacuum circuit breakers.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain percentage biased differential protection scheme for power transformer against internal faults.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'eet304-power-elec',
        "code": 'EET 304',
        "title": 'Power Electronics & Drives',
        "credits": 4,
        "semester": 'Semester 6',
        "branch": 'Electrical & Electronics Engineering',
        "branch_id": 'eee',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Power Semiconductor Devices',
                "syllabus": 'SCR, MOSFET, IGBT, Static and switching characteristics, Two-transistor analogy of SCR, Turn-on methods, dv/dt and di/dt protections.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain two-transistor analogy of SCR and derive expression for anode current. Detail snubber circuit operation.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Controlled Rectifiers',
                "syllabus": 'Single-phase half-wave, full-wave center-tapped, and bridge converters with R, RL, and RLE loads, Discontinuous and continuous conduction modes, Three-phase full converters.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain working of single-phase fully controlled bridge rectifier with RL load and continuous current. Derive average DC output voltage.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'DC-DC Converters (Choppers)',
                "syllabus": 'Step-down (Buck) chopper, Step-up (Boost) chopper, Buck-Boost converter, Continuous conduction mode equations, Voltage and current ripple calculations.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive expression for output voltage of Buck-Boost converter and draw inductor voltage and current waveforms.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Inverters & PWM',
                "syllabus": 'Single-phase half and full-bridge inverters, Three-phase voltage source inverters (180 and 120-degree conduction modes), Sinusoidal PWM (SPWM).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain 180-degree conduction mode of 3-phase Voltage Source Inverter with switching sequence and line-to-line voltage waveforms.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'AC Voltage Controllers & Drives',
                "syllabus": 'Single-phase AC voltage controllers with R and RL loads, Cycloconverters, DC drive speed control, V/f control of induction motor drives.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain V/f speed control of 3-phase induction motor fed from PWM inverter maintaining airgap flux constant.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'eet401-adv-control',
        "code": 'EET 401',
        "title": 'Advanced Control Systems',
        "credits": 4,
        "semester": 'Semester 7',
        "branch": 'Electrical & Electronics Engineering',
        "branch_id": 'eee',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'State Space Representation',
                "syllabus": 'State variable concepts, State vector, State space modeling of physical systems, Conversion from transfer function to state space (Phase variable, Canonical forms).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive state space representation for given differential equation in Controllable and Observable Canonical Forms.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'State Transition Matrix & Solutions',
                "syllabus": 'State transition matrix (STM) properties, Computation of STM using Laplace transform and Cayley-Hamilton theorem, Solution of homogeneous and non-homogeneous state equations.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Compute State Transition Matrix e^{At} for matrix A = [[0, 1], [-2, -3]] using Cayley-Hamilton theorem.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Controllability & Observability',
                "syllabus": "Concepts of controllability and observability, Kalman's test, Gilbert's test, Duality principle, State feedback controller design, Pole placement by Ackermann's formula.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Design state feedback gain matrix K using Ackermann's formula to place closed-loop poles at s = -1, -2.", "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'State Observers & Non-Linearities',
                "syllabus": 'Full-order state observers, Inherent non-linearities: Saturation, Dead zone, Backlash, Friction, Phase plane method: Singular points, Limit cycles.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Phase Plane method for non-linear control analysis. Classify singular points (Node, Saddle, Focus, Center).', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Describing Function & Lyapunov Stability',
                "syllabus": 'Describing function definition, Describing function for saturation and dead zone, Lyapunov stability analysis, Lyapunov direct method.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Determine stability of non-linear system using Lyapunov Direct Method with scalar energy function V(x).', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'eet403-ev-storage',
        "code": 'EET 403',
        "title": 'Electric Vehicles & Energy Storage',
        "credits": 4,
        "semester": 'Semester 7',
        "branch": 'Electrical & Electronics Engineering',
        "branch_id": 'eee',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Electric Vehicle Architecture',
                "syllabus": 'Historical perspective, EV configurations (BEV, HEV, PHEV, FCEV), Vehicle dynamics: Tractive effort, Rolling resistance, Aerodynamic drag, Acceleration force.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive equation for total tractive effort required by an EV cruising at constant velocity on an inclined road.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Electric Motors for Propulsion',
                "syllabus": 'Permanent Magnet Synchronous Motor (PMSM), Brushless DC Motor (BLDC), Switched Reluctance Motor (SRM), Induction Motors for EVs, Torque-speed characteristics.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Compare PMSM, BLDC, and Induction Motors for EV powertrain applications in terms of efficiency, weight, and speed control.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Energy Storage Technologies',
                "syllabus": 'Battery chemistry: Lead-acid, Lithium-ion (NMC, LFP), Solid-state batteries, Supercapacitors, Fuel cells, Ragone plot, State of Charge (SOC) estimation.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain operation of Lithium Iron Phosphate (LiFePO4) battery and discuss Coulomb Counting method for SOC estimation.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Battery Management Systems (BMS)',
                "syllabus": 'BMS architecture, Cell monitoring, Active and passive cell balancing circuits, Thermal management, Thermal runaway protection, CAN bus communication.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain active and passive cell balancing circuits in BMS and discuss thermal runaway prevention mechanisms.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'EV Charging & Grid Integration',
                "syllabus": 'AC charging (Level 1, 2), DC fast charging (Level 3), Wireless charging, Vehicle-to-Grid (V2G) power flow, Impact on electrical distribution grid.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Vehicle-to-Grid (V2G) technology and its benefits for peak shaving and grid frequency regulation.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'eet402-smart-grid',
        "code": 'EET 402',
        "title": 'Smart Grid & High Voltage Engineering',
        "credits": 4,
        "semester": 'Semester 8',
        "branch": 'Electrical & Electronics Engineering',
        "branch_id": 'eee',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Smart Grid Architecture & AMI',
                "syllabus": 'Smart grid definition, Differences between conventional and smart grid, Advanced Metering Infrastructure (AMI), Smart meters, Home Energy Management Systems (HEMS).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Compare conventional grid and smart grid architecture. Detail components of Advanced Metering Infrastructure (AMI).', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Wide Area Measurement & Microgrids',
                "syllabus": 'Phasor Measurement Units (PMU), Synchrophasors, Wide Area Monitoring Systems (WAMS), Microgrids: AC, DC, and Hybrid microgrids, Islanding detection.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain principle and working of Phasor Measurement Unit (PMU) and its role in Wide Area Monitoring Systems.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Breakdown in Insulating Media',
                "syllabus": "Townsend's breakdown criterion, Paschen's law, Streamer mechanism in gases, Breakdown in liquids: Cavitation theory, Breakdown in solid dielectrics.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "State and prove Paschen's Law for breakdown voltage in gases. Discuss factors influencing breakdown.", "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Generation of High Voltages',
                "syllabus": 'High voltage AC: Cascaded transformers, Resonant transformers; High voltage DC: Cockcroft-Walton voltage multiplier; Impulse voltage: Multistage Marx generator.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain operation of multistage Marx Generator circuit for generating standard lightning impulse voltage wave.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'High Voltage Testing & Protection',
                "syllabus": 'Testing of insulators, bushings, and cables, Non-destructive testing: Partial discharge measurement, Lightning surges, Surge arresters (Metal oxide varistors).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain partial discharge detection in high voltage cables and working of ZnO gapless surge arrester.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'met201-mechanics-solids',
        "code": 'MET 201',
        "title": 'Mechanics of Solids',
        "credits": 4,
        "semester": 'Semester 3',
        "branch": 'Mechanical Engineering',
        "branch_id": 'mech',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Stress, Strain & Elastic Constants',
                "syllabus": "Normal and shear stresses, Hooke's law, Stress-strain diagram for ductile and brittle materials, Poisson's ratio, Elastic constants E, G, K, Thermal stresses in composite bars.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Derive relationship between Young's Modulus (E), Modulus of Rigidity (G), and Bulk Modulus (K).", "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 2,
                "title": "Principal Stresses & Mohr's Circle",
                "syllabus": "Stresses on inclined planes, Principal stresses and principal planes, Mohr's circle for plane stress, Theories of failure: Maximum Principal Stress, Maximum Shear Stress, Distortion Energy theory.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'State Von Mises (Distortion Energy) and Tresca (Maximum Shear Stress) theories of failure with graphical representations.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Shear Force & Bending Moment in Beams',
                "syllabus": 'Types of beams and loadings, Shear force and bending moment diagrams for Cantilever, Simply Supported, and Overhanging beams with point loads, UDL, and UVL, Point of contraflexure.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Draw SFD and BMD for simply supported beam of span 6m carrying UDL of 4 kN/m over left half and point load of 10 kN at 4m from left support.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Stresses in Beams & Torsion',
                "syllabus": 'Pure bending theory, Flexure formula (M/I = sigma/y = E/R), Section modulus, Shear stress distribution across I, T, and rectangular sections, Torsion of circular solid and hollow shafts.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive torsion equation T/J = tau/r = G*theta/L for circular shaft and compare torque transmitting capacity of solid vs hollow shafts.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Deflection of Beams & Thin Cylinders',
                "syllabus": "Differential equation of elastic curve, Macaulay's method for beam deflection, Moment-area theorems, Thin cylinders and spheres: Hoop stress, Longitudinal stress, Volumetric strain.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Determine slope at supports and maximum deflection for simply supported beam carrying central point load using Macaulay's method.", "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'met203-thermo',
        "code": 'MET 203',
        "title": 'Engineering Thermodynamics',
        "credits": 4,
        "semester": 'Semester 3',
        "branch": 'Mechanical Engineering',
        "branch_id": 'mech',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'First Law & Energy Conservation',
                "syllabus": 'Macroscopic vs Microscopic view, Thermodynamic equilibrium, Quasi-static process, First Law applied to non-flow and steady flow processes, SFEE.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive Steady Flow Energy Equation (SFEE) and apply it to steam nozzles and gas turbines.', "marks": 10, "frequency": 'Repeated 8 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Second Law & Entropy',
                "syllabus": 'Kelvin-Planck and Clausius statements, Carnot cycle, Carnot theorem, Clausius inequality, Definition and physical concept of Entropy, Principle of increase of entropy.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'State and prove Clausius Inequality. Deduce that entropy of the universe is continually increasing.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Availability & Pure Substances',
                "syllabus": 'Exergy, Availability, Irreversibility, Gouy-Stodola theorem. Pure substances: p-v-T surfaces, Mollier diagram, Quality of steam, Steam calorimeters.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain dryness fraction measurement of steam using Throttling and Separating Calorimeter.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Thermodynamic Relations & Gas Mixtures',
                "syllabus": "Maxwell's relations, T-ds equations, Joule-Thomson coefficient, Inversion curve, Dalton's law of partial pressures, Amagat's law.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Derive Maxwell's four thermodynamic relations from fundamental property relations.", "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Air Standard Power Cycles',
                "syllabus": 'Otto cycle, Diesel cycle, Dual combustion cycle, Brayton cycle, Thermal efficiency expressions, Mean effective pressure (MEP), Comparison of cycles.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive expression for air standard efficiency and mean effective pressure (MEP) of Diesel cycle.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
        ]
    },
    {
        "id": 'met205-materials',
        "code": 'MET 205',
        "title": 'Metallurgy & Material Science',
        "credits": 4,
        "semester": 'Semester 3',
        "branch": 'Mechanical Engineering',
        "branch_id": 'mech',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Crystallography & Crystal Imperfections',
                "syllabus": "Crystal structures (BCC, FCC, HCP), Miller indices, Point defects, Line defects: Edge and Screw dislocations, Burger's vector, Surface and volume defects.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Calculate atomic packing factor (APF) for BCC and FCC crystal structures. Explain Edge and Screw dislocations with Burger's vector.", "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Phase Diagrams & Solidification',
                "syllabus": 'Gibbs phase rule, Hume-Rothery rules for solid solution, Lever rule, Binary isomorphous and eutectic phase systems, Invariant reactions: Eutectic, Peritectic, Eutectoid.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'State and apply Lever Rule to calculate phase fractions in a binary eutectic phase diagram.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Iron-Carbon Equilibrium Diagram',
                "syllabus": 'Fe-Fe3C equilibrium phase diagram, Microstructures: Ferrite, Austenite, Cementite, Pearlite, Ledeburite, Invariant reactions in Fe-C system, Critical temperatures.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Draw neat Iron-Carbon (Fe-Fe3C) equilibrium diagram labeling all phases, temperatures, and invariant reactions (Peritectic, Eutectic, Eutectoid).', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Heat Treatment of Steels',
                "syllabus": 'TTT and CCT diagrams, Annealing (Full, Process, Spheroidizing), Normalizing, Hardening, Tempering, Austempering, Martempering, Surface hardening: Carburizing, Nitriding.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Draw Time-Temperature-Transformation (TTT) diagram for eutectoid steel and explain Austempering and Martempering processes.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Engineering Alloys & Mechanical Testing',
                "syllabus": 'Cast irons (Gray, White, Spheroidal, Malleable), Alloy steels, Non-ferrous alloys: Brasses, Bronzes, Aluminum alloys, Tensile test, Charpy impact test, Hardness testing (Brinell, Rockwell).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Differentiate between Gray cast iron and Spheroidal graphite cast iron in terms of microstructure, properties, and applications.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'met202-fluid',
        "code": 'MET 202',
        "title": 'Fluid Mechanics & Machinery',
        "credits": 4,
        "semester": 'Semester 4',
        "branch": 'Mechanical Engineering',
        "branch_id": 'mech',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Fluid Statics & Buoyancy',
                "syllabus": 'Fluid properties, Viscosity, Hydrostatic law, Pressure measurement: Manometers, Total pressure and Center of pressure on submerged surfaces, Buoyancy and Metacenter.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive expression for total hydrostatic force and depth of center of pressure for vertically submerged plane surface.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": "Fluid Kinematics & Bernoulli's Equation",
                "syllabus": "Continuity equation in 3D Cartesian coordinates, Stream function and Velocity potential function, Euler's equation of motion, Bernoulli's equation and applications (Venturimeter, Pitot tube).",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Derive Bernoulli's equation from Euler's equation of motion along a streamline. State assumptions made.", "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Flow Through Pipes & Losses',
                "syllabus": 'Laminar and turbulent flow, Hagen-Poiseuille equation for viscous flow through circular pipes, Darcy-Weisbach equation for friction loss, Hydraulic gradient line (HGL) and Total energy line (TEL).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive Hagen-Poiseuille equation for laminar flow through circular pipe. Prove maximum velocity is twice mean velocity.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Hydraulic Turbines',
                "syllabus": 'Impact of jets on vanes, Pelton wheel: Velocity triangles, Work done, Hydraulic efficiency, Francis turbine, Kaplan turbine, Specific speed, Unit quantities, Cavitation in turbines.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Draw velocity triangles for Pelton wheel bucket. Derive formula for hydraulic efficiency and maximum efficiency condition.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Hydraulic Pumps',
                "syllabus": 'Centrifugal pumps: Working principle, Impeller types, Manometric head, Manometric efficiency, Priming, Minimum starting speed, Net Positive Suction Head (NPSH), Reciprocating pumps: Air vessels.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain working of centrifugal pump with neat sketch. Derive expression for minimum starting speed of centrifugal pump.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'met204-manufacturing',
        "code": 'MET 204',
        "title": 'Manufacturing Processes',
        "credits": 4,
        "semester": 'Semester 4',
        "branch": 'Mechanical Engineering',
        "branch_id": 'mech',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Metal Casting & Gating Design',
                "syllabus": "Pattern materials and allowances, Molding sand properties, Cores, Gating and risering systems, Solidification of metals (Chvorinov's rule), Special casting: Die, Centrifugal, Investment casting.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Explain gating system components (Sprue, Runner, Ingate, Riser). State and apply Chvorinov's Rule for solidification time.", "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Fusion & Solid-State Welding',
                "syllabus": 'Arc welding: SMAW, TIG, MIG; Oxy-acetylene welding, Resistance welding: Spot and seam; Friction welding, Heat Affected Zone (HAZ), Welding defects.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain TIG and MIG welding processes with schematics. Compare shielding gases and electrode consumptions.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Metal Forming Processes',
                "syllabus": 'Hot and cold working, Rolling: Rolling mills, Angle of bite, Forging: Open die, Closed die, Flash, Extrusion: Forward and backward, Wire drawing.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain rolling process mechanics and derive expression for maximum reduction in pass (delta_h = mu^2 * R).', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Sheet Metal Working',
                "syllabus": 'Press working tools: Punch and die, Shearing operations: Blanking, Piercing, Clearance calculation, Bending: Springback, Deep drawing: Drawing ratio.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Differentiate between blanking and piercing operations with neat sketches. Calculate punch and die sizes with clearance.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Plastics Processing & Powder Metallurgy',
                "syllabus": 'Injection molding, Blow molding, Extrusion molding of polymers, Powder metallurgy: Production of metal powders, Compacting, Sintering operations.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain screw injection molding process for thermoplastics with cycle time stages and tooling sketch.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'met206-machine-tools',
        "code": 'MET 206',
        "title": 'Machine Tools & Metrology',
        "credits": 4,
        "semester": 'Semester 4',
        "branch": 'Mechanical Engineering',
        "branch_id": 'mech',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Mechanics of Metal Cutting',
                "syllabus": "Orthogonal vs oblique cutting, Chip formation types, Merchant's force circle, Cutting tool geometry (ASA and ORS systems), Taylor's tool life equation.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Draw Merchant's Circle Diagram of forces in orthogonal cutting and derive expressions for shear force and friction force.", "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Lathe, Shaper & Milling Machines',
                "syllabus": 'Center lathe operations: Taper turning, Thread cutting; Shaper: Whitworth quick return mechanism; Milling: Up vs Down milling, Simple and differential indexing.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain differential indexing on milling machine. Calculate index crank movement for cutting gear with 73 teeth.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Drilling, Boring & Grinding',
                "syllabus": 'Drilling machines, Twist drill geometry, Boring machines, Grinding wheels: Abrasives, Grain size, Grade, Structure, Bonds, Dressing and truing.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain grinding wheel specification code (e.g., 51 A 46 H 5 V 8) and differentiate between dressing and truing.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Linear, Angular & Surface Metrology',
                "syllabus": 'Slip gauges, Comparators (Mechanical, Pneumatic), Sine bar for angle measurement, Surface roughness parameters: Ra, Rz, Profilometers.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain measurement of taper angle using sine bar and slip gauges with derivations and limitation precautions.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Limits, Fits, Tolerances & CMM',
                "syllabus": "System of limits and fits (Hole basis and Shaft basis per IS 919), Taylor's principle for limit gauge design (GO and NO-GO gauges), Coordinate Measuring Machines (CMM).",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "State Taylor's Principle of limit gauge design. Design progressive plug gauge for hole of 25 H7.", "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
        ]
    },
    {
        "id": 'met301-mechanics-machinery',
        "code": 'MET 301',
        "title": 'Mechanics of Machinery',
        "credits": 4,
        "semester": 'Semester 5',
        "branch": 'Mechanical Engineering',
        "branch_id": 'mech',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Kinematic Chains & Inversions',
                "syllabus": "Degrees of freedom, Kutzbach and Grubler's criteria, Kinematic inversions of four-bar chain and single slider-crank chain, Quick return motion mechanisms.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain inversions of four-bar mechanism and slider-crank chain with neat diagrams and engineering applications.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Velocity & Acceleration Analysis',
                "syllabus": "Instantaneous center method, Kennedy's theorem, Relative velocity method, Acceleration diagrams for mechanisms, Coriolis acceleration component.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Coriolis component of acceleration. Derive its magnitude a_c = 2 * omega * v and discuss direction rules.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Cams & Follower Dynamics',
                "syllabus": 'Types of cams and followers, Displacement, velocity, and acceleration diagrams for Uniform velocity, SHM, and Cycloidal motions, Cam profile synthesis.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Draw cam profile for knife-edge follower with stroke 40mm, outstroke with SHM, dwell, and return with uniform acceleration.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Gears & Epicyclic Gear Trains',
                "syllabus": 'Law of gearing, Involute and Cycloidal profiles, Interference and undercutting, Minimum number of teeth on pinion, Epicyclic gear trains: Tabular and algebraic methods.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive expression for minimum number of teeth on pinion to avoid interference with a standard gear wheel.', "marks": 10, "frequency": 'Repeated 8 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Governors & Gyroscopes',
                "syllabus": 'Centrifugal governors: Watt, Porter, Proell, Hartnell governors, Sensitiveness, Hunting, Stability, Gyroscopic couple on aeroplanes, naval ships, and four-wheeled automobiles.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain gyroscopic effect on a naval ship during steering, pitching, and rolling with direction of gyroscopic couple.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
        ]
    },
    {
        "id": 'met303-thermal',
        "code": 'MET 303',
        "title": 'Thermal Engineering & IC Engines',
        "credits": 4,
        "semester": 'Semester 5',
        "branch": 'Mechanical Engineering',
        "branch_id": 'mech',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Steam Power Cycles & Boilers',
                "syllabus": 'Rankine cycle with reheat and regeneration, High pressure water tube boilers (Benson, Lamont), Boiler mountings and accessories, Equivalent evaporation, Boiler efficiency.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain reheat Rankine cycle with T-s and h-s diagrams. Derive expression for thermal efficiency.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Steam Nozzles & Turbines',
                "syllabus": 'Flow through steam nozzles, Critical pressure ratio, Nozzle efficiency, Compounding of impulse steam turbines (Velocity and Pressure compounding), Reaction turbines, Stage efficiency.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive expression for critical pressure ratio for maximum discharge through steam nozzle for superheated steam.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Combustion in SI & CI Engines',
                "syllabus": 'Combustion stages in SI engines, Flame propagation, Detonation and knocking, Octane rating, Combustion stages in CI engines, Ignition delay, Diesel knock, Cetane rating.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain stages of combustion in CI engine with p-theta diagram. Contrast knocking phenomenon in SI vs CI engines.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Engine Performance & Heat Balance',
                "syllabus": 'Measurement of indicated and brake power (Dynamometers), Morse test for multi-cylinder engines, Volumetric efficiency, Heat balance sheet preparation.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Morse Test for determining indicated power of multi-cylinder petrol engine with mathematical procedure.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Gas Turbines & Jet Propulsion',
                "syllabus": 'Open and closed cycle gas turbines, Brayton cycle with reheat, intercooling and regeneration, Turbojet, Turboprop, and Rocket engines.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Brayton cycle with intercooling, reheating, and regeneration. Draw T-s diagram and explain efficiency gains.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'met302-hmt',
        "code": 'MET 302',
        "title": 'Heat & Mass Transfer',
        "credits": 4,
        "semester": 'Semester 6',
        "branch": 'Mechanical Engineering',
        "branch_id": 'mech',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Conduction Heat Transfer',
                "syllabus": "Fourier's law of heat conduction, General heat conduction equation in Cartesian and Cylindrical coordinates, Critical thickness of insulation, Extended surfaces (Fins).",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive expression for temperature distribution and heat dissipation in a pin fin with insulated tip.', "marks": 10, "frequency": 'Repeated 8 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Transient Conduction & Convection Basics',
                "syllabus": 'Lumped system analysis, Biot and Fourier numbers, Boundary layer concept in convection, Dimensional analysis: Buckingham Pi theorem, Nusselt, Prandtl, Reynolds numbers.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive criteria for lumped capacitance analysis (Bi < 0.1) and temperature response equation.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Forced & Natural Convection',
                "syllabus": 'Flow over flat plates and cylinders, Empirical correlations for laminar and turbulent flows, Natural convection over vertical and horizontal plates, Grashof number.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain significance of Reynolds, Prandtl, Nusselt, and Grashof numbers in convective heat transfer.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Radiation Heat Transfer',
                "syllabus": "Blackbody radiation laws: Planck's law, Wien's displacement law, Stefan-Boltzmann law, Radiation shape factors, Radiosity and irradiation, Radiation shields.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive expression for heat exchange between two infinite parallel gray planes with and without radiation shield.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Heat Exchangers & Mass Transfer',
                "syllabus": "Classification, Logarithmic Mean Temperature Difference (LMTD) for parallel and counterflow, NTU-effectiveness method, Fick's first law of diffusion.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive Logarithmic Mean Temperature Difference (LMTD) expression for counterflow heat exchanger.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
        ]
    },
    {
        "id": 'met304-vibrations',
        "code": 'MET 304',
        "title": 'Dynamics of Machinery & Vibrations',
        "credits": 4,
        "semester": 'Semester 6',
        "branch": 'Mechanical Engineering',
        "branch_id": 'mech',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Balancing of Rotating Masses',
                "syllabus": 'Static and dynamic balancing, Balancing of several masses rotating in same plane and in different parallel planes, Analytical and graphical methods.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Four masses m1, m2, m3, m4 rotate in different planes at radii r1, r2, r3, r4. Find magnitude and position of balance masses.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Balancing of Reciprocating Masses',
                "syllabus": 'Primary and secondary unbalanced forces, Partial balancing of locomotives, Swaying couple, Hammer blow, Balancing of multi-cylinder in-line engines, V-engines.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain hammer blow, swaying couple, and variation in tractive force in partial balancing of two-cylinder locomotive.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Free Undamped & Damped Vibrations',
                "syllabus": "Single degree of freedom systems, Newton's method, Energy method, Viscous damping: Underdamped, critically damped, overdamped systems, Logarithmic decrement.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive expression for logarithmic decrement delta in underdamped spring-mass-damper system.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Forced Vibrations & Vibration Isolation',
                "syllabus": 'Harmonic excitation, Magnification factor, Resonance, Vibration isolation and transmissibility, Whirling of rotating shafts, Critical speed.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive expression for force transmissibility and explain vibration isolation design criteria.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Two Degree of Freedom & Torsional Vibrations',
                "syllabus": 'Natural frequencies and normal modes of 2-DOF systems, Dynamic vibration absorber, Torsional vibrations of single-rotor, two-rotor, and three-rotor systems.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Find natural frequencies and mode shapes of two-rotor torsional vibration system.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'met401-machine-design',
        "code": 'MET 401',
        "title": 'Design of Machine Elements',
        "credits": 4,
        "semester": 'Semester 7',
        "branch": 'Mechanical Engineering',
        "branch_id": 'mech',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Design for Static & Variable Loads',
                "syllabus": 'Design procedure, Factors of safety, Stress concentration factors, Fatigue failure: S-N curves, Endurance limits, Soderberg, Goodman, and Gerber design criteria.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'A machine component subjected to completely reversed bending stress is made of steel with S_ut = 600 MPa. Determine endurance limit using Soderberg and Goodman lines.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Design of Shafts, Keys & Couplings',
                "syllabus": 'Design of shafts based on strength, torsional rigidity, ASME design code, Sunk keys, Feather keys, Design of rigid flange coupling and bushed-pin flexible coupling.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Design a protected type cast iron flange coupling to transmit 15 kW power at 960 rpm from an electric motor to a compressor.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Fasteners & Welded Joints',
                "syllabus": 'Threaded fasteners under static and eccentric loads, Initial tension, Bolt of uniform strength, Welded joints: Transverse and parallel fillet welds under static and eccentric loads.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Design a welded joint for a bracket carrying an eccentric load of 25 kN at an eccentricity of 150mm from structural column.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Mechanical Springs',
                "syllabus": "Helical compression and tension springs, Stress and deflection equations, Wahl's stress concentration factor, Concentric springs, Multi-leaf springs: Semi-elliptic leaf spring design.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Design a helical compression spring for safety valve operating at pressure 1.2 MPa with spring index C = 6 and allowable shear stress 450 MPa.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Bearings & Lubrication',
                "syllabus": "Sliding contact bearings: Petroff's equation, Hydrodynamic lubrication, Sommerfeld number, Bearing design; Rolling contact bearings: Deep groove ball bearings, Rating life, L10 life calculation.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Select a deep groove ball bearing to carry radial load 4 kN and thrust load 2.5 kN operating at 1440 rpm for 90% survival probability after 10000 hours.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'met403-mechatronics',
        "code": 'MET 403',
        "title": 'Mechatronics & Automation',
        "credits": 4,
        "semester": 'Semester 7',
        "branch": 'Mechanical Engineering',
        "branch_id": 'mech',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Sensors & Transducers in Mechatronics',
                "syllabus": 'Mechatronic design process, Sensors: Potentiometers, LVDT, Optical encoders, Hall effect sensors, Thermocouples, Piezoelectric sensors.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain construction and operation of incremental and absolute optical rotary encoders for angular displacement measurement.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Actuators: Pneumatic, Hydraulic & Electrical',
                "syllabus": 'Pneumatic and hydraulic actuators, Directional control valves (3/2, 4/2, 5/2 valves), Solenoid valves, Stepper motors, Servomotors.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain working of 4/2 and 5/2 pilot operated directional control valves with pneumatic circuit diagrams.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Programmable Logic Controllers (PLC)',
                "syllabus": 'PLC architecture, Input/Output modules, Ladder logic programming: NO/NC contacts, Internal relays, Timers (TON, TOF), Counters (CTU, CTD).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Develop PLC ladder logic program for automatic bottle filling and capping conveyor line with timers and photo sensors.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Microcontrollers & Signal Conditioning',
                "syllabus": 'Operational amplifier signal conditioning circuits (Instrumentation amplifier, Active filters, ADC/DAC), Microcontroller interfacing with H-bridge motor drivers.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Design H-bridge DC motor driver circuit using MOSFETs and explain PWM speed control.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Industrial Robotics & Automation',
                "syllabus": 'Robot anatomy, Coordinate systems (Cartesian, Cylindrical, Spherical, Articulated, SCARA), Forward and inverse kinematics, SCADA architecture.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Compare SCARA and 6-axis Articulated robots in terms of workspace, degrees of freedom, and assembly applications.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'met402-power-plant',
        "code": 'MET 402',
        "title": 'Power Plant Engineering & Renewable Energy',
        "credits": 4,
        "semester": 'Semester 8',
        "branch": 'Mechanical Engineering',
        "branch_id": 'mech',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Thermal Power Plant Cycles',
                "syllabus": 'Rankine cycle with reheat and regeneration, Supercritical boiler layouts, Coal handling, Pulverizers, Electrostatic precipitators (ESP), Cooling towers.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain regenerative Rankine cycle with open and closed feedwater heaters. Draw T-s diagram and derive thermal efficiency.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Hydroelectric & Nuclear Power Plants',
                "syllabus": 'Hydro plant classification, Flow duration curve, Mass curve, Surge tanks; Nuclear reactors: PWR, BWR, CANDU, Fast Breeder Reactor (FBR), Nuclear waste disposal.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Describe working of Pressurized Water Reactor (PWR) and Boiling Water Reactor (BWR) with neat coolant circulation schematics.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Power Plant Economics & Tariffs',
                "syllabus": 'Load curves, Base load and peak load plants, Load factor, Capacity factor, Diversity factor, Capital and operating costs, Tariffs: Two-part and Three-part tariffs.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Define Load Factor, Plant Capacity Factor, and Reserve Margin. Discuss their economic impacts on cost per kWh of electricity.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Solar & Wind Energy Systems',
                "syllabus": 'Solar radiation geometry, Flat plate collectors, Photovoltaic cell characteristics, Maximum power point tracking (MPPT), Wind turbine aerofoil mechanics, Betz limit.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'State and prove Betz limit for maximum theoretical power extraction from wind (Cp_max = 16/27 = 59.3%).', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Biomass & Ocean Energy Systems',
                "syllabus": 'Biomass gasification, Fixed and fluidized bed gasifiers, Biogas plants, Ocean Thermal Energy Conversion (OTEC): Claude and Anderson cycles, Tidal power plants.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain closed-cycle OTEC system (Anderson cycle) operating with ammonia as working fluid. Discuss site requirements.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'cet201-solids',
        "code": 'CET 201',
        "title": 'Mechanics of Solids',
        "credits": 4,
        "semester": 'Semester 3',
        "branch": 'Civil Engineering',
        "branch_id": 'ce_cn',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Stress & Strain Analysis',
                "syllabus": "Normal and shear stresses, Hooke's law, Stress-strain diagram for mild steel, Elastic constants E, G, K, Poisson's ratio, Bars of varying cross-sections, Thermal stresses in composite bars.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'A composite bar of steel and copper is subjected to temperature rise of 50 deg C. Calculate thermal stress induced in each material.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": "Principal Stresses & Mohr's Circle",
                "syllabus": "Stresses on inclined planes, Principal planes, Principal stresses, Maximum shear stress, Mohr's circle for biaxial stresses with shear, Theories of elastic failure.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Construct Mohr's circle of stress for a plane element with sigma_x = 80 MPa, sigma_y = -40 MPa, tau_xy = 30 MPa. Find principal stresses and maximum shear stress.", "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Shear Force & Bending Moment Diagrams',
                "syllabus": 'Types of beams, supports, and loads, Relationship between load, shear force, and bending moment, SFD and BMD for Cantilever, Simply Supported, and Overhanging beams.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Draw SFD and BMD for simply supported beam of 8m span carrying UDL of 5 kN/m over whole span and point load 20 kN at center.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Flexural & Shear Stresses in Beams',
                "syllabus": 'Theory of simple bending, Flexure formula (M/I = f/y = E/R), Section modulus of rectangular, circular, I, and T sections, Shear stress distribution across sections.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive shear stress distribution formula q = (F * A * y_bar) / (I * b) across transverse section of a beam.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": "Torsion of Shafts & Euler's Columns",
                "syllabus": "Torsion of solid and hollow circular shafts, Polar modulus, Power transmission, Columns: Euler's column theory for buckling, Effective lengths for different end conditions, Rankine's formula.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Derive Euler's critical crippling load for a column with one end fixed and other end pinned (L_eff = L / sqrt(2)).", "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
        ]
    },
    {
        "id": 'cet203-fluid',
        "code": 'CET 203',
        "title": 'Fluid Mechanics I',
        "credits": 4,
        "semester": 'Semester 3',
        "branch": 'Civil Engineering',
        "branch_id": 'ce_cn',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Fluid Properties & Hydrostatic Pressure',
                "syllabus": "Viscosity, Capillarity, Vapor pressure, Pascal's law, Hydrostatic equation, Pressure measurement using piezometer and U-tube differential manometers, Center of pressure on plane and curved submerged surfaces.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive formula for total hydrostatic force and depth of center of pressure for a circular gate inclined at angle theta to horizontal.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Buoyancy & Fluid Kinematics',
                "syllabus": 'Archimedes principle, Stability of floating bodies, Metacenter and Metacentric height determination, Types of flow, Streamline, Streakline, Pathline, 2D Continuity equation.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Define metacentric height. Derive expression for metacentric height of a floating vessel by experimental tilting method.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Fluid Dynamics & Flow Measurement',
                "syllabus": "Euler's equation of motion, Bernoulli's equation, Momentum equation, Applications: Venturimeter, Orifice meter, Pitot tube, Flow through orifices and mouthpieces.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Derive Bernoulli's equation from Euler's equation. Explain working of Venturimeter and derive expression for actual discharge.", "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Notches, Weirs & Laminar Flow',
                "syllabus": 'Discharge over rectangular, triangular (V-notch), and trapezoidal (Cipolletti) notches, End contractions, Laminar flow between parallel plates, Couette and Poiseuille flows.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive discharge equation for triangular notch Q = (8/15) * C_d * sqrt(2g) * tan(theta/2) * H^(5/2).', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Pipe Flow & Hydraulic Losses',
                "syllabus": 'Darcy-Weisbach equation for friction factor, Minor losses (Sudden expansion, Contraction, Bends), Hydraulic gradient line (HGL), Total energy line (TEL), Pipes in series and parallel, Water hammer.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Two reservoirs with difference in water levels of 15m are connected by pipeline of 300mm diameter and 1200m length. Calculate discharge taking all losses into account.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'cet205-surveying',
        "code": 'CET 205',
        "title": 'Surveying & Geomatics',
        "credits": 4,
        "semester": 'Semester 3',
        "branch": 'Civil Engineering',
        "branch_id": 'ce_cn',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Principles of Surveying & Compass',
                "syllabus": 'General principles of surveying, Classification, Errors and corrections, Prismatic and Surveyor compass, Whole circle bearing vs Quadrantal bearing, Magnetic declination and local attraction corrections.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain fundamental principles of surveying. Calculate corrected bearings of a closed traverse affected by local attraction.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Levelling & Contouring',
                "syllabus": 'Dumpy level, Auto level, Collimation and Rise & Fall reduction methods, Inverted sights, Reciprocal levelling, Curvature and refraction corrections, Contour characteristics, interpolation and uses.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Compare Height of Instrument method and Rise & Fall method with arithmetic checks. Reduce levels of 10 consecutive staff readings.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Theodolite & Traverse Computations',
                "syllabus": "Vernier transit theodolite, Temporary and permanent adjustments, Measurement of horizontal and vertical angles, Gale's traverse table, Balancing closed traverse (Bowditch's and Transit rules).",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Explain temporary adjustments of a theodolite. Describe procedure for balancing closed traverse using Bowditch's rule.", "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Tacheometry & Curve Ranging',
                "syllabus": "Stadia tacheometry, Determination of tacheometric constants K and C, Movable hair method, Tangential tacheometry, Simple circular curves: Setting out by Rankine's deflection angle method.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Derive horizontal distance and elevation formula in stadia tacheometry for inclined sights. Explain Rankine's deflection angle method for curve setting.", "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Total Station, GPS & Remote Sensing',
                "syllabus": 'Electronic Distance Measurement (EDM), Working principle of Total Station, Global Positioning System (GPS): Architecture, DGPS, Principles of aerial photogrammetry and satellite remote sensing.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain operational features of Total Station. Describe GPS space, control, and user segments with positioning principles.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'cet202-struc-analysis1',
        "code": 'CET 202',
        "title": 'Structural Analysis I',
        "credits": 4,
        "semester": 'Semester 4',
        "branch": 'Civil Engineering',
        "branch_id": 'ce_cn',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Energy Principles & Deflections',
                "syllabus": "Strain energy due to axial force, shear, and bending, Castigliano's first and second theorems, Betti-Maxwell reciprocal theorem, Unit load method for deflection of determinate beams and pin-jointed trusses.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Find vertical deflection at free end of cantilever beam carrying UDL over entire length using Castigliano's Theorem.", "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Consistent Deformation Method',
                "syllabus": 'Degree of static and kinematic indeterminacy, Propped cantilevers, Fixed beams, Continuous beams with settlement of supports, Redundant pin-jointed trusses.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Analyze a continuous beam ABC of two equal spans L carrying UDL w with support B sinking by delta using consistent deformation method.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Slope Deflection Method',
                "syllabus": 'Slope deflection equations, Analysis of continuous beams with support settlement, Symmetrical and unsymmetrical portal frames without sidesway.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Analyze two-span continuous beam ABC with fixed ends A and C and sinking support B using Slope Deflection Method.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Moment Distribution Method',
                "syllabus": 'Stiffness factor, Carry-over factor, Distribution factor, Hardy Cross method of moment distribution for continuous beams and non-sway portal frames.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Analyze portal frame ABCD using Moment Distribution Method and draw bending moment diagram.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Influence Lines for Determinate Beams',
                "syllabus": 'Concept of influence lines, Influence line diagrams for reactions, shear force, and bending moment in simply supported beams, Moving point loads and UDL, Absolute maximum bending moment.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Draw ILD for shear force and bending moment at a section 4m from left support in a 12m simply supported beam. Calculate maximum moment due to moving UDL of 10 kN/m longer than span.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
        ]
    },
    {
        "id": 'cet204-soil-mech',
        "code": 'CET 204',
        "title": 'Geotechnical Engineering I',
        "credits": 4,
        "semester": 'Semester 4',
        "branch": 'Civil Engineering',
        "branch_id": 'ce_cn',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Soil Phase Relations & Index Properties',
                "syllabus": 'Three-phase soil system, Water content, Void ratio, Porosity, Degree of saturation, Unit weights, Sieve and hydrometer grain size analysis, Atterberg limits, IS soil classification.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive relationship: gamma = [G + (S * e)] * gamma_w / (1 + e). Explain determination of liquid limit using Casagrande apparatus.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Permeability & Seepage Analysis',
                "syllabus": "Darcy's law, Coefficient of permeability, Constant head and falling head permeability tests, Seepage through soils, Flow net properties, Seepage discharge and piping, Quick sand condition.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive formula for coefficient of permeability in falling head permeameter. Define quick sand condition and critical hydraulic gradient.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Compaction & Consolidation',
                "syllabus": "Standard and Modified Proctor compaction tests, Optimum moisture content (OMC), Terzaghi's 1D consolidation theory, Void ratio vs log pressure curve, Compression index, Pre-consolidation pressure.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Explain Terzaghi's 1D consolidation theory. Derive differential equation of consolidation and define coefficient of consolidation.", "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Shear Strength of Soils',
                "syllabus": 'Mohr-Coulomb failure criterion, Shear parameters c and phi, Direct shear test, Triaxial compression tests (UU, CU, CD), Unconfined compression test, Vane shear test.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Triaxial Shear Test. Differentiate between Unconsolidated Undrained (UU), Consolidated Undrained (CU), and Consolidated Drained (CD) tests.', "marks": 10, "frequency": 'Repeated 8 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Lateral Earth Pressure & Slope Stability',
                "syllabus": "Rankine's and Coulomb's earth pressure theories for active and passive conditions with cohesive and cohesionless soils, Stability of finite slopes: Swedish slip circle method.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Calculate active and passive earth pressure distribution behind a retaining wall of 6m height supporting dry sand with horizontal ground surface.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'cet206-transp',
        "code": 'CET 206',
        "title": 'Transportation Engineering I',
        "credits": 4,
        "semester": 'Semester 4',
        "branch": 'Civil Engineering',
        "branch_id": 'ce_cn',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Highway Planning & Cross-Section Elements',
                "syllabus": 'Role of highway transportation, Road patterns, Highway alignment factors, Cross-sectional elements (Camber, Carriageway, Kerb, Median, Right-of-way), Stopping Sight Distance (SSD), Overtaking Sight Distance (OSD).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive formula for Overtaking Sight Distance (OSD) on two-lane two-way highway per IRC guidelines.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Horizontal & Vertical Highway Alignment',
                "syllabus": 'Superelevation design, Radius of horizontal curve, Extra widening on horizontal curves, Transition curves (Spiral), Gradient types, Summit and Valley curves design for head-light sight distance.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive expression for superelevation e = (v^2) / (225 * R) for mixed traffic conditions. Design superelevation for 80 km/h speed on curve of radius 300m.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Pavement Materials & Testing',
                "syllabus": 'Subgrade soil properties, California Bearing Ratio (CBR) test, Aggregates: Impact, Crushing, Los Angeles abrasion tests, Bitumen tests (Penetration, Softening point, Ductility, Flash and Fire point).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Describe California Bearing Ratio (CBR) laboratory test procedure and its importance in flexible pavement design.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Flexible & Rigid Pavement Design',
                "syllabus": "Flexible pavement design using IRC 37 (Traffic MSA, Subgrade CBR, Resilient modulus), Rigid pavement design per IRC 58: Westergaard's stress equations, Temperature stresses, Joints in concrete pavements.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Calculate critical combination of stresses (Wheel load + Warping stress) at edge and corner of concrete pavement per IRC 58.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Traffic Engineering & Signal Design',
                "syllabus": "Traffic characteristics, Volume, speed and delay studies, Traffic signs and road markings, Intersections at grade and grade-separated, Traffic signals: Webster's method for optimum cycle length.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "Design a two-phase traffic signal by Webster's method for an intersection with given design traffic flows and saturation flows.", "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'cet303-rcc',
        "code": 'CET 303',
        "title": 'Design of Concrete Structures',
        "credits": 4,
        "semester": 'Semester 5',
        "branch": 'Civil Engineering',
        "branch_id": 'ce_cn',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Limit State Design Principles',
                "syllabus": 'Philosophy of limit states, Characteristic loads and strengths, Partial safety factors, Stress-strain curve for concrete and steel, Assumptions in limit state of flexure, Balanced, under-reinforced, and over-reinforced sections.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive expressions for neutral axis depth and moment of resistance of singly reinforced rectangular RCC beam section per IS 456:2000.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Design of Singly & Doubly Reinforced Beams',
                "syllabus": 'Design of singly and doubly reinforced rectangular beams for flexure, Design of flanged beams (T and L beams), Limit state of collapse in shear, Design of shear reinforcement, Development length.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Design a doubly reinforced rectangular beam 250mm x 500mm to resist factored bending moment of 180 kNm using M20 concrete and Fe415 steel.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Design of Slabs & Staircases',
                "syllabus": 'Design of one-way simply supported and continuous slabs, Design of two-way slabs with corners held down and free per IS 456 tables, Design of doglegged staircase.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Design a simply supported two-way slab for a room 4m x 5m carrying live load of 3 kN/m^2 with corners restrained against lifting.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Design of Columns',
                "syllabus": 'Short columns under axial compression, Minimum eccentricity, Short columns under combined axial load and uniaxial/biaxial bending using interaction charts (SP 16), Slender columns.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Design an axially loaded short column of cross-section 400mm x 400mm to carry factored axial load of 1500 kN using M25 concrete and Fe415 steel.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Design of Footings',
                "syllabus": 'Design of isolated square and rectangular footings for uniform soil pressure, Checks for one-way shear, two-way punching shear, and bearing stress at base of column.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Design an isolated square footing for circular column of 400mm diameter carrying axial load of 1000 kN with safe bearing capacity 200 kN/m^2.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'cet301-struc-analysis2',
        "code": 'CET 301',
        "title": 'Structural Analysis II',
        "credits": 4,
        "semester": 'Semester 5',
        "branch": 'Civil Engineering',
        "branch_id": 'ce_cn',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Slope Deflection for Sway Frames',
                "syllabus": 'Degree of kinematic indeterminacy, Slope deflection equations with sidesway, Analysis of single storey single bay portal frames with lateral point and UDL loads.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Analyze portal frame ABCD with lateral point load at column top considering sidesway using Slope Deflection Method.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Moment Distribution for Sway Frames',
                "syllabus": 'Hardy Cross method with sway correction, Analysis of rectangular portal frames with horizontal forces, Multi-storey frames by approximate portal and cantilever methods.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Analyze portal frame subjected to lateral force of 20 kN at beam level using Moment Distribution Method with sidesway correction.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Flexibility Matrix Method',
                "syllabus": 'Flexibility coefficients, Choice of redundants, Compatibility equations, Formulation and analysis of continuous beams, rigid-jointed frames, and pin-jointed trusses.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Analyze continuous beam ABC fixed at A, simply supported at B and C using Flexibility Matrix Method.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Stiffness Matrix Method',
                "syllabus": 'Degree of kinematic indeterminacy, Stiffness coefficients, Element and global stiffness matrices, Direct stiffness method for continuous beams and plane frames.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Formulate global stiffness matrix and analyze continuous beam with two spans using Stiffness Matrix Method.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Plastic Analysis of Steel Structures',
                "syllabus": 'Plastic hinge, Plastic moment of resistance, Shape factor for rectangular, I, and diamond sections, Upper and lower bound theorems, Collapse mechanisms and plastic collapse load for beams and portal frames.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive shape factor for I-section. Determine collapse load W_c for fixed beam carrying central concentrated load W using kinematic mechanism.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'cnt301-crypto',
        "code": 'CNT 301',
        "title": 'Cryptography & Network Security',
        "credits": 4,
        "semester": 'Semester 5',
        "branch": 'Computer Networking',
        "branch_id": 'ce_cn',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Classical Ciphers & Symmetric Cryptography',
                "syllabus": 'Symmetric cipher model, Substitution techniques (Caesar, Playfair, Hill cipher), Transposition techniques, Data Encryption Standard (DES), Advanced Encryption Standard (AES) architecture.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain AES encryption algorithm rounds (SubBytes, ShiftRows, MixColumns, AddRoundKey) with mathematical structures.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Asymmetric Cryptography & Key Exchange',
                "syllabus": 'Principles of public-key cryptosystems, RSA algorithm, Diffie-Hellman key exchange, Man-in-the-middle attack, Elliptic Curve Cryptography (ECC).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'In RSA algorithm with p = 11, q = 13, encryption key e = 7, find private key d and decrypt ciphertext C = 15.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Hash Functions & Digital Signatures',
                "syllabus": 'Cryptographic hash functions (SHA-256, SHA-512), Message Authentication Codes (HMAC), Digital Signature Standard (DSS).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain SHA-512 architecture and message digest generation algorithm.', "marks": 10, "frequency": 'Repeated 7 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Network & Web Security Protocols',
                "syllabus": 'IPSec (AH and ESP, Tunnel vs Transport modes), SSL/TLS handshake protocol, HTTPS, Kerberos authentication.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain TLS 1.3 Handshake Protocol steps for establishing a secure cryptographic session.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Firewalls & Intrusion Detection',
                "syllabus": 'Packet filtering firewalls, Stateful inspection, Application proxy firewalls, Intrusion Detection Systems (IDS vs IPS).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Differentiate between Signature-based IDS and Anomaly-based IDS with real network attack examples.', "marks": 7, "frequency": 'Repeated 6 times'},
                ]
            },
        ]
    },
    {
        "id": 'cnt303-adv-net',
        "code": 'CNT 303',
        "title": 'Advanced Computer Networks & Routing',
        "credits": 4,
        "semester": 'Semester 5',
        "branch": 'Computer Networking',
        "branch_id": 'ce_cn',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Internetworking & IP Addressing',
                "syllabus": 'IPv4 vs IPv6 architecture, Subnetting, VLSM, CIDR, Supernetting, NAT/PAT, IPv6 transition mechanisms (Dual stack, Tunneling, Header translation).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'An ISP is granted a block of addresses starting with 190.100.0.0/16. Design subnet allocation for 4 groups with 64, 32, 16, and 8 subnets.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Unicast & Multicast Routing Protocols',
                "syllabus": 'Distance Vector (RIP v2, Count-to-infinity, Split horizon), Link State (OSPFv3: LSA types, Area hierarchies, Dijkstra), BGP-4: Path vector, AS types, Multicast: IGMP, PIM-SM, PIM-DM.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain OSPF link state advertisements (LSAs), Area types (Backbone, Stub, NSSA), and SPF route calculation.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Transport Layer Protocols & Congestion Control',
                "syllabus": 'TCP state transition diagram, Connection management (3-way handshake, 4-way teardown), Sliding window, Slow start, Congestion avoidance, Fast retransmit, Fast recovery, TCP Tahoe vs Reno vs BBR, QUIC protocol.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain TCP congestion control mechanisms (AIMD, Slow Start, Fast Retransmit, Fast Recovery) with congestion window timeline graph.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Software-Defined Networking (SDN) & OpenFlow',
                "syllabus": 'Data plane vs Control plane separation, SDN controller architecture (OpenDaylight, ONOS), OpenFlow protocol and flow table matching, Network Function Virtualization (NFV).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Software-Defined Networking (SDN) architecture. How does OpenFlow protocol enable flow-based packet forwarding?', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Quality of Service (QoS) & Network Management',
                "syllabus": 'Integrated Services (IntServ, RSVP), Differentiated Services (DiffServ, PHB), Traffic shaping (Leaky Bucket, Token Bucket), SNMPv3 architecture, MIBs, Network monitoring.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Compare Leaky Bucket and Token Bucket traffic shaping algorithms with diagrams and buffer behavior.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'cet302-steel',
        "code": 'CET 302',
        "title": 'Design of Steel Structures',
        "credits": 4,
        "semester": 'Semester 6',
        "branch": 'Civil Engineering',
        "branch_id": 'ce_cn',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Connections in Steel Structures',
                "syllabus": 'Limit state design of steel per IS 800:2007, Bolted connections: Bearing and High Strength Friction Grip (HSFG) bolts, Welded connections: Fillet and butt welds.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Design a lap joint to connect two tie bars 150mm x 10mm using 20mm diameter grade 4.6 bolts to transmit working tensile load of 120 kN.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Design of Tension Members',
                "syllabus": 'Types of tension members, Net effective sectional area, Shear lag effect, Design of single and double angle tension members, Lug angles, Tension splices.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Design an angle section tension member to carry factored tensile load of 250 kN connected to 10mm thick gusset plate.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Design of Compression Members',
                "syllabus": 'Column buckling classes, Effective length, Design of single and built-up columns, Design of lacing and batten systems, Slab base and gusseted column bases.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Design a built-up column consisting of two channel sections placed back-to-back with a single lacing system to carry factored load of 1000 kN.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Design of Beams',
                "syllabus": 'Laterally supported and unsupported beams, Bending and shear strength per IS 800, Check for deflection, Web buckling and web crippling checks.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Design a laterally supported beam for an effective span of 6m carrying UDL of 30 kN/m excluding self weight. Check for shear and deflection.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Roof Trusses & Purlins',
                "syllabus": 'Types of industrial roof trusses, Load calculations (Dead, Live, Wind loads per IS 875 Part 3), Design of angle purlins subjected to biaxial bending.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Design an angle purlin for a truss spaced at 4m with slope 30 degrees carrying wind pressure of 1.2 kN/m^2.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'cet304-environ',
        "code": 'CET 304',
        "title": 'Environmental Engineering',
        "credits": 4,
        "semester": 'Semester 6',
        "branch": 'Civil Engineering',
        "branch_id": 'ce_cn',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Water Demand & Quality Standards',
                "syllabus": 'Water supply system layout, Population forecasting methods (Arithmetic, Geometric, Incremental increase), Water quality parameters: Physical, chemical, and biological, Drinking water standards per IS 10500.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Forecast population of a town after 3 decades using Incremental Increase Method from census data. State IS 10500 limits for turbidity, fluorides, and coliforms.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Water Treatment Technologies',
                "syllabus": 'Aeration, Flash mixing, Coagulation and Flocculation, Sedimentation tanks (Rectangular, Circular), Filtration (Slow sand, Rapid sand, Dual media), Disinfection: Chlorination, Breakpoint chlorination curve.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain breakpoint chlorination curve and residual chlorine. Design rapid sand filter for treating 10 MLD water.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Wastewater Collection & Characteristics',
                "syllabus": "Sewerage systems (Separate, Combined), Design of sanitary sewers per Manning's formula, Sewage characteristics: BOD, COD, Solids, BOD kinetics and first-stage BOD rate constant determination.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive first-stage BOD equation L_t = L_0 * (1 - 10^(-k*t)). A wastewater sample has 5-day BOD at 20 deg C of 200 mg/L. Determine ultimate BOD.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Secondary Wastewater Treatment Units',
                "syllabus": 'Primary treatment: Screening, Grit chamber, Primary settling tank, Secondary treatment: Activated Sludge Process (ASP), Design of aeration tank, F/M ratio, Sludge Volume Index (SVI), Trickling filters.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Design an Activated Sludge aeration tank for 5 MLD domestic wastewater with BOD_5 = 250 mg/L, F/M ratio = 0.3, MLSS = 3000 mg/L.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Sludge Treatment & Air Pollution Control',
                "syllabus": 'Sludge digestion: Anaerobic digester stages, Sludge drying beds, Air pollution: Primary and secondary pollutants, Lapse rates and plume behavior, Particulate control devices (Cyclone separator, ESP, Baghouse filters).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain working principle of Electrostatic Precipitator (ESP). Explain atmospheric stability, lapse rates, and resulting plume behaviors.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'cnt302-wireless',
        "code": 'CNT 302',
        "title": 'Wireless & Mobile Networks',
        "credits": 4,
        "semester": 'Semester 6',
        "branch": 'Computer Networking',
        "branch_id": 'ce_cn',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Wireless Transmission & Cellular Concept',
                "syllabus": 'Radio frequency propagation, Free-space path loss, Fading, Multipath, Cellular architecture, Frequency reuse, Handover strategies, Co-channel interference, Cell splitting, Sectoring.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain cellular frequency reuse concept. Derive expression for frequency reuse distance D = R * sqrt(3N) and co-channel interference ratio.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Multiple Access & Mobile Generations (2G/3G/4G)',
                "syllabus": 'TDMA, FDMA, CDMA (Orthogonal codes, Walsh-Hadamard codes, Near-far problem), 2G (GSM architecture, Channels), 3G (UMTS, WCDMA), 4G (LTE architecture, EPC, OFDMA, SC-FDMA).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain GSM system architecture showing BSS, NSS, and OSS subsystems. Contrast OFDMA and SC-FDMA in 4G LTE.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": '5G New Radio (NR) & Next-Gen Wireless',
                "syllabus": '5G architecture (eMBB, URLLC, mMTC), Service-Based Architecture (SBA), Network slicing, Beamforming, Massive MIMO, Millimeter-wave communication, O-RAN architecture.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain 5G Service-Based Architecture (SBA) and Network Slicing concept for tailoring network resources to distinct verticals.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Wireless LANs & PANs',
                "syllabus": 'IEEE 802.11 Wi-Fi standards (802.11a/b/g/n/ac/ax/be - Wi-Fi 7), CSMA/CA protocol, Hidden and Exposed Terminal Problems, RTS/CTS mechanism, Bluetooth architecture (Piconet, Scatternet), ZigBee (IEEE 802.15.4).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Hidden Terminal and Exposed Terminal problems in CSMA/CA and how RTS/CTS handshake resolves them.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Mobile IP & Mobile Ad-Hoc Networks (MANET)',
                "syllabus": 'Mobile IP operation (Home Agent, Foreign Agent, Care-of Address, Triangle routing, Reverse tunneling), MANET routing protocols: AODV, DSR, OLSR, Vehicular Ad-Hoc Networks (VANETs).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Mobile IPv4 routing mechanism with Agent Discovery, Registration, and Tunneling. Discuss Triangle Routing problem.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'cet401-estimating',
        "code": 'CET 401',
        "title": 'Quantity Surveying & Valuation',
        "credits": 4,
        "semester": 'Semester 7',
        "branch": 'Civil Engineering',
        "branch_id": 'ce_cn',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Methods of Building Estimation',
                "syllabus": 'Units of measurement, Long wall-Short wall method, Centre line method for residential and commercial building estimation, Abstract of estimate.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Prepare detailed estimate for earthwork in excavation, foundation concrete, and brickwork for a two-room building using Centre Line Method.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Analysis of Rates & Specifications',
                "syllabus": 'Rate analysis: Material and labor requirements per KPWD/CPWD data book, Rate analysis for RCC M20, Brickwork in 1:6 cement mortar, Plastering.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Perform rate analysis for 1 cubic meter of Reinforced Cement Concrete (1:1.5:3) including materials, labor, centering, and 10% contractor profit.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Road & Culvert Estimation',
                "syllabus": 'Earthwork calculation in embankments and cuttings: Trapezoidal formula, Prismoidal formula, Detailed estimation of water bound macadam road and slab culvert.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Calculate earthwork in excavation and embankment for a 500m road section using Prismoidal formula with given cross-sections.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Contracts & Tenders',
                "syllabus": 'Tender notice, EMD, Security deposit, Types of contracts (Item rate, Percentage rate, Lump sum, EPC), Conditions of contract, Arbitration.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Draft a standard tender notice for construction of an academic block worth Rs. 5 Crores specifying essential tender conditions.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Valuation of Real Properties',
                "syllabus": 'Difference between cost, price, and value, Depreciation methods (Straight line, Sinking fund, Constant percentage), Capitalized value, Years purchase, Rent fixation.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Calculate capitalized value of a commercial property yielding net annual rent of Rs. 2,40,000 at 8% rate of interest with sinking fund redemption.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'cet403-eq-eng',
        "code": 'CET 403',
        "title": 'Structural Dynamics & Earthquake Engineering',
        "credits": 4,
        "semester": 'Semester 7',
        "branch": 'Civil Engineering',
        "branch_id": 'ce_cn',
        "category": 'PEC',
        "modules": [
            {
                "module_no": 1,
                "title": 'SDOF Vibration Systems',
                "syllabus": 'Undamped and damped free vibration, Equation of motion, Damping ratio, Logarithmic decrement, Harmonically forced vibration, Dynamic amplification factor, Transmissibility.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Derive equation of motion for viscously damped SDOF system and obtain expressions for underdamped displacement response and logarithmic decrement.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'MDOF Systems & Modal Analysis',
                "syllabus": 'Formulation of equations of motion, Mass and stiffness matrices, Natural frequencies and mode shapes, Orthogonality of modes, Modal superposition method for dynamic response.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Find natural frequencies and sketch mode shapes for a two-storey shear building with lumped masses m_1 = m_2 = m and storey stiffnesses k_1 = k_2 = k.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Seismology & Response Spectrum',
                "syllabus": 'Causes of earthquakes, Plate tectonics, Faults, Seismic waves (P, S, Rayleigh, Love), Magnitude vs Intensity (Richter vs MSK/EMS), Response spectrum concept, Elastic response spectrum per IS 1893.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Define Response Spectrum. Explain construction of design response spectrum and importance of site soil conditions per IS 1893:2016.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Equivalent Static Seismic Analysis (IS 1893)',
                "syllabus": 'Seismic design philosophy, Zone factor (Z), Importance factor (I), Response reduction factor (R), Fundamental natural period, Design base shear calculation and vertical distribution.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Calculate design seismic base shear and distribute it vertically along floor levels for a 4-storey commercial building in Zone IV per IS 1893:2016.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Ductile Detailing & Earthquake Resistant Design',
                "syllabus": 'Ductility definition, Factors affecting ductility, IS 13920:2016 ductile detailing provisions for beams, columns, beam-column joints, and shear walls, Soft storey and torsion irregularity.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain ductile detailing requirements for RCC beam-column joints and columns subjected to seismic forces per IS 13920:2016.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
        ]
    },
    {
        "id": 'cnt401-cloud',
        "code": 'CNT 401',
        "title": 'Cloud Computing & Virtualization',
        "credits": 4,
        "semester": 'Semester 7',
        "branch": 'Computer Networking',
        "branch_id": 'ce_cn',
        "category": 'PEC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Cloud Computing Foundations & Models',
                "syllabus": 'Cloud architecture, NIST definition, Essential characteristics, Service models (IaaS, PaaS, SaaS, FaaS/Serverless), Deployment models (Public, Private, Hybrid, Multi-cloud).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Compare IaaS, PaaS, and SaaS service models with architecture stacks, provider vs consumer responsibilities, and use cases.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Virtualization Technologies & Hypervisors',
                "syllabus": 'Hypervisor types (Type 1 Bare-metal vs Type 2 Hosted), Full virtualization, Paravirtualization, Hardware-assisted virtualization (Intel VT-x, AMD-V), Memory and I/O virtualization (SR-IOV).',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain CPU, memory, and I/O virtualization techniques. Differentiate between Type-1 and Type-2 hypervisors with examples.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Containers & Cloud Orchestration',
                "syllabus": 'Containers vs Virtual Machines, Docker architecture (Engine, Images, Dockerfile, Container storage, Networking), Kubernetes architecture: Master and Worker nodes, Pods, Services, Deployments, Ingress.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Kubernetes architecture (kube-apiserver, etcd, kube-scheduler, kubelet, kube-proxy) and Pod lifecycle management.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Cloud Storage Architectures',
                "syllabus": 'Cloud storage architectures: Object storage (Amazon S3 / Google Cloud Storage), Block storage (EBS), File storage (EFS), CAP theorem, Eventual consistency, Distributed hash tables.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain CAP theorem (Consistency, Availability, Partition Tolerance) with PACELC extension for distributed cloud storage systems.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Cloud Security & Serverless Architecture',
                "syllabus": 'Shared responsibility model, IAM policies, VPC, Security groups, Serverless computing: Event-driven functions (AWS Lambda, Cloud Functions), Cold start optimization, Cloud economics.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain the Cloud Shared Responsibility Model. Describe AWS Lambda serverless execution lifecycle and mitigation of cold start latency.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
    {
        "id": 'cnt402-cyber-forensics',
        "code": 'CNT 402',
        "title": 'Cyber Forensics & Ethical Hacking',
        "credits": 4,
        "semester": 'Semester 8',
        "branch": 'Computer Networking',
        "branch_id": 'ce_cn',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Digital Forensics Process & Evidence',
                "syllabus": 'Digital forensic lifecycle: Identification, Collection, Preservation, Examination, Analysis, Reporting, Chain of custody, Order of volatility, Forensic imaging.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain step-by-step digital forensic investigation process and maintaining strict chain of custody for digital evidence.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Disk & File System Forensics',
                "syllabus": 'MBR vs GPT partition tables, FAT, NTFS file systems: Master File Table (MFT), Data streams, Slack space, File carving, Deleted file recovery.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain NTFS architecture, Master File Table (MFT) record attributes, and recovering deleted files from slack space.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Memory & Network Forensics',
                "syllabus": 'Volatile memory capture, RAM analysis using Volatility framework, Network packet capture and inspection using Wireshark, Log correlation, DNS poisoning forensics.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Describe RAM acquisition techniques and analyzing active processes, network connections, and injected DLLs using Volatility.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Ethical Hacking & Penetration Testing',
                "syllabus": 'Penetration testing methodology, Footprinting, Port scanning (Nmap: SYN, FIN, Null scans), Vulnerability assessment, Metasploit framework exploitation.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain Nmap scanning mechanisms (TCP Connect, SYN Stealth, UDP scan) and firewalls evasion techniques.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Web Application Security & Cyber Law',
                "syllabus": 'OWASP Top 10 vulnerabilities (SQL Injection, XSS, CSRF, Broken Auth), Remediation, Indian Information Technology (IT) Act 2000, Section 65 and 66 offences.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain SQL Injection and Cross-Site Scripting (XSS) attack vectors with prevention using parameterized queries.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
        ]
    },
    {
        "id": 'cet402-foundations',
        "code": 'CET 402',
        "title": 'Ground Improvement & Foundation Design',
        "credits": 4,
        "semester": 'Semester 8',
        "branch": 'Civil Engineering',
        "branch_id": 'ce_cn',
        "category": 'PCC',
        "modules": [
            {
                "module_no": 1,
                "title": 'Shallow Foundations & Bearing Capacity',
                "syllabus": "Types of shallow foundations, Terzaghi's bearing capacity theory, General, local, and punching shear failure modes, IS 6403 bearing capacity equation with shape, depth, and inclination factors.",
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": "A square footing 2m x 2m is located at depth 1.5m in sand with c = 0, phi = 35 deg, gamma = 18 kN/m^3. Calculate safe bearing capacity with FOS = 3 using Terzaghi's formula.", "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 2,
                "title": 'Settlement Analysis of Shallow Foundations',
                "syllabus": 'Immediate elastic settlement, Primary consolidation settlement, Permissible total and differential settlements per IS 1904, Raft/Mat foundations: Modulus of subgrade reaction, Conventional design.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Calculate consolidation settlement of a 3m x 3m footing resting on a normally consolidated clay layer of thickness 4m under an increase in effective stress.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 3,
                "title": 'Deep Foundations - Pile Foundations',
                "syllabus": 'Classification of piles, Load carrying capacity of single pile in clay and sand (Static formulas), Dynamic pile driving formulas (Engineering News, Hiley formula), Pile load test per IS 2911, Group action.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Determine ultimate bearing capacity of a 4x4 pile group of 400mm diameter and 12m length driven into soft clay with cohesion c = 40 kN/m^2.', "marks": 10, "frequency": 'Repeated 9 times (Guaranteed)'},
                ]
            },
            {
                "module_no": 4,
                "title": 'Well Foundations & Cofferdams',
                "syllabus": 'Components of well foundation (Well curb, Cutting edge, Steining, Bottom plug, Sand filling, Top plug, Well cap), Forces acting on well foundation, Sinking of wells, Tilts and shifts remediation, Cofferdams.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain components of well foundation with a neat sketch. Describe causes and remedial measures for tilts and shifts during well sinking.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
            {
                "module_no": 5,
                "title": 'Ground Improvement Techniques',
                "syllabus": 'Compaction and Vibro-flotation, Dynamic compaction, Stone columns, Prefabricated vertical drains (PVD) with preloading, Soil stabilization (Cement, Lime, Fly ash), Geosynthetics in geotechnical engineering.',
                "weightage_marks": 15,
                "high_yield_pyqs": [
                    {"q": 'Explain installation and mechanism of Stone Columns for ground improvement in soft clays. Discuss application of geotextiles as reinforcement and filter.', "marks": 10, "frequency": 'Repeated 8 times'},
                ]
            },
        ]
    },
]
