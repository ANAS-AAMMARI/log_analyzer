import argparse

def parse_logs(file_path):
    stats = {'INFO': 0, 'WARNING': 0, 'ERROR': 0}
    with open(file_path, 'r') as f:
        for line in f:
            for level in stats:
                if f"[{level}]" in line:
                    stats[level] += 1
    return stats

def write_report(stats, output_path):
    with open(output_path, 'w') as f:
        for level, count in stats.items():
            f.write(f"{level}: {count}\n")

# main function to handle command line arguments
def main():
    parser = argparse.ArgumentParser(description='Analyseur de logs')
    parser.add_argument('--input', default='log.txt', help='Fichier de log à analyser')
    parser.add_argument('--output', default='rapport.txt', help='Fichier de rapport à générer')
    args = parser.parse_args()

    stats = parse_logs(args.input)
    write_report(stats, args.output)

if __name__ == "__main__":
    main()
