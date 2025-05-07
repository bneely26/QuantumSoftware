import numpy as np

class IsingHamiltonian:
    """
    Class representing the Ising model Hamiltonian.
    """
    def __init__(self, graph):
        """
        Initialize an Ising model Hamiltonian from a NetworkX graph.
        """
        self.G = graph  # Store as self.G to match the usage in energy method
        self.num_sites = graph.number_of_nodes()
        
        # Store edge weights (J values) in a list or array
        # This is what your code is trying to access as ham.J
        self.J = []
        for e in self.G.edges:
            weight = self.G.edges[e].get('weight', 1.0)  # Default to 1.0 if weight not specified
            self.J.append(weight)
            
        # Default values for mu (all zero)
        self.mu = np.zeros(self.num_sites)
    
    def set_mu(self, mu_values):
        """
        Set the values of the magnetic field terms.
        """
        if len(mu_values) != self.num_sites:
            raise ValueError(f"Expected {self.num_sites} mu values, got {len(mu_values)}")
        
        self.mu = np.array(mu_values)
    
    def energy(self, bs):
        """
        Calculate the energy of a given bit string configuration.
        
        Parameters:
        -----------
        bs : BitString
            The spin configuration to calculate energy for
            
        Returns:
        --------
        energy : float
            The energy of the configuration
        """
        energy = 0.0
        
        # Interaction term: sum over edges J_ij * s_i * s_j
        for i, j in self.G.edges:
            # Convert bits (0,1) to spins (-1,1)
            si = 1 if bs.config[i] else -1
            sj = 1 if bs.config[j] else -1
            
            # Get the interaction strength (J) from the graph
            J_ij = self.G.edges[i, j].get('weight', 1.0)
            
            # Add the interaction energy
            energy += J_ij * si * sj
            
        # External field term: sum over sites mu_i * s_i
        for i in range(self.num_sites):
            si = 1 if bs.config[i] else -1
            energy += self.mu[i] * si
            
        return energy
    
    def compute_average_values(self, T):
        """
        Compute exact average values for energy, magnetization, heat capacity,
        and magnetic susceptibility at temperature T.
        
        Parameters:
        -----------
        T : float
            Temperature at which to calculate averages
            
        Returns:
        --------
        E : float
            Average energy
        M : float
            Average magnetization
        HC : float
            Heat capacity
        MS : float
            Magnetic susceptibility
        """
        # This would calculate exact ensemble averages by enumerating all states
        # For small systems, this is feasible
        
        # Initialize accumulators
        Z = 0.0  # Partition function
        E_avg = 0.0
        E2_avg = 0.0
        M_avg = 0.0
        M2_avg = 0.0
        
        # Generate all possible bit configurations for N sites
        from itertools import product
        from montecarlo.bitstring import BitString
        
        for bits in product([0, 1], repeat=self.num_sites):
            # Create BitString from bits
            bs = BitString(self.num_sites)
            for i, bit in enumerate(bits):
                if bit:
                    bs.flip_site(i)  # Set to 1 if bit is 1 (assuming BitString initializes to all 0s)
            
            # Calculate energy and magnetization
            E = self.energy(bs)
            
            # Calculate magnetization (sum of spins)
            M = sum(1 if bit else -1 for bit in bits)
            
            # Boltzmann weight
            weight = np.exp(-E / T)
            
            # Update accumulators
            Z += weight
            E_avg += E * weight
            E2_avg += E**2 * weight
            M_avg += M * weight
            M2_avg += M**2 * weight
        
        # Normalize by partition function
        E_avg /= Z
        E2_avg /= Z
        M_avg /= Z
        M2_avg /= Z
        
        # Calculate heat capacity and magnetic susceptibility
        HC = (E2_avg - E_avg**2) / (T**2)
        MS = (M2_avg - M_avg**2) / T
        
        return E_avg, M_avg, HC, MS