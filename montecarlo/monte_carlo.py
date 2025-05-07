import numpy as np
from montecarlo.bitstring import BitString

class MonteCarlo:
    def __init__(self, hamiltonian):
        """
        Initialize the Monte Carlo simulation with a Hamiltonian.
        
        Parameters:
        -----------
        hamiltonian : IsingHamiltonian
            The Hamiltonian object that defines the energy of the system.
        """
        self.ham = hamiltonian
        self.num_sites = self.ham.num_sites
    
    def run(self, T, n_samples=10000, n_burn=100):
        """
        Run a Monte Carlo simulation at temperature T.
        
        Parameters:
        -----------
        T : float
            Temperature at which to run the simulation.
        n_samples : int
            Number of samples to collect after burn-in.
        n_burn : int
            Number of steps to discard as burn-in before collecting samples.
            
        Returns:
        --------
        E : list
            List of energy values from the simulation.
        M : list
            List of magnetization values from the simulation.
        """
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
        """
        Perform one step of the Metropolis algorithm.
        
        Parameters:
        -----------
        config : BitString
            Current configuration of the system.
        T : float
            Temperature at which to run the simulation.
        """
        for site in range(self.num_sites):
            # Store the current energy
            current_energy = self.ham.energy(config)
            
            # Flip a spin
            config.flip_site(site)
            
            # Calculate the new energy
            new_energy = self.ham.energy(config)
            
            # Calculate energy difference
            delta_E = new_energy - current_energy
            
            # Accept or reject the move based on Metropolis criterion
            if delta_E > 0 and np.random.random() > np.exp(-delta_E / T):
                # Reject the move (flip back)
                config.flip_site(site)
    
    def _calculate_magnetization(self, config):
        """
        Calculate the magnetization of a configuration.
        
        Parameters:
        -----------
        config : BitString
            Configuration for which to calculate the magnetization.
            
        Returns:
        --------
        magnetization : float
            The magnetization of the configuration.
        """
        # In an Ising model, magnetization is the sum of spins
        # where up spins have value 1 and down spins have value -1
        magnetization = 0
        for i in range(len(config.config)):
            # Convert bit value (0,1) to spin value (-1,1)
            spin = 1 if config.config[i] else -1
            magnetization += spin
            
        return magnetization