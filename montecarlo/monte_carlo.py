import numpy as np
from montecarlo.bitstring import BitString

class MonteCarlo:
    def __init__(self, hamiltonian):

        self.ham = hamiltonian
        self.num_sites = self.ham.num_sites
    
    def run(self, T, n_samples=10000, n_burn=100):
        # Initialize a random configuration
        config = BitString(self.num_sites)
        
        # Initialize arrays to store energy and magnetization
        E = []
        M = []
        
        # Burn-in period
        for _ in range(n_burn):
            self._metropolis_step(config, T)
        
        # Sampling period
        for _ in range(n_samples):
            self._metropolis_step(config, T)
            
            # Calculate energy and magnetization
            energy = self.ham.energy(config)
            magnetization = self._calculate_magnetization(config)
            
            # Store values
            E.append(energy)
            M.append(magnetization)
        
        return E, M
    
    def _metropolis_step(self, config, T):
        
        for site in range(self.num_sites):
            # Store the current energy
            current_energy = self.ham.energy(config)
            
            # Flip a spin
            config.flip_site(site)
            
            # Calculate the new energy
            new_energy = self.ham.energy(config)
            
            # Calculate energy difference
            delta_E = new_energy - current_energy
            
            if delta_E > 0 and np.random.random() > np.exp(-delta_E / T):
                # Reject the move (flip back)
                config.flip_site(site)
    
    def _calculate_magnetization(self, config):
        magnetization = 0
        for i in range(len(config.config)):
            # Convert bit value (0,1) to spin value (-1,1)
            spin = 1 if config.config[i] else -1
            magnetization += spin
            
        return magnetization