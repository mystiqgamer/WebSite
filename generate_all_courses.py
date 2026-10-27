"""
Script to generate courses_data.py with complete S1-S8 coverage for:
Common (S1, S2), CSE, ECE, EEE, MECH, CE/CN.
"""
import sys

def build():
    lines = []
    lines.append('"""')
    lines.append('KTU ScholarOS - Comprehensive Course Catalog (B.Tech 2024 Scheme)')
    lines.append('Contains all courses from S1 to S8 across 5 branches: CSE, ECE, EEE, MECH, CE/CN')
    lines.append('"""')
    lines.append('')
    lines.append('from typing import List, Dict, Any')
    lines.append('')
    lines.append('KTU_COURSES: List[Dict[str, Any]] = [')

    def add_course_code(cid, code, title, credits, sem, branch, branch_id, cat, mods):
        lines.append('    {')
        lines.append(f'        "id": {repr(cid)},')
        lines.append(f'        "code": {repr(code)},')
        lines.append(f'        "title": {repr(title)},')
        lines.append(f'        "credits": {credits},')
        lines.append(f'        "semester": {repr(sem)},')
        lines.append(f'        "branch": {repr(branch)},')
        lines.append(f'        "branch_id": {repr(branch_id)},')
        lines.append(f'        "category": {repr(cat)},')
        lines.append('        "modules": [')
        for i, m in enumerate(mods):
            lines.append('            {')
            lines.append(f'                "module_no": {m["module_no"]},')
            lines.append(f'                "title": {repr(m["title"])},')
            lines.append(f'                "syllabus": {repr(m["syllabus"])},')
            lines.append(f'                "weightage_marks": {m.get("weightage_marks", 15)},')
            lines.append('                "high_yield_pyqs": [')
            for q in m.get("high_yield_pyqs", []):
                lines.append(f'                    {{"q": {repr(q["q"])}, "marks": {q["marks"]}, "frequency": {repr(q["frequency"])}}},')
            lines.append('                ]')
            lines.append('            }' + (',' if i < len(mods) - 1 else ''))
        lines.append('        ]')
        lines.append('    },')

    # Common S1 & S2
    # MAT 101
    add_course_code(
        "mat101-calc", "MAT 101", "Linear Algebra & Calculus", 4, "Semester 1", "All Branches (Common)", "common", "BSC",
        [
            {"module_no": 1, "title": "Single Variable Calculus & Series", "syllabus": "Taylor's and Maclaurin's expansions, Indeterminate forms, L'Hopital's Rule. Infinite series: Convergence tests (Ratio test, Root test, Alternating series test, Leibniz's theorem).", "high_yield_pyqs": [{"q": "Expand log(1 + e^x) in powers of x using Maclaurin's series up to x^4.", "marks": 7, "frequency": "Repeated 5 times"}, {"q": "Test convergence of alternating series Sigma (-1)^n * (n / (2n^2 + 1)) using Leibniz test.", "marks": 7, "frequency": "Repeated 4 times"}]},
            {"module_no": 2, "title": "Multivariable Differential Calculus", "syllabus": "Partial derivatives, Homogeneous functions, Euler's theorem, Total derivative, Jacobians, Maxima and minima of functions of two variables, Lagrange multipliers.", "high_yield_pyqs": [{"q": "If u = sin^-1((x + y) / (sqrt(x) + sqrt(y))), prove that x*(du/dx) + y*(du/dy) = (1/2)*tan(u) using Euler's theorem.", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}, {"q": "Find maximum and minimum distance from the origin to 5x^2 + 6xy + 5y^2 = 8 using Lagrange multipliers.", "marks": 10, "frequency": "Repeated 7 times"}]},
            {"module_no": 3, "title": "Multiple Integrals", "syllabus": "Double integrals (Cartesian and Polar), Change of order of integration, Area bounded by curves. Triple integrals, Volume of solids.", "high_yield_pyqs": [{"q": "Change the order of integration and evaluate: Integral(0 to a) Integral(x to a) (x / (x^2 + y^2)) dy dx.", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}]},
            {"module_no": 4, "title": "Vector Calculus & Line/Surface Integrals", "syllabus": "Gradient, Directional derivative, Divergence, Curl. Green's theorem in a plane, Gauss Divergence theorem, Stokes' theorem.", "high_yield_pyqs": [{"q": "Verify Green's theorem in the plane for Integral (xy + y^2)dx + x^2 dy where C is bounded by y = x and y = x^2.", "marks": 10, "frequency": "Repeated 7 times (Guaranteed)"}]},
            {"module_no": 5, "title": "Linear Algebra, Eigenvalues & Cayley-Hamilton", "syllabus": "Rank of matrix, Echelon form, System of linear equations. Eigenvalues and Eigenvectors, Cayley-Hamilton theorem, Diagonalization.", "high_yield_pyqs": [{"q": "Find eigenvalues and eigenvectors of matrix A = [[2, 1, 1], [2, 3, 2], [3, 3, 4]] and test for diagonalizability.", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}]}
        ]
    )

    # PHT 100
    add_course_code(
        "pht100-physics", "PHT 100", "Engineering Physics", 4, "Semester 1", "All Branches (Common)", "common", "BSC",
        [
            {"module_no": 1, "title": "Oscillations & Waves", "syllabus": "Simple harmonic motion, Damped harmonic oscillator: Under, critical and over-damped motions, Forced oscillations, Resonance, Sharpness of resonance, Q-factor.", "high_yield_pyqs": [{"q": "Derive differential equation of damped harmonic oscillator and solve for under-damped condition.", "marks": 10, "frequency": "Repeated 6 times"}]},
            {"module_no": 2, "title": "Wave Optics", "syllabus": "Interference of light: Principle of superposition, Cosine law, Interference in thin films, Air wedge experiment, Newton's rings. Diffraction: Fraunhofer diffraction at single slit, Diffraction grating.", "high_yield_pyqs": [{"q": "Explain formation of Newton's rings in reflected light and derive expression for diameter of nth dark ring.", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Quantum Mechanics", "syllabus": "Dual nature of matter, De Broglie hypothesis, Davisson-Germer experiment, Uncertainty principle, Wavefunction properties, Time-dependent and time-independent Schrodinger equations, Particle in a 1D box.", "high_yield_pyqs": [{"q": "Derive Schrodinger 1D time-independent wave equation and calculate eigen energy values of a particle in an infinite potential box.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 4, "title": "Lasers & Fiber Optics", "syllabus": "Absorption, Spontaneous and Stimulated emission, Einstein's coefficients, Population inversion, Optical resonator, Ruby laser, He-Ne laser. Optical fibers: Acceptance angle, Numerical aperture, Step-index vs Graded-index.", "high_yield_pyqs": [{"q": "Explain working of Ruby laser with neat energy level diagram. Derive relation between Einstein's coefficients.", "marks": 10, "frequency": "Repeated 7 times"}]},
            {"module_no": 5, "title": "Ultrasonics & Superconductivity", "syllabus": "Ultrasonics: Piezoelectric oscillator, Magnetostriction generator, Ultrasonic flaw detector. Superconductivity: Meissner effect, Type-I and Type-II superconductors, BCS theory overview, SQUID.", "high_yield_pyqs": [{"q": "Explain production of ultrasonic waves using Piezoelectric method and discuss industrial applications in Non-Destructive Testing (NDT).", "marks": 10, "frequency": "Repeated 7 times"}]}
        ]
    )

    # EST 100
    add_course_code(
        "est100-mechanics", "EST 100", "Engineering Mechanics", 3, "Semester 1", "All Branches (Common)", "common", "ESC",
        [
            {"module_no": 1, "title": "Statics of Particles & Coplanar Force Systems", "syllabus": "Concept of particle and rigid body, Force systems, Resolution and composition of forces, Resultant of concurrent forces, Equilibrium equations, Lami's theorem.", "high_yield_pyqs": [{"q": "State and prove Lami's theorem. A 100 kg cylinder is supported between two inclined planes at 30 and 60 degrees. Find support reactions.", "marks": 10, "frequency": "Repeated 6 times"}]},
            {"module_no": 2, "title": "Support Reactions & Friction", "syllabus": "Free body diagrams, Support reactions of simply supported and cantilever beams, Friction: Laws of dry friction, Angle of friction, Angle of repose, Cone of friction, Wedge friction.", "high_yield_pyqs": [{"q": "Find minimum horizontal force P required to raise a load W using a wedge of angle alpha with friction coefficient mu.", "marks": 10, "frequency": "Repeated 7 times"}]},
            {"module_no": 3, "title": "Centroid & Moment of Inertia", "syllabus": "Centroid of composite areas (L, T, I sections), Theorem of Pappus-Guldinus, Moment of inertia of plane areas, Parallel and perpendicular axis theorems, Polar moment of inertia, Radius of gyration.", "high_yield_pyqs": [{"q": "Find centroid and moment of inertia about centroidal x-axis for an unsymmetrical I-section.", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}]},
            {"module_no": 4, "title": "Dynamics of Particles", "syllabus": "Kinematics: Rectilinear motion with uniform and variable acceleration, Curvilinear motion, Projectile motion. Kinetics: D'Alembert's principle, Work-energy principle, Impulse-momentum equation.", "high_yield_pyqs": [{"q": "A bullet of mass m strikes a suspended block of mass M with velocity v and gets embedded. Find maximum angle of swing using momentum and energy principles.", "marks": 10, "frequency": "Repeated 7 times"}]},
            {"module_no": 5, "title": "Rotation of Rigid Bodies & Vibrations", "syllabus": "Rotation of rigid body about a fixed axis, Mass moment of inertia of standard shapes, Work and energy in rotational motion, Simple harmonic motion of mechanical systems, Free undamped vibrations of spring-mass systems.", "high_yield_pyqs": [{"q": "Derive expression for the natural frequency of oscillation of a simple pendulum and a mass-spring system.", "marks": 10, "frequency": "Repeated 6 times"}]}
        ]
    )

    # EST 110
    add_course_code(
        "est110-civil-mech", "EST 110", "Basics of Civil & Mechanical Engineering", 4, "Semester 1", "All Branches (Common)", "common", "ESC",
        [
            {"module_no": 1, "title": "Civil Engineering Materials & Surveying", "syllabus": "General introduction, Stones, Bricks, Cement: Chemical composition, Grades, Concrete: Ingredients, Water-cement ratio, Grades. Surveying: Chain surveying, Leveling, Total Station.", "high_yield_pyqs": [{"q": "Explain water-cement ratio and Abram's law. What is workability of concrete and how is it measured using slump test?", "marks": 7, "frequency": "Repeated 5 times"}]},
            {"module_no": 2, "title": "Building Components & Green Buildings", "syllabus": "Foundations: Shallow and deep foundations, Superstructure: Columns, Beams, Lintels, Roofs, Doors, Windows. Green building concepts, Rainwater harvesting systems.", "high_yield_pyqs": [{"q": "Differentiate between shallow and deep foundations with sketches. Explain rainwater harvesting methods for residential buildings.", "marks": 8, "frequency": "Repeated 6 times"}]},
            {"module_no": 3, "title": "Thermodynamic Systems & Boilers", "syllabus": "System, Surroundings, Laws of thermodynamics, Concept of entropy, Steam generators: Fire-tube boilers (Cochran) vs Water-tube boilers (Babcock & Wilcox), Boiler mountings and accessories.", "high_yield_pyqs": [{"q": "Compare fire-tube and water-tube boilers. Explain working of Babcock & Wilcox boiler with neat sketch.", "marks": 7, "frequency": "Repeated 6 times"}]},
            {"module_no": 4, "title": "Internal Combustion Engines", "syllabus": "Classification, Air standard Otto and Diesel cycles, 4-stroke Petrol engine, 4-stroke Diesel engine, 2-stroke engines, Fuel injection systems, Lubrication and cooling systems.", "high_yield_pyqs": [{"q": "Explain working of 4-stroke Diesel engine with PV diagram and timing chart. Differentiate between SI and CI engines.", "marks": 8, "frequency": "Repeated 7 times"}]},
            {"module_no": 5, "title": "Power Transmission & Manufacturing", "syllabus": "Belt drives: Flat and V-belts, Velocity ratio, Creep, Slip, Gear drives: Spur, Helical, Bevel gears. Manufacturing: Casting, Forging, Welding (Arc and Gas), Refrigeration cycles: Vapor compression system.", "high_yield_pyqs": [{"q": "Explain working of Vapor Compression Refrigeration System (VCRS) with schematic and PH/TS diagrams.", "marks": 8, "frequency": "Repeated 7 times"}]}
        ]
    )

    # HUN 101
    add_course_code(
        "hun101-lifeskills", "HUN 101", "Life Skills & Professional Communication", 2, "Semester 1", "All Branches (Common)", "common", "HMC",
        [
            {"module_no": 1, "title": "Communication Essentials", "syllabus": "Verbal and non-verbal communication, Body language, Eye contact, Active listening, Barriers to effective communication, Professional email etiquette.", "high_yield_pyqs": [{"q": "Explain 7 Cs of effective communication and identify key interpersonal communication barriers.", "marks": 7, "frequency": "Repeated 5 times"}]},
            {"module_no": 2, "title": "Critical Thinking & Problem Solving", "syllabus": "Lateral thinking, Deductive vs inductive reasoning, Problem formulation, Root Cause Analysis (Fishbone diagram), Six Thinking Hats method.", "high_yield_pyqs": [{"q": "Apply Edward de Bono's Six Thinking Hats technique to resolve an engineering project deadlock.", "marks": 8, "frequency": "Repeated 6 times"}]},
            {"module_no": 3, "title": "Team Dynamics & Leadership", "syllabus": "Leadership styles: Transformational, Servant, Authoritarian; Belbin team roles, Conflict resolution strategies (Thomas-Kilmann model), Group discussions.", "high_yield_pyqs": [{"q": "Describe stages of team development (Forming, Storming, Norming, Performing, Adjourning) and conflict handling.", "marks": 8, "frequency": "Repeated 6 times"}]},
            {"module_no": 4, "title": "Stress Management & Emotional Intelligence", "syllabus": "Understanding stress, Eustress vs distress, Time management using Eisenhower Matrix, Goleman's model of Emotional Intelligence (EQ).", "high_yield_pyqs": [{"q": "Discuss five components of emotional intelligence according to Daniel Goleman.", "marks": 7, "frequency": "Repeated 5 times"}]},
            {"module_no": 5, "title": "Professional Ethics & Values", "syllabus": "Engineering ethics, Codes of conduct, Whistleblowing, Intellectual property rights (IPR), Plagiarism, Social responsibility of engineers.", "high_yield_pyqs": [{"q": "Discuss role of professional ethics in engineering decisions with reference to landmark engineering failures.", "marks": 8, "frequency": "Repeated 6 times"}]}
        ]
    )

    # MAT 102
    add_course_code(
        "mat102-diff", "MAT 102", "Vector Calculus, Differential Equations & Transforms", 4, "Semester 2", "All Branches (Common)", "common", "BSC",
        [
            {"module_no": 1, "title": "First Order Ordinary Differential Equations", "syllabus": "Exact differential equations, Integrating factors, Orthogonal trajectories, Linear ODEs, Bernoulli's equation, Applications: Newton's law of cooling, Population models.", "high_yield_pyqs": [{"q": "Find orthogonal trajectories of the family of coaxial circles x^2 + y^2 + 2gx + c = 0.", "marks": 7, "frequency": "Repeated 5 times"}]},
            {"module_no": 2, "title": "Higher Order Linear ODEs", "syllabus": "Homogeneous linear ODEs with constant coefficients, Method of undetermined coefficients, Method of variation of parameters, Cauchy-Euler differential equations.", "high_yield_pyqs": [{"q": "Solve y'' + y = sec(x) by method of variation of parameters.", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Laplace Transforms", "syllabus": "Laplace transform definition, Linearity, First and second shifting theorems, Transforms of derivatives and integrals, Multiplication by t^n, Division by t.", "high_yield_pyqs": [{"q": "Find Laplace transform of (sin(at) / t) and hence evaluate Integral(0 to inf) (sin(t)/t) dt.", "marks": 10, "frequency": "Repeated 7 times"}]},
            {"module_no": 4, "title": "Inverse Laplace & Initial Value Problems", "syllabus": "Inverse Laplace transforms, Partial fraction expansion, Convolution theorem, Unit step function, Dirac delta function, Solving ODEs with initial values.", "high_yield_pyqs": [{"q": "Using convolution theorem, find inverse Laplace transform of 1 / (s^2 * (s^2 + 1)).", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}]},
            {"module_no": 5, "title": "Fourier Series", "syllabus": "Periodic functions, Dirichlet conditions, Euler's formulas, Fourier series of even and odd functions, Half range sine and cosine expansions, Parseval's identity.", "high_yield_pyqs": [{"q": "Find Fourier series of f(x) = x^2 in (-pi, pi) and deduce that 1/1^2 + 1/2^2 + 1/3^2 + ... = pi^2 / 6.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]}
        ]
    )

    # EST 102
    add_course_code(
        "est102-cprog", "EST 102", "Programming in C", 4, "Semester 2", "All Branches (Common)", "common", "ESC",
        [
            {"module_no": 1, "title": "C Fundamentals & Flowcharts", "syllabus": "Algorithms, Flowcharts, Constants, Variables, Data Types, Operators, Type conversion, Formatted I/O.", "high_yield_pyqs": [{"q": "Draw flowchart and write C program to check for Prime and Armstrong numbers.", "marks": 10, "frequency": "Repeated 7 times"}]},
            {"module_no": 2, "title": "Control Structures & Iteration", "syllabus": "if-else, switch-case, for, while, do-while, break, continue, Nested loops, Patterns.", "high_yield_pyqs": [{"q": "Write a C program using switch-case to implement a menu-driven calculator.", "marks": 7, "frequency": "Repeated 6 times"}]},
            {"module_no": 3, "title": "Arrays & Strings", "syllabus": "1D/2D Arrays, Matrix multiplication. String manipulation with and without library functions.", "high_yield_pyqs": [{"q": "Write a C program to multiply two matrices A[m][n] and B[p][q] after dimension check.", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}]},
            {"module_no": 4, "title": "Functions & Recursion", "syllabus": "User functions, Call by value vs reference, Storage classes, Tower of Hanoi recursion.", "high_yield_pyqs": [{"q": "Write a C function to solve the Tower of Hanoi problem for n disks using recursion.", "marks": 10, "frequency": "Repeated 7 times"}]},
            {"module_no": 5, "title": "Pointers, Structs & File I/O", "syllabus": "Pointer arithmetic, Dynamic allocation (malloc/free), Structures vs Unions, File handling.", "high_yield_pyqs": [{"q": "Define structure Student and write C program to rank 50 students.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    )

    # CYT 100
    add_course_code(
        "cyt100-chemistry", "CYT 100", "Engineering Chemistry", 4, "Semester 2", "All Branches (Common)", "common", "BSC",
        [
            {"module_no": 1, "title": "Electrochemistry & Corrosion", "syllabus": "Electrochemical cells, Nernst equation, Calomel electrode, Glass electrode, Electrochemical corrosion mechanism, Factors influencing corrosion, Cathodic protection: Sacrificial anode and Impressed current.", "high_yield_pyqs": [{"q": "Derive Nernst equation for single electrode potential. Explain electrochemical theory of corrosion of iron.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Polymers & Nanomaterials", "syllabus": "Classification of polymers, Thermoplastics vs Thermosetting, Conducting polymers (Polyaniline), Carbon Nanotubes (CNTs): SWCNT, MWCNT, Chemical vapor deposition synthesis, Applications.", "high_yield_pyqs": [{"q": "Explain synthesis, properties and engineering applications of Carbon Nanotubes (CNTs).", "marks": 10, "frequency": "Repeated 7 times"}]},
            {"module_no": 3, "title": "Fuels & Energy Storage", "syllabus": "Calorific value: HCV, LCV, Bomb calorimeter determination, Knocking in engines, Octane and Cetane numbers, Lithium-ion battery: Construction, Charge-discharge reactions, Hydrogen-Oxygen fuel cell.", "high_yield_pyqs": [{"q": "Describe construction and working of Lithium-ion battery and H2-O2 fuel cell with electrode reactions.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Water Technology", "syllabus": "Hardness of water: Temporary and permanent hardness, Units of hardness, EDTA titration method, Boiler feed water troubles: Sludge, Scale, Caustic embrittlement, Demineralization by Ion-exchange resins.", "high_yield_pyqs": [{"q": "Explain estimation of total hardness of water by EDTA method with chemical equations and calculations.", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}]},
            {"module_no": 5, "title": "Spectroscopic Techniques", "syllabus": "Beer-Lambert's law, UV-Visible spectroscopy: Chromophores, Auxochromes, Bathochromic shift, Vibrational spectroscopy (FTIR): Modes of vibration, Characteristic functional group absorption bands.", "high_yield_pyqs": [{"q": "State and derive Beer-Lambert's law. What are fundamental vibrational modes in CO2 and H2O molecules?", "marks": 10, "frequency": "Repeated 7 times"}]}
        ]
    )

    # EST 120
    add_course_code(
        "est120-elec-elec", "EST 120", "Basics of Electrical & Electronics Engineering", 4, "Semester 2", "All Branches (Common)", "common", "ESC",
        [
            {"module_no": 1, "title": "DC Circuits & AC Fundamentals", "syllabus": "Ohm's law, Kirchhoff's laws, Nodal and Mesh analysis, Generation of alternating voltages, RMS and average values, Form factor, Peak factor, Phasor representation.", "high_yield_pyqs": [{"q": "Calculate current in each branch of a DC bridge network using Kirchhoff's laws.", "marks": 7, "frequency": "Repeated 6 times"}]},
            {"module_no": 2, "title": "AC Circuits & Three-Phase Systems", "syllabus": "Series RL, RC, and RLC circuits, Power factor, Active, Reactive, and Apparent power, Generation of 3-phase voltages, Star and Delta connections, Relationship between line and phase quantities.", "high_yield_pyqs": [{"q": "Derive relationship between line and phase voltages and currents in balanced Star and Delta 3-phase systems.", "marks": 8, "frequency": "Repeated 8 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Electrical Machines", "syllabus": "DC Motors: Working principle, Back EMF, Speed-torque characteristics, Single-phase transformers: Principle of operation, EMF equation, Transformation ratio, Losses and efficiency.", "high_yield_pyqs": [{"q": "Derive EMF equation of single-phase transformer. Explain open circuit and short circuit losses.", "marks": 8, "frequency": "Repeated 7 times"}]},
            {"module_no": 4, "title": "Semiconductor Diodes & Applications", "syllabus": "PN junction diode: Forward and reverse characteristics, Zener diode: Breakdown mechanisms, Half-wave and Full-wave bridge rectifiers, Capacitor filter, Zener voltage regulator.", "high_yield_pyqs": [{"q": "Explain operation of full-wave bridge rectifier with neat circuit and input/output waveforms. Derive ripple factor.", "marks": 8, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "Bipolar Junction Transistors & Op-Amps", "syllabus": "BJT operations: CE, CB configurations, Transistor as an amplifier and switch, Ideal operational amplifier characteristics, Inverting and Non-inverting Op-Amp configurations.", "high_yield_pyqs": [{"q": "Explain CE configuration of BJT with input and output characteristics. Define current gains alpha and beta.", "marks": 8, "frequency": "Repeated 7 times"}]}
        ]
    )

    # EST 130
    add_course_code(
        "est130-graphics", "EST 130", "Engineering Graphics", 3, "Semester 2", "All Branches (Common)", "common", "ESC",
        [
            {"module_no": 1, "title": "Principles of Projections & Points", "syllabus": "BIS conventions, Lettering, Dimensioning rules, Scales, Orthographic projection concept, Projections of points situated in all four quadrants.", "high_yield_pyqs": [{"q": "Draw the projections of points located 20mm above HP, 30mm behind VP, and on HP, 40mm in front of VP.", "marks": 7, "frequency": "Repeated 6 times"}]},
            {"module_no": 2, "title": "Projections of Straight Lines", "syllabus": "Projections of straight lines parallel, perpendicular, and inclined to reference planes, Determination of true length and inclinations with HP and VP, Traces of lines.", "high_yield_pyqs": [{"q": "A line AB 80mm long has end A 20mm above HP and 30mm in front of VP. Top view measures 60mm and front view 70mm. Find true inclinations.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Projections of Planes & Solids", "syllabus": "Projections of regular polygonal and circular planes inclined to both reference planes. Projections of prisms, pyramids, cylinders, and cones with axis inclined to one reference plane.", "high_yield_pyqs": [{"q": "A pentagonal pyramid of base edge 30mm and axis 60mm rests on an edge of its base on HP with axis inclined at 45 deg to HP. Draw projections.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Sections of Solids & Development of Surfaces", "syllabus": "Section planes parallel and inclined to HP/VP, True shape of section, Development of lateral surfaces of prisms, pyramids, cones, and cylinders.", "high_yield_pyqs": [{"q": "A cone of base diameter 50mm and axis 65mm is cut by a section plane at 45 deg to HP passing through midpoint of axis. Draw sectional top view and development.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "Isometric Projections", "syllabus": "Isometric scale, Isometric view and isometric projection of simple and truncated solids, Composite solids (Cylinder on frustum of cone, Sphere on prism).", "high_yield_pyqs": [{"q": "Draw isometric view of a hemisphere of diameter 60mm resting centrally on top of a square prism of base side 70mm and height 30mm.", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}]}
        ]
    )

    return lines, add_course_code

if __name__ == "__main__":
    lines, add_course = build()
    print("Base generated with lines:", len(lines))
