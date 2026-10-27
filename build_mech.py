"""
Mechanical Engineering Courses Builder (S3 to S8) for KTU 2024 Scheme
"""

def get_mech_courses():
    courses = []

    def make_c(cid, code, title, credits, sem, cat, mods):
        return {
            "id": cid,
            "code": code,
            "title": title,
            "credits": credits,
            "semester": sem,
            "branch": "Mechanical Engineering",
            "branch_id": "mech",
            "category": cat,
            "modules": mods
        }

    # S3
    courses.append(make_c(
        "met201-mechanics-solids", "MET 201", "Mechanics of Solids", 4, "Semester 3", "PCC",
        [
            {"module_no": 1, "title": "Stress, Strain & Elastic Constants", "syllabus": "Normal and shear stresses, Hooke's law, Stress-strain diagram for ductile and brittle materials, Poisson's ratio, Elastic constants E, G, K, Thermal stresses in composite bars.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive relationship between Young's Modulus (E), Modulus of Rigidity (G), and Bulk Modulus (K).", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 2, "title": "Principal Stresses & Mohr's Circle", "syllabus": "Stresses on inclined planes, Principal stresses and principal planes, Mohr's circle for plane stress, Theories of failure: Maximum Principal Stress, Maximum Shear Stress, Distortion Energy theory.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "State Von Mises (Distortion Energy) and Tresca (Maximum Shear Stress) theories of failure with graphical representations.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 3, "title": "Shear Force & Bending Moment in Beams", "syllabus": "Types of beams and loadings, Shear force and bending moment diagrams for Cantilever, Simply Supported, and Overhanging beams with point loads, UDL, and UVL, Point of contraflexure.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Draw SFD and BMD for simply supported beam of span 6m carrying UDL of 4 kN/m over left half and point load of 10 kN at 4m from left support.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 4, "title": "Stresses in Beams & Torsion", "syllabus": "Pure bending theory, Flexure formula (M/I = sigma/y = E/R), Section modulus, Shear stress distribution across I, T, and rectangular sections, Torsion of circular solid and hollow shafts.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive torsion equation T/J = tau/r = G*theta/L for circular shaft and compare torque transmitting capacity of solid vs hollow shafts.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "Deflection of Beams & Thin Cylinders", "syllabus": "Differential equation of elastic curve, Macaulay's method for beam deflection, Moment-area theorems, Thin cylinders and spheres: Hoop stress, Longitudinal stress, Volumetric strain.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Determine slope at supports and maximum deflection for simply supported beam carrying central point load using Macaulay's method.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    courses.append(make_c(
        "met203-thermo", "MET 203", "Engineering Thermodynamics", 4, "Semester 3", "PCC",
        [
            {"module_no": 1, "title": "First Law & Energy Conservation", "syllabus": "Macroscopic vs Microscopic view, Thermodynamic equilibrium, Quasi-static process, First Law applied to non-flow and steady flow processes, SFEE.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive Steady Flow Energy Equation (SFEE) and apply it to steam nozzles and gas turbines.", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}]},
            {"module_no": 2, "title": "Second Law & Entropy", "syllabus": "Kelvin-Planck and Clausius statements, Carnot cycle, Carnot theorem, Clausius inequality, Definition and physical concept of Entropy, Principle of increase of entropy.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "State and prove Clausius Inequality. Deduce that entropy of the universe is continually increasing.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Availability & Pure Substances", "syllabus": "Exergy, Availability, Irreversibility, Gouy-Stodola theorem. Pure substances: p-v-T surfaces, Mollier diagram, Quality of steam, Steam calorimeters.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain dryness fraction measurement of steam using Throttling and Separating Calorimeter.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Thermodynamic Relations & Gas Mixtures", "syllabus": "Maxwell's relations, T-ds equations, Joule-Thomson coefficient, Inversion curve, Dalton's law of partial pressures, Amagat's law.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive Maxwell's four thermodynamic relations from fundamental property relations.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 5, "title": "Air Standard Power Cycles", "syllabus": "Otto cycle, Diesel cycle, Dual combustion cycle, Brayton cycle, Thermal efficiency expressions, Mean effective pressure (MEP), Comparison of cycles.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive expression for air standard efficiency and mean effective pressure (MEP) of Diesel cycle.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]}
        ]
    ))

    courses.append(make_c(
        "met205-materials", "MET 205", "Metallurgy & Material Science", 4, "Semester 3", "PCC",
        [
            {"module_no": 1, "title": "Crystallography & Crystal Imperfections", "syllabus": "Crystal structures (BCC, FCC, HCP), Miller indices, Point defects, Line defects: Edge and Screw dislocations, Burger's vector, Surface and volume defects.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Calculate atomic packing factor (APF) for BCC and FCC crystal structures. Explain Edge and Screw dislocations with Burger's vector.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Phase Diagrams & Solidification", "syllabus": "Gibbs phase rule, Hume-Rothery rules for solid solution, Lever rule, Binary isomorphous and eutectic phase systems, Invariant reactions: Eutectic, Peritectic, Eutectoid.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "State and apply Lever Rule to calculate phase fractions in a binary eutectic phase diagram.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Iron-Carbon Equilibrium Diagram", "syllabus": "Fe-Fe3C equilibrium phase diagram, Microstructures: Ferrite, Austenite, Cementite, Pearlite, Ledeburite, Invariant reactions in Fe-C system, Critical temperatures.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Draw neat Iron-Carbon (Fe-Fe3C) equilibrium diagram labeling all phases, temperatures, and invariant reactions (Peritectic, Eutectic, Eutectoid).", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 4, "title": "Heat Treatment of Steels", "syllabus": "TTT and CCT diagrams, Annealing (Full, Process, Spheroidizing), Normalizing, Hardening, Tempering, Austempering, Martempering, Surface hardening: Carburizing, Nitriding.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Draw Time-Temperature-Transformation (TTT) diagram for eutectoid steel and explain Austempering and Martempering processes.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 5, "title": "Engineering Alloys & Mechanical Testing", "syllabus": "Cast irons (Gray, White, Spheroidal, Malleable), Alloy steels, Non-ferrous alloys: Brasses, Bronzes, Aluminum alloys, Tensile test, Charpy impact test, Hardness testing (Brinell, Rockwell).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Differentiate between Gray cast iron and Spheroidal graphite cast iron in terms of microstructure, properties, and applications.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    # S4
    courses.append(make_c(
        "met202-fluid", "MET 202", "Fluid Mechanics & Machinery", 4, "Semester 4", "PCC",
        [
            {"module_no": 1, "title": "Fluid Statics & Buoyancy", "syllabus": "Fluid properties, Viscosity, Hydrostatic law, Pressure measurement: Manometers, Total pressure and Center of pressure on submerged surfaces, Buoyancy and Metacenter.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive expression for total hydrostatic force and depth of center of pressure for vertically submerged plane surface.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Fluid Kinematics & Bernoulli's Equation", "syllabus": "Continuity equation in 3D Cartesian coordinates, Stream function and Velocity potential function, Euler's equation of motion, Bernoulli's equation and applications (Venturimeter, Pitot tube).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive Bernoulli's equation from Euler's equation of motion along a streamline. State assumptions made.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Flow Through Pipes & Losses", "syllabus": "Laminar and turbulent flow, Hagen-Poiseuille equation for viscous flow through circular pipes, Darcy-Weisbach equation for friction loss, Hydraulic gradient line (HGL) and Total energy line (TEL).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive Hagen-Poiseuille equation for laminar flow through circular pipe. Prove maximum velocity is twice mean velocity.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 4, "title": "Hydraulic Turbines", "syllabus": "Impact of jets on vanes, Pelton wheel: Velocity triangles, Work done, Hydraulic efficiency, Francis turbine, Kaplan turbine, Specific speed, Unit quantities, Cavitation in turbines.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Draw velocity triangles for Pelton wheel bucket. Derive formula for hydraulic efficiency and maximum efficiency condition.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 5, "title": "Hydraulic Pumps", "syllabus": "Centrifugal pumps: Working principle, Impeller types, Manometric head, Manometric efficiency, Priming, Minimum starting speed, Net Positive Suction Head (NPSH), Reciprocating pumps: Air vessels.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain working of centrifugal pump with neat sketch. Derive expression for minimum starting speed of centrifugal pump.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    courses.append(make_c(
        "met204-manufacturing", "MET 204", "Manufacturing Processes", 4, "Semester 4", "PCC",
        [
            {"module_no": 1, "title": "Metal Casting & Gating Design", "syllabus": "Pattern materials and allowances, Molding sand properties, Cores, Gating and risering systems, Solidification of metals (Chvorinov's rule), Special casting: Die, Centrifugal, Investment casting.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain gating system components (Sprue, Runner, Ingate, Riser). State and apply Chvorinov's Rule for solidification time.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 2, "title": "Fusion & Solid-State Welding", "syllabus": "Arc welding: SMAW, TIG, MIG; Oxy-acetylene welding, Resistance welding: Spot and seam; Friction welding, Heat Affected Zone (HAZ), Welding defects.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain TIG and MIG welding processes with schematics. Compare shielding gases and electrode consumptions.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 3, "title": "Metal Forming Processes", "syllabus": "Hot and cold working, Rolling: Rolling mills, Angle of bite, Forging: Open die, Closed die, Flash, Extrusion: Forward and backward, Wire drawing.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain rolling process mechanics and derive expression for maximum reduction in pass (delta_h = mu^2 * R).", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Sheet Metal Working", "syllabus": "Press working tools: Punch and die, Shearing operations: Blanking, Piercing, Clearance calculation, Bending: Springback, Deep drawing: Drawing ratio.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Differentiate between blanking and piercing operations with neat sketches. Calculate punch and die sizes with clearance.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "Plastics Processing & Powder Metallurgy", "syllabus": "Injection molding, Blow molding, Extrusion molding of polymers, Powder metallurgy: Production of metal powders, Compacting, Sintering operations.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain screw injection molding process for thermoplastics with cycle time stages and tooling sketch.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    courses.append(make_c(
        "met206-machine-tools", "MET 206", "Machine Tools & Metrology", 4, "Semester 4", "PCC",
        [
            {"module_no": 1, "title": "Mechanics of Metal Cutting", "syllabus": "Orthogonal vs oblique cutting, Chip formation types, Merchant's force circle, Cutting tool geometry (ASA and ORS systems), Taylor's tool life equation.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Draw Merchant's Circle Diagram of forces in orthogonal cutting and derive expressions for shear force and friction force.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 2, "title": "Lathe, Shaper & Milling Machines", "syllabus": "Center lathe operations: Taper turning, Thread cutting; Shaper: Whitworth quick return mechanism; Milling: Up vs Down milling, Simple and differential indexing.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain differential indexing on milling machine. Calculate index crank movement for cutting gear with 73 teeth.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 3, "title": "Drilling, Boring & Grinding", "syllabus": "Drilling machines, Twist drill geometry, Boring machines, Grinding wheels: Abrasives, Grain size, Grade, Structure, Bonds, Dressing and truing.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain grinding wheel specification code (e.g., 51 A 46 H 5 V 8) and differentiate between dressing and truing.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Linear, Angular & Surface Metrology", "syllabus": "Slip gauges, Comparators (Mechanical, Pneumatic), Sine bar for angle measurement, Surface roughness parameters: Ra, Rz, Profilometers.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain measurement of taper angle using sine bar and slip gauges with derivations and limitation precautions.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "Limits, Fits, Tolerances & CMM", "syllabus": "System of limits and fits (Hole basis and Shaft basis per IS 919), Taylor's principle for limit gauge design (GO and NO-GO gauges), Coordinate Measuring Machines (CMM).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "State Taylor's Principle of limit gauge design. Design progressive plug gauge for hole of 25 H7.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]}
        ]
    ))

    # S5
    courses.append(make_c(
        "met301-mechanics-machinery", "MET 301", "Mechanics of Machinery", 4, "Semester 5", "PCC",
        [
            {"module_no": 1, "title": "Kinematic Chains & Inversions", "syllabus": "Degrees of freedom, Kutzbach and Grubler's criteria, Kinematic inversions of four-bar chain and single slider-crank chain, Quick return motion mechanisms.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain inversions of four-bar mechanism and slider-crank chain with neat diagrams and engineering applications.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Velocity & Acceleration Analysis", "syllabus": "Instantaneous center method, Kennedy's theorem, Relative velocity method, Acceleration diagrams for mechanisms, Coriolis acceleration component.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Coriolis component of acceleration. Derive its magnitude a_c = 2 * omega * v and discuss direction rules.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Cams & Follower Dynamics", "syllabus": "Types of cams and followers, Displacement, velocity, and acceleration diagrams for Uniform velocity, SHM, and Cycloidal motions, Cam profile synthesis.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Draw cam profile for knife-edge follower with stroke 40mm, outstroke with SHM, dwell, and return with uniform acceleration.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Gears & Epicyclic Gear Trains", "syllabus": "Law of gearing, Involute and Cycloidal profiles, Interference and undercutting, Minimum number of teeth on pinion, Epicyclic gear trains: Tabular and algebraic methods.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive expression for minimum number of teeth on pinion to avoid interference with a standard gear wheel.", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}]},
            {"module_no": 5, "title": "Governors & Gyroscopes", "syllabus": "Centrifugal governors: Watt, Porter, Proell, Hartnell governors, Sensitiveness, Hunting, Stability, Gyroscopic couple on aeroplanes, naval ships, and four-wheeled automobiles.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain gyroscopic effect on a naval ship during steering, pitching, and rolling with direction of gyroscopic couple.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]}
        ]
    ))

    courses.append(make_c(
        "met303-thermal", "MET 303", "Thermal Engineering & IC Engines", 4, "Semester 5", "PCC",
        [
            {"module_no": 1, "title": "Steam Power Cycles & Boilers", "syllabus": "Rankine cycle with reheat and regeneration, High pressure water tube boilers (Benson, Lamont), Boiler mountings and accessories, Equivalent evaporation, Boiler efficiency.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain reheat Rankine cycle with T-s and h-s diagrams. Derive expression for thermal efficiency.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Steam Nozzles & Turbines", "syllabus": "Flow through steam nozzles, Critical pressure ratio, Nozzle efficiency, Compounding of impulse steam turbines (Velocity and Pressure compounding), Reaction turbines, Stage efficiency.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive expression for critical pressure ratio for maximum discharge through steam nozzle for superheated steam.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Combustion in SI & CI Engines", "syllabus": "Combustion stages in SI engines, Flame propagation, Detonation and knocking, Octane rating, Combustion stages in CI engines, Ignition delay, Diesel knock, Cetane rating.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain stages of combustion in CI engine with p-theta diagram. Contrast knocking phenomenon in SI vs CI engines.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 4, "title": "Engine Performance & Heat Balance", "syllabus": "Measurement of indicated and brake power (Dynamometers), Morse test for multi-cylinder engines, Volumetric efficiency, Heat balance sheet preparation.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Morse Test for determining indicated power of multi-cylinder petrol engine with mathematical procedure.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "Gas Turbines & Jet Propulsion", "syllabus": "Open and closed cycle gas turbines, Brayton cycle with reheat, intercooling and regeneration, Turbojet, Turboprop, and Rocket engines.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain Brayton cycle with intercooling, reheating, and regeneration. Draw T-s diagram and explain efficiency gains.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    # S6
    courses.append(make_c(
        "met302-hmt", "MET 302", "Heat & Mass Transfer", 4, "Semester 6", "PCC",
        [
            {"module_no": 1, "title": "Conduction Heat Transfer", "syllabus": "Fourier's law of heat conduction, General heat conduction equation in Cartesian and Cylindrical coordinates, Critical thickness of insulation, Extended surfaces (Fins).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive expression for temperature distribution and heat dissipation in a pin fin with insulated tip.", "marks": 10, "frequency": "Repeated 8 times (Guaranteed)"}]},
            {"module_no": 2, "title": "Transient Conduction & Convection Basics", "syllabus": "Lumped system analysis, Biot and Fourier numbers, Boundary layer concept in convection, Dimensional analysis: Buckingham Pi theorem, Nusselt, Prandtl, Reynolds numbers.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive criteria for lumped capacitance analysis (Bi < 0.1) and temperature response equation.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 3, "title": "Forced & Natural Convection", "syllabus": "Flow over flat plates and cylinders, Empirical correlations for laminar and turbulent flows, Natural convection over vertical and horizontal plates, Grashof number.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain significance of Reynolds, Prandtl, Nusselt, and Grashof numbers in convective heat transfer.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Radiation Heat Transfer", "syllabus": "Blackbody radiation laws: Planck's law, Wien's displacement law, Stefan-Boltzmann law, Radiation shape factors, Radiosity and irradiation, Radiation shields.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive expression for heat exchange between two infinite parallel gray planes with and without radiation shield.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 5, "title": "Heat Exchangers & Mass Transfer", "syllabus": "Classification, Logarithmic Mean Temperature Difference (LMTD) for parallel and counterflow, NTU-effectiveness method, Fick's first law of diffusion.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive Logarithmic Mean Temperature Difference (LMTD) expression for counterflow heat exchanger.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]}
        ]
    ))

    courses.append(make_c(
        "met304-vibrations", "MET 304", "Dynamics of Machinery & Vibrations", 4, "Semester 6", "PCC",
        [
            {"module_no": 1, "title": "Balancing of Rotating Masses", "syllabus": "Static and dynamic balancing, Balancing of several masses rotating in same plane and in different parallel planes, Analytical and graphical methods.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Four masses m1, m2, m3, m4 rotate in different planes at radii r1, r2, r3, r4. Find magnitude and position of balance masses.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 2, "title": "Balancing of Reciprocating Masses", "syllabus": "Primary and secondary unbalanced forces, Partial balancing of locomotives, Swaying couple, Hammer blow, Balancing of multi-cylinder in-line engines, V-engines.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain hammer blow, swaying couple, and variation in tractive force in partial balancing of two-cylinder locomotive.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Free Undamped & Damped Vibrations", "syllabus": "Single degree of freedom systems, Newton's method, Energy method, Viscous damping: Underdamped, critically damped, overdamped systems, Logarithmic decrement.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive expression for logarithmic decrement delta in underdamped spring-mass-damper system.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Forced Vibrations & Vibration Isolation", "syllabus": "Harmonic excitation, Magnification factor, Resonance, Vibration isolation and transmissibility, Whirling of rotating shafts, Critical speed.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Derive expression for force transmissibility and explain vibration isolation design criteria.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 5, "title": "Two Degree of Freedom & Torsional Vibrations", "syllabus": "Natural frequencies and normal modes of 2-DOF systems, Dynamic vibration absorber, Torsional vibrations of single-rotor, two-rotor, and three-rotor systems.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Find natural frequencies and mode shapes of two-rotor torsional vibration system.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    # S7
    courses.append(make_c(
        "met401-machine-design", "MET 401", "Design of Machine Elements", 4, "Semester 7", "PCC",
        [
            {"module_no": 1, "title": "Design for Static & Variable Loads", "syllabus": "Design procedure, Factors of safety, Stress concentration factors, Fatigue failure: S-N curves, Endurance limits, Soderberg, Goodman, and Gerber design criteria.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "A machine component subjected to completely reversed bending stress is made of steel with S_ut = 600 MPa. Determine endurance limit using Soderberg and Goodman lines.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 2, "title": "Design of Shafts, Keys & Couplings", "syllabus": "Design of shafts based on strength, torsional rigidity, ASME design code, Sunk keys, Feather keys, Design of rigid flange coupling and bushed-pin flexible coupling.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Design a protected type cast iron flange coupling to transmit 15 kW power at 960 rpm from an electric motor to a compressor.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 3, "title": "Fasteners & Welded Joints", "syllabus": "Threaded fasteners under static and eccentric loads, Initial tension, Bolt of uniform strength, Welded joints: Transverse and parallel fillet welds under static and eccentric loads.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Design a welded joint for a bracket carrying an eccentric load of 25 kN at an eccentricity of 150mm from structural column.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Mechanical Springs", "syllabus": "Helical compression and tension springs, Stress and deflection equations, Wahl's stress concentration factor, Concentric springs, Multi-leaf springs: Semi-elliptic leaf spring design.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Design a helical compression spring for safety valve operating at pressure 1.2 MPa with spring index C = 6 and allowable shear stress 450 MPa.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 5, "title": "Bearings & Lubrication", "syllabus": "Sliding contact bearings: Petroff's equation, Hydrodynamic lubrication, Sommerfeld number, Bearing design; Rolling contact bearings: Deep groove ball bearings, Rating life, L10 life calculation.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Select a deep groove ball bearing to carry radial load 4 kN and thrust load 2.5 kN operating at 1440 rpm for 90% survival probability after 10000 hours.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    courses.append(make_c(
        "met403-mechatronics", "MET 403", "Mechatronics & Automation", 4, "Semester 7", "PCC",
        [
            {"module_no": 1, "title": "Sensors & Transducers in Mechatronics", "syllabus": "Mechatronic design process, Sensors: Potentiometers, LVDT, Optical encoders, Hall effect sensors, Thermocouples, Piezoelectric sensors.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain construction and operation of incremental and absolute optical rotary encoders for angular displacement measurement.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Actuators: Pneumatic, Hydraulic & Electrical", "syllabus": "Pneumatic and hydraulic actuators, Directional control valves (3/2, 4/2, 5/2 valves), Solenoid valves, Stepper motors, Servomotors.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain working of 4/2 and 5/2 pilot operated directional control valves with pneumatic circuit diagrams.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 3, "title": "Programmable Logic Controllers (PLC)", "syllabus": "PLC architecture, Input/Output modules, Ladder logic programming: NO/NC contacts, Internal relays, Timers (TON, TOF), Counters (CTU, CTD).", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Develop PLC ladder logic program for automatic bottle filling and capping conveyor line with timers and photo sensors.", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 4, "title": "Microcontrollers & Signal Conditioning", "syllabus": "Operational amplifier signal conditioning circuits (Instrumentation amplifier, Active filters, ADC/DAC), Microcontroller interfacing with H-bridge motor drivers.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Design H-bridge DC motor driver circuit using MOSFETs and explain PWM speed control.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 5, "title": "Industrial Robotics & Automation", "syllabus": "Robot anatomy, Coordinate systems (Cartesian, Cylindrical, Spherical, Articulated, SCARA), Forward and inverse kinematics, SCADA architecture.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Compare SCARA and 6-axis Articulated robots in terms of workspace, degrees of freedom, and assembly applications.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    # S8
    courses.append(make_c(
        "met402-power-plant", "MET 402", "Power Plant Engineering & Renewable Energy", 4, "Semester 8", "PCC",
        [
            {"module_no": 1, "title": "Thermal Power Plant Cycles", "syllabus": "Rankine cycle with reheat and regeneration, Supercritical boiler layouts, Coal handling, Pulverizers, Electrostatic precipitators (ESP), Cooling towers.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain regenerative Rankine cycle with open and closed feedwater heaters. Draw T-s diagram and derive thermal efficiency.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 2, "title": "Hydroelectric & Nuclear Power Plants", "syllabus": "Hydro plant classification, Flow duration curve, Mass curve, Surge tanks; Nuclear reactors: PWR, BWR, CANDU, Fast Breeder Reactor (FBR), Nuclear waste disposal.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Describe working of Pressurized Water Reactor (PWR) and Boiling Water Reactor (BWR) with neat coolant circulation schematics.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 3, "title": "Power Plant Economics & Tariffs", "syllabus": "Load curves, Base load and peak load plants, Load factor, Capacity factor, Diversity factor, Capital and operating costs, Tariffs: Two-part and Three-part tariffs.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Define Load Factor, Plant Capacity Factor, and Reserve Margin. Discuss their economic impacts on cost per kWh of electricity.", "marks": 10, "frequency": "Repeated 8 times"}]},
            {"module_no": 4, "title": "Solar & Wind Energy Systems", "syllabus": "Solar radiation geometry, Flat plate collectors, Photovoltaic cell characteristics, Maximum power point tracking (MPPT), Wind turbine aerofoil mechanics, Betz limit.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "State and prove Betz limit for maximum theoretical power extraction from wind (Cp_max = 16/27 = 59.3%).", "marks": 10, "frequency": "Repeated 9 times (Guaranteed)"}]},
            {"module_no": 5, "title": "Biomass & Ocean Energy Systems", "syllabus": "Biomass gasification, Fixed and fluidized bed gasifiers, Biogas plants, Ocean Thermal Energy Conversion (OTEC): Claude and Anderson cycles, Tidal power plants.", "weightage_marks": 15, "high_yield_pyqs": [{"q": "Explain closed-cycle OTEC system (Anderson cycle) operating with ammonia as working fluid. Discuss site requirements.", "marks": 10, "frequency": "Repeated 8 times"}]}
        ]
    ))

    return courses
