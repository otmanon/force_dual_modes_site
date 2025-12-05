"""
Demo of the contact interaction adaptive subspace method.

This demo takes as input a config.json file, which specifies the following:

"mesh_file": "path/to/mesh.obj",
"force_distribution": "force_distribution.npy", # force distribution on the mesh
"subspace_params": {
    "m": 10,
}
"cubature_params": {
    "k": 100,
}
"sim_params": {
    "h": 0.01, # time step
    "rho": 1e3, # density of the material
    "ym": 1e6, # Young's modulus of the material
    "pr": 0.4,  # Poisson's ratio of the material
    "material": "fcr", # material of the mesh
    "bI": [], # indices of the boundary vertices
    "solver_p": {
        "max_iter": 100,
        "do_line_search": True,
        "tol": 1e-6, # tolerance for the Newton solver
        "max_time": 10, # maximum time for the simulation
        "verbose": True # whether to print verbose output
    }
}
"""

