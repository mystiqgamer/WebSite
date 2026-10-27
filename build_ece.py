"""
ECE Courses Builder (S3 to S8) for KTU 2024 Scheme
"""

def get_ece_courses():
    courses = []

    def make_c(cid, code, title, credits, sem, cat, mods):
        return {
            "id": cid,
            "code": code,
            "title": title,
            "credits": credits,
            "semester": sem,
            "branch": "Electronics & Communication Engineering",
            "branch_id": "ece",
            "category": cat,
            "modules": mods
        }

    # S3
    courses.append(make_c(
        "mat201-pde-complex", "MAT 201", "Partial Differential Equations & Complex Analysis", 4, "Semester 3", "BSC",
        [
            {"module_no": 1, "title": "Partial Differential Equations", "syllabus": "Formation of PDE, Solutions of first order linear PDEs: Lagrange's method, Charpit's method for non-linear first order PDEs.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Solve Lagrange's linear PDE: x(y^2 - z^2)p + y(z^2 - x^2)q = z(x^2 - y^2).", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "1D Wave & Heat Equations", "syllabus": "Method of separation of variables, One-dimensional wave equation: Vibrating string, One-dimensional heat conduction equation with Dirichlet and Neumann boundary conditions.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Solve 1D wave equation d^2u/dt^2 = c^2 * d^2u/dx^2 for string with fixed ends and initial displacement f(x).", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Complex Analytic Functions", "syllabus": "Functions of complex variables, Cauchy-Riemann equations in Cartesian and Polar forms, Analytic functions, Harmonic conjugate, Conformal mapping (w = z^2, w = e^z, Bilinear transformation).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Prove that u(x, y) = e^x * cos(y) is harmonic and find its harmonic conjugate v(x, y) to construct analytic function f(z).", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Complex Integration", "syllabus": "Line integrals in complex plane, Cauchy's integral theorem, Cauchy's integral formula for derivatives of analytic functions, Morera's theorem, Liouville's theorem.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Evaluate Integral_C (e^{2z} / (z + 1)^4) dz where C is circle |z| = 2 using Cauchy's integral formula.", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}]},
            {"module_no": 5, "title": "Singularities & Residue Calculus", "syllabus": "Taylor's series, Laurent's series expansion, Zeros and poles, Essential singularities, Cauchy's residue theorem, Evaluation of real definite integrals around unit circle.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Evaluate Integral(0 to 2pi) (1 / (5 + 4*sin(theta))) d(theta) using contour integration and Cauchy's Residue Theorem.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]}
        ]
    ))

    courses.append(make_c(
        "ect201-ssd", "ECT 201", "Solid State Devices", 4, "Semester 3", "PCC",
        [
            {"module_no": 1, "title": "Semiconductor Physics", "syllabus": "Carrier concentrations in intrinsic/extrinsic semiconductors, Fermi level, Drift and diffusion currents, Continuity equation.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive expression for carrier concentration in intrinsic semiconductor and locate Fermi energy level.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "PN Junction Diode", "syllabus": "Built-in potential, Depletion width, V-I characteristics, Junction capacitance (Depletion and Diffusion), Breakdown (Zener & Avalanche).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive diode equation for ideal PN junction and explain reverse breakdown mechanisms.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Bipolar Junction Transistor", "syllabus": "BJT fundamentals, Minority carrier distribution, Ebers-Moll model, Base width modulation (Early effect), Punch-through.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Early effect in BJT and derive terminal currents using Ebers-Moll model.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "MOSFET Fundamentals", "syllabus": "MOS capacitor, Accumulation, Depletion, Inversion, Threshold voltage equation, Drain current equation in linear and saturation regions.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive drain current equation for n-channel enhancement MOSFET in saturation and triode regions.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 5, "title": "Short Channel Effects & Special Devices", "syllabus": "Drain Induced Barrier Lowering (DIBL), Velocity saturation, Hot carrier effects, FinFET, Tunnel FET, LED, Solar Cell.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Short Channel Effects (SCE) in MOSFETs: DIBL and sub-threshold conduction.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    courses.append(make_c(
        "ect203-lcd", "ECT 203", "Logic Circuit Design", 4, "Semester 3", "PCC",
        [
            {"module_no": 1, "title": "Boolean Algebra & Optimization", "syllabus": "Boolean axioms, De Morgan's laws, SOP and POS canonical forms, 4 and 5-variable K-Maps with don't care conditions, Quine-McCluskey tabular reduction.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Minimize F(A, B, C, D) = Sigma m(1, 3, 7, 11, 15) + d(0, 2, 5) using Quine-McCluskey method.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Combinational Logic Design", "syllabus": "Carry look-ahead adder, Magnitude comparators, Encoders, Priority encoders, Decoders, Multiplexers, De-multiplexers, Code converters (Gray to Binary).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Design a 4-bit Carry Look-Ahead (CLA) Adder and show that it operates faster than Ripple Carry Adder.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Sequential Logic & Latches", "syllabus": "Latches vs Flip-flops, SR, JK, D, T flip-flops, Master-Slave JK flip-flop, Race-around condition, Characteristic and excitation equations.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Convert JK flip-flop to D flip-flop and T flip-flop showing excitation tables and K-Maps.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Synchronous & Asynchronous Counters", "syllabus": "Design of synchronous mod-N counters, Ripple counters, Up/Down counters, Shift registers (SISO, SIPO, PISO, PIPO), Ring and Johnson counters.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Design a 3-bit synchronous Up-Down counter using T flip-flops with control input M.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "Finite State Machines & PLDs", "syllabus": "Mealy and Moore FSM models, State diagrams, State reduction, State assignment, Programmable Logic Arrays (PLA), Programmable Array Logic (PAL).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Design a Moore sequence detector to detect serial bit stream '1011' using D flip-flops.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]}
        ]
    ))

    courses.append(make_c(
        "ect205-nt", "ECT 205", "Network Theory", 4, "Semester 3", "PCC",
        [
            {"module_no": 1, "title": "Network Topology & Circuit Equations", "syllabus": "Graph of a network, Tree, Co-tree, Incidence matrix, Fundamental cut-set matrix, Fundamental tie-set matrix, Node and Mesh formulations.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Draw graph for given electrical circuit, select a tree, and write fundamental tie-set and cut-set matrices.", "marks": 10, "frequency": "Repeated 7 times"}]},
            {"module_no": 2, "title": "Network Theorems in Frequency Domain", "syllabus": "Superposition theorem, Thevenin's theorem, Norton's theorem, Maximum power transfer theorem, Reciprocity theorem applied to AC and coupled circuits.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Find Thevenin's equivalent circuit across terminals AB for an AC circuit with dependent voltage and current sources.", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Transient Analysis using Laplace Transforms", "syllabus": "Transient response of series and parallel RL, RC, and RLC circuits with DC and sinusoidal excitations, Initial and final conditions.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "In a series RLC circuit with R = 2 ohm, L = 1 H, C = 0.5 F connected to DC supply V, find current i(t) for t > 0.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Two-Port Network Parameters", "syllabus": "Z, Y, ABCD (Transmission), h, and g parameters, Relationships between parameters, Interconnection of two-port networks (Series, Parallel, Cascade).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive relationship between Transmission (ABCD) parameters and Impedance (Z) parameters of a two-port network.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "Resonance & Filters", "syllabus": "Series and Parallel resonance, Q-factor, Selectivity, Bandwidth, Constant-k and m-derived low-pass and high-pass passive filter prototypes.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Design a constant-k low-pass T-section filter with cut-off frequency 5 kHz and nominal design impedance 600 ohm.", "marks": 10, "frequency": "Repeated 7 times"}]}
        ]
    ))

    # S4
    courses.append(make_c(
        "ect202-analog-ckt", "ECT 202", "Analog Circuits", 4, "Semester 4", "PCC",
        [
            {"module_no": 1, "title": "BJT & MOSFET Small Signal Models", "syllabus": "Biasing of BJT and MOSFET, Stability factor, Hybrid-pi model of BJT, Low frequency analysis of CE, CB, CC amplifiers, CS and CD MOSFET amplifiers.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive voltage gain, input impedance, and output impedance of CE amplifier using hybrid-pi small signal model.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Frequency Response of Amplifiers", "syllabus": "High frequency models of BJT and MOSFET, Miller's theorem, Low-frequency and high-frequency poles, Gain-bandwidth product, Multistage amplifiers.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "State and prove Miller's theorem. Determine high 3-dB cut-off frequency of a Common Emitter amplifier stage.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 3, "title": "Feedback Amplifiers", "syllabus": "General feedback structure, Properties of negative feedback, Feedback topologies: Voltage-series, Current-series, Voltage-shunt, Current-shunt, Stability analysis.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Analyze Voltage-Series negative feedback amplifier and prove that input impedance increases and output impedance decreases.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 4, "title": "Oscillators & Waveform Generators", "syllabus": "Barkhausen criteria for oscillation, RC phase shift oscillator, Wien bridge oscillator, Hartley, Colpitts, Crystal oscillators, Astable multivibrators.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive frequency of oscillation and minimum transistor gain h_fe required for sustained oscillations in RC phase shift oscillator.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 5, "title": "Power Amplifiers & Tuned Amplifiers", "syllabus": "Classification: Class A, Class B push-pull, Class AB, Class C, Conversion efficiency, Harmonic distortion, Single and double tuned amplifiers.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain operation of Class B push-pull power amplifier. Prove that maximum theoretical conversion efficiency is 78.5%.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    courses.append(make_c(
        "ect204-signals", "ECT 204", "Signals & Systems", 4, "Semester 4", "PCC",
        [
            {"module_no": 1, "title": "Signal & System Foundations", "syllabus": "Continuous-time and Discrete-time signals, Transformations, Energy and Power signals, LTI systems: Linearity, Time-invariance, Causality, BIBO stability.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Determine whether system y(t) = t * x(t) is linear, time-invariant, causal, and stable.", "marks": 7, "frequency": "Repeated 6 times"}]},
            {"module_no": 2, "title": "Convolution & Time-Domain Analysis", "syllabus": "Impulse response, Continuous convolution integral, Discrete convolution sum, Properties of convolution, Step response, Interconnected LTI systems.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Compute convolution of x[n] = (0.5)^n * u[n] with h[n] = u[n] and plot output sequence.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 3, "title": "Fourier Transform Analysis", "syllabus": "Continuous-Time Fourier Transform (CTFT), Properties: Duality, Time shifting, Frequency differentiation, Parseval's relation, Frequency response of LTI systems.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Find Fourier transform of rectangular pulse x(t) = 1 for |t| < T/2 and plot its sinc spectrum.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Laplace Transform in System Analysis", "syllabus": "Laplace transform, Region of Convergence (ROC) properties, Inverse Laplace transform, Transfer function H(s), Pole-zero plots, Stability and causality.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Find transfer function and impulse response for differential equation y''(t) + 5y'(t) + 6y(t) = x'(t) + x(t).", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "Z-Transform & Discrete Frequency Response", "syllabus": "Z-transform, ROC properties, Inverse Z-transform (Partial fractions, Residue), Discrete transfer function H(z), Stability analysis of discrete LTI systems.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Find inverse Z-transform of X(z) = z / (z - 1)(z - 2) for (a) |z| > 2, (b) 1 < |z| < 2, (c) |z| < 1.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]}
        ]
    ))

    # S4 continued
    courses.append(make_c(
        "ect206-comp-micro", "ECT 206", "Computer Architecture & Microcontrollers", 4, "Semester 4", "PCC",
        [
            {"module_no": 1, "title": "Computer Organization & Bus Structures", "syllabus": "Functional units of a computer, Von Neumann architecture, Bus structures, Memory locations and addresses, Memory operations, Instructions and instruction sequencing.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Von Neumann architecture and memory addressing modes with register transfer notations.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Pipelining & Processing Unit", "syllabus": "Fundamental concepts, Execution of a complete instruction, Multiple bus organization, Hardwired vs microprogrammed control, Pipelining hazards.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain pipeline hazards (structural, data, control hazards) and branch prediction mechanisms.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 3, "title": "8051 Microcontroller Architecture", "syllabus": "8051 architecture, Memory organization, Special Function Registers, Port structure, Timers and counters, Serial interface, Interrupts.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain 8051 internal architecture with ALU, PC, DPTR, register banks, and PSW.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 4, "title": "8051 Programming & Addressing Modes", "syllabus": "Addressing modes of 8051, Instruction set: Data transfer, Arithmetic, Logical, Boolean, Branching instructions, Assembly programs.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Write an 8051 assembly program to generate square wave of 2 kHz frequency using Timer 0 in Mode 1.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "ARM Processor Architecture Basics", "syllabus": "ARM design philosophy, RISC architecture, ARM Cortex-M architecture, Register set, Thumb-2 instruction set, Exception handling overview.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain ARM Cortex-M core registers and exception handling mechanism.", "marks": 10, "frequency": "Repeated 7 times"}]}
        ]
    ))

    # S5
    courses.append(make_c(
        "ect301-lic", "ECT 301", "Linear Integrated Circuits", 4, "Semester 5", "PCC",
        [
            {"module_no": 1, "title": "Operational Amplifier Fundamentals", "syllabus": "Differential amplifier, CMRR, Slew rate, Input offset voltage and current, Ideal and practical Op-Amp characteristics, Frequency compensation.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive expression for CMRR of differential amplifier. Explain high frequency compensation techniques.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Linear Applications of Op-Amp", "syllabus": "Inverting and Non-inverting amplifiers, Summing amplifier, Instrumentation amplifier, Integrator, Differentiator, Log and antilog amplifiers.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive output voltage expression for three Op-Amp Instrumentation Amplifier and discuss CMRR advantages.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Non-Linear Applications & Comparators", "syllabus": "Comparators, Schmitt trigger with hysteresis, Zero crossing detector, Peak detector, Precision rectifiers (Half-wave and Full-wave).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain inverting Schmitt trigger circuit. Derive expressions for Upper and Lower Threshold voltages (UTP and LTP).", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 4, "title": "Active Filters & Waveform Generators", "syllabus": "First and second-order low-pass and high-pass Butterworth filters, Astable and monostable multivibrators using Op-Amp, Triangular wave generator.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Design second-order Butterworth active lowpass filter with cut-off frequency 1 kHz and passband gain 2.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "Timers, PLL & Voltage Regulators", "syllabus": "IC 555 timer in astable and monostable modes, Phase Locked Loop (PLL IC 565), Lock range and Capture range, Voltage regulator IC 723.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain internal block diagram of IC 555 timer and derive frequency of oscillation in astable mode.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]}
        ]
    ))

    courses.append(make_c(
        "ect303-dsp", "ECT 303", "Digital Signal Processing", 4, "Semester 5", "PCC",
        [
            {"module_no": 1, "title": "Discrete Fourier Transform (DFT)", "syllabus": "DFT definition, IDFT, Properties: Circular shift, Circular convolution, Linear convolution via DFT.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Compute 8-point DFT of x[n] = {1, 2, 2, 1, 0, 0, 0, 0} and explain circular shift property.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Fast Fourier Transform (FFT)", "syllabus": "Radix-2 Decimation-in-Time (DIT) FFT, Decimation-in-Frequency (DIF) FFT, Butterfly operations, In-place computation, Computational complexity.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive Radix-2 DIT-FFT algorithm and draw complete 8-point butterfly signal flow graph.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "IIR Filter Design", "syllabus": "Analog filter prototypes: Butterworth and Chebyshev, Bilinear Transformation, Impulse Invariant transformation, Frequency warping effect.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Design digital Butterworth lowpass filter with passband edge 0.2 pi, stopband edge 0.6 pi using Bilinear Transformation.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 4, "title": "FIR Filter Design", "syllabus": "Linear phase conditions, Design of FIR filters using Windows (Rectangular, Hamming, Hanning, Blackman), Frequency sampling method.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Design linear phase FIR lowpass filter with cut-off frequency 0.5 rad/sample of length M = 7 using Hamming window.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "Filter Structures & Finite Word Length Effects", "syllabus": "Direct form I & II, Cascade, Parallel structures. Quantization errors, Limit cycle oscillations, Deadband effect.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Realize given second-order IIR system in Direct Form II and Cascade Form. Explain limit cycle oscillations.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    courses.append(make_c(
        "ect305-comms", "ECT 305", "Analog & Digital Communication", 4, "Semester 5", "PCC",
        [
            {"module_no": 1, "title": "Continuous Wave Amplitude Modulation", "syllabus": "AM fundamentals, DSB-SC, SSB-SC, VSB modulation, Envelop detectors, Costas loop, Superheterodyne AM receiver.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive expression for AM wave and explain envelope detection. Compare power and bandwidth of DSB-FC, DSB-SC, and SSB.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Angle Modulation & Demodulation", "syllabus": "Frequency Modulation (FM), Phase Modulation (PM), Carson's rule, Narrowband and Wideband FM, Armstrong indirect FM generation, Foster-Seeley discriminator.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Armstrong Indirect Method for FM generation with block diagram and frequency multipliers.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 3, "title": "Pulse Modulation & Baseband Transmission", "syllabus": "Sampling theorem, Aliasing, PAM, PWM, PPM, Pulse Code Modulation (PCM): Quantization noise, A-law and mu-law companding, Delta modulation.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain PCM transmission and reception. Derive expression for signal-to-quantization noise ratio (SQNR).", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 4, "title": "Digital Bandpass Modulation Techniques", "syllabus": "ASK, FSK, BPSK, QPSK, Constellation diagrams, Coherent detection of BPSK, Bit Error Rate (BER) comparisons.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain QPSK transmitter and receiver with constellation diagram and signal space analysis.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "Spread Spectrum Systems", "syllabus": "Pseudo-noise sequences, Direct Sequence Spread Spectrum (DSSS), Frequency Hopping Spread Spectrum (FHSS), Processing gain, Jamming margin.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Direct Sequence Spread Spectrum (DSSS) transmitter and receiver. Define processing gain.", "marks": 10, "frequency": "Repeated 7 times"}]}
        ]
    ))

    # S6
    courses.append(make_c(
        "ect302-emtl", "ECT 302", "Electromagnetics & Transmission Lines", 4, "Semester 6", "PCC",
        [
            {"module_no": 1, "title": "Electrostatics & Magnetostatics", "syllabus": "Coulomb's law, Gauss's law, Divergence theorem, Biot-Savart law, Ampere's circuital law, Stokes' theorem, Magnetic boundary conditions.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "State and prove Gauss's Law in electrostatics. Derive continuity equation from Ampere's law.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Maxwell's Equations & Boundary Conditions", "syllabus": "Displacement current, Maxwell's equations in differential and integral forms, Electromagnetic boundary conditions at media interfaces.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive Maxwell's four equations in differential and phasor forms. Explain displacement current concept.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Electromagnetic Wave Propagation", "syllabus": "Wave equation, Uniform plane waves in lossless and lossy media, Intrinsic impedance, Skin depth, Poynting vector and power flow.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "State and derive Poynting Theorem for electromagnetic energy flow in time-varying fields.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 4, "title": "Transmission Line Equations", "syllabus": "Transmission line parameters, Telegrapher's equations, Characteristic impedance Z0, Propagation constant, Reflection coefficient, VSWR.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive transmission line equations and expressions for characteristic impedance Z0 and propagation constant gamma.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "Smith Chart & Impedance Matching", "syllabus": "Smith chart fundamentals, Reflection coefficient, Input impedance, Quarter-wave transformer, Single-stub matching.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain single-stub shunt impedance matching using Smith chart with an illustrative numerical problem.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    courses.append(make_c(
        "ect304-vlsi", "ECT 304", "VLSI Circuit Design", 4, "Semester 6", "PCC",
        [
            {"module_no": 1, "title": "MOS Transistor Physics & CMOS Inverter", "syllabus": "MOS threshold voltage, I-V equations, Channel length modulation, Body effect, Static CMOS inverter: VTC characteristics, Noise margins, Propagation delays.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive switching threshold voltage V_th of static CMOS inverter and compute noise margins NM_H and NM_L.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Combinational CMOS Circuits", "syllabus": "Static CMOS logic gates, Euler path for stick diagrams, Layout design rules (Lambda based), Dynamic CMOS logic: Pre-charge and evaluate, Domino logic.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Design CMOS complex logic gate for Y = !((A + B) * (C + D)). Draw Euler path and stick diagram.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Sequential Logic Circuits & Memory", "syllabus": "Static latches and flip-flops, Transmission gate registers, Dynamic latches, SRAM 6T cell read/write operation, DRAM 1T cell refresh operation.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain 6T SRAM cell architecture. Detail read and write operational cycles with timing diagrams.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Data Path Subsystems", "syllabus": "High-speed adders: Carry Lookahead, Carry Select, Carry Skip adders, Multipliers: Wallace Tree multiplier, Baugh-Wooley array multiplier, Barrel shifters.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Design 16-bit Carry Select Adder (CSA) and compare its propagation delay with Ripple Carry Adder.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "VLSI Testing & Design for Testability (DFT)", "syllabus": "Fault models: Stuck-at-0 and Stuck-at-1 faults, D-algorithm for test generation, Scan-path architecture, Built-In Self-Test (BIST), Boundary Scan (JTAG).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Boundary Scan architecture (IEEE 1149.1) with TAP controller and instruction register.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    # S7
    courses.append(make_c(
        "ect401-microwave", "ECT 401", "Microwave & Antenna Engineering", 4, "Semester 7", "PCC",
        [
            {"module_no": 1, "title": "Microwave Waveguides & S-Parameters", "syllabus": "Rectangular waveguides: TE and TM modes, Cut-off frequency, Wave impedance, S-parameters properties, Magic Tee, Directional couplers, Isolators.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive scattering matrix (S-matrix) of Magic Tee. Explain its application as a balanced duplexer.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Microwave Sources & Tubes", "syllabus": "Two-cavity klystron amplifier, Velocity modulation, Reflex klystron oscillator, Magnetron, Gunn diode: Gunn effect, Ridley-Watkins-Hilsum theory.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain bunching process and velocity modulation in two-cavity klystron with Applegate diagram.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 3, "title": "Antenna Fundamentals", "syllabus": "Radiation mechanism, Current distribution on thin dipoles, Radiation patterns, Gain, Directivity, Radiation resistance, Friis transmission formula.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive radiation resistance and directivity of an oscillating half-wave dipole antenna (R_rad = 73 ohm).", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 4, "title": "Wire & Aperture Antennas", "syllabus": "Small loop antenna, Horn antennas: E-plane, H-plane sectoral horns, Parabolic reflector antennas: Cassegrain feed, Microstrip patch antenna design.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain working and feeding mechanisms of parabolic reflector antenna with aperture efficiency calculation.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "Antenna Arrays & Wave Propagation", "syllabus": "Two-element arrays, Uniform linear arrays: Broadside and End-fire arrays, Pattern multiplication, Ground wave, Sky wave, and Space wave propagation.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "State and explain principle of pattern multiplication. Find null directions for 4-element broadside array.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    courses.append(make_c(
        "ect403-wireless-comm", "ECT 403", "Wireless & Mobile Communication", 4, "Semester 7", "PCC",
        [
            {"module_no": 1, "title": "Cellular Concept & System Design", "syllabus": "Frequency reuse, Channel assignment strategies, Handoff strategies, Interference: Co-channel and Adjacent channel, Cell splitting, Sectoring.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain cellular frequency reuse concept. Derive expression for capacity improvement by cell splitting.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Mobile Radio Propagation & Fading", "syllabus": "Free space propagation, Reflection, Diffraction, Scattering, Log-distance path loss model, Small-scale fading: Multipath, Doppler shift, Rayleigh and Rician distributions.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain small-scale multipath propagation mechanisms. Contrast Rayleigh and Rician fading distributions.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 3, "title": "Multiple Access & Modulation Techniques", "syllabus": "CDMA principles, PN sequences, Near-far problem, Orthogonal Frequency Division Multiplexing (OFDM), Cyclic prefix, PAPR reduction.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain OFDM transmitter and receiver architecture with cyclic prefix role in mitigating ISI.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Diversity, Equalization & MIMO", "syllabus": "Equalization: Linear vs Decision feedback, Diversity: Space, Time, Frequency, Maximal Ratio Combining (MRC), MIMO systems: Spatial multiplexing, Beamforming.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain MIMO architecture. Differentiate between spatial multiplexing and space-time block coding (Alamouti scheme).", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 5, "title": "4G LTE & 5G NR Standards", "syllabus": "LTE architecture (E-UTRAN, EPC), 5G New Radio (NR) architecture, Massive MIMO, Millimeter-wave communication, Network Slicing, URLLC.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain 5G standalone architecture with Network Slicing and Service-Based Architecture (SBA).", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    # S8
    courses.append(make_c(
        "ect402-opt-sat", "ECT 402", "Optical & Satellite Communication", 4, "Semester 8", "PCC",
        [
            {"module_no": 1, "title": "Optical Fiber Transmission Principles", "syllabus": "Ray theory, Numerical aperture, Acceptance angle, Single-mode and Multi-mode fibers, Attenuation mechanisms: Rayleigh scattering, Material absorption.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive expression for Numerical Aperture and acceptance angle of step-index optical fiber.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Dispersion & Optical Components", "syllabus": "Intermodal dispersion, Intramodal dispersion (Material and Waveguide dispersion), Optical sources: Laser diode, Photodetectors: PIN and APD photodiodes.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Avalanche Photodiode (APD) operation, multiplication factor, and quantum efficiency.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 3, "title": "Optical Link Design & WDM", "syllabus": "Point-to-point link design, Power budget analysis, Rise-time budget, Wavelength Division Multiplexing (WDM) architecture, EDFA optical amplifiers.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Perform link power budget and rise-time budget analysis for a 50 km optical link operating at 2.5 Gbps.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Satellite Orbits & Mechanics", "syllabus": "Kepler's laws, Orbital elements, GEO, LEO, MEO orbits, Look angle determination: Azimuth and Elevation angles, Orbital perturbations.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "State Kepler's laws. Calculate look angles (azimuth and elevation) for a geostationary satellite from an earth station.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 5, "title": "Satellite Subsystems & Link Budget", "syllabus": "Spacecraft subsystems: TT&C, Power, Altitude control; Transponders, Earth station design, Satellite link budget: Carrier-to-Noise ratio (C/N), G/T ratio.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive satellite uplink and downlink budget equation for received Carrier-to-Noise ratio (C/N).", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    return courses
