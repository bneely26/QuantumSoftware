"""
Unit and regression test for the graphbuilder package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import graphbuilder


def test_graphbuilder_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "graphbuilder" in sys.modules

def test_1():
    G = graphbuilder.build_graph1(verbose=1)
    assert G.number_of_nodes() == 10

def test_2():
    G = graphbuilder.build_graph2(verbose=1)
    assert G.number_of_nodes() == 6

def test_1d():
    G = graphbuilder.build_1d_graph(20,verbose=1)
    assert G.number_of_nodes() == 20 

if __name__== "__main__":
    test_graphbuilder_imported()
    test_1()
    test_2()
    test_1d()
