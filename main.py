from csec_news import CybersecHeadlines

# Import block classes
from csec_news import CybersecHeadlines
from network_health import NetworkHealth

def main():
    # Create instances of blocks
    cybersec_block = CybersecHeadlines()
    network_block = NetworkHealth()

    # Gather data for each block
    cybersec_block.gather_data()
    network_block.gather_data()

    # Display the blocks
    # cybersec_block.display()
    # network_block.display()
    print(cybersec_block.render())
    print(network_block.render())


if __name__ == "__main__":
    main()