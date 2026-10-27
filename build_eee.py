"""
EEE Courses Builder (S3 to S8) for KTU 2024 Scheme
"""

def get_eee_courses():
    courses = []

    def make_c(cid, code, title, credits, sem, cat, mods):
        return {
            "id": cid,
            "code": code,
            "title": title,
            "credits": credits,
            "semester": sem,
            "branch": "Electrical & Electronics Engineering",
            "branch_id": "eee",
            "category": cat,
            "modules": mods
        }

    # S3
    courses.append(make_c(
        "eet201-circuits", "EET 201", "Circuits & Networks", 4, "Semester 3", "PCC",
        [
            {"module_no": 1, "title": "Circuit Analysis Techniques", "syllabus": "Mesh and Node analysis with dependent sources, Source transformations, Duality, Graph theory: Incidence matrix, Tie-set and cut-set matrices.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Find node voltages in a bridge circuit containing coupled inductors and dependent voltage sources.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Network Theorems", "syllabus": "Superposition, Thevenin's, Norton's, Maximum Power Transfer, Reciprocity, Millman's and Tellegen's theorems applied to AC and DC circuits.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "State and prove Maximum Power Transfer theorem for complex source and load impedances.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Transient Analysis", "syllabus": "DC and sinusoidal response of RL, RC, and RLC series and parallel circuits using Laplace Transform, Initial and final conditions.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Find the transient capacitor voltage v_c(t) in an underdamped series RLC circuit excited by DC voltage V.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Two-Port Networks & Transformed Circuits", "syllabus": "Z, Y, ABCD, h-parameters, Interrelationships, Condition for reciprocity and symmetry, Driving point and transfer impedances.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Determine Z-parameters of a symmetrical lattice network and verify condition for reciprocity.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "Magnetic Circuits & 3-Phase Systems", "syllabus": "Dot convention in coupled circuits, Coefficient of coupling, Series and parallel resonance, Unbalanced three-phase systems.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Write loop equations for magnetically coupled circuit using dot convention and calculate equivalent inductance.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    courses.append(make_c(
        "eet203-measurements", "EET 203", "Electrical Measurements & Instrumentation", 4, "Semester 3", "PCC",
        [
            {"module_no": 1, "title": "Indicating Instruments", "syllabus": "Classification, Deflecting, controlling, and damping torques, PMMC instruments, Moving iron (Attraction and repulsion) instruments, Shunts and multipliers.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive torque equation of Moving Iron instrument. Explain why its scale is non-linear.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Measurement of Resistance & Bridges", "syllabus": "Measurement of low, medium, and high resistance: Kelvin's double bridge, Wheatstone bridge, Megger; AC bridges: Maxwell's, Hay's, Schering bridges.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive balance equation for Kelvin's Double Bridge for measurement of low resistance.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Power & Energy Measurement", "syllabus": "Electrodynamometer wattmeter, Errors and compensation, Two-wattmeter method for balanced and unbalanced 3-phase power, Induction type energy meter.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Two-Wattmeter method for measuring 3-phase power. Derive expression for power factor in terms of wattmeter readings.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 4, "title": "Instrument Transformers & Potentiometers", "syllabus": "Current Transformers (CT), Potential Transformers (PT), Ratio and phase angle errors, DC potentiometers (Crompton potentiometer), AC potentiometers.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain working of Current Transformer (CT). Derive expressions for ratio and phase angle errors with phasor diagram.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "Digital Instruments & Transducers", "syllabus": "Digital voltmeters (Successive approximation, Dual slope), CRO, DSO, Transducers: LVDT, Strain gauges, Thermocouples, RTD.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain construction and working of Linear Variable Differential Transformer (LVDT) with characteristics.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    courses.append(make_c(
        "eet205-analog-elec", "EET 205", "Analog Electronics", 4, "Semester 3", "PCC",
        [
            {"module_no": 1, "title": "Diode Circuits & Power Supplies", "syllabus": "Half wave, Full wave center tapped and bridge rectifiers with C, LC, and CLC filters, Ripple factor, Voltage regulation using Zener diode.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain working of full-wave bridge rectifier with capacitor filter and derive ripple factor expression.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Transistor Biasing & Small Signal Models", "syllabus": "BJT biasing: Fixed bias, Collector to base bias, Self bias, Stability factors, Small signal h-parameter model for CE configuration.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive stability factors S, S', and S'' for voltage divider self-bias BJT circuit.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 3, "title": "FET & MOSFET Amplifiers", "syllabus": "JFET construction, Drain and transfer characteristics, Pinch-off voltage, MOSFET: Depletion and Enhancement types, Small signal analysis of Common Source amplifier.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain drain and transfer characteristics of n-channel enhancement MOSFET. Derive transconductance g_m.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Feedback Amplifiers & Oscillators", "syllabus": "Principle of negative feedback, Topologies: Voltage/Current Series/Shunt, Barkhausen criterion, RC phase shift oscillator, Hartley, Colpitts oscillators.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive expression for frequency of oscillation of Colpitts oscillator with BJT circuit.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "Operational Amplifiers & Wave Shaping", "syllabus": "Ideal Op-Amp characteristics, Inverting and non-inverting amplifiers, Summing amplifier, Differential amplifier, Schmitt trigger, Precision rectifiers.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain inverting Schmitt trigger using Op-Amp and derive expressions for threshold voltages V_UT and V_LT.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    # S4
    courses.append(make_c(
        "eet202-dc-trans", "EET 202", "DC Machines & Transformers", 4, "Semester 4", "PCC",
        [
            {"module_no": 1, "title": "DC Generators", "syllabus": "Armature windings, EMF equation, Armature reaction, Demagnetizing and cross-magnetizing ampere-turns, Commutation, Characteristics of DC generators.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain armature reaction in DC generator. How are cross-magnetizing and demagnetizing effects mitigated using interpoles and compensating windings?", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 2, "title": "DC Motors", "syllabus": "Working principle, Back EMF, Torque equation, Motor characteristics, Starters: 3-point and 4-point starters, Speed control: Armature resistance and Field flux control, Ward-Leonard system.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Draw neat schematic of 3-point starter for DC shunt motor and explain functions of No-Volt Coil (NVC) and Overload Release (OLR).", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Testing of DC Machines", "syllabus": "Losses in DC machines, Efficiency calculation, Swinburne's test, Hopkinson's regenerative test, Field's test, Retardation test.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Hopkinson's regenerative test for finding efficiency of two identical DC shunt machines.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Single-Phase Transformers", "syllabus": "Core and Shell types, EMF equation, Equivalent circuit, Phasor diagrams on no-load and full load (lagging/leading pf), Voltage regulation, Maximum efficiency condition.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive condition for maximum efficiency of single-phase transformer. Draw its complete exact equivalent circuit.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 5, "title": "Testing & Polyphase Transformers", "syllabus": "Open circuit (OC) and short circuit (SC) tests, Sumpner's back-to-back test, All-day efficiency, Auto-transformers, 3-phase transformer connections (Star-Star, Delta-Delta, Scott connection).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Scott connection of two single-phase transformers for 3-phase to 2-phase conversion with phasor diagrams.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    courses.append(make_c(
        "eet204-emft", "EET 204", "Electromagnetic Field Theory", 4, "Semester 4", "PCC",
        [
            {"module_no": 1, "title": "Vector Analysis & Electrostatic Fields", "syllabus": "Coordinate systems (Cartesian, Cylindrical, Spherical), Coulomb's law, Electric field intensity, Gauss's law and applications, Divergence theorem, Electric potential.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "State and prove Gauss's Law in electrostatics. Apply it to find electric field due to an infinite line charge.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Conductors, Dielectrics & Capacitance", "syllabus": "Current density, Continuity equation, Polarization in dielectrics, Boundary conditions at dielectric interfaces, Poisson's and Laplace's equations, Capacitance of coaxial cable.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive boundary conditions for electric flux density D and field E across dielectric interface.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 3, "title": "Magnetostatic Fields", "syllabus": "Biot-Savart's law, Ampere's circuital law and applications, Magnetic flux density, Vector magnetic potential, Stokes' theorem, Force on moving charge in magnetic field.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive expression for magnetic flux density B on the axis of a circular current loop using Biot-Savart's law.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Magnetic Forces, Materials & Inductance", "syllabus": "Magnetic force on differential current element, Magnetization in materials, Boundary conditions for magnetic fields, Self and mutual inductances.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive expression for self-inductance of a toroid with rectangular cross-section.", "marks": 10, "frequency": "Repeated 7 times"}]},
            {"module_no": 5, "title": "Time-Varying Fields & Maxwell's Equations", "syllabus": "Faraday's law, Transformer and motional EMF, Displacement current density, Maxwell's equations in differential and integral forms, Poynting vector and theorem.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive Maxwell's equations in differential form from fundamental laws. Explain displacement current concept.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]}
        ]
    ))

    # S5
    courses.append(make_c(
        "eet301-power", "EET 301", "Power Systems I", 4, "Semester 5", "PCC",
        [
            {"module_no": 1, "title": "Transmission Line Parameters", "syllabus": "Resistance, Inductance of single-phase and 3-phase lines with symmetrical and unsymmetrical spacing, Transposition, GMD and GMR, Capacitance calculations.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive expression for loop inductance of a 3-phase transposed overhead transmission line with unsymmetrical spacing.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 2, "title": "Line Performance & Modeling", "syllabus": "Short, medium (Nominal T and Pi), and long transmission lines (Rigorous solution), ABCD parameters, Ferranti effect, Surge Impedance Loading (SIL).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive ABCD constants for Nominal-Pi model of medium transmission line. Explain Ferranti effect.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Mechanical Design of Overhead Lines", "syllabus": "Line supports, Conductor types (ACSR), Calculation of sag and tension with equal and unequal supports, Effect of wind and ice loading.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive sag formula for transmission line conductors supported between towers at unequal levels.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Insulators & Corona", "syllabus": "Pin, Suspension, Strain insulators, Potential distribution over suspension insulator string, String efficiency, Methods of improving string efficiency (Guard ring), Corona.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Define string efficiency. Derive expression for voltage distribution in a 3-unit suspension insulator string.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 5, "title": "Underground Cables & Distribution", "syllabus": "Classification, Insulation resistance, Capacitance of single-core and 3-core belted cables, Grading of cables (Capacitance and Intersheath grading), Distribution systems.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Capacitance Grading of underground cables with mathematical derivations and stress distribution curves.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    courses.append(make_c(
        "eet303-ac-machines", "EET 303", "Induction Machines & Synchronous Machines", 4, "Semester 5", "PCC",
        [
            {"module_no": 1, "title": "3-Phase Induction Motors Fundamentals", "syllabus": "Production of rotating magnetic field, Principle of operation, Slip, Torque equation, Torque-slip characteristics, Condition for maximum torque, Equivalent circuit.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive expression for torque developed by 3-phase induction motor and deduce condition for maximum starting torque.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 2, "title": "Testing & Speed Control of Induction Motors", "syllabus": "No-load and Blocked-rotor tests, Circle diagram, Starters (DOL, Star-Delta, Auto-transformer), Speed control: V/f control, Pole changing, Slip power recovery.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain circle diagram construction from no-load and blocked rotor test data to determine efficiency and power factor.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 3, "title": "Single Phase Induction & Special Motors", "syllabus": "Double field revolving theory, Starting methods: Split phase, Capacitor start/run, Shaded pole motors, Universal motor, Stepper motor.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Double Field Revolving Theory for single-phase induction motors with torque-speed curves.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Synchronous Alternators", "syllabus": "Construction: Salient pole and cylindrical rotor, Armature winding factors (Pitch and distribution factors), EMF equation, Armature reaction, Voltage regulation: EMF, MMF, Potier methods.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Potier Reactance Method (Zero Power Factor Method) for voltage regulation of alternator with phasor diagram.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 5, "title": "Synchronous Motors & Parallel Operation", "syllabus": "Principle of operation, Methods of starting, V and Inverted V curves, Synchronous condenser, Parallel operation of alternators, Synchronizing power.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain V and Inverted-V curves of synchronous motor and its application as synchronous condenser for power factor correction.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    courses.append(make_c(
        "eet307-control", "EET 307", "Linear Control Systems", 4, "Semester 5", "PCC",
        [
            {"module_no": 1, "title": "System Modeling & Transfer Functions", "syllabus": "Open-loop vs Closed-loop, Transfer function of physical systems (Electrical, Mechanical), Block diagram reduction, Mason's gain formula.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Find overall transfer function C(s)/R(s) of given multiple-feedback system using Mason's Gain Formula.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Time Domain Response", "syllabus": "Standard test signals, Transient response of first and second order systems, Specifications: Rise time, Peak time, Peak overshoot, Settling time, Steady state error constants.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive expressions for Peak Time (t_p) and Maximum Percentage Overshoot (M_p) of second-order underdamped system.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Stability & Routh-Hurwitz Criterion", "syllabus": "Concept of stability, BIBO stability, Routh-Hurwitz stability criterion, Special cases (Zero row, First column zero), Relative stability.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Determine stability and find range of K for system with characteristic equation s^4 + 6s^3 + 11s^2 + 6s + K = 0 using Routh array.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 4, "title": "Root Locus Technique", "syllabus": "Root locus concept, Rules for construction: Angle of asymptotes, Centroid, Breakaway and break-in points, Angles of departure and arrival.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Sketch complete root locus for unity feedback system with G(s) = K / [s(s + 2)(s^2 + 6s + 25)].", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 5, "title": "Frequency Response Analysis", "syllabus": "Bode plot: Gain margin and Phase margin, Nyquist stability criterion, Polar plots, Introduction to Lead, Lag, and Lag-Lead compensators.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Draw Bode plot for open-loop transfer function G(s)H(s) = 200 / [s(s + 2)(s + 10)] and determine Gain Margin and Phase Margin.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]}
        ]
    ))

    # S6
    courses.append(make_c(
        "eet302-power2", "EET 302", "Power Systems II", 4, "Semester 6", "PCC",
        [
            {"module_no": 1, "title": "Power System Modeling & Y-Bus", "syllabus": "Per-unit system, Single-line diagram, Primitive network, Bus admittance matrix (Y_bus) formation by inspection and singular transformation.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Form Bus Admittance Matrix (Y_bus) for given 4-bus power system network by direct inspection.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Load Flow Studies", "syllabus": "Classification of buses, Gauss-Seidel method, Newton-Raphson method in polar coordinates, Fast Decoupled load flow method.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Newton-Raphson load flow algorithm with Jacobian matrix structure in polar form.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Symmetrical & Unsymmetrical Fault Analysis", "syllabus": "Symmetrical 3-phase fault, Symmetrical components (Positive, Negative, Zero sequence), Analysis of Single Line-to-Ground (LG), Line-to-Line (LL), and Double Line-to-Ground (LLG) faults.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive fault current expression for Single Line to Ground (LG) fault through impedance Z_f with sequence network interconnection.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 4, "title": "Power System Stability", "syllabus": "Steady-state and transient stability, Swing equation, Power angle curve, Equal Area Criterion, Critical clearing angle and critical clearing time.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive swing equation of a synchronous generator connected to infinite bus. State Equal Area Criterion.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 5, "title": "Protection Schemes & Circuit Breakers", "syllabus": "Overcurrent relays, Distance relays (Impedance, Mho), Differential protection of transformers and generators, Circuit breakers: Arc quenching principles, SF6 and Vacuum circuit breakers.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain percentage biased differential protection scheme for power transformer against internal faults.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    courses.append(make_c(
        "eet304-power-elec", "EET 304", "Power Electronics & Drives", 4, "Semester 6", "PCC",
        [
            {"module_no": 1, "title": "Power Semiconductor Devices", "syllabus": "SCR, MOSFET, IGBT, Static and switching characteristics, Two-transistor analogy of SCR, Turn-on methods, dv/dt and di/dt protections.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain two-transistor analogy of SCR and derive expression for anode current. Detail snubber circuit operation.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 2, "title": "Controlled Rectifiers", "syllabus": "Single-phase half-wave, full-wave center-tapped, and bridge converters with R, RL, and RLE loads, Discontinuous and continuous conduction modes, Three-phase full converters.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain working of single-phase fully controlled bridge rectifier with RL load and continuous current. Derive average DC output voltage.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "DC-DC Converters (Choppers)", "syllabus": "Step-down (Buck) chopper, Step-up (Boost) chopper, Buck-Boost converter, Continuous conduction mode equations, Voltage and current ripple calculations.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive expression for output voltage of Buck-Boost converter and draw inductor voltage and current waveforms.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Inverters & PWM", "syllabus": "Single-phase half and full-bridge inverters, Three-phase voltage source inverters (180 and 120-degree conduction modes), Sinusoidal PWM (SPWM).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain 180-degree conduction mode of 3-phase Voltage Source Inverter with switching sequence and line-to-line voltage waveforms.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 5, "title": "AC Voltage Controllers & Drives", "syllabus": "Single-phase AC voltage controllers with R and RL loads, Cycloconverters, DC drive speed control, V/f control of induction motor drives.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain V/f speed control of 3-phase induction motor fed from PWM inverter maintaining airgap flux constant.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    # S7
    courses.append(make_c(
        "eet401-adv-control", "EET 401", "Advanced Control Systems", 4, "Semester 7", "PCC",
        [
            {"module_no": 1, "title": "State Space Representation", "syllabus": "State variable concepts, State vector, State space modeling of physical systems, Conversion from transfer function to state space (Phase variable, Canonical forms).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive state space representation for given differential equation in Controllable and Observable Canonical Forms.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "State Transition Matrix & Solutions", "syllabus": "State transition matrix (STM) properties, Computation of STM using Laplace transform and Cayley-Hamilton theorem, Solution of homogeneous and non-homogeneous state equations.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Compute State Transition Matrix e^{At} for matrix A = [[0, 1], [-2, -3]] using Cayley-Hamilton theorem.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 3, "title": "Controllability & Observability", "syllabus": "Concepts of controllability and observability, Kalman's test, Gilbert's test, Duality principle, State feedback controller design, Pole placement by Ackermann's formula.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Design state feedback gain matrix K using Ackermann's formula to place closed-loop poles at s = -1, -2.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "State Observers & Non-Linearities", "syllabus": "Full-order state observers, Inherent non-linearities: Saturation, Dead zone, Backlash, Friction, Phase plane method: Singular points, Limit cycles.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Phase Plane method for non-linear control analysis. Classify singular points (Node, Saddle, Focus, Center).", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "Describing Function & Lyapunov Stability", "syllabus": "Describing function definition, Describing function for saturation and dead zone, Lyapunov stability analysis, Lyapunov direct method.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Determine stability of non-linear system using Lyapunov Direct Method with scalar energy function V(x).", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    courses.append(make_c(
        "eet403-ev-storage", "EET 403", "Electric Vehicles & Energy Storage", 4, "Semester 7", "PCC",
        [
            {"module_no": 1, "title": "Electric Vehicle Architecture", "syllabus": "Historical perspective, EV configurations (BEV, HEV, PHEV, FCEV), Vehicle dynamics: Tractive effort, Rolling resistance, Aerodynamic drag, Acceleration force.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive equation for total tractive effort required by an EV cruising at constant velocity on an inclined road.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Electric Motors for Propulsion", "syllabus": "Permanent Magnet Synchronous Motor (PMSM), Brushless DC Motor (BLDC), Switched Reluctance Motor (SRM), Induction Motors for EVs, Torque-speed characteristics.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Compare PMSM, BLDC, and Induction Motors for EV powertrain applications in terms of efficiency, weight, and speed control.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 3, "title": "Energy Storage Technologies", "syllabus": "Battery chemistry: Lead-acid, Lithium-ion (NMC, LFP), Solid-state batteries, Supercapacitors, Fuel cells, Ragone plot, State of Charge (SOC) estimation.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain operation of Lithium Iron Phosphate (LiFePO4) battery and discuss Coulomb Counting method for SOC estimation.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Battery Management Systems (BMS)", "syllabus": "BMS architecture, Cell monitoring, Active and passive cell balancing circuits, Thermal management, Thermal runaway protection, CAN bus communication.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain active and passive cell balancing circuits in BMS and discuss thermal runaway prevention mechanisms.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "EV Charging & Grid Integration", "syllabus": "AC charging (Level 1, 2), DC fast charging (Level 3), Wireless charging, Vehicle-to-Grid (V2G) power flow, Impact on electrical distribution grid.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Vehicle-to-Grid (V2G) technology and its benefits for peak shaving and grid frequency regulation.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    # S8
    courses.append(make_c(
        "eet402-smart-grid", "EET 402", "Smart Grid & High Voltage Engineering", 4, "Semester 8", "PCC",
        [
            {"module_no": 1, "title": "Smart Grid Architecture & AMI", "syllabus": "Smart grid definition, Differences between conventional and smart grid, Advanced Metering Infrastructure (AMI), Smart meters, Home Energy Management Systems (HEMS).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Compare conventional grid and smart grid architecture. Detail components of Advanced Metering Infrastructure (AMI).", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Wide Area Measurement & Microgrids", "syllabus": "Phasor Measurement Units (PMU), Synchrophasors, Wide Area Monitoring Systems (WAMS), Microgrids: AC, DC, and Hybrid microgrids, Islanding detection.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain principle and working of Phasor Measurement Unit (PMU) and its role in Wide Area Monitoring Systems.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 3, "title": "Breakdown in Insulating Media", "syllabus": "Townsend's breakdown criterion, Paschen's law, Streamer mechanism in gases, Breakdown in liquids: Cavitation theory, Breakdown in solid dielectrics.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "State and prove Paschen's Law for breakdown voltage in gases. Discuss factors influencing breakdown.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Generation of High Voltages", "syllabus": "High voltage AC: Cascaded transformers, Resonant transformers; High voltage DC: Cockcroft-Walton voltage multiplier; Impulse voltage: Multistage Marx generator.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain operation of multistage Marx Generator circuit for generating standard lightning impulse voltage wave.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 5, "title": "High Voltage Testing & Protection", "syllabus": "Testing of insulators, bushings, and cables, Non-destructive testing: Partial discharge measurement, Lightning surges, Surge arresters (Metal oxide varistors).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain partial discharge detection in high voltage cables and working of ZnO gapless surge arrester.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    return courses
