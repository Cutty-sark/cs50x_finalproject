from csec_news import CybersecHeadlines

def main():

    cybersec_block = CybersecHeadlines()

    cybersec_block.gather_data()

    cybersec_block.display()

if __name__ == "__main__":
    main()
