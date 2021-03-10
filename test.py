import argparse
import os
from shutil import copyfile

#immuneml --inputs file1 file2 file3 --output_dir /some/path --yaml_path abc.yml --metadata abc.csv --tool galaxy_yaml_tool

def get_args():
    parser = argparse.ArgumentParser(description='Tool for detecting known and novel MicroRNAs')
    parser.add_argument('-o', '--output_dir', help='Output directory', default='.', required=True)
    parser.add_argument('-i', '--inputs', help='Input directory', default='.', required=True, nargs='+')
    parser.add_argument('-y', '--yaml', help='Yaml input', default='.', required=True)
    parser.add_argument('-m', '--metadata', help='Metadata input', default='.', required=False)
    parser.add_argument('-t', '--tool', help='Tool', default='.', required=False)

    return parser.parse_args()


def main():
    print('main')
    args = get_args()

    print(args.output_dir)
    print(args.inputs)

    #os.mkdir(args.output_dir)
    i = 0
    html_files_links = ''
    for f in args.inputs:
        filename = str(i) + '.txt'
        copyfile(f, os.path.join(args.output_dir, str(i) + '.txt'))
        i += 1
        html_files_links += '<li><a href="' + filename + '" title="' + filename + '">Input file ' + str(i) + '</a></li>'

    copyfile(args.yaml, os.path.join(args.output_dir, 'yaml_file.txt'))
    copyfile(args.metadata, os.path.join(args.output_dir, 'metadata_file.txt'))
    copyfile('pipout.txt', os.path.join(args.output_dir, 'pipout.txt'))
    copyfile('immuneout.txt', os.path.join(args.output_dir, 'immuneout.txt'))
    html_files_links += '<li><a href="yaml_file.txt" title="YAML file">YAML file</a></li>'
    html_files_links += '<li><a href="metadata_file.txt" title="Metadata file">Metadata file</a></li>'
    html_files_links += '<li><a href="pipout.txt" title="Pip output">Pip output</a></li>'
    html_files_links += '<li><a href="immuneout.txt" title="ImmuneML output">ImmuneML output</a></li>'

    html_output = open(os.path.join(args.output_dir, 'output.html'), 'w')

    html_test = '''<nav>
    <ul>'''

    html_test += html_files_links
    html_test += '''</ul>
    </nav>'''
    html_output.write(html_test)
    html_output.close()


if __name__ == '__main__':
    main()




