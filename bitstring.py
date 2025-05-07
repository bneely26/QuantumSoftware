import numpy as np


class BitString:
    """
    A class representing a configuration of binary bits (0s and 1s).
    Used for representing spin configurations in the Ising model.
    """
    def __init__(self, N):
        """
        Initialize a BitString with N bits, all set to 0.
        
        Parameters
        ----------
        N : int
            Number of bits in the configuration
        """
        self.N = N
        self.config = np.zeros(N, dtype=int)

    def __repr__(self):
        """
        Return a string representation of the bit configuration.
        """
        return ''.join(str(bit) for bit in self.config)

    def __str__(self):
        """
        Return a string representation of the bit configuration.
        """
        return self.__repr__()

    def __eq__(self, other):
        """
        Compare two BitString objects for equality.
        
        Parameters
        ----------
        other : BitString
            Another BitString object to compare with
            
        Returns
        -------
        bool
            True if the configurations are identical, False otherwise
        """
        return np.array_equal(self.config, other.config)
    
    def __len__(self):
        """
        Return the number of bits in the configuration.
        
        Returns
        -------
        int
            Length of the bit configuration
        """
        return self.N
    
    def size(self):
        """
        Return the number of bits in the configuration.
        
        Returns
        -------
        int
            Length of the bit configuration
        """
        return self.N

    def on(self):
        """
        Return the number of bits that are set to 1.
        
        Returns
        -------
        int
            Count of bits that are on (1)
        """
        return np.sum(self.config)

    def off(self):
        """
        Return the number of bits that are set to 0.
        
        Returns
        -------
        int
            Count of bits that are off (0)
        """
        return self.N - np.sum(self.config)

    def flip_site(self, i):
        """
        Flip the bit at site i (0->1 or 1->0).
        
        Parameters
        ----------
        i : int
            Index of the bit to flip
        """
        self.config[i] = 1 - self.config[i]

    def get_bit(self, index):
        """
        Get the bit value (0 or 1) at the specified index.
        
        Parameters
        ----------
        index : int
            Index of the bit to get
            
        Returns
        -------
        int
            Value of the bit (0 or 1)
        """
        return self.config[index]
    
    def getBit(self, index):
        """
        Legacy method - Get the bit value at the specified index.
        
        Parameters
        ----------
        index : int
            Index of the bit to get
            
        Returns
        -------
        int
            Value of the bit (0 or 1)
        """
        return self.config[index]

    def getArray(self):
        """
        Return the bit configuration as a numpy array.
        
        Returns
        -------
        numpy.ndarray
            Array representation of the bit configuration
        """
        return self.config

    def get_spin(self, site_idx):
        """
        Get the spin value (+1 or -1) for the specified site.
        
        Parameters
        ----------
        site_idx : int
            Index of the site
            
        Returns
        -------
        int
            Spin value (+1 if bit is 0, -1 if bit is 1)
        """
        return 1 - 2 * self.config[site_idx]

    def integer(self):
        """
        Return the decimal integer corresponding to the BitString.
        
        Returns
        -------
        int
            Decimal representation of the bit configuration
        """
        # Use binary representation for more efficient conversion
        powers = 2 ** np.arange(self.N - 1, -1, -1)
        return np.sum(self.config * powers)

    def set_config(self, s):
        """
        Set the configuration from a list of integers.
        
        Parameters
        ----------
        s : list or numpy.ndarray
            List of bit values (0s and 1s)
        """
        if len(s) != self.N:
            raise ValueError(f"Expected {self.N} bits, got {len(s)}")
        self.config = np.array(s, dtype=int)

    def set_integer_config(self, dec):
        """
        Set the bit configuration based on a decimal integer.
        
        Parameters
        ----------
        dec : int
            Decimal integer to convert to binary configuration
            
        Returns
        -------
        numpy.ndarray
            The new bit configuration
        """
        if dec < 0 or dec >= 2**self.N:
            raise ValueError(f"Integer {dec} is out of range for {self.N} bits")
        
        # Convert to binary more efficiently
        binary = format(dec, f'0{self.N}b')
        self.config = np.array([int(bit) for bit in binary], dtype=int)
        
        return self.config